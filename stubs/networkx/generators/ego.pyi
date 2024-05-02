__all__ = ["ego_graph"]

from ..classes.graph import Graph

def ego_graph(G: Graph, n, radius=1, center: bool = True, undirected: bool = False, distance=None): ...
