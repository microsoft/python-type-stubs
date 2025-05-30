import warnings
from collections.abc import Mapping

from ...classes.graph import Graph

__all__ = [
    "betweenness_centrality_subset",
    "betweenness_centrality_source",
    "edge_betweenness_centrality_subset",
]

def betweenness_centrality_subset(G: Graph, sources, targets, normalized: bool = False, weight=None) -> Mapping: ...
def edge_betweenness_centrality_subset(G: Graph, sources, targets, normalized: bool = False, weight=None) -> Mapping: ...

# obsolete name
def betweenness_centrality_source(G: Graph, normalized=True, weight=None, sources=None): ...
