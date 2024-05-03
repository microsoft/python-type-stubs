from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...utils import not_implemented_for, pairwise

__all__ = ["is_semiconnected"]

def is_semiconnected(G: Graph, topo_order: ArrayLike | tuple | None = None) -> bool: ...
