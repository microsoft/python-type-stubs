from numpy import float64, int64, ndarray
from typing import Optional, Tuple, Union, Literal, Any, Callable
from numpy.typing import ArrayLike, NDArray

# Authors: Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Thomas Rueckstiess <ruecksti@in.tum.de>
#          James Bergstra <james.bergstra@umontreal.ca>
#          Jan Schlueter <scikit-learn@jan-schlueter.de>
#          Nelle Varoquaux
#          Peter Prettenhofer <peter.prettenhofer@gmail.com>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Robert Layton <robertlayton@gmail.com>
# License: BSD 3 clause

from abc import ABC, abstractmethod
import warnings

import numpy as np
from numpy.random import RandomState
import scipy.sparse as sp

from ..base import (
    BaseEstimator,
    ClusterMixin,
    TransformerMixin,
    _ClassNamePrefixFeaturesOutMixin,
)
from ..metrics.pairwise import euclidean_distances
from ..metrics.pairwise import _euclidean_distances
from ..utils.extmath import row_norms, stable_cumsum
from ..utils.fixes import threadpool_limits
from ..utils.fixes import threadpool_info

from ..utils.sparsefuncs import mean_variance_axis
from ..utils import check_array
from ..utils import check_random_state
from ..utils.validation import check_is_fitted, _check_sample_weight
from ..utils.validation import _is_arraylike_not_scalar
from ..exceptions import ConvergenceWarning
from scipy.sparse._csr import csr_matrix

###############################################################################
# Initialization heuristic

def kmeans_plusplus(
    X: NDArray | ArrayLike,
    n_clusters: int,
    *,
    x_squared_norms: ArrayLike | None = None,
    random_state: int | RandomState | None = None,
    n_local_trials: int | None = None,
) -> tuple[np.ndarray, np.ndarray]: ...
def _kmeans_plusplus(
    X: Union[ndarray, csr_matrix],
    n_clusters: int,
    x_squared_norms: ndarray,
    random_state: RandomState,
    n_local_trials: None = None,
) -> Tuple[ndarray, ndarray]: ...

###############################################################################
# K-means batch estimation by EM (expectation maximization)

def _tolerance(X: Union[ndarray, csr_matrix], tol: float) -> Union[int, float64]: ...
def k_means(
    X: NDArray | ArrayLike,
    n_clusters: int,
    *,
    sample_weight: ArrayLike | None = None,
    init: Literal["k-means++", "random"] | Callable | ArrayLike = "k-means++",
    n_init: int = 10,
    max_iter: int = 300,
    verbose: bool = False,
    tol: float = 1e-4,
    random_state: int | RandomState | None = None,
    copy_x: bool = True,
    algorithm: Literal["lloyd", "elkan", "auto", "full"] = "lloyd",
    return_n_iter: bool = False,
) -> tuple[np.ndarray, NDArray, float, int]: ...
def _kmeans_single_elkan(
    X,
    sample_weight,
    centers_init,
    max_iter=300,
    verbose=False,
    x_squared_norms=None,
    tol=1e-4,
    n_threads=1,
): ...
def _kmeans_single_lloyd(
    X: Union[ndarray, csr_matrix],
    sample_weight: ndarray,
    centers_init: ndarray,
    max_iter: int = 300,
    verbose: Union[int, bool] = False,
    x_squared_norms: Optional[ndarray] = None,
    tol: Union[float, float64] = 1e-4,
    n_threads: int = 1,
) -> Tuple[ndarray, float, ndarray, int]: ...
def _labels_inertia(
    X: Union[ndarray, csr_matrix],
    sample_weight: ndarray,
    x_squared_norms: ndarray,
    centers: ndarray,
    n_threads: int = 1,
    return_inertia: bool = True,
) -> Tuple[ndarray, float]: ...
def _labels_inertia_threadpool_limit(
    X: Union[ndarray, csr_matrix],
    sample_weight: ndarray,
    x_squared_norms: ndarray,
    centers: ndarray,
    n_threads: int = 1,
    return_inertia: bool = True,
) -> Tuple[ndarray, float]: ...

class _BaseKMeans(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, ClusterMixin, BaseEstimator, ABC):
    def __init__(
        self,
        n_clusters: Union[int64, int],
        *,
        init,
        n_init,
        max_iter,
        tol,
        verbose,
        random_state,
    ) -> None: ...
    def _check_params(self, X: Union[ndarray, csr_matrix]) -> None: ...
    @abstractmethod
    def _warn_mkl_vcomp(self, n_active_threads): ...
    def _check_mkl_vcomp(self, X: Union[ndarray, csr_matrix], n_samples: int) -> None: ...
    def _validate_center_shape(self, X: ndarray, centers: ndarray) -> None: ...
    def _check_test_data(self, X: ndarray) -> ndarray: ...
    def _init_centroids(
        self,
        X: Union[ndarray, csr_matrix],
        x_squared_norms: ndarray,
        init: Union[ndarray, str],
        random_state: RandomState,
        init_size: Optional[int] = None,
        n_centroids: Optional[int] = None,
    ) -> ndarray: ...
    def fit_predict(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> NDArray: ...
    def predict(self, X: NDArray | ArrayLike, sample_weight: ArrayLike | None = None) -> NDArray: ...
    def fit_transform(self, X: NDArray | ArrayLike, y=None, sample_weight: ArrayLike | None = None) -> np.ndarray: ...
    def transform(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def _transform(self, X): ...
    def score(self, X: NDArray | ArrayLike, y=None, sample_weight: ArrayLike | None = None) -> float: ...
    def _more_tags(self): ...

class KMeans(_BaseKMeans):
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: Literal["k-means++", "random"] | Callable | ArrayLike = "k-means++",
        n_init: int = 10,
        max_iter: int = 300,
        tol: float = 1e-4,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        copy_x: bool = True,
        algorithm: Literal["lloyd", "elkan", "auto", "full"] = "lloyd",
    ) -> None: ...
    def _check_params(self, X: Union[ndarray, csr_matrix]) -> None: ...
    def _warn_mkl_vcomp(self, n_active_threads): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "KMeans": ...

def _mini_batch_step(
    X: Union[ndarray, csr_matrix],
    x_squared_norms: ndarray,
    sample_weight: ndarray,
    centers: ndarray,
    centers_new: ndarray,
    weight_sums: ndarray,
    random_state: RandomState,
    random_reassign: bool = False,
    reassignment_ratio: float = 0.01,
    verbose: Union[int, bool] = False,
    n_threads: int = 1,
) -> float: ...

class MiniBatchKMeans(_BaseKMeans):
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: Literal["k-means++", "random"] | Callable | ArrayLike = "k-means++",
        max_iter: int = 100,
        batch_size: int = 1024,
        verbose: int = 0,
        compute_labels: bool = True,
        random_state: int | RandomState | None = None,
        tol: float = 0.0,
        max_no_improvement: int = 10,
        init_size: int | None = None,
        n_init: int = 3,
        reassignment_ratio: float = 0.01,
    ) -> None: ...
    def _check_params(self, X: Union[ndarray, csr_matrix]) -> None: ...
    def _warn_mkl_vcomp(self, n_active_threads): ...
    def _mini_batch_convergence(
        self,
        step: int,
        n_steps: int,
        n_samples: int,
        centers_squared_diff: int,
        batch_inertia: float,
    ) -> bool: ...
    def _random_reassign(self) -> bool: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "MiniBatchKMeans": ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "MiniBatchKMeans": ...
