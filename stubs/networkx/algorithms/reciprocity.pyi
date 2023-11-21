from typing import Mapping

from networkx import NetworkXError

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["reciprocity", "overall_reciprocity"]

def reciprocity(G: Graph, nodes=None) -> Mapping: ...
def overall_reciprocity(G: Graph): ...
