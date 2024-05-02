from itertools import count

from ...classes.graph import Graph
from ...utils import BinaryHeap, not_implemented_for, py_random_state
from .community_utils import is_partition

__all__ = ["kernighan_lin_bisection"]

@py_random_state(4)
def kernighan_lin_bisection(
    G: Graph,
    partition: tuple | None = None,
    max_iter: int = 10,
    weight="weight",
    seed=None,
) -> tuple: ...
