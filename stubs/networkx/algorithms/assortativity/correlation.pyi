from ...classes.graph import Graph
from .mixing import (
    attribute_mixing_matrix,
    degree_mixing_matrix,
)
from .pairs import node_degree_xy

__all__ = [
    "degree_pearson_correlation_coefficient",
    "degree_assortativity_coefficient",
    "attribute_assortativity_coefficient",
    "numeric_assortativity_coefficient",
]

def degree_assortativity_coefficient(
    G: Graph, x="out", y="in", weight=None, nodes=None
) -> float: ...
def degree_pearson_correlation_coefficient(
    G: Graph, x="out", y="in", weight=None, nodes=None
) -> float: ...
def attribute_assortativity_coefficient(
    G: Graph, attribute: str, nodes=None
) -> float: ...
def numeric_assortativity_coefficient(
    G: Graph, attribute: str, nodes=None
) -> float: ...
def attribute_ac(M): ...
