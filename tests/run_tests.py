import os
import subprocess
import sys
from pathlib import Path


def install_requirements(test_folder: Path):
    print("\nInstalling requirements...")
    return subprocess.run(
        (sys.executable, "-m", "pip", "install", "--upgrade", "-r", os.path.join(test_folder, "requirements.txt"))
    )


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
    test_folder = Path(__file__).parent
    root = test_folder.parent
    os.chdir(root)

    install_requirements(test_folder).check_returncode()
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
