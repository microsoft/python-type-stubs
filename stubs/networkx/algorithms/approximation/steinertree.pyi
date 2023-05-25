from numpy.typing import ArrayLike
from itertools import chain
from ...classes.graph import Graph
from ...utils import not_implemented_for, pairwise

__all__ = ["metric_closure", "steiner_tree"]

def metric_closure(G: Graph, weight="weight"): ...
def steiner_tree(G: Graph, terminal_nodes: ArrayLike, weight="weight"): ...
