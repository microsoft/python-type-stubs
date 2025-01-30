import os
import subprocess
import sys
from pathlib import Path


def install_requirements():
    print("\nInstalling requirements...")
    return subprocess.run((sys.executable, "-m", "pip", "install", "--upgrade", "isort", "black"))


def run_isort():
    print("\nRunning isort...")
    return subprocess.run((sys.executable, "-m", "isort", "."))


def run_black():
    print("\nRunning Black...")
    return subprocess.run((sys.executable, "-m", "black", "."))


def main():
    test_folder = Path(__file__).parent
    root = test_folder.parent
    os.chdir(root)

    install_requirements().check_returncode()
    results = (
        run_isort(),
        run_black(),
    )
    if sum([result.returncode for result in results]) > 0:
        print("\nOne or more tests failed. See above for details.")
    else:
        print("\nAll tests passed!")


if __name__ == "__main__":
    main()
