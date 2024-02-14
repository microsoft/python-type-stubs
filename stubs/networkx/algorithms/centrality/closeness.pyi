import functools
from typing import Mapping

from ...classes.graph import Graph
from ...exception import NetworkXError
from ...utils.decorators import not_implemented_for

__all__ = ["closeness_centrality", "incremental_closeness_centrality"]

def closeness_centrality(G: Graph, u=None, distance=None, wf_improved=True) -> Mapping: ...
def incremental_closeness_centrality(
    G: Graph,
    edge: tuple,
    prev_cc: Mapping | None = None,
    insertion: bool = True,
    wf_improved=True,
) -> Mapping: ...
