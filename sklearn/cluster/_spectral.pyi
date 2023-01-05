from numpy import ndarray
from typing import Literal, Callable, Any, Mapping
from numpy.typing import ArrayLike, NDArray

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Brian Cheung
#         Wei LI <kuantkid@gmail.com>
#         Andrew Knyazev <Andrew.Knyazev@ucdenver.edu>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np
from numpy.random import RandomState

from scipy.linalg import LinAlgError, qr, svd
from scipy.sparse import csc_matrix

from ..base import BaseEstimator, ClusterMixin
from ..utils import check_random_state, as_float_array, check_scalar
from ..metrics.pairwise import pairwise_kernels
from ..neighbors import kneighbors_graph, NearestNeighbors
from ..manifold import spectral_embedding
from ._kmeans import k_means
from scipy.sparse._coo import coo_matrix

def cluster_qr(vectors: ArrayLike) -> NDArray: ...
def discretize(
    vectors: ArrayLike,
    *,
    copy: bool = True,
    max_svd_restarts: int = 30,
    n_iter_max: int = 20,
    random_state: int | RandomState | None = None,
) -> NDArray: ...
def spectral_clustering(
    affinity: NDArray | ArrayLike,
    *,
    n_clusters: int = 8,
    n_components: int | None = None,
    eigen_solver: None | Literal["arpack", "lobpcg", "amg"] = None,
    random_state: int | RandomState | None = None,
    n_init: int = 10,
    eigen_tol: float = 0.0,
    assign_labels: Literal["kmeans", "discretize", "cluster_qr"] = "kmeans",
    verbose: bool = False,
) -> NDArray: ...

class SpectralClustering(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        eigen_solver: Literal["arpack", "lobpcg", "amg"] | None = None,
        n_components: int | None = None,
        random_state: int | RandomState | None = None,
        n_init: int = 10,
        gamma: float = 1.0,
        affinity: str | Callable = "rbf",
        n_neighbors: int = 10,
        eigen_tol: float = 0.0,
        assign_labels: Literal["kmeans", "discretize", "cluster_qr"] = "kmeans",
        degree: float = 3,
        coef0: float = 1,
        kernel_params: Mapping[str, Any] | None = None,
        n_jobs: int | None = None,
        verbose: bool = False,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y=None) -> Any: ...
    def fit_predict(self, X: NDArray | ArrayLike, y=None) -> NDArray: ...
    def _more_tags(self): ...
