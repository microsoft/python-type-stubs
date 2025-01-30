import copy

from ..classes.graph import Graph

__all__ = ["kl_connected_subgraph", "is_kl_connected"]

def kl_connected_subgraph(G: Graph, k, l, low_memory: bool = False, same_as_graph: bool = False): ...
def is_kl_connected(G: Graph, k, l, low_memory: bool = False) -> bool: ...
