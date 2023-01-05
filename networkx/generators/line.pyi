from collections import defaultdict
from functools import partial
from itertools import combinations

from ..classes.graph import Graph
from ..utils import arbitrary_element
from ..utils.decorators import not_implemented_for

__all__ = ["line_graph", "inverse_line_graph"]

def line_graph(G: Graph, create_using=None): ...
def inverse_line_graph(G: Graph): ...
