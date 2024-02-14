import itertools
import math
from collections import defaultdict

from ..classes.graph import Graph
from ..utils import py_random_state
from .classic import complete_graph, empty_graph, path_graph, star_graph
from .degree_seq import degree_sequence_tree

__all__ = [
    "fast_gnp_random_graph",
    "gnp_random_graph",
    "dense_gnm_random_graph",
    "gnm_random_graph",
    "erdos_renyi_graph",
    "binomial_graph",
    "newman_watts_strogatz_graph",
    "watts_strogatz_graph",
    "connected_watts_strogatz_graph",
    "random_regular_graph",
    "barabasi_albert_graph",
    "dual_barabasi_albert_graph",
    "extended_barabasi_albert_graph",
    "powerlaw_cluster_graph",
    "random_lobster",
    "random_shell_graph",
    "random_powerlaw_tree",
    "random_powerlaw_tree_sequence",
    "random_kernel_graph",
]

@py_random_state(2)
def fast_gnp_random_graph(n: int, p: float, seed=None, directed=False): ...
@py_random_state(2)
def gnp_random_graph(n: int, p: float, seed=None, directed=False): ...

# add some aliases to common names
binomial_graph = ...
erdos_renyi_graph = ...

@py_random_state(2)
def dense_gnm_random_graph(n: int, m: int, seed=None): ...
@py_random_state(2)
def gnm_random_graph(n: int, m: int, seed=None, directed=False): ...
@py_random_state(3)
def newman_watts_strogatz_graph(n: int, k: int, p: float, seed=None): ...
@py_random_state(3)
def watts_strogatz_graph(n: int, k: int, p: float, seed=None): ...
@py_random_state(4)
def connected_watts_strogatz_graph(n: int, k: int, p: float, tries: int = 100, seed=None): ...
@py_random_state(2)
def random_regular_graph(d: int, n, seed=None): ...
@py_random_state(2)
def barabasi_albert_graph(n: int, m: int, seed=None, initial_graph: Graph | None = None) -> Graph: ...
@py_random_state(4)
def dual_barabasi_albert_graph(n: int, m1: int, m2: int, p: float, seed=None, initial_graph: Graph | None = None) -> Graph: ...
@py_random_state(4)
def extended_barabasi_albert_graph(n: int, m: int, p: float, q: float, seed=None) -> Graph: ...
@py_random_state(3)
def powerlaw_cluster_graph(n: int, m: int, p: float, seed=None): ...
@py_random_state(3)
def random_lobster(n: int, p1: float, p2: float, seed=None): ...
@py_random_state(1)
def random_shell_graph(constructor, seed=None): ...
@py_random_state(2)
def random_powerlaw_tree(n: int, gamma: float = 3, seed=None, tries: int = 100): ...
@py_random_state(2)
def random_powerlaw_tree_sequence(n: int, gamma: float = 3, seed=None, tries: int = 100): ...
@py_random_state(3)
def random_kernel_graph(n: int, kernel_integral, kernel_root=None, seed=None): ...
