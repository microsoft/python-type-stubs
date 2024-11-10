import itertools
from collections import defaultdict
from collections.abc import Mapping
from functools import cached_property
from typing import Mapping

from ...classes.graph import Graph
from ...exception import NetworkXError
from ...utils import not_implemented_for
from . import local_node_connectivity

__all__ = ["k_components"]

def k_components(G: Graph, min_density: float = 0.95) -> Mapping: ...

class _AntiGraph(Graph):
    all_edge_dict: dict = ...

    def single_edge_dict(self): ...

    edge_attr_dict_factory = single_edge_dict  # type: ignore

    def __getitem__(self, n) -> Mapping: ...
    def neighbors(self, n): ...


    @cached_property
    def adj(self): ...
    def subgraph(self, nodes): ...


    @cached_property
    def degree(self): ...
    def adjacency(self): ...
