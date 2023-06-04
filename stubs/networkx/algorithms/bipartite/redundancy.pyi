from typing import Mapping
from itertools import combinations

from networkx import NetworkXError
from ...classes.graph import Graph

__all__ = ["node_redundancy"]

def node_redundancy(G: Graph, nodes=None) -> Mapping: ...
