from collections import deque

from ...classes.graph import Graph
from ...algorithms.flow.utils import build_residual_network
from ...utils import pairwise

__all__ = ["dinitz"]

def dinitz(
    G: Graph,
    s,
    t,
    capacity: str = "capacity",
    residual=None,
    value_only: bool = False,
    cutoff=None,
): ...
def dinitz_impl(G: Graph, s, t, capacity, residual, cutoff): ...
