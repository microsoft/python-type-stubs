import math
from bisect import bisect_left
from collections.abc import Iterable
from itertools import accumulate, combinations, product
from typing import Mapping

from numpy.typing import ArrayLike

from .._typing import Scalar
from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = [
    "geometric_edges",
    "geographical_threshold_graph",
    "navigable_small_world_graph",
    "random_geometric_graph",
    "soft_random_geometric_graph",
    "thresholded_random_geometric_graph",
    "waxman_graph",
]

def euclidean(x, y): ...
def geometric_edges(G: Graph, radius: Scalar, p: Scalar = 2) -> ArrayLike: ...
@py_random_state(5)
def random_geometric_graph(
    n: int | Iterable,
    radius: float,
    dim: int = 2,
    pos: Mapping | None = None,
    p: float = 2,
    seed=None,
) -> Graph: ...
@py_random_state(6)
def soft_random_geometric_graph(
    n: int | Iterable,
    radius: float,
    dim: int = 2,
    pos: Mapping | None = None,
    p: float = 2,
    p_dist=None,
    seed=None,
) -> Graph: ...
@py_random_state(7)
def geographical_threshold_graph(
    n: int | Iterable,
    theta: float,
    dim: int = 2,
    pos: Mapping | None = None,
    weight: Mapping | None = None,
    metric=None,
    p_dist=None,
    seed=None,
) -> Graph: ...
@py_random_state(6)
def waxman_graph(
    n: int | Iterable,
    beta: float = 0.4,
    alpha: float = 0.1,
    L: float | None = None,
    domain=...,
    metric=None,
    seed=None,
) -> Graph: ...
@py_random_state(5)
def navigable_small_world_graph(n: int, p: int = 1, q: int = 1, r: float = 2, dim: int = 2, seed=None): ...
@py_random_state(7)
def thresholded_random_geometric_graph(
    n: int | Iterable,
    radius: float,
    theta: float,
    dim: int = 2,
    pos: Mapping | None = None,
    weight: Mapping | None = None,
    p=2,
    seed=None,
) -> Graph: ...
