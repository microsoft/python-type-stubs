from importlib.abc import Traversable
from typing import Final

from numpy.typing import ArrayLike

__all__ = ["graph_atlas", "graph_atlas_g"]

NUM_GRAPHS: Final = 1253
ATLAS_FILE: Traversable

def graph_atlas(i: int) -> ArrayLike: ...
def graph_atlas_g() -> ArrayLike: ...
