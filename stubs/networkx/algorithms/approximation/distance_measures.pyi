from ...classes.graph import Graph
from ...utils.decorators import py_random_state

__all__ = ["diameter"]

@py_random_state(1)
def diameter(G: Graph, seed=None): ...
