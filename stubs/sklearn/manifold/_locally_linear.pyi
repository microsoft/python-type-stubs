from typing import Any, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from scipy.sparse.linalg import eigsh as eigsh, LinearOperator
from numpy import ndarray
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.linalg import svd as svd, qr as qr, solve as solve
from numbers import Integral as Integral, Real as Real
from ..utils.extmath import stable_cumsum as stable_cumsum
from ..neighbors._unsupervised import NearestNeighbors
from scipy.sparse import eye as eye
from ..base import (
    BaseEstimator,
    TransformerMixin,
    _UnstableArchMixin,
    ClassNamePrefixFeaturesOutMixin,
)
from scipy.sparse._csr import csr_matrix
from .._typing import MatrixLike, Float, ArrayLike, Int
from ..utils import check_random_state as check_random_state, check_array as check_array
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    FLOAT_DTYPES as FLOAT_DTYPES,
)

LocallyLinearEmbedding_Self = TypeVar(
    "LocallyLinearEmbedding_Self", bound="LocallyLinearEmbedding"
)


import numpy as np


def barycenter_weights(
    X: MatrixLike, Y: MatrixLike, indices: MatrixLike, reg: Float = 1e-3
) -> ndarray:
    ...


def barycenter_kneighbors_graph(
    X: ArrayLike | NearestNeighbors,
    n_neighbors: Int,
    reg: Float = 1e-3,
    n_jobs: None | int = None,
) -> csr_matrix:
    ...


def null_space(
    M: MatrixLike | LinearOperator,
    k: Int,
    k_skip: Int = 1,
    eigen_solver: Literal["auto", "arpack", "dense", "arpack"] = "arpack",
    tol: Float = 1e-6,
    max_iter: Int = 100,
    random_state: None | Int | RandomState = None,
) -> tuple[ndarray, Float]:
    ...


def locally_linear_embedding(
    X: ArrayLike | NearestNeighbors,
    *,
    n_neighbors: Int,
    n_components: Int,
    reg: Float = 1e-3,
    eigen_solver: Literal["auto", "arpack", "dense", "auto"] = "auto",
    tol: Float = 1e-6,
    max_iter: Int = 100,
    method: Literal["standard", "hessian", "modified", "ltsa", "standard"] = "standard",
    hessian_tol: Float = 1e-4,
    modified_tol: Float = 1e-12,
    random_state: RandomState | None | Int = None,
    n_jobs: None | int = None,
) -> tuple[ndarray, Float] | tuple[ndarray, float]:
    ...


class LocallyLinearEmbedding(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    _UnstableArchMixin,
    BaseEstimator,
):
    nbrs_: NearestNeighbors = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    reconstruction_error_: float = ...
    embedding_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_neighbors: Int = 5,
        n_components: Int = 2,
        reg: Float = 1e-3,
        eigen_solver: Literal["auto", "arpack", "dense", "auto"] = "auto",
        tol: Float = 1e-6,
        max_iter: Int = 100,
        method: Literal[
            "standard", "hessian", "modified", "ltsa", "standard"
        ] = "standard",
        hessian_tol: Float = 1e-4,
        modified_tol: Float = 1e-12,
        neighbors_algorithm: Literal[
            "auto", "brute", "kd_tree", "ball_tree", "auto"
        ] = "auto",
        random_state: RandomState | None | Int = None,
        n_jobs: None | int = None,
    ) -> None:
        ...

    def fit(
        self: LocallyLinearEmbedding_Self, X: MatrixLike, y: Any = None
    ) -> LocallyLinearEmbedding_Self:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
