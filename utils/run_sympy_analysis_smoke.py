"""Run the protected SymPy Pyright analysis smoke test with a generous timeout."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-seconds", type=float, default=60.0)
    parser.add_argument("--fixture", type=Path, default=Path("tests/sympy_analysis_smoke.py"))
    args = parser.parse_args()
    started = time.monotonic()
    result = subprocess.run((sys.executable, "-m", "pyright", str(args.fixture)), check=False)
    elapsed = time.monotonic() - started
    print(f"Pyright smoke test completed in {elapsed:.1f}s (limit: {args.max_seconds:.1f}s).")
    if elapsed > args.max_seconds:
        print("Pyright smoke test exceeded the generous gross-regression threshold.", file=sys.stderr)
        return 1
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
