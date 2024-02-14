import itertools

from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = ["biadjacency_matrix", "from_biadjacency_matrix"]

def biadjacency_matrix(
    G: Graph,
    row_order,
    column_order: ArrayLike | None = None,
    dtype=None,
    weight="weight",
    format="csr",
): ...
def from_biadjacency_matrix(A, create_using=None, edge_attribute: str = "weight"): ...
