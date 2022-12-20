from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = [
    "uniform_random_intersection_graph",
    "k_random_intersection_graph",
    "general_random_intersection_graph",
]

@py_random_state(3)
def uniform_random_intersection_graph(n: int, m: int, p: float, seed=None): ...
@py_random_state(3)
def k_random_intersection_graph(n: int, m: int, k: float, seed=None): ...
@py_random_state(3)
def general_random_intersection_graph(n: int, m: int, p, seed=None): ...
