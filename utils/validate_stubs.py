#!/bin/python
# ruff: noqa: F841 # TODO: plenty of unused variables. Validate what was the intent.
from __future__ import annotations

__doc__ = """Validate Stubs.

Usage:
  validate_stubs <package> [--path=<stubpath>] [--class=<c>] [--function=<f>]
  validate_stubs -h | --help
  validate_stubs --version

Options:
  -h --help          Show this screen.
  --version          Show version.
  --path=<stubpath>  Where to find stubs (default to parent directory)
  --function=<f>     Restrict to the named function (or method if used with --class).
  --class=<c>        Restrict to the named class.
"""

import importlib
import importlib.machinery
import inspect
import sys
import typing as _typing
from enum import Enum
from operator import attrgetter
from typing import (
    Callable,
    Literal,
    _overload_dummy,  # type: ignore[attr-defined] # _overload_dummy not exposed
)

import docopt

overloads: dict[str, Callable] = {}


def my_overload(func):
    key = func.__module__ + "." + func.__name__
    if key not in overloads:

        def fn(*args, **kwds):
            _overload_dummy(args, kwds)

        overloads[key] = fn
        fn.__overloads__ = [func]  # type: ignore[attr-defined] # __overloads__ not exposed
    else:
        overloads[key].__overloads__.append(func)  # type: ignore[attr-defined] # __overloads__ not exposed
    return overloads[key]


_typing.overload = my_overload


def import_dual(m: str, stub_path: str) -> tuple:
    """
    Import both a stub package and a real package with the same name.

    Parameters:

    m (str): module name
    stub_path (str): location of type stubs

    Returns:
    Tuple - the tuple of (real module, stub module)

    """

    def _clean(m: str) -> None:
        to_del = [k for k in sys.modules.keys() if k == m or k.startswith(m + ".")]
        for k in to_del:
            del sys.modules[k]
        importlib.invalidate_caches()

    _clean(m)

    m1 = importlib.import_module(m)

    _clean(m)

    sys.path_hooks.insert(0, importlib.machinery.FileFinder.path_hook((importlib.machinery.SourceFileLoader, [".pyi"])))
    sys.path.insert(0, stub_path)

    try:
        m2 = importlib.import_module(m)
        return m1, m2
    finally:
        sys.path.pop(0)
        sys.path_hooks.pop(0)
        _clean(m)


class Item:
    class ItemType(Enum):
        MODULE = 1
        CLASS = 2
        FUNCTION = 3
        PROPERTY = 4

    def __init__(
        self, file: str, module: str, name: str, object_: object, type_: ItemType, children: dict[str, Item] | None = None
    ) -> None:
        self.file = file
        self.module = module
        self.name = name
        self.object_ = object_
        self.type_ = type_
        self.children = children or {}
        self.done = False
        self.analog: Item | None = None

    def ismodule(self) -> bool:
        return self.type_ == Item.ItemType.MODULE

    def isclass(self) -> bool:
        return self.type_ == Item.ItemType.CLASS

    def isfunction(self) -> bool:
        return self.type_ == Item.ItemType.FUNCTION

    @staticmethod
    def make_function(file: str, module: str, name: str, object_: object) -> Item:
        return Item(file, module, name, object_, Item.ItemType.FUNCTION)

    @staticmethod
    def make_class(file: str, module: str, name: str, object_: object, children: dict[str, Item]) -> Item:
        return Item(file, module, name, object_, Item.ItemType.CLASS, children)

    @staticmethod
    def make_module(file: str, module: str, name: str, object_: object, children: dict[str, Item]) -> Item:
        return Item(file, module, name, object_, Item.ItemType.MODULE, children)


def isfrompackage(v: object, path: str) -> bool:
    # Try to ensure the object lives below the root path and is not
    # imported from elsewhere.
    try:
        f = inspect.getfile(v)  # type: ignore[arg-type] # Catching TypeError
        return f.startswith(path)
    except TypeError:  # builtins or non-modules; for the latter we return True for now
        return not inspect.ismodule(v)


def isfrommodule(v: object, module: str, default: bool = True) -> bool:
    try:
        # Make sure it came from this module
        __module__ = v.__dict__["__module__"]
        assert isinstance(__module__, str)
        return module == __module__
    except Exception:
        return default


