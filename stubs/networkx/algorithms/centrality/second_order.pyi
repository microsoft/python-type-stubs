from collections.abc import Mapping

from ...classes.graph import Graph
from ...utils import not_implemented_for

# Authors: Erwan Le Merrer (erwan.lemerrer@technicolor.com)

__all__ = ["second_order_centrality"]

def second_order_centrality(G: Graph) -> Mapping: ...
