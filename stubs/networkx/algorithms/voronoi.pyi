from typing import Mapping
from ..classes.graph import Graph
from ..utils import groups

__all__ = ["voronoi_cells"]

def voronoi_cells(G: Graph, center_nodes: set, weight="weight") -> Mapping: ...
