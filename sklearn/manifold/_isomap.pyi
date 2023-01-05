from sklearn.neighbors._unsupervised import NearestNeighbors
from typing import Union, Literal, Callable, Mapping, Any
from numpy.typing import ArrayLike

# Author: Jake Vanderplas  -- <vanderplas@astro.washington.edu>
# License: BSD 3 clause (C) 2011
import warnings

import numpy as np

from scipy.sparse import issparse
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import connected_components

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..neighbors import NearestNeighbors, kneighbors_graph
from ..neighbors import radius_neighbors_graph
from ..utils.validation import check_is_fitted
from ..decomposition import KernelPCA
from ..preprocessing import KernelCenterer
from ..utils.graph import _fix_connected_components
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

class Isomap(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        n_neighbors: int | None = 5,
        radius: float | None = None,
        n_components: int = 2,
        eigen_solver: Literal["auto", "arpack", "dense"] = "auto",
        tol: float = 0,
        max_iter: int | None = None,
        path_method: Literal["auto", "FW", "D"] = "auto",
        neighbors_algorithm: Literal["auto", "brute", "kd_tree", "ball_tree"] = "auto",
        n_jobs: int | None = None,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
    ) -> None: ...
    def _fit_transform(self, X: Union[ndarray, csr_matrix]) -> None: ...
    def reconstruction_error(self) -> float: ...
    def fit(self, X: ArrayLike | BallTree | KDTree | NearestNeighbors, y: None = None) -> "Isomap": ...
    def fit_transform(self, X: ArrayLike | BallTree | KDTree, y: None = None) -> ArrayLike: ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
