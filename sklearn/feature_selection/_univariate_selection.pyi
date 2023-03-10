from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot, row_norms as row_norms
from .._typing import ArrayLike, MatrixLike, Int, Float
from scipy import special as special, stats
from ..base import BaseEstimator
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin
from numpy import ndarray
from ..utils import (
    as_float_array as as_float_array,
    check_array as check_array,
    check_X_y as check_X_y,
    safe_sqr as safe_sqr,
    safe_mask as safe_mask,
)
from numbers import Integral as Integral, Real as Real
from scipy.sparse import issparse as issparse
from joblib.memory import MemorizedFunc

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
def f_oneway(*args) -> tuple[float, float] | tuple[ndarray, ndarray]:
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

    _parameter_constraints: dict = ...

    def __init__(self, score_func: MemorizedFunc | Callable) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...


######################################################################
# Specific filters
######################################################################
class SelectPercentile(_BaseFilter):

    _parameter_constraints: dict = ...

    def __init__(
        self, score_func: MemorizedFunc | Callable = ..., *, percentile: Int = 10
    ) -> None:
        ...


class SelectKBest(_BaseFilter):

    _parameter_constraints: dict = ...

    def __init__(self, score_func: Callable = ..., *, k: int | str = 10) -> None:
        ...


class SelectFpr(_BaseFilter):

    _parameter_constraints: dict = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


class SelectFdr(_BaseFilter):

    _parameter_constraints: dict = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


class SelectFwe(_BaseFilter):

    _parameter_constraints: dict = ...

    def __init__(self, score_func: Callable = ..., *, alpha: Float = 5e-2) -> None:
        ...


######################################################################
# Generic filter
######################################################################

# TODO this class should fit on either p-values or scores,
# depending on the mode.
class GenericUnivariateSelect(_BaseFilter):

    _selection_modes: dict = ...

    _parameter_constraints: dict = ...

    def __init__(
        self,
        score_func: Callable = ...,
        *,
        mode: Literal[
            "percentile", "k_best", "fpr", "fdr", "fwe", "percentile"
        ] = "percentile",
        param: int | float | str = 1e-5
    ) -> None:
        ...
