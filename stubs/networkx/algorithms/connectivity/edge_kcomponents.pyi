import itertools as it
from functools import partial

from ...classes.graph import Graph
from ...algorithms import bridges
from ...utils import arbitrary_element, not_implemented_for

__all__ = [
    "k_edge_components",
    "k_edge_subgraphs",
    "bridge_components",
    "EdgeComponentAuxGraph",
]

def k_edge_components(G: Graph, k): ...
def k_edge_subgraphs(G: Graph, k): ...
def bridge_components(G: Graph): ...

class EdgeComponentAuxGraph:
    @classmethod
    def construct(cls, G: Graph): ...
    def k_edge_components(self, k): ...
    def k_edge_subgraphs(self, k): ...

def general_k_edge_subgraphs(G: Graph, k): ...
