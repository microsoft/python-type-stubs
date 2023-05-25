import warnings

from ..utils import edges_equal, graphs_equal, nodes_equal

__all__ = [
    "assert_nodes_equal",
    "assert_edges_equal",
    "assert_graphs_equal",
    "almost_equal",
]

def almost_equal(x, y, places=7): ...
def assert_nodes_equal(nodes1, nodes2): ...
def assert_edges_equal(edges1, edges2): ...
def assert_graphs_equal(graph1, graph2): ...
