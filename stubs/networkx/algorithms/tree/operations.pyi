from functools import partial
from itertools import accumulate, chain

from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["join"]

def join(rooted_trees: ArrayLike, label_attribute: str | None = None): ...
