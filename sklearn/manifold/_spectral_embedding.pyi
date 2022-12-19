from typing import Union, Literal, Callable, Any
from numpy.typing import ArrayLike, NDArray

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Wei LI <kuantkid@gmail.com>
# License: BSD 3 clause

import warnings

import numpy as np
from numpy.random import RandomState
from scipy import sparse
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import laplacian as csgraph_laplacian

from ..base import BaseEstimator
from ..utils import (
    check_array,
    check_random_state,
    check_symmetric,
)
from ..utils._arpack import _init_arpack_v0
from ..utils.extmath import _deterministic_vector_sign_flip
from ..metrics.pairwise import rbf_kernel
from ..neighbors import kneighbors_graph, NearestNeighbors
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csr import csr_matrix
from scipy.sparse._dia import dia_matrix

def _graph_connected_component(graph, node_id): ...
def _graph_is_connected(graph: Union[csr_matrix, coo_matrix]) -> bool: ...
def _set_diag(laplacian: coo_matrix, value: int, norm_laplacian: bool) -> Union[csr_matrix, dia_matrix]: ...
def spectral_embedding(
    adjacency: ArrayLike,
    *,
    n_components: int = 8,
    eigen_solver: Literal["arpack", "lobpcg", "amg"] | None = None,
    random_state: int | RandomState | None = None,
    eigen_tol: float = 0.0,
    norm_laplacian: bool = True,
    drop_first: bool = True,
) -> NDArray: ...

class SpectralEmbedding(BaseEstimator):
    def __init__(
        self,
        n_components: int = 2,
        *,
        affinity: Literal["nearest_neighbors", "rbf", "precomputed", "precomputed_nearest_neighbors"]
        | Callable = "nearest_neighbors",
        gamma: float | None = None,
        random_state: int | RandomState | None = None,
        eigen_solver: Literal["arpack", "lobpcg", "amg"] | None = None,
        n_neighbors: int | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def _more_tags(self): ...
    def _get_affinity_matrix(self, X: ndarray, Y: None = None) -> csr_matrix: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "SpectralEmbedding": ...
    def fit_transform(self, X: NDArray | ArrayLike, y: None = None) -> ArrayLike: ...
