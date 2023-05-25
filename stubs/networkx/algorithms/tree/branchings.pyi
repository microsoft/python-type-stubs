from ...classes.multidigraph import MultiDiGraph
from ...classes.digraph import DiGraph
from typing import Literal
from ...algorithms.tree.branchings import ArborescenceIterator

# TODO: Implement method from Gabow, Galil, Spence and Tarjan:
#
# @article{
#    year={1986},
#    issn={0209-9683},
#    journal={Combinatorica},
#    volume={6},
#    number={2},
#    doi={10.1007/BF02579168},
#    title={Efficient algorithms for finding minimum spanning trees in
#        undirected and directed graphs},
#    url={https://doi.org/10.1007/BF02579168},
#    publisher={Springer-Verlag},
#    keywords={68 B 15; 68 C 05},
#    author={Gabow, Harold N. and Galil, Zvi and Spencer, Thomas and Tarjan,
#        Robert E.},
#    pages={109-122},
#    language={English}
# }
import string
from dataclasses import dataclass, field
from enum import Enum
from operator import itemgetter
from queue import PriorityQueue

from ...classes.graph import Graph
from ...utils import py_random_state

from .recognition import is_arborescence, is_branching

__all__ = [
    "branching_weight",
    "greedy_branching",
    "maximum_branching",
    "minimum_branching",
    "maximum_spanning_arborescence",
    "minimum_spanning_arborescence",
    "ArborescenceIterator",
    "Edmonds",
]

KINDS: set = ...

STYLES: dict = ...

INF = ...

@py_random_state(1)
def random_string(L=15, seed=None): ...
def branching_weight(
    G: DiGraph, attr: str = "weight", default: float = 1
) -> int | float: ...
@py_random_state(4)
def greedy_branching(
    G: DiGraph, attr: str = "weight", default: float = 1, kind: str = "max", seed=None
): ...

class MultiDiGraph_EdgeKey(MultiDiGraph):
    def __init__(self, incoming_graph_data=None, **attr): ...
    def remove_node(self, n): ...
    def remove_nodes_from(self, nbunch): ...
    def add_edge(self, u_for_edge, v_for_edge, key_for_edge, **attr): ...
    def add_edges_from(self, ebunch_to_add, **attr): ...
    def remove_edge_with_key(self, key): ...
    def remove_edges_from(self, ebunch): ...

def get_path(G: Graph, u, v): ...

class Edmonds:
    def __init__(self, G: Graph, seed=None): ...
    def _init(self, attr, default, kind, style, preserve_attrs, seed, partition): ...
    def find_optimum(
        self,
        attr: str = "weight",
        default: float = 1,
        kind: Literal["min", "max"] = "max",
        style: Literal["branching", "arborescence"] = "branching",
        preserve_attrs: bool = False,
        partition: str | None = None,
        seed=None,
    ): ...

def maximum_branching(
    G: Graph,
    attr: str = "weight",
    default: float = 1,
    preserve_attrs: bool = False,
    partition: str | None = None,
): ...
def minimum_branching(
    G: Graph,
    attr: str = "weight",
    default: float = 1,
    preserve_attrs: bool = False,
    partition: str | None = None,
): ...
def maximum_spanning_arborescence(
    G: Graph,
    attr: str = "weight",
    default: float = 1,
    preserve_attrs: bool = False,
    partition: str | None = None,
): ...
def minimum_spanning_arborescence(
    G: Graph,
    attr: str = "weight",
    default: float = 1,
    preserve_attrs: bool = False,
    partition: str | None = None,
): ...

docstring_branching: str = ...

docstring_arborescence = ...

maximum_branching.__doc__ = ...

minimum_branching.__doc__ = ...

maximum_spanning_arborescence.__doc__ = ...

minimum_spanning_arborescence.__doc__ = ...

class ArborescenceIterator:
    ...

    def __init__(
        self,
        G: Graph,
        weight: str = "weight",
        minimum: bool = True,
        init_partition: tuple | None = None,
    ): ...
    def __iter__(self) -> ArborescenceIterator: ...
    def __next__(self): ...
    def _partition(self, partition, partition_arborescence): ...
    def _write_partition(self, partition): ...
    def _clear_partition(self, G): ...
