from ...classes.graph import Graph
from .boykovkolmogorov import boykov_kolmogorov
from .dinitz_alg import dinitz
from .edmondskarp import edmonds_karp
from .preflowpush import preflow_push
from .shortestaugmentingpath import shortest_augmenting_path
from .utils import build_flow_dict

# Define the default flow function for computing maximum flow.
default_flow_func = ...
# Functions that don't support cutoff for minimum cut computations.
flow_funcs: list = ...

__all__ = ["maximum_flow", "maximum_flow_value", "minimum_cut", "minimum_cut_value"]

def maximum_flow(
    flowG: Graph, _s, _t, capacity: str = "capacity", flow_func=None, **kwargs
): ...
def maximum_flow_value(
    flowG: Graph, _s, _t, capacity: str = "capacity", flow_func=None, **kwargs
): ...
def minimum_cut(
    flowG: Graph, _s, _t, capacity: str = "capacity", flow_func=None, **kwargs
): ...
def minimum_cut_value(
    flowG: Graph, _s, _t, capacity: str = "capacity", flow_func=None, **kwargs
): ...
