from typing import Mapping
from operator import itemgetter

from ...classes.graph import Graph

__all__ = ["load_centrality", "edge_load_centrality"]

def newman_betweenness_centrality(
    G: Graph, v=None, cutoff=None, normalized=True, weight=None
) -> Mapping: ...

load_centrality = ...

def edge_load_centrality(G: Graph, cutoff=False): ...
