from ...utils import not_implemented_for
from ...classes.graph import Graph

__all__ = [
    "clique_removal",
    "max_clique",
    "large_clique_size",
    "maximum_independent_set",
]

def maximum_independent_set(G: Graph) -> set: ...
def max_clique(G: Graph) -> set: ...
def clique_removal(G: Graph): ...
def large_clique_size(G: Graph): ...
