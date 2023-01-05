from .matching import hopcroft_karp_matching
from ...algorithms.covering import min_edge_cover as _min_edge_cover
from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = ["min_edge_cover"]

def min_edge_cover(G: Graph, matching_algorithm=None) -> set: ...
