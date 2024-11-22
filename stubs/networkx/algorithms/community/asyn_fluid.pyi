from collections.abc import Iterable

from ...classes.graph import Graph
from ...utils import py_random_state

__all__ = ["asyn_fluidc"]

@py_random_state(3)
def asyn_fluidc(G: Graph, k, max_iter=100, seed=None) -> Iterable: ...
