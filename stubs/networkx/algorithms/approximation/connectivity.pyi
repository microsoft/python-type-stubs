import itertools
from collections.abc import Mapping
from operator import itemgetter

from ...classes.graph import Graph

__all__ = [
    "local_node_connectivity",
    "node_connectivity",
    "all_pairs_node_connectivity",
]

def local_node_connectivity(G: Graph, source, target, cutoff=None): ...
def node_connectivity(G: Graph, s=None, t=None): ...
def all_pairs_node_connectivity(G: Graph, nbunch=None, cutoff=None) -> Mapping: ...
