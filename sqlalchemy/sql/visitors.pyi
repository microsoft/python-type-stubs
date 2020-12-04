from typing import Any

class VisitableType(type):
    def __init__(cls, clsname: Any, bases: Any, clsdict: Any) -> None: ...

class Visitable: ...

class ClauseVisitor:
    __traverse_options__: Any = ...
    def traverse_single(self, obj: Any, **kw: Any): ...
    def iterate(self, obj: Any): ...
    def traverse(self, obj: Any): ...
    @property
    def visitor_iterator(self) -> None: ...
    def chain(self, visitor: Any): ...

class CloningVisitor(ClauseVisitor):
    def copy_and_process(self, list_: Any): ...
    def traverse(self, obj: Any): ...

class ReplacingCloningVisitor(CloningVisitor):
    def replace(self, elem: Any) -> None: ...
    def traverse(self, obj: Any): ...

def iterate(obj: Any, opts: Any): ...
def iterate_depthfirst(obj: Any, opts: Any): ...
def traverse_using(iterator: Any, obj: Any, visitors: Any): ...
def traverse(obj: Any, opts: Any, visitors: Any): ...
def traverse_depthfirst(obj: Any, opts: Any, visitors: Any): ...
def cloned_traverse(obj: Any, opts: Any, visitors: Any): ...
def replacement_traverse(obj: Any, opts: Any, replace: Any): ...
