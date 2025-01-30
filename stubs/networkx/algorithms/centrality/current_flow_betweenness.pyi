from typing import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for, py_random_state, reverse_cuthill_mckee_ordering
from .flow_matrix import CGInverseLaplacian, FullInverseLaplacian, SuperLUInverseLaplacian, flow_matrix_row

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
