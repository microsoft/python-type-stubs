import warnings
from collections import deque
from collections.abc import Mapping
from heapq import heappop, heappush
from itertools import count

from ...classes.graph import Graph
from ...utils import py_random_state
from ...utils.decorators import not_implemented_for

__all__ = ["betweenness_centrality", "edge_betweenness_centrality", "edge_betweenness"]

@py_random_state(5)
def betweenness_centrality(
    G: Graph,
    k=None,
    normalized: bool = True,
    weight=None,
    endpoints: bool = False,
    seed=None,
) -> Mapping: ...
@py_random_state(4)
def edge_betweenness_centrality(G: Graph, k=None, normalized: bool = True, weight=None, seed=None) -> Mapping: ...

# obsolete name
def edge_betweenness(G: Graph, k=None, normalized=True, weight=None, seed=None): ...
