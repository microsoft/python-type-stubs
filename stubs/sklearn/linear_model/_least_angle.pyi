from math import log as log
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Iterable, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import interpolate as interpolate, linalg as linalg
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import MultiOutputMixin, RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..model_selection import BaseCrossValidator, check_cv as check_cv
from ..model_selection._split import BaseShuffleSplit
from ..utils import arrayfuncs as arrayfuncs, as_float_array as as_float_array, check_random_state as check_random_state
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ._base import LinearModel, LinearRegression as LinearRegression

LassoLarsIC_Self = TypeVar("LassoLarsIC_Self", bound="LassoLarsIC")
Lars_Self = TypeVar("Lars_Self", bound="Lars")
LarsCV_Self = TypeVar("LarsCV_Self", bound="LarsCV")

import sys
import warnings

import numpy as np

SOLVE_TRIANGULAR_ARGS: dict = ...

def lars_path(
    X: None | MatrixLike,
    y: None | ArrayLike,
    Xy: None | MatrixLike | ArrayLike = None,
    *,
    Gram: None | MatrixLike | str = None,
    max_iter: Int = 500,
    alpha_min: Float = 0,
    method: Literal["lar", "lasso", "lar"] = "lar",
    copy_X: bool = True,
    eps: Float = ...,
    copy_Gram: bool = True,
    verbose: Int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
) -> tuple[ndarray, ndarray, ndarray, int]: ...
def lars_path_gram(
    Xy: MatrixLike | ArrayLike,
    Gram: MatrixLike,
    *,
    n_samples: float | int,
    max_iter: Int = 500,
    alpha_min: Float = 0,
    method: Literal["lar", "lasso", "lar"] = "lar",
    copy_X: bool = True,
    eps: Float = ...,
    copy_Gram: bool = True,
    verbose: Int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
) -> tuple[ndarray, ndarray, ndarray, int]: ...

###############################################################################
# Estimator classes

class Lars(MultiOutputMixin, RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: ArrayLike | int = ...
    intercept_: float | ArrayLike = ...
    coef_: ArrayLike = ...
    coef_path_: ArrayLike | list[ArrayLike] = ...
    active_: list[list] | list = ...
    alphas_: ArrayLike | list[ArrayLike] = ...

    _parameter_constraints: ClassVar[dict] = ...

    method: ClassVar[str] = ...
    positive: ClassVar[bool] = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: int | bool = False,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | ArrayLike | bool = "auto",
        n_nonzero_coefs: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        jitter: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(
        self: Lars_Self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        Xy: None | MatrixLike | ArrayLike = None,
    ) -> Lars_Self: ...

class LassoLars(Lars):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: ArrayLike | int = ...
    intercept_: float | ArrayLike = ...
    coef_: ArrayLike = ...
    coef_path_: ArrayLike | list[ArrayLike] = ...
    active_: list[list] | list = ...
    alphas_: ArrayLike | list[ArrayLike] = ...

    _parameter_constraints: ClassVar[dict] = ...

    method: ClassVar[str] = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        verbose: int | bool = False,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | ArrayLike | bool = "auto",
        max_iter: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        positive: bool = False,
        jitter: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class LarsCV(Lars):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: ArrayLike | int = ...
    mse_path_: ArrayLike = ...
    cv_alphas_: ArrayLike = ...
    alphas_: ArrayLike = ...
    alpha_: float = ...
    coef_path_: ArrayLike = ...
    intercept_: float = ...
    coef_: ArrayLike = ...
    active_: list[list] | list = ...

    _parameter_constraints: ClassVar[dict] = ...

    for parameter in ["n_nonzero_coefs", "jitter", "fit_path", "random_state"]:
        pass

    method: ClassVar[str] = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: int | bool = False,
        max_iter: Int = 500,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | ArrayLike | bool = "auto",
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        max_n_alphas: Int = 1000,
        n_jobs: None | int = None,
        eps: Float = ...,
        copy_X: bool = True,
    ) -> None: ...
    def fit(self: LarsCV_Self, X: MatrixLike, y: ArrayLike) -> LarsCV_Self: ...

class LassoLarsCV(LarsCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    active_: list[int] = ...
    n_iter_: ArrayLike | int = ...
    mse_path_: ArrayLike = ...
    cv_alphas_: ArrayLike = ...
    alphas_: ArrayLike = ...
    alpha_: float = ...
    coef_path_: ArrayLike = ...
    intercept_: float = ...
    coef_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    method: ClassVar[str] = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: int | bool = False,
        max_iter: Int = 500,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | bool = "auto",
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        max_n_alphas: Int = 1000,
        n_jobs: None | int = None,
        eps: Float = ...,
        copy_X: bool = True,
        positive: bool = False,
    ) -> None: ...

class LassoLarsIC(LassoLars):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    noise_variance_: float = ...
    criterion_: ArrayLike = ...
    n_iter_: int = ...
    alphas_: ArrayLike | list[ArrayLike] = ...
    alpha_: float = ...
    intercept_: float = ...
    coef_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    for parameter in ["jitter", "fit_path", "alpha", "random_state"]:
        pass

    def __init__(
        self,
        criterion: Literal["aic", "bic", "aic"] = "aic",
        *,
        fit_intercept: bool = True,
        verbose: int | bool = False,
        normalize: str | bool = "deprecated",
        precompute: Literal["auto", "auto"] | ArrayLike | bool = "auto",
        max_iter: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        positive: bool = False,
        noise_variance: None | Float = None,
    ) -> None: ...
    def fit(self: LassoLarsIC_Self, X: MatrixLike, y: ArrayLike, copy_X: None | bool = None) -> LassoLarsIC_Self: ...
