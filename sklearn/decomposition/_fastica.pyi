from typing import Any, Callable, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import MatrixLike, Int, Float
from scipy import linalg as linalg
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils import (
    check_array as check_array,
    as_float_array as as_float_array,
    check_random_state as check_random_state,
)
from numbers import Integral as Integral, Real as Real

# Authors: Pierre Lafaye de Micheaux, Stefan van der Walt, Gael Varoquaux,
#          Bertrand Thirion, Alexandre Gramfort, Denis A. Engemann
# License: BSD 3 clause

import warnings

import numpy as np

__all__ = ["fastica", "FastICA"]


def fastica(
    X: MatrixLike,
    n_components: None | Int = None,
    *,
    algorithm: Literal["parallel", "deflation", "parallel"] = "parallel",
    whiten: bool | str = "warn",
    fun: Literal["logcosh", "exp", "cube", "logcosh"] | Callable = "logcosh",
    fun_args: dict | None = None,
    max_iter: Int = 200,
    tol: Float = 1e-04,
    w_init: None | MatrixLike = None,
    whiten_solver: Literal["eigh", "svd", "svd"] = "svd",
    random_state: RandomState | None | Int = None,
    return_X_mean: bool = False,
    compute_sources: bool = True,
    return_n_iter: bool = False,
) -> tuple[ndarray | None, ndarray, ndarray | None, ndarray, int]:
    ...


class FastICA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        algorithm: Literal["parallel", "deflation", "parallel"] = "parallel",
        whiten: bool | str = "warn",
        fun: Literal["logcosh", "exp", "cube", "logcosh"] | Callable = "logcosh",
        fun_args: dict | None = None,
        max_iter: Int = 200,
        tol: Float = 1e-4,
        w_init: None | MatrixLike = None,
        whiten_solver: Literal["eigh", "svd", "svd"] = "svd",
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike, copy: bool = True) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike, copy: bool = True) -> ndarray:
        ...
