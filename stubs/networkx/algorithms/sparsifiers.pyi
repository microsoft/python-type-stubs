from typing import Any

from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = ["spanner"]

@py_random_state(3)
def spanner(G: Graph, stretch: float, weight: Any = None, seed=None): ...
