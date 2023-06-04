from collections.abc import Iterable
from typing import Mapping
from numpy.typing import ArrayLike

import itertools

from ...classes.graph import Graph

__all__ = [
    "clustering",
    "average_clustering",
    "latapy_clustering",
    "robins_alexander_clustering",
]

def cc_dot(nu, nv): ...
def cc_max(nu, nv): ...
def cc_min(nu, nv): ...

modes: dict = ...

def latapy_clustering(G: Graph, nodes=None, mode: str = "dot") -> Mapping: ...

clustering = ...

def average_clustering(
    G: Graph, nodes: ArrayLike | Iterable | None = None, mode: str = "dot"
) -> float: ...
def robins_alexander_clustering(G: Graph) -> float: ...
