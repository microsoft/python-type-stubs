from collections.abc import Iterable
from numpy.typing import ArrayLike
from ..classes.graph import Graph

# Original author: D. Eppstein, UC Irvine, August 12, 2003.
# The original code at https://www.ics.uci.edu/~eppstein/PADS/ is public domain.
from ..classes.graph import Graph
from ..exception import NetworkXError
from ..readwrite.graph6 import data_to_n, n_to_data
from ..utils import not_implemented_for, open_file

__all__ = ["from_sparse6_bytes", "read_sparse6", "to_sparse6_bytes", "write_sparse6"]

def from_sparse6_bytes(string: str) -> Graph: ...
def to_sparse6_bytes(
    G: Graph, nodes: ArrayLike | Iterable | None = None, header: bool = True
): ...
def read_sparse6(path): ...
def write_sparse6(
    G: Graph, path, nodes: ArrayLike | Iterable | None = None, header: bool = True
): ...
