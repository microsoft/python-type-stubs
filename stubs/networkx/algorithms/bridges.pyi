from itertools import chain

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["bridges", "has_bridges", "local_bridges"]

def bridges(G: Graph, root=None): ...
def has_bridges(G: Graph, root=None) -> bool: ...
def local_bridges(G: Graph, with_span: bool = True, weight=None): ...
