from ...classes.digraph import DiGraph
from ...classes.graph import Graph
from ...utils import pairwise

__all__ = ["global_reaching_centrality", "local_reaching_centrality"]

def global_reaching_centrality(G: DiGraph, weight=None, normalized=True) -> float: ...
def local_reaching_centrality(G: DiGraph, v, paths=None, weight=None, normalized=True) -> float: ...
