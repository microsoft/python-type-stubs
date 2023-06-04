from typing import Mapping

from itertools import accumulate

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["rich_club_coefficient"]

def rich_club_coefficient(G: Graph, normalized=True, Q=100, seed=None) -> Mapping: ...
