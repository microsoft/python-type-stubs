from typing import Mapping

# Define the default maximum flow function.
from ...classes.graph import Graph

default_flow_func = ...

__all__ = ["k_components"]

def k_components(G: Graph, flow_func=None) -> Mapping: ...
def build_k_number_dict(kcomps): ...
