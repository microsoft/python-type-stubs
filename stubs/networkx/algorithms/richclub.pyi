from typing import Mapping

from ..classes.graph import Graph

__all__ = ["rich_club_coefficient"]

def rich_club_coefficient(G: Graph, normalized=True, Q=100, seed=None) -> Mapping: ...