def gather(name: str, m: object) -> Item:
    """
    Parameters:
    name: module name
    m: module object
    root: package path
    completed: a set of modules already traversed
    items: the list of discovered items
    """

    def _gather(mpath: str, m: object, root: str, fpath: str, completed: set, items: dict):
        """
        Parameters:
        mpath: module path (e.g. pandas.core)
        m: module object
        root: package path
        fpath: module file path relative to package root directory; (may be unnecessary)
        completed: a set of modules already traversed
        items: the dict of discovered items
        """

        for k, v in m.__dict__.items():
            if not (inspect.isclass(v) or inspect.isfunction(v) or inspect.ismodule(v)):
                continue
            if inspect.isbuiltin(v) or k[0] == "_" or not isfrompackage(v, root) or not isfrommodule(v, mpath):
                continue

            if inspect.ismodule(v):
                if v not in completed:
                    completed.add(v)
                    mfpath = inspect.getfile(v)
                    if mfpath.startswith(root):
                        mfpath = mfpath[len(root) + 1 :]
                        members: dict[str, Item] = {}
                        items[k] = Item.make_module(mfpath, mpath, k, v, members)
                        _gather(mpath + "." + k, v, root, mfpath, completed, members)
            elif inspect.isfunction(v):
                if k in items:
                    print(f"{name} already has a function {k}")
                items[k] = Item.make_function(fpath, mpath, k, v)
            elif inspect.isclass(v):
                members = {}
                items[k] = Item.make_class(fpath, mpath, k, v, members)
                for kc, vc in inspect.getmembers(v):
                    if kc[0] != "_" and (inspect.isfunction(vc) or str(type(vc)) == "<class 'property'>"):
                        members[kc] = Item.make_function(fpath, mpath, kc, vc)
            else:
                pass

    fpath = m.__dict__["__file__"]
    root = fpath[: fpath.rfind("/")]  # fix for windows
    members: dict[str, Item] = {}
    package = Item.make_module(fpath, "", name, m, members)
    _gather(name, m, root, fpath, set(), members)
    return package


def walk(tree: dict, fn: Callable, *args, postproc: Callable | None = None, path=None):
    """
    Walk the object tree and apply a function.
    If the function returns True, do not walk its children,
    but add the object to a postproc list and if a postproc function
    is provided, call that at the end for those objects. This gives
    us some flexibility in both traversing the tree and collecting
    and processing certain nodes.
    TODO: see if we ever use the postproc facility and remove it if not.
    """
    if path is None:
        path = ""
    to_postproc = []
    for k, v in tree.items():
        if fn(path, k, v, *args):
            to_postproc.append(k)
        elif v.children:
            walk(v.children, fn, *args, postproc=postproc, path=path + "/" + k)
    if postproc:
        postproc(tree, to_postproc)


def collect_items(root: Item) -> tuple[list[Item], list[Item]]:
    def _collect(path, name, node: Item, functions: list[Item], classes: list[Item]):
        if node.isclass():
            classes.append(node)
            return True  # Don't recurse
        elif node.isfunction():
            functions.append(node)

    functions: list[Item] = []
    classes: list[Item] = []
    walk(root.children, _collect, functions, classes)
    functions = sorted(functions, key=attrgetter("name"))
    classes = sorted(classes, key=attrgetter("name"))
    return functions, classes


def match_pairs(real: list[Item], stub: list[Item], label: str, owner: str = ""):
    i_r = 0
    i_s = 0
    while i_r < len(real) or i_s < len(stub):
        if i_r == len(real) or (i_s < len(stub) and real[i_r].name > stub[i_s].name):
            fn = stub[i_s]
            print(f"No match for stub {label} {fn.module}.{owner}{fn.name}")
            i_s += 1
        elif i_s == len(stub) or real[i_r].name < stub[i_s].name:
            fn = real[i_r]
            print(f"No stub for {label} {fn.module}.{owner}{fn.name}")
            i_r += 1
        else:
            # TODO: Check for uniqueness
            stub[i_s].analog = real[i_r]
            real[i_r].analog = stub[i_s]
            i_s += 1
            i_r += 1


def compare_args(real: Item, stub: Item, owner: str | None = None):
    """
    owner - name of owner class, if a member; else None if a top-level function
    """
    # Note that this isinstance check currently doesn't work for mypy: https://github.com/python/mypy/issues/11071
    if not (isinstance(stub.object_, Callable) and isinstance(real.object_, Callable)):  # type: ignore[arg-type]
        print(f"Can't compare args for non-callables. real: {real.object_}; stub: {stub.object_}")
        return
    if owner is None:
        owner = ""
    elif owner and owner[-1] != ".":
        owner += "."
    module = stub.module
    name = stub.name
    # if stub.object_ == _overload_dummy:
    if hasattr(stub.object_, "__overloads__"):
        print(
            f"Can't validate @overloaded function {module}.{owner}{name} with {len(stub.object_.__overloads__)} overloads"  # pyright: ignore[reportFunctionMemberAccess] # __overloads__ not exposed
        )
        return

    try:
        sc = stub.object_.__code__.co_argcount  # type: ignore[attr-defined] # https://github.com/python/mypy/issues/11071
        ac = real.object_.__code__.co_argcount  # type: ignore[attr-defined] # https://github.com/python/mypy/issues/11071
        sa = inspect.signature(stub.object_)  # type: ignore[arg-type] # https://github.com/python/mypy/issues/11071
        sn = list(sa.parameters.keys())
        aa = inspect.signature(real.object_)  # type: ignore[arg-type] # https://github.com/python/mypy/issues/11071
        an = list(aa.parameters.keys())
        diff = ""

        for i, p in enumerate(sn):
            if i >= len(an):
                diff += f"\tExtra stub parameter {p}\n"
            elif p != an[i]:
                diff += f"\tMismatched parameter names at position {i}: {p} != {an[i]}\n"
            else:
                sp = sa.parameters[p].kind
                ap = aa.parameters[p].kind
                if sp != ap:
                    diff += f"\tMismatched parameter types at position {i} {p}: {sp.description} != {ap.description}\n"

        if len(an) > len(sn):
            i = len(sn)
            while i < len(an):
                diff += f"\tExtra real parameter {an[i]}\n"
                i += 1

        if diff:
            print(f"Mismatched arguments for {module}.{owner}{name}:\n{diff}")
        else:
            print(f"{module}.{owner}{name} passes argument checks")

    except Exception as e:
        if str(e).find("'property' object") >= 0:
            pass
            # print(f"Failed to validate property {module}.{owner}{name}")
        else:
            print(f"Failed to validate {module}.{owner}{name}: {e}")


