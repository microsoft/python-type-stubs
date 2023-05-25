from itertools import islice

from ...classes.graph import Graph

from ...utils import BinaryHeap, arbitrary_element, not_implemented_for

__all__ = ["stoer_wagner"]

def stoer_wagner(G: Graph, weight: str = "weight", heap=...): ...
