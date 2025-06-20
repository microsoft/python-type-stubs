from typing import Literal

from ...classes.digraph import DiGraph
from ...classes.graph import Graph
from ...classes.multidigraph import MultiDiGraph
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
def branching_weight(G: DiGraph, attr: str = "weight", default: float = 1) -> int | float: ...
@py_random_state(4)
def greedy_branching(G: DiGraph, attr: str = "weight", default: float = 1, kind: str = "max", seed=None): ...

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

class ArborescenceIterator:
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
