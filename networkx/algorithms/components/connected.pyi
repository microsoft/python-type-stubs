from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

from ...utils import arbitrary_element

__all__ = [
    "number_connected_components",
    "connected_components",
    "is_connected",
    "node_connected_component",
]

def connected_components(G: Graph): ...
def number_connected_components(G: Graph): ...
def is_connected(G: Graph) -> bool: ...
def node_connected_component(G: Graph, n) -> set: ...
