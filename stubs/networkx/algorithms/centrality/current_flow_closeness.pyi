from collections.abc import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for, reverse_cuthill_mckee_ordering
from .flow_matrix import CGInverseLaplacian, FullInverseLaplacian, SuperLUInverseLaplacian

__all__ = ["current_flow_closeness_centrality", "information_centrality"]

def current_flow_closeness_centrality(G: Graph, weight=None, dtype=..., solver="lu") -> Mapping: ...

information_centrality = ...
