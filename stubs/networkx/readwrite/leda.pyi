from collections.abc import Iterable

# Original author: D. Eppstein, UC Irvine, August 12, 2003.
# The original code at http://www.ics.uci.edu/~eppstein/PADS/ is public domain.

__all__ = ["read_leda", "parse_leda"]


def read_leda(path, encoding="UTF-8"): ...
def parse_leda(lines: str | Iterable): ...
