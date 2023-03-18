from typing import Any, Callable, ClassVar, Literal, TypeVar
from ..decomposition import KernelPCA as KernelPCA
from scipy.sparse._csr import csr_matrix
from ..preprocessing import KernelCenterer as KernelCenterer
from scipy.sparse.csgraph import (
    shortest_path as shortest_path,
    connected_components as connected_components,
)
from ..neighbors._ball_tree import BallTree
from ..neighbors._kd_tree import KDTree
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from ..neighbors import (
    NearestNeighbors,
    kneighbors_graph as kneighbors_graph,
    radius_neighbors_graph as radius_neighbors_graph,
)
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from scipy.sparse import issparse as issparse
from .._typing import Float, Int, ArrayLike, MatrixLike
from ..utils.validation import check_is_fitted as check_is_fitted

Isomap_Self = TypeVar("Isomap_Self", bound="Isomap")


# Author: Jake Vanderplas  -- <vanderplas@astro.washington.edu>
# License: BSD 3 clause (C) 2011
import warnings

import numpy as np


class Isomap(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dist_matrix_: ArrayLike = ...
    nbrs_: NearestNeighbors = ...
    kernel_pca_: Any = ...
    embedding_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_neighbors: None | int = 5,
        radius: None | Float = None,
        n_components: Int = 2,
        eigen_solver: Literal["auto", "arpack", "dense", "auto"] = "auto",
        tol: Float = 0,
        max_iter: None | Int = None,
        path_method: Literal["auto", "FW", "D", "auto"] = "auto",
        neighbors_algorithm: Literal[
            "auto", "brute", "kd_tree", "ball_tree", "auto"
        ] = "auto",
        n_jobs: None | int = None,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: None | dict = None,
    ) -> None:
        ...

    def reconstruction_error(self) -> float:
        ...

    def fit(
        self: Isomap_Self,
        X: ArrayLike | BallTree | NearestNeighbors | KDTree | csr_matrix,
        y: Any = None,
    ) -> Isomap_Self:
        ...

    def fit_transform(self, X: BallTree | ArrayLike | KDTree, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
