
from ..classes.graph import Graph

__all__ = ["immediate_dominators", "dominance_frontiers"]

def immediate_dominators(G: Graph, start): ...
def dominance_frontiers(G: Graph, start): ...
