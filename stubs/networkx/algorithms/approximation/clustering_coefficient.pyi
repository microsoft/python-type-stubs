from ...utils import not_implemented_for, py_random_state
from ...classes.graph import Graph

__all__ = ["average_clustering"]

@py_random_state(2)
def average_clustering(G: Graph, trials=1000, seed=None) -> float: ...
