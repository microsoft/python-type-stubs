from typing import Literal, Callable
from numpy.typing import ArrayLike

import itertools
import warnings
from collections import defaultdict

from .classes.graph import Graph
from .utils import not_implemented_for

__all__ = [
    "from_numpy_matrix",
    "to_numpy_matrix",
    "from_pandas_adjacency",
    "to_pandas_adjacency",
    "from_pandas_edgelist",
    "to_pandas_edgelist",
    "to_numpy_recarray",
    "from_scipy_sparse_array",
    "from_scipy_sparse_matrix",
    "to_scipy_sparse_array",
    "to_scipy_sparse_matrix",
    "from_numpy_array",
    "to_numpy_array",
]

def to_pandas_adjacency(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    order=None,
    multigraph_weight=...,
    weight: str | None = "weight",
    nonedge: float = 0.0,
): ...
def from_pandas_adjacency(df, create_using=None): ...
def to_pandas_edgelist(
    G: Graph,
    source: str | int = "source",
    target: str | int = "target",
    nodelist: ArrayLike | None = None,
    dtype=None,
    order=None,
    edge_key=None,
): ...
def from_pandas_edgelist(
    df,
    source: str | int = "source",
    target: str | int = "target",
    edge_attr=None,
    create_using=None,
    edge_key=None,
): ...
def to_numpy_matrix(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight=...,
    weight="weight",
    nonedge=0.0,
): ...
def from_numpy_matrix(A, parallel_edges: bool = False, create_using=None): ...
def to_numpy_recarray(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    order: Literal["C", "F"] | None = None,
): ...
def to_scipy_sparse_array(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    weight="weight",
    format="csr",
): ...
def to_scipy_sparse_matrix(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    weight="weight",
    format="csr",
): ...
def from_scipy_sparse_matrix(
    A, parallel_edges: bool = False, create_using=None, edge_attribute: str = "weight"
): ...
def from_scipy_sparse_array(
    A, parallel_edges: bool = False, create_using=None, edge_attribute: str = "weight"
): ...
def to_numpy_array(
    G: Graph,
    nodelist: ArrayLike | None = None,
    dtype=None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight: Callable = ...,
    weight="weight",
    nonedge=0.0,
): ...
def from_numpy_array(A, parallel_edges: bool = False, create_using=None): ...
