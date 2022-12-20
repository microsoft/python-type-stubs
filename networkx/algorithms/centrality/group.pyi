from numpy.typing import ArrayLike
from copy import deepcopy
from ...classes.graph import Graph

from ...utils.decorators import not_implemented_for

__all__ = [
    "group_betweenness_centrality",
    "group_closeness_centrality",
    "group_degree_centrality",
    "group_in_degree_centrality",
    "group_out_degree_centrality",
    "prominent_group",
]

def group_betweenness_centrality(
    G: Graph, C, normalized=True, weight=None, endpoints=False
): ...
def prominent_group(
    G: Graph,
    k: int,
    weight=None,
    C=None,
    endpoints=False,
    normalized=True,
    greedy=False,
) -> tuple[float, ArrayLike]: ...
def group_closeness_centrality(G: Graph, S: ArrayLike | set, weight=None) -> float: ...
def group_degree_centrality(G: Graph, S: ArrayLike | set) -> float: ...
def group_in_degree_centrality(G: Graph, S: ArrayLike | set) -> float: ...
def group_out_degree_centrality(G: Graph, S: ArrayLike | set) -> float: ...
