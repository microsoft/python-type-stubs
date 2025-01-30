import math
import types
from itertools import permutations
from typing import Callable

from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = [
    "categorical_node_match",
    "categorical_edge_match",
    "categorical_multiedge_match",
    "numerical_node_match",
    "numerical_edge_match",
    "numerical_multiedge_match",
    "generic_node_match",
    "generic_edge_match",
    "generic_multiedge_match",
]

def copyfunc(f, name=None): ...
def allclose(x, y, rtol: float = ..., atol: float = 1e-08): ...

categorical_doc: str = ...

def categorical_node_match(attr: str | ArrayLike, default): ...

categorical_edge_match = ...

def categorical_multiedge_match(attr: str | ArrayLike, default): ...

# Docstrings for categorical functions.
tmpdoc = ...

numerical_doc: str = ...

def numerical_node_match(
    attr: str | ArrayLike,
    default,
    rtol: float = ...,
    atol: float = 1e-08,
): ...

numerical_edge_match = ...

def numerical_multiedge_match(
    attr: str | ArrayLike,
    default,
    rtol: float = ...,
    atol: float = 1e-08,
): ...

# Docstrings for numerical functions.
tmpdoc = ...

generic_doc: str = ...

def generic_node_match(attr: str | ArrayLike, default, op: ArrayLike | Callable): ...

generic_edge_match = ...

def generic_multiedge_match(attr: str | ArrayLike, default, op: ArrayLike | Callable): ...