def compare_functions(real: list[Item], stub: list[Item], owner: str | None = None):
    if owner is None:
        owner = ""
    elif owner and owner[-1] != ".":
        owner += "."
    match_pairs(real, stub, "function", owner)

    # For the functions that do have analogs, compare the
    # signatures.
    i_s = 0
    while i_s < len(stub):
        s = stub[i_s]
        a = s.analog
        if a:
            compare_args(a, s, owner)
        i_s += 1


def compare_classes(real: list[Item], stub: list[Item]):
    match_pairs(real, stub, "class")
    # For the classes that do have analogs, compare the
    # methods.
    i_s = 0
    while i_s < len(stub):
        s = stub[i_s]
        a = s.analog
        if a:
            real_functions, _ = collect_items(a)
            stub_functions, _ = collect_items(s)
            compare_functions(real_functions, stub_functions, s.name)
        i_s += 1


def find_item(items: list[Item], name: str, which: Literal["stub", "real"], type_: Literal["class", "function"]) -> Item | None:
    """
    which - whether this is 'stub' or 'real'
    """
    i = 0
    while i < len(items):
        if items[i].name == name:
            return items[i]
            break
        i += 1
    print(f"No {which} {type_} found with name {name}")
    return None


def compare_class(real: list[Item], stub: list[Item], class_: str):
    a = find_item(real, class_, "real", "class")
    s = find_item(stub, class_, "stub", "class")
    if a is None or s is None:
        return
    real_functions, _ = collect_items(a)
    stub_functions, _ = collect_items(s)
    compare_functions(real_functions, stub_functions, s.name)


def find_mismatched_modules(real: Item, stub: Item):
    """
    Print out all the modules in real package where
    we don't have a matching module in the stubs.
    """

    def has_module(path: str, name: str, node: Item, stub: Item):
        if not node.ismodule():
            return
        components = path.split("/")[1:]
        components.append(name)
        for c in components:
            if c in stub.children:
                stubs = stub.children[c]
            else:
                print(f"No module {node.module}.{name} in stubs")
                break

    walk(real.children, has_module, stub)


def find_module(package: Item, module: str):
    modules = module.split(".")[1:]
    root = package
    for m in modules:
        if m not in root.children:
            return
        root = root.children[m]
    return root


def compare(
    name: str,
    stubpath: str | None = None,
    submodule: str | None = None,
    class_: str | None = None,
    function_: str | None = None,
):
    split = name.find(".")
    if split > 0:
        submodule = name
        name = name[:split]

    if stubpath is None:
        stubpath = ".."

    real, stub = import_dual(name, stubpath)
    real = gather(name, real)
    stub = gather(name, stub)

    # Collect the top level functions and classes
    real_functions, real_classes = collect_items(real)
    stub_functions, stub_classes = collect_items(stub)

    if function_ is not None:
        if class_ is not None:
            ac = find_item(real_classes, class_, "real", "class")
            sc = find_item(stub_classes, class_, "stub", "class")
            if ac is not None and sc is not None:
                real_functions, _ = collect_items(ac)
                stub_functions, _ = collect_items(sc)
                af = find_item(real_functions, function_, "real", "function")
                sf = find_item(stub_functions, function_, "stub", "function")
                if af is not None and sf is not None:
                    compare_args(af, sf, class_)
        else:
            # Top-level function
            af = find_item(real_functions, function_, "real", "function")
            sf = find_item(stub_functions, function_, "stub", "function")
            if af is not None and sf is not None:
                compare_args(af, sf)
    elif class_ is not None:
        compare_class(real_classes, stub_classes, class_=class_)
    elif submodule is not None:
        s = find_module(stub, submodule)
        if s is None:
            print(f"No stub {submodule} found")
        else:
            a = find_module(real, submodule)
            if a is None:
                print(f"No real module {submodule} found")
        # TODO: add the other checks but limit to this submodule
    else:
        find_mismatched_modules(real, stub)
        compare_functions(real_functions, stub_functions)
        compare_classes(real_classes, stub_classes)

    # TODO: if real code has type hints should compare with stubs

    # Get the docstrings and report mismatches
    # TODO


if __name__ == "__main__":
    args = docopt.docopt(__doc__, version="Validate Stubs 0.1")
    compare(args["<package>"], args["--path"], class_=args["--class"], function_=args["--function"])
