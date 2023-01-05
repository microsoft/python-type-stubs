from collections.abc import Iterable

# Original author: D. Eppstein, UC Irvine, August 12, 2003.
# The original code at http://www.ics.uci.edu/~eppstein/PADS/ is public domain.

__all__ = ["read_leda", "parse_leda"]

from ..classes.graph import Graph
from ..exception import NetworkXError
from ..utils import open_file

def read_leda(path, encoding="UTF-8"): ...
def parse_leda(lines: str | Iterable): ...
