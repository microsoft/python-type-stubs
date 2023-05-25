from typing import Mapping
from itertools import combinations

from ...classes.graph import Graph

__all__ = ["dispersion"]

def dispersion(
    G: Graph, u=None, v=None, normalized: bool = True, alpha=1.0, b=0.0, c=0.0
) -> Mapping: ...
