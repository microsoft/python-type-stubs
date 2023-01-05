from collections.abc import Generator, Iterable
from typing import Tuple, Union, Literal, Any
from numpy.typing import NDArray, ArrayLike

# Author: Vlad Niculae
#
# License: BSD 3 clause

import warnings
from math import sqrt

import numpy as np
from scipy import linalg
from scipy.linalg.lapack import get_lapack_funcs

from ._base import LinearModel, _pre_fit, _deprecate_normalize
from ..base import RegressorMixin, MultiOutputMixin
from ..utils import as_float_array, check_array
from ..utils.fixes import delayed
from ..model_selection import check_cv
from numpy import int64, ndarray

premature: str = ...

def _cholesky_omp(
    X: ndarray,
    y: ndarray,
    n_nonzero_coefs: Union[int64, int],
    tol: None = None,
    copy_X: bool = True,
    return_path: bool = False,
) -> Union[Tuple[ndarray, ndarray, int], Tuple[ndarray, ndarray, ndarray, int]]: ...
def _gram_omp(
    Gram: ndarray,
    Xy: ndarray,
    n_nonzero_coefs: int,
    tol_0: None = None,
    tol: None = None,
    copy_Gram: bool = True,
    copy_Xy: bool = True,
    return_path: bool = False,
) -> Tuple[ndarray, ndarray, int]: ...
def orthogonal_mp(
    X: NDArray,
    y: NDArray,
    *,
    n_nonzero_coefs: int | None = None,
    tol: float | None = None,
    precompute: bool | Literal["auto"] = False,
    copy_X: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
) -> tuple[NDArray, ArrayLike | int]: ...
def orthogonal_mp_gram(
    Gram: NDArray,
    Xy: NDArray,
    *,
    n_nonzero_coefs: int | None = None,
    tol: float | None = None,
    norms_squared: ArrayLike | None = None,
    copy_Gram: bool = True,
    copy_Xy: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
) -> tuple[NDArray, ArrayLike | int]: ...

class OrthogonalMatchingPursuit(MultiOutputMixin, RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        n_nonzero_coefs: int | None = None,
        tol: float | None = None,
        fit_intercept: bool = True,
        normalize: bool = ...,
        precompute: bool | Literal["auto"] = "auto",
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "OrthogonalMatchingPursuit": ...

def _omp_path_residues(
    X_train: ndarray,
    y_train: ndarray,
    X_test: ndarray,
    y_test: ndarray,
    copy: bool = True,
    fit_intercept: bool = True,
    normalize: bool = True,
    max_iter: int = 100,
) -> ndarray: ...

class OrthogonalMatchingPursuitCV(RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        copy: bool = True,
        fit_intercept: bool = True,
        normalize: bool = ...,
        max_iter: int | None = None,
        cv: int | Generator | Iterable | None = None,
        n_jobs: int | None = None,
        verbose: bool | int = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "OrthogonalMatchingPursuitCV": ...
