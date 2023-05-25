from ..classes import DiGraph, MultiDiGraph
from ..utils import not_implemented_for
from ..classes.graph import Graph

__all__ = ["stochastic_graph"]

def stochastic_graph(G: Graph, copy: bool = True, weight="weight"): ...
