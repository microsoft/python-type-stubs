from collections.abc import Iterable
from numpy.typing import ArrayLike
from ..classes.graph import Graph

# Original author: D. Eppstein, UC Irvine, August 12, 2003.
# The original code at http://www.ics.uci.edu/~eppstein/PADS/ is public domain.
from itertools import islice

from ..classes.graph import Graph
from ..exception import NetworkXError
from ..utils import not_implemented_for, open_file

__all__ = ["from_graph6_bytes", "read_graph6", "to_graph6_bytes", "write_graph6"]

def from_graph6_bytes(bytes_in) -> Graph: ...
def to_graph6_bytes(
    G: Graph, nodes: ArrayLike | Iterable | None = None, header: bool = True
): ...
def read_graph6(path): ...
def write_graph6(
    G: Graph, path: str, nodes: ArrayLike | Iterable | None = None, header: bool = True
): ...
def write_graph6_file(
    G: Graph, f, nodes: ArrayLike | Iterable | None = None, header: bool = True
): ...
def data_to_n(data): ...
def n_to_data(n): ...
