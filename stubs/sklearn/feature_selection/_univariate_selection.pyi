from typing import Callable, ClassVar, Literal, TypeVar
from ..utils.validation import check_is_fitted as check_is_fitted
from scipy import special as special, stats
from ._base import SelectorMixin
from numpy import ndarray
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot, row_norms as row_norms
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from joblib.memory import MemorizedFunc
from ..base import BaseEstimator
from scipy.sparse import issparse as issparse
from .._typing import MatrixLike, ArrayLike, Int, Float
from ..utils import (
    as_float_array as as_float_array,
    check_array as check_array,
    check_X_y as check_X_y,
    safe_sqr as safe_sqr,
    safe_mask as safe_mask,
)
from ..preprocessing import LabelBinarizer as LabelBinarizer

_BaseFilter_Self = TypeVar("_BaseFilter_Self", bound="_BaseFilter")


# Authors: V. Michel, B. Thirion, G. Varoquaux, A. Gramfort, E. Duchesnay.
#          L. Buitinck, A. Joly
# License: BSD 3 clause


import numpy as np
import warnings


######################################################################
# Scoring functions


# The following function is a rewriting of scipy.stats.f_oneway
# Contrary to the scipy.stats.f_oneway implementation it does not
# copy the data while keeping the inputs unchanged.
def f_oneway(*args) -> tuple[ndarray, ndarray] | tuple[float, float]:
    ...


def f_classif(X: MatrixLike | ArrayLike, y: ArrayLike) -> tuple[ndarray, ndarray]:
    ...


def chi2(X: MatrixLike | ArrayLike, y: ArrayLike) -> tuple[ndarray, ndarray]:
    ...


def r_regression(
    X: MatrixLike | ArrayLike,
    y: ArrayLike,
    *,
    center: bool = True,
    force_finite: bool = True
) -> ndarray:
    ...


def f_regression(
    X: MatrixLike | ArrayLike,
    y: ArrayLike,
    *,
    center: bool = True,
    force_finite: bool = True
) -> tuple[ndarray, ndarray]:
    ...


######################################################################
# Base classes


class _BaseFilter(SelectorMixin, BaseEstimator):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, score_func: Callable | MemorizedFunc) -> None:
        ...

    def fit(self: _BaseFilter_Self, X: MatrixLike, y: ArrayLike) -> _BaseFilter_Self:
        ...


######################################################################
# Specific filters
######################################################################
class SelectPercentile(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, score_func: Callable | MemorizedFunc = ..., *, percentile: Int = 10
    ) -> None:
        ...


class SelectKBest(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, score_func: Callable = ..., *, k: str | int = 10) -> None:
        ...


class SelectFpr(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


class SelectFdr(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


class SelectFwe(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


######################################################################
# Generic filter
######################################################################

# TODO this class should fit on either p-values or scores,
# depending on the mode.
class GenericUnivariateSelect(_BaseFilter):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pvalues_: ArrayLike = ...
    scores_: ArrayLike = ...

    _selection_modes: ClassVar[dict] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        score_func: Callable = ...,
        *,
        mode: Literal[
            "percentile", "k_best", "fpr", "fdr", "fwe", "percentile"
        ] = "percentile",
        param: float | str | int = 1e-5
    ) -> None:
        ...
