from collections.abc import Iterable
from numpy.typing import ArrayLike
from ..classes.graph import Graph
from ..utils import not_implemented_for, py_random_state

__all__ = ["maximal_independent_set"]

@py_random_state(2)
def maximal_independent_set(
    G: Graph, nodes: ArrayLike | Iterable | None = None, seed=None
) -> ArrayLike: ...
