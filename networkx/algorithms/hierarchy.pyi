from ..classes.digraph import DiGraph
from ..classes.multidigraph import MultiDiGraph

__all__ = ["flow_hierarchy"]

def flow_hierarchy(G: DiGraph | MultiDiGraph, weight=None) -> float: ...
