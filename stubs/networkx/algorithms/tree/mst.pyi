from dataclasses import dataclass, field
from enum import Enum
from heapq import heappop, heappush
from itertools import count
from math import isnan
from operator import itemgetter
from queue import PriorityQueue

from ...algorithms.tree.mst import SpanningTreeIterator
from ...classes.graph import Graph
from ...utils import UnionFind, not_implemented_for, py_random_state

__all__ = [
    "minimum_spanning_edges",
    "maximum_spanning_edges",
    "minimum_spanning_tree",
    "maximum_spanning_tree",
    "random_spanning_tree",
    "partition_spanning_tree",
    "EdgePartition",
    "SpanningTreeIterator",
]

class EdgePartition(Enum):
    OPEN = ...
    INCLUDED = ...
    EXCLUDED = ...

def boruvka_mst_edges(G: Graph, minimum=True, weight="weight", keys=False, data=True, ignore_nan=False): ...
def kruskal_mst_edges(
    G: Graph,
    minimum,
    weight="weight",
    keys=True,
    data=True,
    ignore_nan=False,
    partition=None,
): ...
def prim_mst_edges(G: Graph, minimum, weight="weight", keys=True, data=True, ignore_nan=False): ...

ALGORITHMS: dict = ...

def minimum_spanning_edges(
    G: Graph,
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool = True,
    ignore_nan=False,
): ...
def maximum_spanning_edges(
    G: Graph,
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool = True,
    ignore_nan=False,
): ...
def minimum_spanning_tree(G: Graph, weight: str = "weight", algorithm: str = "kruskal", ignore_nan=False): ...
def partition_spanning_tree(
    G: Graph,
    minimum=True,
    weight: str = "weight",
    partition: str = "partition",
    ignore_nan=False,
): ...
def maximum_spanning_tree(G: Graph, weight: str = "weight", algorithm: str = "kruskal", ignore_nan=False): ...
@py_random_state(3)
def random_spanning_tree(G: Graph, weight: str | None = None, *, multiplicative: bool = True, seed=None): ...

class SpanningTreeIterator:
    def __init__(
        self,
        G: Graph,
        weight: str = "weight",
        minimum: bool = True,
        ignore_nan: bool = False,
    ): ...
    def __iter__(self) -> SpanningTreeIterator: ...
    def __next__(self): ...
    def _partition(self, partition, partition_tree): ...
    def _write_partition(self, partition): ...
    def _clear_partition(self, G): ...
