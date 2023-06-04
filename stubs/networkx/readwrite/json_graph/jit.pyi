import json
import warnings

from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

__all__ = ["jit_graph", "jit_data"]

def jit_graph(data, create_using=None): ...
def jit_data(G: Graph, indent=None, default=None): ...
