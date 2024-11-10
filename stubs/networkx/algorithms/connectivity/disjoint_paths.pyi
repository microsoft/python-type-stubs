# Define the default maximum flow function to use for the undelying
# maximum flow computations
from ...classes.graph import Graph

default_flow_func = ...

# Functions to build auxiliary data structures.

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
