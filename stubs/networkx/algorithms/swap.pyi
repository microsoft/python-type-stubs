import math

from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = ["double_edge_swap", "connected_double_edge_swap"]

@py_random_state(3)
def double_edge_swap(G: Graph, nswap=1, max_tries=100, seed=None): ...
@py_random_state(3)
def connected_double_edge_swap(G: Graph, nswap=1, _window_threshold=3, seed=None) -> int: ...
