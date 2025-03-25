from collections.abc import Mapping
from itertools import chain

from ...classes.graph import Graph

__all__ = ["tree_data", "tree_graph"]

# NOTE: Remove attrs from signature in 3.0
def tree_data(
    G: Graph,
    root,
    attrs: Mapping | None = None,
    ident: str = "id",
    children: str = "children",
) -> Mapping: ...
def tree_graph(
    data: Mapping,
    attrs: Mapping | None = None,
    ident: str = "id",
    children: str = "children",
): ...
