from collections import deque
from itertools import islice

from ...classes.graph import Graph
from ...utils import arbitrary_element
from .utils import CurrentEdge, GlobalRelabelThreshold, Level, build_residual_network, detect_unboundedness

__all__ = ["preflow_push"]

def preflow_push_impl(G: Graph, s, t, capacity, residual, global_relabel_freq, value_only): ...
def preflow_push(
    G: Graph,
    s,
    t,
    capacity: str = "capacity",
    residual=None,
    global_relabel_freq=1,
    value_only: bool = False,
): ...
