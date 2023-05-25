from collections.abc import Iterable
from typing import Any
from itertools import chain
from ..classes.graph import Graph

__all__ = ["edge_boundary", "node_boundary"]

def edge_boundary(
    G: Graph,
    nbunch1: Iterable,
    nbunch2: Iterable | None = None,
    data: bool | Any = False,
    keys: bool = False,
    default: Any = None,
): ...
def node_boundary(
    G: Graph, nbunch1: Iterable, nbunch2: Iterable | None = None
) -> set: ...
