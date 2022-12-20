from itertools import combinations

from ..classes.graph import Graph

from ..utils import arbitrary_element, not_implemented_for

__all__ = [
    "is_eulerian",
    "eulerian_circuit",
    "eulerize",
    "is_semieulerian",
    "has_eulerian_path",
    "eulerian_path",
]

def is_eulerian(G: Graph): ...
def is_semieulerian(G: Graph): ...
def eulerian_circuit(G: Graph, source=None, keys: bool = False): ...
def has_eulerian_path(G: Graph, source=None): ...
def eulerian_path(G: Graph, source=None, keys=False): ...
def eulerize(G: Graph): ...
