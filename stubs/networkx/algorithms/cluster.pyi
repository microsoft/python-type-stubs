from typing import Mapping

from collections import Counter
from itertools import chain, combinations
from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = [
    "triangles",
    "average_clustering",
    "clustering",
    "transitivity",
    "square_clustering",
    "generalized_degree",
]

def triangles(G: Graph, nodes=None) -> Mapping: ...
def average_clustering(
    G: Graph, nodes=None, weight=None, count_zeros: bool = True
) -> float: ...
def clustering(G: Graph, nodes=None, weight=None) -> float | dict: ...
def transitivity(G: Graph) -> float: ...
def square_clustering(G: Graph, nodes=None) -> Mapping: ...
def generalized_degree(G: Graph, nodes=None): ...
