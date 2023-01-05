from typing import Literal, Mapping
from collections import defaultdict

from ...classes.graph import Graph

__all__ = ["average_degree_connectivity", "k_nearest_neighbors"]

def average_degree_connectivity(
    G: Graph,
    source="in+out",
    target: Literal["in+out", "out", "in"] = "in+out",
    nodes=None,
    weight=None,
) -> Mapping: ...
def k_nearest_neighbors(
    G: Graph, source="in+out", target="in+out", nodes=None, weight=None
): ...
