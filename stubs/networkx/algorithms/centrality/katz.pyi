import math
from collections.abc import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = ["katz_centrality", "katz_centrality_numpy"]

def katz_centrality(
    G: Graph,
    alpha: float = 0.1,
    beta=1.0,
    max_iter=1000,
    tol=1.0e-6,
    nstart: Mapping | None = None,
    normalized=True,
    weight=None,
) -> Mapping: ...
def katz_centrality_numpy(
    G: Graph,
    alpha: float = 0.1,
    beta=1.0,
    normalized: bool = True,
    weight: str | None = None,
) -> Mapping: ...
