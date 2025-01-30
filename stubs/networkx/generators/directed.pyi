import numbers
from collections import Counter

from ..classes import MultiDiGraph
from ..classes.graph import Graph
from ..generators.classic import empty_graph
from ..utils import discrete_sequence, py_random_state, weighted_choice

__all__ = [
    "gn_graph",
    "gnc_graph",
    "gnr_graph",
    "random_k_out_graph",
    "scale_free_graph",
]

@py_random_state(3)
def gn_graph(n: int, kernel=None, create_using=None, seed=None): ...
@py_random_state(3)
def gnr_graph(n: int, p: float, create_using=None, seed=None): ...
@py_random_state(2)
def gnc_graph(n: int, create_using=None, seed=None): ...
@py_random_state(7)
def scale_free_graph(
    n,
    alpha: float = 0.41,
    beta: float = 0.54,
    gamma: float = 0.05,
    delta_in: float = 0.2,
    delta_out: float = 0,
    create_using=None,
    seed=None,
    initial_graph=None,
) -> MultiDiGraph: ...
@py_random_state(4)
def random_uniform_k_out_graph(n: int, k: int, self_loops: bool = True, with_replacement: bool = True, seed=None): ...
@py_random_state(4)
def random_k_out_graph(n: int, k: int, alpha: float, self_loops: bool = True, seed=None) -> MultiDiGraph: ...
