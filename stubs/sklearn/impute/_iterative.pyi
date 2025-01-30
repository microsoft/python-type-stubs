from collections import namedtuple as namedtuple
from numbers import Integral as Integral, Real as Real
from time import time as time
from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import stats as stats

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, clone as clone
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..linear_model import BayesianRidge as BayesianRidge
from ..preprocessing import normalize as normalize
from ..utils import check_array as check_array, check_random_state as check_random_state, is_scalar_nan as is_scalar_nan
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval, StrOptions as StrOptions
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted
from ._base import MissingIndicator, SimpleImputer, _BaseImputer

IterativeImputer_Self = TypeVar("IterativeImputer_Self", bound=IterativeImputer)

import warnings

import numpy as np

_ImputerTriplet = ...

class IterativeImputer(_BaseImputer):
    random_state_: RandomState = ...
    indicator_: MissingIndicator = ...
    n_features_with_missing_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    imputation_sequence_: list[tuple] = ...
    initial_imputer_: SimpleImputer = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: None | BaseEstimator = None,
        *,
        missing_values: float = ...,
        sample_posterior: bool = False,
        max_iter: Int = 10,
        tol: Float = 1e-3,
        n_nearest_features: None | Int = None,
        initial_strategy: Literal["mean", "median", "most_frequent", "constant"] = "mean",
        imputation_order: Literal["ascending", "descending", "roman", "arabic", "random"] = "ascending",
        skip_complete: bool = False,
        min_value: float | ArrayLike = ...,
        max_value: float | ArrayLike = ...,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
    def fit(self: IterativeImputer_Self, X: MatrixLike, y: Any = None) -> IterativeImputer_Self: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
