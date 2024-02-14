import itertools

# Define the default maximum flow function to use in all flow based
# cut algorithms.
from ...algorithms.flow import build_residual_network, edmonds_karp
from ...classes.graph import Graph

default_flow_func = ...

from .utils import build_auxiliary_edge_connectivity, build_auxiliary_node_connectivity

__all__ = [
    "minimum_st_node_cut",
    "minimum_node_cut",
    "minimum_st_edge_cut",
    "minimum_edge_cut",
]

def minimum_st_edge_cut(G: Graph, s, t, flow_func=None, auxiliary=None, residual=None) -> set: ...
def minimum_st_node_cut(G: Graph, s, t, flow_func=None, auxiliary=None, residual=None) -> set: ...
def minimum_node_cut(G: Graph, s=None, t=None, flow_func=None) -> set: ...
def minimum_edge_cut(G: Graph, s=None, t=None, flow_func=None) -> set: ...
