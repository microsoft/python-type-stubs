from numpy.typing import ArrayLike
from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

__all__ = ["harmonic_function"]

def harmonic_function(
    G: Graph, max_iter: int = 30, label_name: str = "label"
) -> ArrayLike: ...
