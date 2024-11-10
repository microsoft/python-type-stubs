from typing import Callable

from networkx import DiGraph, Graph

from ..classes.graph import Graph

__all__ = ["generic_graph_view", "subgraph_view", "reverse_view"]

def generic_graph_view(G: Graph, create_using=None): ...
def subgraph_view(G: Graph, filter_node: Callable = ..., filter_edge: Callable = ...) -> Graph: ...
def reverse_view(G: DiGraph) -> DiGraph: ...
