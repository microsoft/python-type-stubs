from collections import Counter
from collections.abc import Iterable

from ...algorithms.components import is_connected
from ...classes.graph import Graph
from ...exception import NetworkXError
from ...utils import groups, not_implemented_for, py_random_state

__all__ = ["asyn_fluidc"]

@py_random_state(3)
def asyn_fluidc(G: Graph, k, max_iter=100, seed=None) -> Iterable: ...
