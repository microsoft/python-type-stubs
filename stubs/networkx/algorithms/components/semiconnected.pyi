from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["is_semiconnected"]

def is_semiconnected(G: Graph, topo_order: ArrayLike | tuple | None = None) -> bool: ...
