from sklearn.neighbors._unsupervised import NearestNeighbors
from typing import Optional, Tuple, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray
from numpy import float64, ndarray

# Author: Fabian Pedregosa -- <fabian.pedregosa@inria.fr>
#         Jake Vanderplas  -- <vanderplas@astro.washington.edu>
# License: BSD 3 clause (C) INRIA 2011

import numpy as np
from scipy.linalg import eigh, svd, qr, solve
from scipy.sparse import eye, csr_matrix
from scipy.sparse.linalg import eigsh

from ..base import (
    BaseEstimator,
    TransformerMixin,
    _UnstableArchMixin,
    _ClassNamePrefixFeaturesOutMixin,
)
from ..utils import check_random_state, check_array
from ..utils._arpack import _init_arpack_v0
from ..utils.extmath import stable_cumsum
from ..utils.validation import check_is_fitted
from ..utils.validation import FLOAT_DTYPES
from ..neighbors import NearestNeighbors
import scipy.sparse._csr
from numpy.random import RandomState
from scipy.sparse.linalg import LinearOperator

def barycenter_weights(X: ArrayLike, Y: ArrayLike, indices: ArrayLike, reg: float = 1e-3) -> ArrayLike: ...
def barycenter_kneighbors_graph(
    X: NearestNeighbors | ArrayLike,
    n_neighbors: int,
    reg: float = 1e-3,
    n_jobs: int | None = None,
) -> NDArray: ...
def null_space(
    M: NDArray | LinearOperator,
    k: int,
    k_skip: int = 1,
    eigen_solver: Literal["auto", "arpack", "dense"] = "arpack",
    tol: float = 1e-6,
    max_iter: int = 100,
    random_state: int | RandomState | None = None,
) -> Tuple[ndarray, float64]: ...
def locally_linear_embedding(
    X: NearestNeighbors | ArrayLike,
    *,
    n_neighbors: int,
    n_components: int,
    reg: float = 1e-3,
    eigen_solver: Literal["auto", "arpack", "dense"] = "auto",
    tol: float = 1e-6,
    max_iter: int = 100,
    method: Literal["standard", "hessian", "modified", "ltsa"] = "standard",
    hessian_tol: float = 1e-4,
    modified_tol: float = 1e-12,
    random_state: int | RandomState | None = None,
    n_jobs: int | None = None,
) -> tuple[ArrayLike, float]: ...

class LocallyLinearEmbedding(
    _ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    _UnstableArchMixin,
    BaseEstimator,
):
    def __init__(
        self,
        *,
        n_neighbors: int = 5,
        n_components: int = 2,
        reg: float = 1e-3,
        eigen_solver: Literal["auto", "arpack", "dense"] = "auto",
        tol: float = 1e-6,
        max_iter: int = 100,
        method: Literal["standard", "hessian", "modified", "ltsa"] = "standard",
        hessian_tol: float = 1e-4,
        modified_tol: float = 1e-12,
        neighbors_algorithm: Literal["auto", "brute", "kd_tree", "ball_tree"] = "auto",
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def _fit_transform(self, X: ndarray) -> None: ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def fit_transform(self, X: ArrayLike, y: None = None) -> ArrayLike: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
