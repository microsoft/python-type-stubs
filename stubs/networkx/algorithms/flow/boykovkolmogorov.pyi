from collections import deque
from operator import itemgetter

from ...algorithms.flow.utils import build_residual_network
from ...classes.graph import Graph

__all__ = ["boykov_kolmogorov"]

def boykov_kolmogorov(
    G: Graph,
    s,
    t,
    capacity: str = "capacity",
    residual=None,
    value_only: bool = False,
    cutoff=None,
): ...
def boykov_kolmogorov_impl(G: Graph, s, t, capacity, residual, cutoff): ...
