from typing import Mapping
import math

from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = ["eigenvector_centrality", "eigenvector_centrality_numpy"]

def eigenvector_centrality(
    G: Graph, max_iter=100, tol=1.0e-6, nstart=None, weight=None
) -> Mapping: ...
def eigenvector_centrality_numpy(
    G: Graph, weight=None, max_iter=50, tol=0
) -> Mapping: ...
