from heapq import heappop, heappush
from itertools import count

from ...classes.graph import Graph

__all__ = ["astar_path", "astar_path_length"]

def astar_path(G: Graph, source, target, heuristic=None, weight="weight"): ...
def astar_path_length(G: Graph, source, target, heuristic=None, weight="weight"): ...
