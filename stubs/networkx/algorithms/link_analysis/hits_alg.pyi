from typing import Mapping

from ...classes.graph import Graph

__all__ = ["hits", "hits_numpy", "hits_scipy", "authority_matrix", "hub_matrix"]

def hits(
    G: Graph,
    max_iter=100,
    tol: float = 1.0e-8,
    nstart: Mapping | None = None,
    normalized=True,
): ...
def authority_matrix(G: Graph, nodelist=None): ...
def hub_matrix(G: Graph, nodelist=None): ...
def hits_numpy(G: Graph, normalized=True): ...
def hits_scipy(
    G: Graph,
    max_iter=100,
    tol: float = 1.0e-6,
    nstart: Mapping | None = None,
    normalized=True,
): ...
