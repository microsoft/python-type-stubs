from functools import reduce

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["immediate_dominators", "dominance_frontiers"]

def immediate_dominators(G: Graph, start): ...
def dominance_frontiers(G: Graph, start): ...
