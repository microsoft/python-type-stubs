
from ..classes.graph import Graph

__all__ = ["line_graph", "inverse_line_graph"]

def line_graph(G: Graph, create_using=None): ...
def inverse_line_graph(G: Graph): ...
