from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["bethe_hessian_matrix"]

def bethe_hessian_matrix(G: Graph, r: float | None = None, nodelist: ArrayLike | None = None): ...
