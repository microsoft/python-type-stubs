from ...utils.decorators import py_random_state
from ...classes.graph import Graph

__all__ = ["diameter"]

@py_random_state(1)
def diameter(G: Graph, seed=None): ...
