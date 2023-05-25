from collections.abc import Iterable

from itertools import repeat
from math import sqrt

from ..classes import set_node_attributes
from ..exception import NetworkXError
from ..generators.classic import cycle_graph, empty_graph, path_graph
from ..relabel import relabel_nodes
from ..utils import flatten, nodes_or_number, pairwise

__all__ = [
    "grid_2d_graph",
    "grid_graph",
    "hypercube_graph",
    "triangular_lattice_graph",
    "hexagonal_lattice_graph",
]

def grid_2d_graph(m, n, periodic: bool | Iterable = False, create_using=None): ...
def grid_graph(dim, periodic: bool | Iterable = False): ...
def hypercube_graph(n: int): ...
def triangular_lattice_graph(
    m: int, n: int, periodic=False, with_positions=True, create_using=None
): ...
def hexagonal_lattice_graph(
    m: int, n: int, periodic: bool = False, with_positions=True, create_using=None
): ...
