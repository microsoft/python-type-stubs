from typing import Callable

from ...classes.graph import Graph
from . import isomorphvf2 as vf2

__all__ = ["GraphMatcher", "DiGraphMatcher", "MultiGraphMatcher", "MultiDiGraphMatcher"]

class GraphMatcher(vf2.GraphMatcher):
    def __init__(
        self,
        G1: Graph,
        G2: Graph,
        node_match: Callable | None = None,
        edge_match: Callable | None = None,
    ): ...

    semantic_feasibility = ...

class DiGraphMatcher(vf2.DiGraphMatcher):
    def __init__(
        self,
        G1: Graph,
        G2: Graph,
        node_match: Callable | None = None,
        edge_match: Callable | None = None,
    ): ...
    def semantic_feasibility(self, G1_node, G2_node): ...

# The "semantics" of edge_match are different for multi(di)graphs, but
# the implementation is the same.  So, technically we do not need to
# provide "multi" versions, but we do so to match NetworkX's base classes.

class MultiGraphMatcher(GraphMatcher): ...
class MultiDiGraphMatcher(DiGraphMatcher): ...
