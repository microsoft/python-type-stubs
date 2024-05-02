from ..classes import DiGraph, MultiDiGraph
from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["stochastic_graph"]

def stochastic_graph(G: Graph, copy: bool = True, weight="weight"): ...
