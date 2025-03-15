from collections.abc import Mapping

from ...classes.graph import Graph

__all__ = ["average_neighbor_degree"]

def average_neighbor_degree(G: Graph, source="out", target="out", nodes=None, weight=None) -> Mapping: ...
