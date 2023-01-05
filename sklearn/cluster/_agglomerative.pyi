from numpy import ndarray
from typing import Optional, Tuple, Union, Literal, Callable, Any
from numpy.typing import ArrayLike, NDArray
import warnings
from heapq import heapify, heappop, heappush, heappushpop

import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components

from ..base import BaseEstimator, ClusterMixin, _ClassNamePrefixFeaturesOutMixin
from ..metrics.pairwise import paired_distances
from ..utils.graph import _fix_connected_components
from ..utils.validation import check_memory

# mypy error: Module 'sklearn.cluster' has no attribute '_hierarchical_fast'
from . import _hierarchical_fast as _hierarchical  # type: ignore
from ._feature_agglomeration import AgglomerationTransform
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csr import csr_matrix
from scipy.sparse._lil import lil_matrix

###############################################################################
# For non fully-connected graphs

def _fix_connectivity(X: ndarray, connectivity: Union[csr_matrix, coo_matrix], affinity: str) -> Tuple[lil_matrix, int]: ...
def _single_linkage_tree(
    connectivity: coo_matrix,
    n_samples: int,
    n_nodes: int,
    n_clusters: None,
    n_connected_components: int,
    return_distance: bool,
) -> Tuple[ndarray, int, int, ndarray]: ...

###############################################################################
# Hierarchical tree building functions

def ward_tree(
    X: ArrayLike,
    *,
    connectivity: NDArray | None = None,
    n_clusters: int | None = None,
    return_distance: bool = False,
) -> tuple[np.ndarray, int, int, NDArray | None, np.ndarray]: ...

# single average and complete linkage
def linkage_tree(
    X: ArrayLike,
    connectivity: NDArray | None = None,
    n_clusters: int | None = None,
    linkage: Literal["average", "complete", "single"] = "complete",
    affinity: str | Callable = "euclidean",
    return_distance: bool = False,
) -> tuple[np.ndarray, int, int, NDArray | None, np.ndarray]: ...

# Matching names to tree-building strategies
def _complete_linkage(*args, **kwargs) -> Union[Tuple[ndarray, int, int, ndarray], Tuple[ndarray, int, int, None]]: ...
def _average_linkage(*args, **kwargs) -> Union[Tuple[ndarray, int, int, ndarray], Tuple[ndarray, int, int, None]]: ...
def _single_linkage(*args, **kwargs) -> Union[Tuple[ndarray, int, int, ndarray], Tuple[ndarray, int, int, None]]: ...

_TREE_BUILDERS = ...

###############################################################################
# Functions for cutting hierarchical clustering tree

def _hc_cut(n_clusters: int, children: ndarray, n_leaves: int) -> ndarray: ...

###############################################################################

class AgglomerativeClustering(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        n_clusters: int | None = 2,
        *,
        affinity: str | Callable = "euclidean",
        memory=None,
        connectivity: ArrayLike | Callable | None = None,
        compute_full_tree: bool | Literal["auto"] = "auto",
        linkage: Literal["ward", "complete", "average", "single"] = "ward",
        distance_threshold: float | None = None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "AgglomerativeClustering": ...
    def _fit(self, X: ndarray) -> Union[AgglomerativeClustering, FeatureAgglomeration]: ...
    def fit_predict(self, X: ArrayLike, y: None = None) -> NDArray: ...

class FeatureAgglomeration(_ClassNamePrefixFeaturesOutMixin, AgglomerativeClustering, AgglomerationTransform):
    def __init__(
        self,
        n_clusters: int = 2,
        *,
        affinity: str | Callable = "euclidean",
        memory=None,
        connectivity: ArrayLike | Callable | None = None,
        compute_full_tree: bool | Literal["auto"] = "auto",
        linkage: Literal["ward", "complete", "average", "single"] = "ward",
        pooling_func: Callable = ...,
        distance_threshold: float | None = None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "FeatureAgglomeration": ...
    @property
    def fit_predict(self): ...
