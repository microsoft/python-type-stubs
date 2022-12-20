from typing import Callable
from networkx import Graph, DiGraph
from ..classes.graph import Graph
from ..classes.coreviews import (
    FilterAdjacency,
    FilterAtlas,
    FilterMultiAdjacency,
    UnionAdjacency,
    UnionMultiAdjacency,
)
from ..classes.filters import no_filter
from ..exception import NetworkXError
from ..utils import not_implemented_for

__all__ = ["generic_graph_view", "subgraph_view", "reverse_view"]

def generic_graph_view(G: Graph, create_using=None): ...
def subgraph_view(
    G: Graph, filter_node: Callable = ..., filter_edge: Callable = ...
) -> Graph: ...
def reverse_view(G: DiGraph) -> DiGraph: ...
