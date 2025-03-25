from collections.abc import Mapping
from warnings import warn

from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["pagerank", "pagerank_numpy", "pagerank_scipy", "google_matrix"]

def pagerank(
    G: Graph,
    alpha: float = 0.85,
    personalization: Mapping | None = None,
    max_iter=100,
    tol: float = 1.0e-6,
    nstart: Mapping | None = None,
    weight="weight",
    dangling: Mapping | None = None,
) -> Mapping: ...
def google_matrix(
    G: Graph,
    alpha: float = 0.85,
    personalization: Mapping | None = None,
    nodelist: ArrayLike | None = None,
    weight="weight",
    dangling: Mapping | None = None,
): ...
def pagerank_numpy(
    G: Graph,
    alpha: float = 0.85,
    personalization: Mapping | None = None,
    weight="weight",
    dangling: Mapping | None = None,
) -> Mapping: ...
def pagerank_scipy(
    G: Graph,
    alpha: float = 0.85,
    personalization: Mapping | None = None,
    max_iter=100,
    tol: float = 1.0e-6,
    nstart: Mapping | None = None,
    weight="weight",
    dangling: Mapping | None = None,
) -> Mapping: ...
