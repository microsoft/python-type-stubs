from itertools import chain
from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

__all__ = [
    "biconnected_components",
    "biconnected_component_edges",
    "is_biconnected",
    "articulation_points",
]

def is_biconnected(G: Graph) -> bool: ...
def biconnected_component_edges(G: Graph): ...
def biconnected_components(G: Graph): ...
def articulation_points(G: Graph): ...
