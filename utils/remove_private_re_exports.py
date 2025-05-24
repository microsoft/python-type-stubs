"""
Applies Ruff's
[useless-import-alias (PLC0414)](https://docs.astral.sh/ruff/rules/useless-import-alias/#useless-import-alias-plc0414)
+ [unused-import (F401)](https://docs.astral.sh/ruff/rules/unused-import/)
on stubs files. Normally `useless-import-alias` only applies to `.py`.
So this is achieved by temporarily renaming all private module type stubs.

This isn't necessarily perfect, and temporarily renaming tons of files could be brittle,
so is offered as a tool rather than a test.
"""

import sys
from pathlib import Path
from subprocess import check_call

root = Path(__file__).parent.parent
ruff_cmd = (sys.executable, "-m", "ruff")


def main() -> None:
    paths = [
        path
        for path in (root / "stubs").rglob("*.pyi")
        if path.name != "__init__.pyi" and any(part.startswith("_") for part in path.parts)
    ]

    for path in paths:
        path.rename(path.with_suffix(".py"))

    check_call(
        (
            *ruff_cmd,
            "check",
            "--fix",
            "--unsafe-fixes",
            "--select=PLC0414,F401",
            # Because of the current lint.per-file-ignores configuration,
            # F401 currently doesn't apply to modules that are private because of a folder name
            # ie: stubs/_foo/bar.py(i)
            "--per-file-ignores=!*.py:F401",
        )
    )

    for path in paths:
        path.with_suffix(".py").rename(path)

    check_call((*ruff_cmd, "check", "--fix"))
    check_call((*ruff_cmd, "format"))


if __name__ == "__main__":
    main()
