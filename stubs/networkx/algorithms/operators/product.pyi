from itertools import product

from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = [
    "tensor_product",
    "cartesian_product",
    "lexicographic_product",
    "strong_product",
    "power",
    "rooted_product",
]

# Generators for producting graph products

def tensor_product(G: Graph, H): ...
def cartesian_product(G: Graph, H): ...
def lexicographic_product(G: Graph, H): ...
def strong_product(G: Graph, H): ...
def power(G: Graph, k): ...
def rooted_product(G: Graph, H, root): ...
