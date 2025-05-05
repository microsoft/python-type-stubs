from collections.abc import Mapping

from ...algorithms.components import connected_components
from ...classes.graph import Graph
from ...exception import AmbiguousSolution

__all__ = [
    "is_bipartite",
    "is_bipartite_node_set",
    "color",
    "sets",
    "density",
    "degrees",
]

def color(G: Graph) -> Mapping: ...
def is_bipartite(G: Graph): ...
def is_bipartite_node_set(G: Graph, nodes): ...
def sets(G: Graph, top_nodes=None) -> tuple[set, set]: ...
def density(B, nodes) -> float: ...
def degrees(B, nodes, weight=None) -> tuple[dict, ...]: ...
