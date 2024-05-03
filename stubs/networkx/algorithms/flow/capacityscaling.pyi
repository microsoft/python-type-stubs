__all__ = ["capacity_scaling"]

from itertools import chain
from math import log

from ...classes.graph import Graph
from ...utils import BinaryHeap, arbitrary_element, not_implemented_for

def capacity_scaling(
    G: Graph,
    demand: str = "demand",
    capacity: str = "capacity",
    weight: str = "weight",
    heap=...,
): ...
