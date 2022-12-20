from ...classes.digraph import DiGraph
from ...classes.multidigraph import MultiDiGraph
from ...utils.decorators import not_implemented_for

__all__ = [
    "number_attracting_components",
    "attracting_components",
    "is_attracting_component",
]

def attracting_components(G: DiGraph | MultiDiGraph): ...
def number_attracting_components(G: DiGraph | MultiDiGraph) -> int: ...
def is_attracting_component(G: DiGraph | MultiDiGraph) -> bool: ...
