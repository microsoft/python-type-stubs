from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = ["random_cograph"]

@py_random_state(1)
def random_cograph(n: int, seed=None): ...
