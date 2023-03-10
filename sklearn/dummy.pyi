from typing import Any, Literal
from .utils import check_random_state as check_random_state
from numpy.random import RandomState
from ._typing import Int, ArrayLike, MatrixLike, Float
from .base import BaseEstimator, ClassifierMixin, RegressorMixin, MultiOutputMixin
from .utils.multiclass import class_distribution as class_distribution
from numpy import ndarray
from .utils._param_validation import StrOptions as StrOptions, Interval as Interval
from .utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
)
from numbers import Integral as Integral, Real as Real

# Author: Mathieu Blondel <mathieu@mblondel.org>
#         Arnaud Joly <a.joly@ulg.ac.be>
#         Maheshakya Wijewardena <maheshakya.10@cse.mrt.ac.lk>
# License: BSD 3 clause

import warnings

import numpy as np
import scipy.sparse as sp


class DummyClassifier(MultiOutputMixin, ClassifierMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        strategy: Literal[
            "most_frequent", "prior", "stratified", "uniform", "constant", "prior"
        ] = "prior",
        random_state: RandomState | None | Int = None,
        constant: int | str | None | ArrayLike = None
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> list[ndarray] | ndarray:
        ...

    def predict_log_proba(self, X: ArrayLike) -> list[ndarray] | ndarray:
        ...

    def score(
        self,
        X: None | MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> float:
        ...


class DummyRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        strategy: Literal["mean", "median", "quantile", "constant", "mean"] = "mean",
        constant: int | float | None | ArrayLike = None,
        quantile: float | None = None
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(
        self, X: MatrixLike, return_std: bool = False
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def score(
        self,
        X: None | MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...
