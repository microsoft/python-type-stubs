from typing import Any

from itertools import chain

from ..classes.graph import Graph
from .components import is_connected, is_strongly_connected
from .shortest_paths import shortest_path_length as spl

__all__ = ["wiener_index"]

#: Rename the :func:`chain.from_iterable` function for the sake of
#: brevity.
chaini = ...

def wiener_index(G: Graph, weight: Any = None) -> float: ...
