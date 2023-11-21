from typing import Callable

from numpy.typing import ArrayLike

__all__ = ["forest_str"]

def forest_str(
    graph,
    with_labels: bool = True,
    sources: ArrayLike | None = None,
    write: Callable | None = None,
    ascii_only: bool = False,
): ...
