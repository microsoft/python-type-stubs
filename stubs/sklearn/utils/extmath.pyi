from typing import Literal, Sequence
from numpy.random import RandomState
from scipy.sparse._csr import csr_matrix
from scipy import linalg as linalg, sparse as sparse
from numpy import ndarray
from scipy.sparse._dia import dia_matrix
from .sparsefuncs_fast import csr_row_norms as csr_row_norms
from ._array_api import get_namespace as get_namespace
from scipy.sparse import spmatrix
from .validation import check_array as check_array
from .._typing import ArrayLike, Float, MatrixLike, Int
from . import check_random_state as check_random_state

# Authors: Gael Varoquaux
#          Alexandre Gramfort
#          Alexandre T. Passos
#          Olivier Grisel
#          Lars Buitinck
#          Stefan van der Walt
#          Kyle Kastner
#          Giorgio Patrini
# License: BSD 3 clause

import warnings

import numpy as np


def squared_norm(x: ArrayLike) -> Float:
    ...


def row_norms(X: csr_matrix | ArrayLike, squared: bool = False) -> ndarray:
    ...


def fast_logdet(A: MatrixLike) -> Float:
    ...


def density(w: ArrayLike, **kwargs) -> float:
    ...


def safe_sparse_dot(
    a: MatrixLike | ArrayLike | dia_matrix,
    b: MatrixLike | ArrayLike,
    *,
    dense_output: bool = False,
) -> ndarray | spmatrix:
    ...


def randomized_range_finder(
    A: MatrixLike,
    *,
    size: Int,
    n_iter: Int,
    power_iteration_normalizer: Literal["auto", "QR", "LU", "none", "auto"] = "auto",
    random_state: RandomState | None | Int = None,
) -> ndarray:
    ...


def randomized_svd(
    M: MatrixLike | ArrayLike,
    n_components: Int,
    *,
    n_oversamples: Int = 10,
    n_iter: Literal["auto", "auto"] | Int = "auto",
    power_iteration_normalizer: Literal["auto", "QR", "LU", "none", "auto"] = "auto",
    transpose: Literal["auto", "auto"] | bool = "auto",
    flip_sign: bool = True,
    random_state: RandomState | None | Int = None,
    svd_lapack_driver: Literal["gesdd", "gesvd", "gesdd"] = "gesdd",
) -> tuple[ndarray, ndarray, ndarray]:
    ...


def weighted_mode(
    a: ArrayLike, w: ArrayLike, *, axis: Int = 0
) -> tuple[ndarray, ndarray]:
    ...


def cartesian(
    arrays: Sequence[ArrayLike] | ArrayLike, out: None | MatrixLike = None
) -> ndarray:
    ...


def svd_flip(
    u: ArrayLike, v: ArrayLike, u_based_decision: bool = True
) -> tuple[ndarray, ndarray]:
    ...


def log_logistic(
    X: MatrixLike | ArrayLike, out: None | MatrixLike | ArrayLike = None
) -> ndarray:
    ...


def softmax(X: MatrixLike, copy: bool = True) -> ndarray:
    ...


def make_nonnegative(
    X: csr_matrix | ArrayLike, min_value: Float = 0
) -> csr_matrix | ndarray:
    ...


def stable_cumsum(
    arr: ArrayLike, axis: None | Int = None, rtol: Float = 1e-05, atol: Float = 1e-08
) -> ndarray:
    ...
