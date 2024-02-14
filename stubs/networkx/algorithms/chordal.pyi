import sys
import warnings

from ..algorithms.components import connected_components
from ..classes.graph import Graph
from ..exception import NetworkXException
from ..utils import arbitrary_element, not_implemented_for

__all__ = [
    "is_chordal",
    "find_induced_nodes",
    "chordal_graph_cliques",
    "chordal_graph_treewidth",
    "NetworkXTreewidthBoundExceeded",
    "complete_to_chordal_graph",
]

class NetworkXTreewidthBoundExceeded(NetworkXException):
    pass

def is_chordal(G: Graph) -> bool: ...
def find_induced_nodes(G: Graph, s, t, treewidth_bound: float = ...): ...
def chordal_graph_cliques(G: Graph): ...
def chordal_graph_treewidth(G: Graph) -> int: ...
def complete_to_chordal_graph(G: Graph): ...
