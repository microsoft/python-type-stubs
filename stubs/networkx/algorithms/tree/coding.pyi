from collections import Counter
from itertools import chain

from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...exception import NetworkXException
from ...utils import not_implemented_for

__all__ = [
    "from_nested_tuple",
    "from_prufer_sequence",
    "NotATree",
    "to_nested_tuple",
    "to_prufer_sequence",
]

class NotATree(NetworkXException):
    pass

def to_nested_tuple(T, root, canonical_form: bool = False) -> tuple: ...
def from_nested_tuple(sequence: tuple, sensible_relabeling: bool = False): ...
def to_prufer_sequence(T) -> ArrayLike: ...
def from_prufer_sequence(sequence: ArrayLike): ...
