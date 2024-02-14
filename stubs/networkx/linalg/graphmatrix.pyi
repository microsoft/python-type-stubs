from numpy.typing import ArrayLike

from ..classes.graph import Graph

__all__ = ["incidence_matrix", "adj_matrix", "adjacency_matrix"]

def incidence_matrix(G: Graph, nodelist=None, edgelist=None, oriented=False, weight=None): ...
def adjacency_matrix(G: Graph, nodelist: ArrayLike | None = None, dtype=None, weight="weight"): ...

adj_matrix = ...
