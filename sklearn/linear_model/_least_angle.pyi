from collections.abc import Generator, Iterable
from typing import List, Optional, Tuple, Union, Literal, Any
from numpy.typing import ArrayLike

# Author: Fabian Pedregosa <fabian.pedregosa@inria.fr>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux
#
# License: BSD 3 clause

from math import log
import sys
import warnings

import numpy as np
from numpy.random import RandomState
from scipy import linalg, interpolate
from scipy.linalg.lapack import get_lapack_funcs

from ._base import LinearModel, LinearRegression
from ._base import _deprecate_normalize, _preprocess_data
from ..base import RegressorMixin, MultiOutputMixin

# mypy error: Module 'sklearn.utils' has no attribute 'arrayfuncs'
from ..utils import arrayfuncs, as_float_array  # type: ignore
from ..utils import check_random_state
from ..model_selection import check_cv
from ..exceptions import ConvergenceWarning
from ..utils.fixes import delayed
from numpy import float64, int64, ndarray
from pandas.core.series import Series

SOLVE_TRIANGULAR_ARGS: dict = ...

def lars_path(
    X: ArrayLike | None,
    y: ArrayLike | None,
    Xy: ArrayLike | None = None,
    *,
    Gram: ArrayLike | Literal["auto"] | None = None,
    max_iter: int = 500,
    alpha_min: float = 0,
    method: Literal["lar", "lasso"] = "lar",
    copy_X: bool = True,
    eps: float = ...,
    copy_Gram: bool = True,
    verbose: int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
) -> tuple[ArrayLike, ArrayLike, ArrayLike, int]: ...
def lars_path_gram(
    Xy: ArrayLike,
    Gram: ArrayLike,
    *,
    n_samples: int | float,
    max_iter: int = 500,
    alpha_min: float = 0,
    method: Literal["lar", "lasso"] = "lar",
    copy_X: bool = True,
    eps: float = ...,
    copy_Gram: bool = True,
    verbose: int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
) -> tuple[ArrayLike, ArrayLike, ArrayLike, int]: ...
def _lars_path_solver(
    X: ndarray,
    y: ndarray,
    Xy: Optional[ndarray] = None,
    Gram: Optional[Union[ndarray, str]] = None,
    n_samples: None = None,
    max_iter: int = 500,
    alpha_min: Union[int, float, float64] = 0,
    method: str = "lar",
    copy_X: bool = True,
    eps: float64 = np.finfo(float).eps,
    copy_Gram: bool = True,
    verbose: Union[int, bool] = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
) -> Union[
    Tuple[ndarray, List[int64], ndarray, int],
    Tuple[ndarray, List[int64], ndarray],
    Tuple[ndarray, List[Any], ndarray, int],
]: ...

###############################################################################
# Estimator classes

class Lars(MultiOutputMixin, RegressorMixin, LinearModel):

    method: str = ...
    positive: bool = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        n_nonzero_coefs: int = 500,
        eps: float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        jitter: float | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    @staticmethod
    def _get_gram(precompute: Union[ndarray, str], X: ndarray, y: ndarray) -> ndarray: ...
    def _fit(
        self,
        X: ndarray,
        y: ndarray,
        max_iter: int,
        alpha: Union[float, float64],
        fit_path: bool,
        normalize: bool,
        Xy: Optional[ndarray] = None,
    ) -> Union[LassoLars, LassoLarsCV, Lars]: ...
    def fit(self, X: ArrayLike, y: ArrayLike, Xy: ArrayLike | None = None) -> Union[LassoLars, Lars]: ...

class LassoLars(Lars):

    method: str = ...

    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        max_iter: int = 500,
        eps: float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        positive: bool = False,
        jitter: float | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...

###############################################################################
# Cross-validated estimator classes

def _check_copy_and_writeable(array: ndarray, copy: bool = False) -> ndarray: ...
def _lars_path_residues(
    X_train: ndarray,
    y_train: ndarray,
    X_test: ndarray,
    y_test: ndarray,
    Gram: Optional[str] = None,
    copy: bool = True,
    method: str = "lars",
    verbose: int = False,
    fit_intercept: bool = True,
    normalize: bool = True,
    max_iter: int = 500,
    eps: float64 = np.finfo(float).eps,
    positive: bool = False,
) -> Tuple[ndarray, List[int64], ndarray, ndarray]: ...

class LarsCV(Lars):

    method: str = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        max_iter: int = 500,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        cv: int | Generator | Iterable | None = None,
        max_n_alphas: int = 1000,
        n_jobs: int | None = None,
        eps: float = ...,
        copy_X: bool = True,
    ): ...
    def _more_tags(self): ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "LassoLarsCV": ...

class LassoLarsCV(LarsCV):

    method: str = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        max_iter: int = 500,
        normalize: bool = ...,
        precompute: bool | Literal["auto"] = "auto",
        cv: int | Generator | Iterable | None = None,
        max_n_alphas: int = 1000,
        n_jobs: int | None = None,
        eps: float = ...,
        copy_X: bool = True,
        positive: bool = False,
    ) -> None: ...

class LassoLarsIC(LassoLars):
    def __init__(
        self,
        criterion: Literal["aic", "bic"] = "aic",
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        max_iter: int = 500,
        eps: float = ...,
        copy_X: bool = True,
        positive: bool = False,
        noise_variance: float | None = None,
    ) -> None: ...
    def _more_tags(self): ...
    def fit(self, X: ArrayLike, y: ArrayLike, copy_X: bool | None = None) -> "LassoLarsIC": ...
    def _estimate_noise_variance(self, X: ndarray, y: ndarray, positive: bool) -> float64: ...
