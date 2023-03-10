from typing import Any, Literal
from .._typing import Estimator, Int, Float, ArrayLike, MatrixLike
from time import time as time
from ..linear_model import BayesianRidge
from ..preprocessing import normalize as normalize
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from ._base import _BaseImputer, SimpleImputer as SimpleImputer
from ..utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    is_scalar_nan as is_scalar_nan,
)
from ..neighbors._regression import KNeighborsRegressor
from ..pipeline import Pipeline
from scipy import stats as stats
from ..utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from ..ensemble._forest import RandomForestRegressor
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..base import clone as clone
from collections import namedtuple as namedtuple
from numbers import Integral as Integral, Real as Real
import warnings
import numpy as np


_ImputerTriplet = ...


class IterativeImputer(_BaseImputer):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: Pipeline
        | Estimator
        | KNeighborsRegressor
        | BayesianRidge
        | None
        | RandomForestRegressor = None,
        *,
        missing_values: int | float = ...,
        sample_posterior: bool = False,
        max_iter: Int = 10,
        tol: Float = 1e-3,
        n_nearest_features: None | Int = None,
        initial_strategy: Literal[
            "mean", "median", "most_frequent", "constant", "mean"
        ] = "mean",
        imputation_order: Literal[
            "ascending", "descending", "roman", "arabic", "random", "ascending"
        ] = "ascending",
        skip_complete: bool = False,
        min_value: float | ArrayLike = ...,
        max_value: float | ArrayLike = ...,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
