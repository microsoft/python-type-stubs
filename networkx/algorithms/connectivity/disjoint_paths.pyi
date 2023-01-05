from ...classes.graph import Graph

# Define the default maximum flow function to use for the undelying
# maximum flow computations
from ...algorithms.flow import (
    edmonds_karp,
    preflow_push,
    shortest_augmenting_path,
)
from ...exception import NetworkXNoPath

default_flow_func = ...
from itertools import filterfalse as _filterfalse

# Functions to build auxiliary data structures.
from .utils import build_auxiliary_edge_connectivity, build_auxiliary_node_connectivity

__all__ = ["edge_disjoint_paths", "node_disjoint_paths"]

def edge_disjoint_paths(
    G: Graph,
    s,
    t,
    flow_func=None,
    cutoff: int | None = None,
    auxiliary=None,
    residual=None,
): ...
def node_disjoint_paths(
    G: Graph,
    s,
    t,
    flow_func=None,
    cutoff: int | None = None,
    auxiliary=None,
    residual=None,
): ...
