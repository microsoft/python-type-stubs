import os
import subprocess
import sys
from pathlib import Path


def install_requirements():
    print("\nInstalling requirements...")
    subprocess.check_call((sys.executable, "-m", "pip", "install", "pip>=25.1"))
    subprocess.check_call((sys.executable, "-m", "pip", "install", "--upgrade", "--group", "tests"))


def run_pyright():
    print("\nRunning Pyright...")
    # https://github.com/RobertCraigie/pyright-python#keeping-pyright-and-pylance-in-sync
    del os.environ["PYRIGHT_PYTHON_FORCE_VERSION"]
    os.environ["PYRIGHT_PYTHON_PYLANCE_VERSION"] = "latest-prerelease"
    return subprocess.run((sys.executable, "-m", "pyright"))


def run_mypy():
    print("\nRunning mypy...")
    return subprocess.run((sys.executable, "-m", "mypy"))


def main():
    os.chdir(Path(__file__).parent.parent)

    install_requirements()
    results = (
        run_mypy(),
        run_pyright(),
    )
    if sum([result.returncode for result in results]) > 0:
        print("\nOne or more tests failed. See above for details.")
    else:
        print("\nAll tests passed!")


if __name__ == "__main__":
    main()
