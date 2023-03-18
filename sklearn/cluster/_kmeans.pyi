from typing import Any, Callable, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils.extmath import row_norms as row_norms, stable_cumsum as stable_cumsum
from ..utils.fixes import (
    threadpool_limits as threadpool_limits,
    threadpool_info as threadpool_info,
)
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.sparsefuncs_fast import assign_rows_csr as assign_rows_csr
from ._k_means_common import CHUNK_SIZE as CHUNK_SIZE
from ..metrics.pairwise import euclidean_distances as euclidean_distances
from ..utils.validation import check_is_fitted as check_is_fitted
from ..utils._readonly_array_wrapper import ReadonlyArrayWrapper as ReadonlyArrayWrapper
from abc import ABC, abstractmethod as abstractmethod
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from numbers import Integral as Integral, Real as Real
from ..base import (
    BaseEstimator,
    ClusterMixin,
    TransformerMixin,
    ClassNamePrefixFeaturesOutMixin,
)
from ._k_means_lloyd import (
    lloyd_iter_chunked_dense as lloyd_iter_chunked_dense,
    lloyd_iter_chunked_sparse as lloyd_iter_chunked_sparse,
)
from ..utils import check_array as check_array, check_random_state as check_random_state
from .._typing import MatrixLike, ArrayLike, Int, Float
from ._k_means_elkan import (
    init_bounds_dense as init_bounds_dense,
    init_bounds_sparse as init_bounds_sparse,
    elkan_iter_chunked_dense as elkan_iter_chunked_dense,
    elkan_iter_chunked_sparse as elkan_iter_chunked_sparse,
)

KMeans_Self = TypeVar("KMeans_Self", bound="KMeans")
MiniBatchKMeans_Self = TypeVar("MiniBatchKMeans_Self", bound="MiniBatchKMeans")

import warnings

import numpy as np
import scipy.sparse as sp


###############################################################################
# Initialization heuristic


def kmeans_plusplus(
    X: MatrixLike | ArrayLike,
    n_clusters: Int,
    *,
    x_squared_norms: None | ArrayLike = None,
    random_state: None | RandomState | int = None,
    n_local_trials: None | Int = None,
) -> tuple[ndarray, ndarray]:
    ...


def k_means(
    X: MatrixLike | ArrayLike,
    n_clusters: Int,
    *,
    sample_weight: None | ArrayLike = None,
    init: MatrixLike
    | Callable
    | Literal["k-means++", "random", "k-means++"] = "k-means++",
    n_init: Literal["auto", "warn"] | int = "warn",
    max_iter: Int = 300,
    verbose: bool = False,
    tol: Float = 1e-4,
    random_state: RandomState | None | Int = None,
    copy_x: bool = True,
    algorithm: Literal["lloyd", "elkan", "auto", "full", "lloyd"] = "lloyd",
    return_n_iter: bool = False,
) -> tuple[ndarray, ndarray, float] | tuple[ndarray, ndarray, float, int]:
    ...


class _BaseKMeans(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, ClusterMixin, BaseEstimator, ABC
):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: Int,
        *,
        init,
        n_init,
        max_iter,
        tol,
        verbose,
        random_state,
    ) -> None:
        ...

    def fit_predict(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> ndarray:
        ...

    def predict(
        self, X: MatrixLike | ArrayLike, sample_weight: None | ArrayLike = None
    ) -> ndarray:
        ...

    def fit_transform(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> float:
        ...


class KMeans(_BaseKMeans):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    inertia_: float = ...
    labels_: ndarray = ...
    cluster_centers_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: Int = 8,
        *,
        init: MatrixLike
        | Callable
        | Literal["k-means++", "random", "k-means++"] = "k-means++",
        n_init: Literal["auto", "warn"] | int = "warn",
        max_iter: Int = 300,
        tol: Float = 1e-4,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        copy_x: bool = True,
        algorithm: Literal["lloyd", "elkan", "auto", "full", "lloyd"] = "lloyd",
    ) -> None:
        ...

    def fit(
        self: KMeans_Self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> KMeans_Self:
        ...


class MiniBatchKMeans(_BaseKMeans):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_steps_: int = ...
    n_iter_: int = ...
    inertia_: float = ...
    labels_: ndarray = ...
    cluster_centers_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: Int = 8,
        *,
        init: MatrixLike
        | Callable
        | Literal["k-means++", "random", "k-means++"] = "k-means++",
        max_iter: Int = 100,
        batch_size: Int = 1024,
        verbose: Int = 0,
        compute_labels: bool = True,
        random_state: RandomState | None | Int = None,
        tol: Float = 0.0,
        max_no_improvement: Int = 10,
        init_size: None | Int = None,
        n_init: Literal["auto", "warn"] | int = "warn",
        reassignment_ratio: Float = 0.01,
    ) -> None:
        ...

    def fit(
        self: MiniBatchKMeans_Self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> MiniBatchKMeans_Self:
        ...

    def partial_fit(
        self: MiniBatchKMeans_Self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> MiniBatchKMeans_Self:
        ...
