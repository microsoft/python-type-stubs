import math
from collections.abc import Mapping
from typing import Literal

from numpy.typing import ArrayLike

from ...algorithms.tree.mst import random_spanning_tree
from ...classes.graph import Graph
from ...utils import not_implemented_for, pairwise, py_random_state

__all__ = [
    "traveling_salesman_problem",
    "christofides",
    "asadpour_atsp",
    "greedy_tsp",
    "simulated_annealing_tsp",
    "threshold_accepting_tsp",
]

def swap_two_nodes(soln, seed) -> ArrayLike: ...
def move_one_node(soln, seed) -> ArrayLike: ...
def christofides(G: Graph, weight="weight", tree=None) -> ArrayLike: ...
def traveling_salesman_problem(G: Graph, weight="weight", nodes=None, cycle=True, method=None) -> ArrayLike: ...
@py_random_state(2)
def asadpour_atsp(G: Graph, weight="weight", seed=None, source=None): ...
def held_karp_ascent(G: Graph, weight="weight"): ...
def spanning_tree_distribution(G: Graph, z: Mapping) -> Mapping: ...
def greedy_tsp(G: Graph, weight="weight", source=None): ...
@py_random_state(9)
def simulated_annealing_tsp(
    G: Graph,
    init_cycle,
    weight="weight",
    source=None,
    temp=100,
    move="1-1",
    max_iterations=10,
    N_inner=100,
    alpha=0.01,
    seed=None,
): ...
@py_random_state(9)
def threshold_accepting_tsp(
    G: Graph,
    init_cycle: ArrayLike | Literal["greedy"],
    weight="weight",
    source=None,
    threshold=1,
    move="1-1",
    max_iterations=10,
    N_inner=100,
    alpha=0.1,
    seed=None,
): ...
