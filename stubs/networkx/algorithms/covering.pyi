from functools import partial
from itertools import chain

from ..classes.graph import Graph
from ..utils import arbitrary_element, not_implemented_for

__all__ = ["min_edge_cover", "is_edge_cover"]

def min_edge_cover(G: Graph, matching_algorithm=None) -> set: ...
def is_edge_cover(G: Graph, cover: set) -> bool: ...
