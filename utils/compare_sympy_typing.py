"""Conservatively compare the partial SymPy stubs with inline SymPy annotations."""

from __future__ import annotations

import argparse
import ast
import importlib.metadata
import json
import sys
from pathlib import Path
from typing import Any

PROTECTED_FILES = {
    "core/evalf.pyi",
    "core/power.pyi",
    "simplify/powsimp.pyi",
    "simplify/simplify.pyi",
}
TYPED = "first_party_typed"
UNTYPED = "present_but_insufficiently_annotated"
MISSING = "missing_or_unmappable"
DYNAMIC = "dynamic_or_reexported"


def _is_overload(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    return any(
        (isinstance(decorator, ast.Name) and decorator.id == "overload")
        or (isinstance(decorator, ast.Attribute) and decorator.attr == "overload")
        for decorator in node.decorator_list
    )


def _function_is_typed(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    arguments = (*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs)
    if arguments and arguments[0].arg in {"self", "cls"}:
        arguments = arguments[1:]
    return (
        node.returns is not None
        and all(argument.annotation is not None for argument in arguments)
        and (node.args.vararg is None or node.args.vararg.annotation is not None)
        and (node.args.kwarg is None or node.args.kwarg.annotation is not None)
    )


def _declaration_name(node: ast.AST, prefix: str = "") -> str | None:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return f"{prefix}{node.name}"
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return f"{prefix}{node.target.id}"
    return None


def declarations(tree: ast.Module) -> tuple[dict[str, dict[str, Any]], bool]:
    """Return material declarations and whether the module has dynamic exports."""
    found: dict[str, dict[str, Any]] = {}
    dynamic = any(
        (isinstance(node, ast.FunctionDef) and node.name == "__getattr__") or isinstance(node, (ast.Import, ast.ImportFrom))
        for node in tree.body
    )

    def visit(nodes: list[ast.stmt], prefix: str = "") -> None:
        for node in nodes:
            name = _declaration_name(node, prefix)
            if name is None:
                continue
            if isinstance(node, ast.ClassDef):
                found[name] = {"kind": "class", "typed": True, "overload": False}
                visit(node.body, f"{name}.")
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                kind = (
                    "property"
                    if any(isinstance(decorator, ast.Name) and decorator.id == "property" for decorator in node.decorator_list)
                    else "async_function"
                    if isinstance(node, ast.AsyncFunctionDef)
                    else "function"
                )
                found[name] = {"kind": kind, "typed": _function_is_typed(node), "overload": _is_overload(node)}
            else:
                found[name] = {"kind": "attribute", "typed": True, "overload": False}

    visit(tree.body)
    return found, dynamic


def _source_path(sympy_root: Path, relative_stub: Path) -> Path | None:
    relative = relative_stub.with_suffix(".py")
    candidates = (sympy_root / relative, sympy_root / relative.parent / relative.stem / "__init__.py")
    return next((path for path in candidates if path.is_file()), None)


def compare_file(stub_path: Path, stub_root: Path, sympy_root: Path) -> dict[str, Any]:
    relative = stub_path.relative_to(stub_root)
    source_path = _source_path(sympy_root, relative)
    stub_declarations, _ = declarations(ast.parse(stub_path.read_text(encoding="utf-8"), filename=str(stub_path)))
    result: dict[str, Any] = {
        "stub_file": relative.as_posix(),
        "source_file": str(source_path) if source_path else None,
        "protected": relative.as_posix() in PROTECTED_FILES,
        "declarations": [],
    }
    if source_path is None:
        result["declarations"] = [
            {"name": name, **declaration, "status": MISSING, "reason": "No corresponding source module was found."}
            for name, declaration in stub_declarations.items()
        ]
        result["candidate"] = False
        return result

    source_declarations, source_dynamic = declarations(
        ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    )
    for name, declaration in stub_declarations.items():
        source = source_declarations.get(name)
        if source is None:
            status = DYNAMIC if source_dynamic else MISSING
            reason = "Source module has dynamic exports." if source_dynamic else "No same-named source declaration was found."
        elif source["kind"] != declaration["kind"]:
            status, reason = MISSING, "The same name has a different declaration kind upstream."
        elif declaration["kind"] == "class":
            status, reason = TYPED, "The class exists; its explicit members are compared separately."
        elif source["typed"]:
            status, reason = TYPED, "The same declaration has annotations for every parameter and return value."
        else:
            status, reason = UNTYPED, "The same declaration lacks a parameter or return annotation."
        result["declarations"].append({"name": name, **declaration, "status": status, "reason": reason})
    result["candidate"] = bool(result["declarations"]) and all(
        declaration["status"] == TYPED for declaration in result["declarations"]
    )
    return result


def compare_tree(stub_root: Path, sympy_root: Path) -> dict[str, Any]:
    files = [compare_file(path, stub_root, sympy_root) for path in sorted(stub_root.rglob("*.pyi"))]
    return {
        "stub_root": str(stub_root.resolve()),
        "sympy_root": str(sympy_root.resolve()),
        "sympy_version": importlib.metadata.version("sympy"),
        "protected_files": sorted(PROTECTED_FILES),
        "files": files,
        "candidates": [file["stub_file"] for file in files if file["candidate"] and not file["protected"]],
        "protected_candidates": [file["stub_file"] for file in files if file["candidate"] and file["protected"]],
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# SymPy partial-stub comparison",
        "",
        f"* SymPy: `{report['sympy_version']}`",
        f"* Stub root: `{report['stub_root']}`",
        f"* Installed SymPy root: `{report['sympy_root']}`",
        "",
        "## Automated removal candidates",
        "",
    ]
    candidates = report["candidates"]
    lines.extend([f"- `{path}`" for path in candidates] or ["None."])
    lines.extend(["", "## Protected performance files", ""])
    for file in report["files"]:
        if file["protected"]:
            lines.append(f"- `{file['stub_file']}`: Protected performance workaround; never deleted automatically.")
    lines.extend(["", "## Other retained files", ""])
    for file in report["files"]:
        if file["candidate"] or file["protected"]:
            continue
        reasons = sorted({declaration["reason"] for declaration in file["declarations"] if declaration["status"] != TYPED})
        lines.append(f"- `{file['stub_file']}`: {' '.join(reasons)}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stub-root", type=Path, default=Path("stubs/sympy-stubs"))
    parser.add_argument("--sympy-root", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="Fail when a non-protected candidate is found.")
    args = parser.parse_args()
    try:
        report = compare_tree(args.stub_root, args.sympy_root)
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        args.markdown_out.write_text(markdown(report), encoding="utf-8")
    except (OSError, SyntaxError, importlib.metadata.PackageNotFoundError) as error:
        print(f"comparison failed: {error}", file=sys.stderr)
        return 2
    return int(args.check and bool(report["candidates"]))


if __name__ == "__main__":
    raise SystemExit(main())
