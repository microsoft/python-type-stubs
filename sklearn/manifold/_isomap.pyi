from typing import Any, Callable, Literal
from .._typing import Float, Int, MatrixLike
from ..preprocessing import KernelCenterer as KernelCenterer
from scipy.sparse import issparse as issparse
from ..neighbors._unsupervised import NearestNeighbors
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..neighbors import (
    kneighbors_graph as kneighbors_graph,
    radius_neighbors_graph as radius_neighbors_graph,
)
from ..decomposition import KernelPCA as KernelPCA
from ..neighbors._ball_tree import BallTree
from ..utils.validation import check_is_fitted as check_is_fitted
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from ..neighbors import KDTree
from scipy.sparse.csgraph import (
    shortest_path as shortest_path,
    connected_components as connected_components,
)
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from numbers import Integral as Integral, Real as Real

# Author: Jake Vanderplas  -- <vanderplas@astro.washington.edu>
# License: BSD 3 clause (C) 2011
import warnings

import numpy as np


class Isomap(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        n_neighbors: int | None = 5,
        radius: None | Float = None,
        n_components: Int = 2,
        eigen_solver: Literal["auto", "arpack", "dense", "auto"] = "auto",
        tol: Float = 0,
        max_iter: None | Int = None,
        path_method: Literal["auto", "FW", "D", "auto"] = "auto",
        neighbors_algorithm: Literal[
            "auto", "brute", "kd_tree", "ball_tree", "auto"
        ] = "auto",
        n_jobs: int | None = None,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: dict | None = None,
    ) -> None:
        ...

    def reconstruction_error(self) -> float:
        ...

    def fit(
        self, X: NearestNeighbors | KDTree | BallTree | csr_matrix, y: Any = None
    ) -> Any:
        ...

    def fit_transform(self, X: KDTree | BallTree | ndarray, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
