from typing import Mapping
from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = [
    "extrema_bounding",
    "eccentricity",
    "diameter",
    "radius",
    "periphery",
    "center",
    "barycenter",
    "resistance_distance",
]

def extrema_bounding(G: Graph, compute="diameter"): ...
def eccentricity(G: Graph, v=None, sp=None) -> Mapping: ...
def diameter(G: Graph, e=None, usebounds=False): ...
def periphery(G: Graph, e=None, usebounds=False) -> ArrayLike: ...
def radius(G: Graph, e=None, usebounds=False): ...
def center(G: Graph, e=None, usebounds=False) -> ArrayLike: ...
def barycenter(G: Graph, weight=None, attr=None, sp=None) -> ArrayLike: ...
def resistance_distance(
    G: Graph, nodeA, nodeB, weight=None, invert_weight=True
) -> float: ...
