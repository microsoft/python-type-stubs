from collections.abc import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = [
    "subgraph_centrality_exp",
    "subgraph_centrality",
    "communicability_betweenness_centrality",
    "estrada_index",
]

def subgraph_centrality_exp(G: Graph) -> Mapping: ...
def subgraph_centrality(G: Graph) -> Mapping: ...
def communicability_betweenness_centrality(G: Graph) -> Mapping: ...
def estrada_index(G: Graph) -> float: ...
