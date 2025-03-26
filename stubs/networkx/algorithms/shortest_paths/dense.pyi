from collections.abc import Mapping

from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = [
    "floyd_warshall",
    "floyd_warshall_predecessor_and_distance",
    "reconstruct_path",
    "floyd_warshall_numpy",
]

def floyd_warshall_numpy(G: Graph, nodelist=None, weight="weight"): ...
def floyd_warshall_predecessor_and_distance(G: Graph, weight="weight") -> dict: ...
def reconstruct_path(source, target, predecessors: Mapping) -> ArrayLike: ...
def floyd_warshall(G: Graph, weight="weight") -> Mapping: ...
