
from numpy.typing import ArrayLike

from ...exception import NetworkXException

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
