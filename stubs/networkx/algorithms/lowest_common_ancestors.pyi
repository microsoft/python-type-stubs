from collections import defaultdict
from collections.abc import Mapping, Set as AbstractSet
from itertools import combinations_with_replacement
from typing import Any

from ..classes.graph import Graph
from ..utils import UnionFind, arbitrary_element, not_implemented_for

__all__ = [
    "all_pairs_lowest_common_ancestor",
    "tree_all_pairs_lowest_common_ancestor",
    "lowest_common_ancestor",
]

def all_pairs_lowest_common_ancestor(G: Graph, pairs=None): ...
def lowest_common_ancestor(G: Graph, node1, node2, default: Any = None): ...
def tree_all_pairs_lowest_common_ancestor(G: Graph, root=None, pairs=None): ...
