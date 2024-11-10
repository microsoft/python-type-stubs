from ...classes.graph import Graph

__all__ = [
    "number_weakly_connected_components",
    "weakly_connected_components",
    "is_weakly_connected",
]

def weakly_connected_components(G: Graph): ...
def number_weakly_connected_components(G: Graph): ...
def is_weakly_connected(G: Graph) -> bool: ...
