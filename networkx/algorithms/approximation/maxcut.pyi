from typing import Any
from ..._typing import Scalar
from ...utils.decorators import not_implemented_for, py_random_state
from ...classes.graph import Graph

__all__ = ["randomized_partitioning", "one_exchange"]

@py_random_state(1)
def randomized_partitioning(
    G: Graph, seed=None, p: Scalar = 0.5, weight: Any = None
): ...
@py_random_state(2)
def one_exchange(
    G: Graph, initial_cut: set | None = None, seed=None, weight: Any = None
): ...
