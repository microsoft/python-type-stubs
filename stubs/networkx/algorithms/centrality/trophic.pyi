from collections.abc import Mapping

from ...classes.digraph import DiGraph
from ...utils import not_implemented_for

__all__ = ["trophic_levels", "trophic_differences", "trophic_incoherence_parameter"]

def trophic_levels(G: DiGraph, weight="weight") -> Mapping: ...
def trophic_differences(G: DiGraph, weight="weight") -> Mapping: ...
def trophic_incoherence_parameter(G: DiGraph, weight="weight", cannibalism: bool = False) -> float: ...
