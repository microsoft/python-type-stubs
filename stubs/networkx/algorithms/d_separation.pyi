from collections import deque

from ..classes.graph import Graph
from ..utils import UnionFind, not_implemented_for

__all__ = ["d_separated"]

def d_separated(G: Graph, x: set, y: set, z: set) -> bool: ...
