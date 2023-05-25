from ..classes.digraph import DiGraph
from numpy.typing import ArrayLike
from ..classes.graph import Graph
from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["modularity_matrix", "directed_modularity_matrix"]

def modularity_matrix(G: Graph, nodelist: ArrayLike | None = None, weight=None): ...
def directed_modularity_matrix(
    G: DiGraph, nodelist: ArrayLike | None = None, weight=None
): ...
