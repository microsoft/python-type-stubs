from typing import Any

from ..classes.graph import Graph

__all__ = ["wiener_index"]

#: Rename the :func:`chain.from_iterable` function for the sake of
#: brevity.
chaini = ...

def wiener_index(G: Graph, weight: Any = None) -> float: ...
