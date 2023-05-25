from collections import deque

from ...classes.graph import Graph

__all__ = [
    "bfs_edges",
    "bfs_tree",
    "bfs_predecessors",
    "bfs_successors",
    "descendants_at_distance",
    "bfs_layers",
]

def generic_bfs_edges(
    G: Graph, source, neighbors=None, depth_limit=None, sort_neighbors=None
): ...
def bfs_edges(
    G: Graph, source, reverse: bool = False, depth_limit=None, sort_neighbors=None
): ...
def bfs_tree(
    G: Graph, source, reverse: bool = False, depth_limit=None, sort_neighbors=None
): ...
def bfs_predecessors(G: Graph, source, depth_limit=None, sort_neighbors=None): ...
def bfs_successors(G: Graph, source, depth_limit=None, sort_neighbors=None): ...
def bfs_layers(G: Graph, sources): ...
def descendants_at_distance(G: Graph, source, distance): ...
