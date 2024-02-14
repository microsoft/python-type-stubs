from itertools import chain, combinations, permutations, product

from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...exception import NetworkXException
from ...utils import arbitrary_element

__all__ = [
    "contracted_edge",
    "contracted_nodes",
    "equivalence_classes",
    "identified_nodes",
    "quotient_graph",
]

chaini = ...

def equivalence_classes(iterable: ArrayLike | tuple | set, relation): ...
def quotient_graph(
    G: Graph,
    partition,
    edge_relation=None,
    node_data=None,
    edge_data=None,
    relabel: bool = False,
    create_using=None,
): ...
def contracted_nodes(G: Graph, u, v, self_loops: bool = True, copy: bool = True): ...

identified_nodes = ...

def contracted_edge(G: Graph, edge: tuple, self_loops: bool = True, copy=True): ...
