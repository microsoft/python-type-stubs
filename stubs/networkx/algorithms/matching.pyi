from typing import Mapping
from collections import Counter
from itertools import combinations, repeat

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = [
    "is_matching",
    "is_maximal_matching",
    "is_perfect_matching",
    "max_weight_matching",
    "min_weight_matching",
    "maximal_matching",
]

def maximal_matching(G: Graph) -> set: ...
def matching_dict_to_set(matching): ...
def is_matching(G: Graph, matching: Mapping | set) -> bool: ...
def is_maximal_matching(G: Graph, matching: Mapping | set) -> bool: ...
def is_perfect_matching(G: Graph, matching: Mapping | set) -> bool: ...
def min_weight_matching(
    G: Graph, maxcardinality: bool | None = None, weight="weight"
) -> set: ...
def max_weight_matching(G: Graph, maxcardinality=False, weight="weight") -> set: ...
