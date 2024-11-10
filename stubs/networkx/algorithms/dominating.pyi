from collections.abc import Iterable

from ..classes.graph import Graph

__all__ = ["dominating_set", "is_dominating_set"]

def dominating_set(G: Graph, start_with=None) -> set: ...
def is_dominating_set(G: Graph, nbunch: Iterable): ...
