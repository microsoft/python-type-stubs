from numpy.typing import ArrayLike
import heapq

from ..classes.graph import Graph

__all__ = [
    "is_graphical",
    "is_multigraphical",
    "is_pseudographical",
    "is_digraphical",
    "is_valid_degree_sequence_erdos_gallai",
    "is_valid_degree_sequence_havel_hakimi",
]

def is_graphical(sequence, method="eg") -> bool: ...
def is_valid_degree_sequence_havel_hakimi(deg_sequence: ArrayLike) -> bool: ...
def is_valid_degree_sequence_erdos_gallai(deg_sequence: ArrayLike) -> bool: ...
def is_multigraphical(sequence: ArrayLike) -> bool: ...
def is_pseudographical(sequence) -> bool: ...
def is_digraphical(in_sequence, out_sequence) -> bool: ...
