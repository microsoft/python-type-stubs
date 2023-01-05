from typing import Iterator, Union, Callable, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Michal Krawczyk <mkrwczyk.1@gmail.com>

import warnings

import numpy as np
import scipy.sparse as sp
from numpy.random import RandomState

from ._kmeans import _BaseKMeans
from ._kmeans import _kmeans_single_elkan
from ._kmeans import _kmeans_single_lloyd
from ._kmeans import _labels_inertia_threadpool_limit
from ..utils.extmath import row_norms
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_sample_weight
from ..utils.validation import check_random_state
from ..utils.validation import _is_arraylike_not_scalar
from numpy import float64, ndarray

class _BisectingTree:
    def __init__(self, center: ndarray, indices: ndarray, score: Union[int, float64]) -> None: ...
    def split(self, labels: ndarray, centers: ndarray, scores: ndarray) -> None: ...
    def get_cluster_to_bisect(self) -> "_BisectingTree": ...
    def iter_leaves(self) -> Iterator[_BisectingTree]: ...

class BisectingKMeans(_BaseKMeans):
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: Literal["k-means++", "random"] | Callable = "random",
        n_init: int = 1,
        random_state: int | RandomState | None = None,
        max_iter: int = 300,
        verbose: int = 0,
        tol: float = 1e-4,
        copy_x: bool = True,
        algorithm: Literal["lloyd", "elkan"] = "lloyd",
        bisecting_strategy: Literal["biggest_inertia", "largest_cluster"] = "biggest_inertia",
    ) -> None: ...
    def _check_params(self, X: ndarray) -> None: ...
    def _warn_mkl_vcomp(self, n_active_threads): ...
    def _inertia_per_cluster(self, X: ndarray, centers: ndarray, labels: ndarray, sample_weight: ndarray) -> ndarray: ...
    def _bisect(
        self,
        X: ndarray,
        x_squared_norms: ndarray,
        sample_weight: ndarray,
        cluster_to_bisect: _BisectingTree,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "BisectingKMeans": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _predict_recursive(self, X, x_squared_norms, sample_weight, cluster_node): ...
    def _more_tags(self): ...
