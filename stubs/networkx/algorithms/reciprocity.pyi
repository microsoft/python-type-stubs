from typing import Mapping

from ..classes.graph import Graph

__all__ = ["reciprocity", "overall_reciprocity"]

def reciprocity(G: Graph, nodes=None) -> Mapping: ...
def overall_reciprocity(G: Graph): ...
