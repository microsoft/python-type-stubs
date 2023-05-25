from .._typing import MatrixLike, ArrayLike, Int
from numpy import ndarray
from .sparsefuncs_fast import (
    csr_mean_variance_axis0 as _csr_mean_var_axis0,
    csc_mean_variance_axis0 as _csc_mean_var_axis0,
    incr_mean_variance_axis0 as _incr_mean_var_axis0,
)

# Authors: Manoj Kumar
#          Thomas Unterthiner
#          Giorgio Patrini
#
# License: BSD 3 clause
import scipy.sparse as sp
import numpy as np


def inplace_csr_column_scale(X: MatrixLike, scale: MatrixLike):
    ...


def inplace_csr_row_scale(X: MatrixLike, scale: ArrayLike):
    ...


def mean_variance_axis(
    X: MatrixLike,
    axis: int,
    weights: None | ArrayLike = None,
    return_sum_weights: bool = False,
) -> tuple[ndarray, ndarray, ndarray] | tuple[ndarray, ndarray]:
    ...


def incr_mean_variance_axis(
    X: MatrixLike,
    *,
    axis: int,
    last_mean: ArrayLike,
    last_var: ArrayLike,
    last_n: float | ArrayLike,
    weights: None | ArrayLike = None
) -> tuple[ndarray, ndarray, ndarray]:
    ...


def inplace_column_scale(X: MatrixLike, scale: MatrixLike):
    ...


def inplace_row_scale(X: MatrixLike, scale: MatrixLike):
    ...


def inplace_swap_row_csc(X: MatrixLike, m: Int, n: Int):
    ...


def inplace_swap_row_csr(X: MatrixLike, m: Int, n: Int):
    ...


def inplace_swap_row(X: MatrixLike, m: Int, n: Int):
    ...


def inplace_swap_column(X: MatrixLike, m: Int, n: Int):
    ...


def min_max_axis(
    X: MatrixLike, axis: int, ignore_nan: bool = False
) -> tuple[ndarray, ndarray]:
    ...


def count_nonzero(
    X: MatrixLike, axis: None | int = None, sample_weight: None | ArrayLike = None
) -> float | ndarray | int:
    ...


def csc_median_axis_0(X: MatrixLike) -> ndarray:
    ...
