from collections import deque

from ...classes.graph import Graph
from .edmondskarp import edmonds_karp_core
from .utils import CurrentEdge, build_residual_network

__all__ = ["shortest_augmenting_path"]

def shortest_augmenting_path_impl(G: Graph, s, t, capacity, residual, two_phase, cutoff): ...
def shortest_augmenting_path(
    G: Graph,
    s,
    t,
    capacity: str = "capacity",
    residual=None,
    value_only: bool = False,
    two_phase: bool = False,
    cutoff=None,
): ...
