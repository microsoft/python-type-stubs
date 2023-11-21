from typing import Mapping

from ...classes.graph import Graph
from ...utils import dict_to_numpy_array
from .pairs import node_attribute_xy, node_degree_xy

__all__ = [
    "attribute_mixing_matrix",
    "attribute_mixing_dict",
    "degree_mixing_matrix",
    "degree_mixing_dict",
    "numeric_mixing_matrix",
    "mixing_dict",
]

def attribute_mixing_dict(G: Graph, attribute: str, nodes=None, normalized=False) -> Mapping: ...
def attribute_mixing_matrix(
    G: Graph,
    attribute: str,
    nodes=None,
    mapping: Mapping | None = None,
    normalized=True,
): ...
def degree_mixing_dict(G: Graph, x="out", y="in", weight=None, nodes=None, normalized=False) -> Mapping: ...
def degree_mixing_matrix(
    G: Graph,
    x="out",
    y="in",
    weight=None,
    nodes=None,
    normalized=True,
    mapping: Mapping | None = None,
): ...
def numeric_mixing_matrix(
    G: Graph,
    attribute: str,
    nodes=None,
    normalized=True,
    mapping: Mapping | None = None,
): ...
def mixing_dict(xy, normalized=False) -> Mapping: ...
