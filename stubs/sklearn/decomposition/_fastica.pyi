from typing import Any, Callable, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from scipy import linalg as linalg
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numbers import Integral as Integral, Real as Real
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from .._typing import MatrixLike, Int, Float
from ..utils import (
    check_array as check_array,
    as_float_array as as_float_array,
    check_random_state as check_random_state,
)
from ..utils.validation import check_is_fitted as check_is_fitted

FastICA_Self = TypeVar("FastICA_Self", bound="FastICA")


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
    whiten: str | bool = "warn",
    fun: Literal["logcosh", "exp", "cube", "logcosh"] | Callable = "logcosh",
    fun_args: None | dict = None,
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
    whitening_: ndarray = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    mean_: ndarray = ...
    mixing_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        algorithm: Literal["parallel", "deflation", "parallel"] = "parallel",
        whiten: str | bool = "warn",
        fun: Literal["logcosh", "exp", "cube", "logcosh"] | Callable = "logcosh",
        fun_args: None | dict = None,
        max_iter: Int = 200,
        tol: Float = 1e-4,
        w_init: None | MatrixLike = None,
        whiten_solver: Literal["eigh", "svd", "svd"] = "svd",
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def fit(self: FastICA_Self, X: MatrixLike, y: Any = None) -> FastICA_Self:
        ...

    def transform(self, X: MatrixLike, copy: bool = True) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike, copy: bool = True) -> ndarray:
        ...
