from collections import deque

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["tutte_polynomial", "chromatic_polynomial"]

def tutte_polynomial(G: Graph): ...
def chromatic_polynomial(G: Graph): ...
