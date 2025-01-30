from ...algorithms.flow.utils import build_residual_network
from ...classes.graph import Graph

__all__ = ["edmonds_karp"]

def edmonds_karp_core(R, s, t, cutoff): ...
def edmonds_karp_impl(G: Graph, s, t, capacity, residual, cutoff): ...
def edmonds_karp(
    G: Graph,
    s,
    t,
    capacity: str = "capacity",
    residual=None,
    value_only: bool = False,
    cutoff=None,
): ...
