from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["voterank"]

def voterank(G: Graph, number_of_nodes=None) -> ArrayLike: ...
