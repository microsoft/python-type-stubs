from collections import defaultdict

from ..classes.graph import Graph
from ..utils import not_implemented_for, pairwise

__all__ = [
    "cycle_basis",
    "simple_cycles",
    "recursive_simple_cycles",
    "find_cycle",
    "minimum_cycle_basis",
]

def cycle_basis(G: Graph, root=None): ...
def simple_cycles(G: Graph): ...
def recursive_simple_cycles(G: Graph): ...
def find_cycle(G: Graph, source=None, orientation=None): ...
def minimum_cycle_basis(G: Graph, weight: str | None = None): ...
