from typing import Mapping

from ...classes.graph import Graph

__all__ = ["percolation_centrality"]

def percolation_centrality(
    G: Graph, attribute="percolation", states=None, weight=None
) -> Mapping: ...
