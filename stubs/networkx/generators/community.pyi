from numpy.typing import ArrayLike
import itertools
import math

from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = [
    "caveman_graph",
    "connected_caveman_graph",
    "relaxed_caveman_graph",
    "random_partition_graph",
    "planted_partition_graph",
    "gaussian_random_partition_graph",
    "ring_of_cliques",
    "windmill_graph",
    "stochastic_block_model",
    "LFR_benchmark_graph",
]

def caveman_graph(l: int, k: int): ...
def connected_caveman_graph(l: int, k: int): ...
@py_random_state(3)
def relaxed_caveman_graph(l: int, k: int, p: float, seed=None): ...
@py_random_state(3)
def random_partition_graph(
    sizes: ArrayLike, p_in: float, p_out: float, seed=None, directed=False
): ...
@py_random_state(4)
def planted_partition_graph(
    l: int, k: int, p_in: float, p_out: float, seed=None, directed=False
): ...
@py_random_state(6)
def gaussian_random_partition_graph(
    n: int, s: float, v: float, p_in: float, p_out: float, directed=False, seed=None
): ...
def ring_of_cliques(num_cliques: int, clique_size: int): ...
def windmill_graph(n: int, k: int): ...
@py_random_state(3)
def stochastic_block_model(
    sizes: ArrayLike,
    p,
    nodelist: ArrayLike | None = None,
    seed=None,
    directed=False,
    selfloops=False,
    sparse=True,
): ...
@py_random_state(11)
def LFR_benchmark_graph(
    n: int,
    tau1: float,
    tau2: float,
    mu: float,
    average_degree: float | None = None,
    min_degree: int | None = None,
    max_degree: int | None = None,
    min_community: int | None = None,
    max_community: int | None = None,
    tol: float = 1.0e-7,
    max_iters: int = 500,
    seed=None,
): ...
