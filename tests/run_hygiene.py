import os
import subprocess
import sys
from pathlib import Path


def install_requirements() -> None:
    print("\nInstalling requirements...")
    subprocess.check_call((sys.executable, "-m", "pip", "install", "pip>=25.1"))
    subprocess.check_call((sys.executable, "-m", "pip", "install", "--upgrade", "--group", "hygiene"))


def run_ruff_fix() -> subprocess.CompletedProcess[bytes]:
    print("\nRunning Ruff check --fix...")
    return subprocess.run((sys.executable, "-m", "ruff", "check", "--fix"))


def run_ruff_format() -> subprocess.CompletedProcess[bytes]:
    print("\nRunning Ruff format...")
    return subprocess.run((sys.executable, "-m", "ruff", "format"))


def main() -> None:
    os.chdir(Path(__file__).parent.parent)

    install_requirements()
    results = (
        run_ruff_fix(),
        run_ruff_format(),
    )
    if sum([result.returncode for result in results]) > 0:
        print("\nOne or more tests failed. See above for details.")
    else:
        print("\nAll tests passed!")


if __name__ == "__main__":
    main()
