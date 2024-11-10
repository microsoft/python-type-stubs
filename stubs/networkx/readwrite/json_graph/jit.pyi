
from ...classes.graph import Graph

__all__ = ["jit_graph", "jit_data"]

def jit_graph(data, create_using=None): ...
def jit_data(G: Graph, indent=None, default=None): ...
