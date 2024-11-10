from typing import Mapping

# Define the default maximum flow function to use in all flow based
# connectivity algorithms.
from ...classes.graph import Graph

default_flow_func = ...


__all__ = [
    "average_node_connectivity",
    "local_node_connectivity",
    "node_connectivity",
    "local_edge_connectivity",
    "edge_connectivity",
    "all_pairs_node_connectivity",
]

def local_node_connectivity(G: Graph, s, t, flow_func=None, auxiliary=None, residual=None, cutoff=None): ...
def node_connectivity(G: Graph, s=None, t=None, flow_func=None): ...
def average_node_connectivity(G: Graph, flow_func=None) -> float: ...
def all_pairs_node_connectivity(G: Graph, nbunch=None, flow_func=None) -> Mapping: ...
def local_edge_connectivity(G: Graph, s, t, flow_func=None, auxiliary=None, residual=None, cutoff=None): ...
def edge_connectivity(G: Graph, s=None, t=None, flow_func=None, cutoff=None): ...
