from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, cast

SCRIPT = Path(__file__).parent.parent / "utils" / "compare_sympy_typing.py"
SPEC = importlib.util.spec_from_file_location("compare_sympy_typing", SCRIPT)
assert SPEC and SPEC.loader
comparison: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparison)


def _compare(tmp_path: Path, stub: str, source: str) -> dict[str, Any]:
    stub_root = tmp_path / "stubs"
    sympy_root = tmp_path / "sympy"
    (stub_root / "sample.pyi").parent.mkdir(parents=True)
    sympy_root.mkdir()
    (stub_root / "sample.pyi").write_text(stub, encoding="utf-8")
    (sympy_root / "sample.py").write_text(source, encoding="utf-8")
    return cast("dict[str, Any]", comparison.compare_file(stub_root / "sample.pyi", stub_root, sympy_root))


def test_overloads_methods_properties_classes_and_attributes_are_covered(tmp_path: Path) -> None:
    result = _compare(
        tmp_path,
        """\
from typing import overload
x: int
@overload
def parse(value: int) -> int: ...
@overload
def parse(value: str) -> str: ...
class Item:
    def method(self, value: int) -> str: ...
    @property
    def name(self) -> str: ...
""",
        """\
x: int = 1
def parse(value: int | str) -> int | str:
    return value
class Item:
    def method(self, value: int) -> str:
        return str(value)
    @property
    def name(self) -> str:
        return "item"
""",
    )
    assert result["candidate"] is True
    assert {item["status"] for item in result["declarations"]} == {comparison.TYPED}


def test_missing_annotations_and_names_retain_file(tmp_path: Path) -> None:
    result = _compare(
        tmp_path,
        "def typed(value: int) -> str: ...\ndef absent(value: int) -> str: ...\n",
        "def typed(value):\n    return str(value)\n",
    )
    statuses = {item["name"]: item["status"] for item in result["declarations"]}
    assert result["candidate"] is False
    assert statuses == {
        "typed": comparison.UNTYPED,
        "absent": comparison.MISSING,
    }


def test_dynamic_or_reexported_source_is_not_a_candidate(tmp_path: Path) -> None:
    result = _compare(
        tmp_path,
        "def exported(value: int) -> str: ...\n",
        "from somewhere import exported\n",
    )
    assert result["candidate"] is False
    assert result["declarations"][0]["status"] == comparison.DYNAMIC


def test_class_without_explicit_stub_members_is_not_covered(tmp_path: Path) -> None:
    result = _compare(tmp_path, "class Item: ...\n", "class Item:\n    pass\n")
    assert result["candidate"] is False
    assert result["declarations"][0]["status"] == comparison.UNTYPED


def test_each_overload_must_be_typed(tmp_path: Path) -> None:
    result = _compare(
        tmp_path,
        "from typing import overload\n@overload\ndef parse(value: int) -> int: ...\n@overload\ndef parse(value: str) -> str: ...\n",
        "from typing import overload\n@overload\ndef parse(value) -> int: ...\n@overload\ndef parse(value: str) -> str: ...\n",
    )
    assert result["candidate"] is False
    assert result["declarations"][0]["status"] == comparison.UNTYPED
