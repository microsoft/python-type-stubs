"""Automatic stub testing (stubtest): https://mypy.readthedocs.io/en/stable/stubtest.html"""

import os
import shutil
import sys
import tempfile
from collections.abc import Collection
from pathlib import Path
from subprocess import CompletedProcess, run

root = Path(__file__).parent.parent
stubs_path = root / "stubs"
PARTIAL_STUBS_MARKER = "-stubs"


def run_stubtest(module: str) -> CompletedProcess[bytes]:
    module_path = stubs_path / module
    if not (module_path).is_dir():
        raise ValueError(f"{module_path} is not folder or does not exists")
    allowlist = module_path / "stubtest_allowlist.txt"
    clean_module_name = module.removesuffix(PARTIAL_STUBS_MARKER)
    args = (
        "mypy.stubtest",
        clean_module_name,
        "--mypy-config-file",
        str(root / "pyproject.toml"),
        *("--allowlist", str(allowlist)) * allowlist.exists(),
        # "--ignore-positional-only",
        # "--generate-allowlist",
    )
    if module.endswith(PARTIAL_STUBS_MARKER):
        # We need the module name to match runtime, so copy foo-stubs into temp/foo
        with tempfile.TemporaryDirectory() as tmpdir:
            shutil.copytree(module_path, Path(tmpdir, clean_module_name))
            args += ("--ignore-missing-stub",)
            print(f"\nRunning {' '.join(args)!r} ...", flush=True)
            return run((sys.executable, "-m", *args), cwd=tmpdir)
    else:
        print(f"\nRunning {' '.join(args)!r} ...", flush=True)
        return run((sys.executable, "-m", *args), cwd=stubs_path)


def main(modules: Collection[str]) -> int:
    returncode = 0
    if not modules:
        modules = os.listdir(stubs_path)
    for stub_module in modules:
        if stub_module in {
            # This stub has been upstreamed and is only kept for backwards compatibility
            # The version that is stubbed does not match the one we install for type testing
            "matplotlib",
            # This stub is being upstreamed to typeshed and not worth fixing all issues.
            # networkx 3.5 also isn't available on Python 3.10
            "networkx",
        }:
            print(f"\nSkipped {stub_module}", flush=True)
            continue
        if stub_module.startswith("."):
            continue
        returncode += run_stubtest(stub_module).returncode

    sys.exit(returncode)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Cancelled")
        sys.exit(1)
