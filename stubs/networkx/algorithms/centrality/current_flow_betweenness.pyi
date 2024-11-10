from typing import Mapping

from ...classes.graph import Graph
from ...utils import py_random_state

__all__ = [
    "current_flow_betweenness_centrality",
    "approximate_current_flow_betweenness_centrality",
    "edge_current_flow_betweenness_centrality",
]

@py_random_state(7)
def approximate_current_flow_betweenness_centrality(
    G: Graph,
    normalized=True,
    weight=None,
    dtype=...,
    solver="full",
    epsilon: float = 0.5,
    kmax: int = 10000,
    seed=None,
) -> Mapping: ...
def current_flow_betweenness_centrality(G: Graph, normalized=True, weight=None, dtype=..., solver="full") -> Mapping: ...
def edge_current_flow_betweenness_centrality(G: Graph, normalized=True, weight=None, dtype=..., solver="full") -> Mapping: ...
