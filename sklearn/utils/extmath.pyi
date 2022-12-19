from numpy import float32, float64, int64, ndarray
from typing import Callable, List, Optional, Tuple, Union, Literal
from numpy.typing import ArrayLike, NDArray

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
from scipy import linalg, sparse

from . import check_random_state
from ._logistic_sigmoid import _log_logistic_sigmoid
from .sparsefuncs_fast import csr_row_norms
from .validation import check_array
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix
from scipy.sparse._dia import dia_matrix

def squared_norm(x: ArrayLike) -> float: ...
def row_norms(X: ArrayLike, squared: bool = False) -> ArrayLike: ...
def fast_logdet(A: ArrayLike) -> Union[float, float64]: ...
def density(w: ArrayLike, **kwargs) -> float: ...
def safe_sparse_dot(a: NDArray, b: NDArray, *, dense_output: bool = False) -> NDArray: ...
def randomized_range_finder(
    A: NDArray,
    *,
    size: int,
    n_iter: int,
    power_iteration_normalizer: Literal["auto", "QR", "LU", "none"] = "auto",
    random_state: int | RandomState | None = None,
) -> NDArray: ...
def randomized_svd(
    M: NDArray,
    n_components: int,
    *,
    n_oversamples: int = 10,
    n_iter: int | Literal["auto"] = "auto",
    power_iteration_normalizer: Literal["auto", "QR", "LU", "none"] = "auto",
    transpose: bool | Literal["auto"] = "auto",
    flip_sign: bool = True,
    random_state: int | RandomState | None = "warn",
) -> Tuple[ndarray, ndarray, ndarray]: ...
def _randomized_eigsh(
    M,
    n_components,
    *,
    n_oversamples=10,
    n_iter="auto",
    power_iteration_normalizer="auto",
    selection="module",
    random_state=None,
): ...
def weighted_mode(a: ArrayLike, w: ArrayLike, *, axis: int = 0) -> tuple[NDArray, NDArray]: ...
def cartesian(arrays: ArrayLike, out: None = None) -> ndarray: ...
def svd_flip(u: NDArray, v: NDArray, u_based_decision: bool = True) -> NDArray: ...
def log_logistic(X: ArrayLike, out: ArrayLike | None = None) -> np.ndarray: ...
def softmax(X: ArrayLike, copy: bool = True) -> np.ndarray: ...
def make_nonnegative(X: ArrayLike, min_value: float = 0) -> ArrayLike: ...

# Use at least float64 for the accumulating functions to avoid precision issue
# see https://github.com/numpy/numpy/issues/9393. The float64 is also retained
# as it is in case the float overflows
def _safe_accumulator_op(op: Callable, x: ndarray, *args, **kwargs) -> Union[ndarray, float64]: ...
def _incremental_mean_and_var(
    X: ndarray,
    last_mean: Union[ndarray, float],
    last_variance: Union[ndarray, float],
    last_sample_count: Union[ndarray, float],
    sample_weight: None = None,
) -> Tuple[ndarray, ndarray, ndarray]: ...
def _deterministic_vector_sign_flip(u: ndarray) -> ndarray: ...
def stable_cumsum(arr: ArrayLike, axis: int | None = None, rtol: float = 1e-05, atol: float = 1e-08) -> ndarray: ...
