from typing import Callable
from ...classes.graph import Graph
from ...exception import NetworkXError

__all__ = [
    "could_be_isomorphic",
    "fast_could_be_isomorphic",
    "faster_could_be_isomorphic",
    "is_isomorphic",
]

def could_be_isomorphic(G1: Graph, G2: Graph): ...

graph_could_be_isomorphic = ...

def fast_could_be_isomorphic(G1: Graph, G2: Graph): ...

fast_graph_could_be_isomorphic = ...

def faster_could_be_isomorphic(G1: Graph, G2: Graph): ...

faster_graph_could_be_isomorphic = ...

def is_isomorphic(
    G1: Graph,
    G2: Graph,
    node_match: Callable | None = None,
    edge_match: Callable | None = None,
): ...
