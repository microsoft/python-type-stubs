from ...classes.graph import Graph
from ...utils import not_implemented_for
from ..matching import maximal_matching

__all__ = ["min_weighted_dominating_set", "min_edge_dominating_set"]

# TODO Why doesn't this algorithm work for directed graphs?

def min_weighted_dominating_set(G: Graph, weight: str | None = None) -> set: ...
def min_edge_dominating_set(G: Graph) -> set: ...
