from collections import defaultdict
from itertools import combinations
from operator import itemgetter
from typing import Mapping

# Define the default maximum flow function.
from ...algorithms.flow import edmonds_karp
from ...classes.graph import Graph
from ...utils import not_implemented_for

default_flow_func = ...

__all__ = ["k_components"]

def k_components(G: Graph, flow_func=None) -> Mapping: ...
def build_k_number_dict(kcomps): ...
