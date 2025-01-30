from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

__all__ = ["local_and_global_consistency"]

def local_and_global_consistency(G: Graph, alpha: float = 0.99, max_iter: int = 30, label_name: str = "label") -> ArrayLike: ...
