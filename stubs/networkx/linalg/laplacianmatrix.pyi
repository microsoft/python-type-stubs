from ..classes.digraph import DiGraph
from numpy.typing import ArrayLike
from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = [
    "laplacian_matrix",
    "normalized_laplacian_matrix",
    "total_spanning_tree_weight",
    "directed_laplacian_matrix",
    "directed_combinatorial_laplacian_matrix",
]

def laplacian_matrix(G: Graph, nodelist: ArrayLike | None = None, weight="weight"): ...
def normalized_laplacian_matrix(
    G: Graph, nodelist: ArrayLike | None = None, weight="weight"
): ...
def total_spanning_tree_weight(G: Graph, weight: str | None = None) -> float: ...

###############################################################################
# Code based on work from https://github.com/bjedwards

def directed_laplacian_matrix(
    G: DiGraph,
    nodelist: ArrayLike | None = None,
    weight="weight",
    walk_type=None,
    alpha=0.95,
): ...
def directed_combinatorial_laplacian_matrix(
    G: DiGraph,
    nodelist: ArrayLike | None = None,
    weight="weight",
    walk_type=None,
    alpha=0.95,
): ...
