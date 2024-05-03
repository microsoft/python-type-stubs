from ...classes.graph import Graph
from ...utils import not_implemented_for
from .edmondskarp import edmonds_karp
from .utils import build_residual_network

default_flow_func = ...

__all__ = ["gomory_hu_tree"]

def gomory_hu_tree(G: Graph, capacity: str = "capacity", flow_func=None): ...
