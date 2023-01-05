from collections import deque

from ...classes.graph import Graph

FORWARD: str = ...
REVERSE: str = ...

__all__ = ["edge_bfs"]

def edge_bfs(G: Graph, source=None, orientation=None): ...
