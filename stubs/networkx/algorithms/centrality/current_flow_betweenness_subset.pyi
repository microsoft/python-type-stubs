from typing import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for, reverse_cuthill_mckee_ordering
from .flow_matrix import flow_matrix_row

__all__ = [
    "current_flow_betweenness_centrality_subset",
    "edge_current_flow_betweenness_centrality_subset",
]

def current_flow_betweenness_centrality_subset(
    G: Graph, sources, targets, normalized=True, weight=None, dtype=..., solver="lu"
) -> Mapping: ...
def edge_current_flow_betweenness_centrality_subset(
    G: Graph, sources, targets, normalized=True, weight=None, dtype=..., solver="lu"
) -> Mapping: ...
