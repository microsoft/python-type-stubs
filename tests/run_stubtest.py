"""Automatic stub testing (stubtest): https://mypy.readthedocs.io/en/stable/stubtest.html"""

import os
import shutil
import sys
import tempfile
from collections.abc import Collection, Generator
from pathlib import Path
from subprocess import CompletedProcess, run

if sys.version_info >= (3,11):
    from contextlib import chdir as chdir_context
else:
    from contextlib import contextmanager

    @contextmanager
    def chdir_context(path: str) -> Generator[None, None, None]:
        previous_working_directory = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(previous_working_directory)

root = Path(__file__).parent.parent
stubs_path = root / "stubs"
PARTIAL_STUBS_MARKER = "-stubs"


def call_stubtest(module: str) -> CompletedProcess[bytes]:
    allowlist = stubs_path / module / "stubtest_allowlist.txt"
    clean_module_name = module.removesuffix(PARTIAL_STUBS_MARKER)
    args = (
        "mypy.stubtest",
        clean_module_name,
        "--mypy-config-file",
        str(root / "pyproject.toml"),
        *("--allowlist", str(allowlist)) * allowlist.exists(),
        # "--generate-allowlist",
    )
    print(f"\nRunning {' '.join(args)!r} ...")
    if module.endswith(PARTIAL_STUBS_MARKER):
        # We need the module name to match runtime, so copy foo-stubs into temp/foo
        with tempfile.TemporaryDirectory() as tmpdir, chdir_context(tmpdir):
            shutil.copytree(stubs_path / module, Path(tmpdir, clean_module_name))
            return run((sys.executable, "-m", *args, "--ignore-missing-stub"))
    else:
        return run((sys.executable, "-m", *args))


def main(modules: Collection[str]) -> int:
    os.chdir(stubs_path)
    returncode = 0
    if not modules:
        modules = os.listdir()
    for stub_module in modules:
        if stub_module in {
            # This stub has been upstreamed and is only kept for backwards compatibility
            # The version that is stubbed does not match the one we install for type testing
            "matplotlib",
            # Requires way too much to validate against runtime for our very slim partial stub
            "transformers-stubs",
        }:
            print(f"\nSkipped {stub_module}")
            continue
        if stub_module.startswith("."):
            continue
        returncode += call_stubtest(stub_module).returncode

    sys.exit(returncode)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Cancelled")
        sys.exit(1)
