from typing import Any

from itertools import chain

from ..classes.graph import Graph

__all__ = [
    "boundary_expansion",
    "conductance",
    "cut_size",
    "edge_expansion",
    "mixing_expansion",
    "node_expansion",
    "normalized_cut_size",
    "volume",
]

# TODO STILL NEED TO UPDATE ALL THE DOCUMENTATION!

def cut_size(G: Graph, S, T=None, weight: Any = None): ...
def volume(G: Graph, S, weight: Any = None): ...
def normalized_cut_size(G: Graph, S, T=None, weight: Any = None): ...
def conductance(G: Graph, S, T=None, weight: Any = None): ...
def edge_expansion(G: Graph, S, T=None, weight: Any = None): ...
def mixing_expansion(G: Graph, S, T=None, weight: Any = None): ...

# TODO What is the generalization to two arguments, S and T? Does the
# denominator become `min(len(S), len(T))`?
def node_expansion(G: Graph, S): ...

# TODO What is the generalization to two arguments, S and T? Does the
# denominator become `min(len(S), len(T))`?
def boundary_expansion(G: Graph, S): ...
