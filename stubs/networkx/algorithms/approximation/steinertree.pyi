
from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["metric_closure", "steiner_tree"]

def metric_closure(G: Graph, weight="weight"): ...
def steiner_tree(G: Graph, terminal_nodes: ArrayLike, weight="weight"): ...
