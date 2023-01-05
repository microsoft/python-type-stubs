from collections.abc import Iterable
from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..utils import not_implemented_for

from .distance_measures import diameter

__all__ = [
    "is_distance_regular",
    "is_strongly_regular",
    "intersection_array",
    "global_parameters",
]

def is_distance_regular(G: Graph) -> bool: ...
def global_parameters(b: ArrayLike, c: ArrayLike) -> Iterable: ...
def intersection_array(G: Graph): ...

# TODO There is a definition for directed strongly regular graphs.

def is_strongly_regular(G: Graph) -> bool: ...
