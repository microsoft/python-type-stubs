from typing import Mapping

from ...classes.graph import Graph

__all__ = ["cytoscape_data", "cytoscape_graph"]

def cytoscape_data(G: Graph, attrs=None, name: str = "name", ident: str = "id") -> Mapping: ...
def cytoscape_graph(data: Mapping, attrs=None, name: str = "name", ident: str = "id"): ...
