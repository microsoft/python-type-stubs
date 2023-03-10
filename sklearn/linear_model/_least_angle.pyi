from typing import Any, Iterable, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from collections.abc import Iterable
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import MatrixLike, ArrayLike, Int, Float
from math import log as log
from scipy import linalg as linalg, interpolate as interpolate
from ..base import RegressorMixin, MultiOutputMixin
from ..model_selection import check_cv as check_cv
from ._base import LinearModel, LinearRegression as LinearRegression
from numpy import ndarray
from ..utils import (
    arrayfuncs as arrayfuncs,
    as_float_array as as_float_array,
    check_random_state as check_random_state,
)
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs
from ..model_selection import BaseCrossValidator
import sys
import warnings
import numpy as np

SOLVE_TRIANGULAR_ARGS: dict = ...


def lars_path(
    X: None | MatrixLike,
    y: None | ArrayLike,
    Xy: None | MatrixLike | ArrayLike = None,
    *,
    Gram: str | None | MatrixLike = None,
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
) -> tuple[ndarray, ndarray, ndarray, int]:
    ...


def lars_path_gram(
    Xy: MatrixLike | ArrayLike,
    Gram: MatrixLike,
    *,
    n_samples: int | float,
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
) -> tuple[ndarray, ndarray, ndarray, int]:
    ...


###############################################################################
# Estimator classes


class Lars(MultiOutputMixin, RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    method: str = ...
    positive: bool = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] | ArrayLike = "auto",
        n_nonzero_coefs: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        jitter: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        Xy: None | MatrixLike | ArrayLike = None,
    ) -> Any:
        ...


class LassoLars(Lars):

    _parameter_constraints: dict = ...

    method: str = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] | ArrayLike = "auto",
        max_iter: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        fit_path: bool = True,
        positive: bool = False,
        jitter: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...


class LarsCV(Lars):

    _parameter_constraints: dict = ...

    for parameter in ["n_nonzero_coefs", "jitter", "fit_path", "random_state"]:
        pass

    method: str = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        max_iter: Int = 500,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] | ArrayLike = "auto",
        cv: Iterable | BaseCrossValidator | int | None = None,
        max_n_alphas: Int = 1000,
        n_jobs: int | None = None,
        eps: Float = ...,
        copy_X: bool = True,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...


class LassoLarsCV(LarsCV):

    _parameter_constraints: dict = ...

    method: str = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        max_iter: Int = 500,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] = "auto",
        cv: Iterable | BaseCrossValidator | int | None = None,
        max_n_alphas: Int = 1000,
        n_jobs: int | None = None,
        eps: Float = ...,
        copy_X: bool = True,
        positive: bool = False,
    ) -> None:
        ...


class LassoLarsIC(LassoLars):

    _parameter_constraints: dict = ...

    for parameter in ["jitter", "fit_path", "alpha", "random_state"]:
        pass

    def __init__(
        self,
        criterion: Literal["aic", "bic", "aic"] = "aic",
        *,
        fit_intercept: bool = True,
        verbose: bool | int = False,
        normalize: bool | str = "deprecated",
        precompute: bool | Literal["auto", "auto"] | ArrayLike = "auto",
        max_iter: Int = 500,
        eps: Float = ...,
        copy_X: bool = True,
        positive: bool = False,
        noise_variance: None | Float = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike, copy_X: bool | None = None) -> Any:
        ...
