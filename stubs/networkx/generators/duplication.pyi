from ..classes.graph import Graph
from ..exception import NetworkXError
from ..utils import py_random_state

__all__ = ["partial_duplication_graph", "duplication_divergence_graph"]

@py_random_state(4)
def partial_duplication_graph(N: int, n: int, p: float, q: float, seed=None): ...
@py_random_state(2)
def duplication_divergence_graph(n: int, p: float, seed=None) -> Graph: ...
