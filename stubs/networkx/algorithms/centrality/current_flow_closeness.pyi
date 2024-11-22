from typing import Mapping

from ...classes.graph import Graph

__all__ = ["current_flow_closeness_centrality", "information_centrality"]

def current_flow_closeness_centrality(G: Graph, weight=None, dtype=..., solver="lu") -> Mapping: ...

information_centrality = ...
