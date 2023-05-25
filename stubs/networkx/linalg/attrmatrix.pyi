from numpy.typing import ArrayLike

from ..classes.graph import Graph

__all__ = ["attr_matrix", "attr_sparse_matrix"]

def attr_matrix(
    G: Graph,
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: ArrayLike | None = None,
    dtype=None,
    order=None,
): ...
def attr_sparse_matrix(
    G: Graph,
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: ArrayLike | None = None,
    dtype=None,
): ...
