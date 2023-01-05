from typing import Optional, Tuple, Union, Any, Literal
from numpy.typing import ArrayLike

# Authors : Kemal Eren
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod

import numpy as np
from numpy.random import RandomState
from numpy.typing import NDArray
import numbers

from scipy.linalg import norm
from scipy.sparse import dia_matrix, issparse
from scipy.sparse.linalg import eigsh, svds

from . import KMeans, MiniBatchKMeans
from ..base import BaseEstimator, BiclusterMixin
from ..utils import check_random_state
from ..utils import check_scalar

from ..utils.extmath import make_nonnegative, randomized_svd, safe_sparse_dot

from ..utils.validation import assert_all_finite
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

__all__ = ["SpectralCoclustering", "SpectralBiclustering"]

def _scale_normalize(
    X: Union[ndarray, csr_matrix]
) -> Union[Tuple[csr_matrix, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
def _bistochastic_normalize(X, max_iter=1000, tol=1e-5): ...
def _log_normalize(X: ndarray) -> ndarray: ...

class BaseSpectral(BiclusterMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        n_clusters: Union[int, Tuple[int, int]] = 3,
        svd_method: str = "randomized",
        n_svd_vecs: None = None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state: Optional[int] = None,
    ) -> None: ...
    def _check_parameters(self, n_samples: int) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> Union[SpectralCoclustering, SpectralBiclustering]: ...
    def _svd(self, array: Union[ndarray, csr_matrix], n_components: int, n_discard: int) -> Tuple[ndarray, ndarray]: ...
    def _k_means(self, data: ndarray, n_clusters: int) -> Tuple[ndarray, ndarray]: ...
    def _more_tags(self): ...

class SpectralCoclustering(BaseSpectral):
    def __init__(
        self,
        n_clusters: int = 3,
        *,
        svd_method: Literal["randomized", "arpack"] = "randomized",
        n_svd_vecs: int | None = None,
        mini_batch: bool = False,
        init: Literal["k-means++", "random"] | NDArray = "k-means++",
        n_init: int = 10,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _check_parameters(self, n_samples: int) -> None: ...
    def _fit(self, X: Union[ndarray, csr_matrix]) -> None: ...

class SpectralBiclustering(BaseSpectral):
    def __init__(
        self,
        n_clusters: int | tuple[int, int] = 3,
        *,
        method: Literal["bistochastic", "scale", "log"] = "bistochastic",
        n_components: int = 6,
        n_best: int = 3,
        svd_method: Literal["randomized", "arpack"] = "randomized",
        n_svd_vecs: int | None = None,
        mini_batch: bool = False,
        init: Literal["k-means++", "random"] | NDArray = "k-means++",
        n_init: int = 10,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _check_parameters(self, n_samples: int) -> None: ...
    def _fit(self, X: ndarray) -> None: ...
    def _fit_best_piecewise(self, vectors: ndarray, n_best: int, n_clusters: int) -> ndarray: ...
    def _project_and_cluster(self, data: ndarray, vectors: ndarray, n_clusters: int) -> ndarray: ...
