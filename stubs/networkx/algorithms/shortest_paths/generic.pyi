from ...classes.graph import Graph

__all__ = [
    "shortest_path",
    "all_shortest_paths",
    "shortest_path_length",
    "average_shortest_path_length",
    "has_path",
]

def has_path(G: Graph, source, target): ...
def shortest_path(
    G: Graph, source=None, target=None, weight=None, method="dijkstra"
) -> list | dict: ...
def shortest_path_length(
    G: Graph, source=None, target=None, weight=None, method="dijkstra"
): ...
def average_shortest_path_length(G: Graph, weight=None, method=None): ...
def all_shortest_paths(G: Graph, source, target, weight=None, method="dijkstra"): ...
