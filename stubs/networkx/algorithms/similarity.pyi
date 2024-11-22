import math
import time
import warnings
from collections.abc import Mapping
from functools import reduce
from itertools import product
from operator import mul
from typing import Callable

from ..classes.graph import Graph

__all__ = [
    "graph_edit_distance",
    "optimal_edit_paths",
    "optimize_graph_edit_distance",
    "optimize_edit_paths",
    "simrank_similarity",
    "simrank_similarity_numpy",
    "panther_similarity",
    "generate_random_paths",
]

def debug_print(*args, **kwargs): ...
def graph_edit_distance(
    G1,
    G2,
    node_match: Callable | None = None,
    edge_match: Callable | None = None,
    node_subst_cost: Callable | None = None,
    node_del_cost: Callable | None = None,
    node_ins_cost: Callable | None = None,
    edge_subst_cost: Callable | None = None,
    edge_del_cost: Callable | None = None,
    edge_ins_cost: Callable | None = None,
    roots=None,
    upper_bound=None,
    timeout=None,
): ...
def optimal_edit_paths(
    G1,
    G2,
    node_match: Callable | None = None,
    edge_match: Callable | None = None,
    node_subst_cost: Callable | None = None,
    node_del_cost: Callable | None = None,
    node_ins_cost: Callable | None = None,
    edge_subst_cost: Callable | None = None,
    edge_del_cost: Callable | None = None,
    edge_ins_cost: Callable | None = None,
    upper_bound=None,
): ...
def optimize_graph_edit_distance(
    G1,
    G2,
    node_match: Callable | None = None,
    edge_match: Callable | None = None,
    node_subst_cost: Callable | None = None,
    node_del_cost: Callable | None = None,
    node_ins_cost: Callable | None = None,
    edge_subst_cost: Callable | None = None,
    edge_del_cost: Callable | None = None,
    edge_ins_cost: Callable | None = None,
    upper_bound=None,
): ...
def optimize_edit_paths(
    G1,
    G2,
    node_match: Callable | None = None,
    edge_match: Callable | None = None,
    node_subst_cost: Callable | None = None,
    node_del_cost: Callable | None = None,
    node_ins_cost: Callable | None = None,
    edge_subst_cost: Callable | None = None,
    edge_del_cost: Callable | None = None,
    edge_ins_cost: Callable | None = None,
    upper_bound=None,
    strictly_decreasing: bool = True,
    roots=None,
    timeout=None,
): ...
def simrank_similarity(
    G: Graph,
    source=None,
    target=None,
    importance_factor: float = 0.9,
    max_iterations=1000,
    tolerance: float = 1e-4,
) -> dict | float: ...
def simrank_similarity_numpy(
    G: Graph,
    source=None,
    target=None,
    importance_factor=0.9,
    max_iterations=100,
    tolerance=1e-4,
): ...
def panther_similarity(G: Graph, source, k=5, path_length=5, c=0.5, delta=0.1, eps=None) -> Mapping: ...
def generate_random_paths(G: Graph, sample_size, path_length=5, index_map: Mapping | None = None): ...
