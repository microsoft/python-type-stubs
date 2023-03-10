from typing import Any, Mapping
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ._stochastic_gradient import (
    BaseSGDClassifier,
    BaseSGDRegressor,
    DEFAULT_EPSILON as DEFAULT_EPSILON,
)
from numpy.random import RandomState
from .._typing import Float, Int, ArrayLike, MatrixLike
from numbers import Real as Real

# Authors: Rob Zinkov, Mathieu Blondel
# License: BSD 3 clause


class PassiveAggressiveClassifier(BaseSGDClassifier):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        C: Float = 1.0,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: None | Float = 1e-3,
        early_stopping: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: Int = 5,
        shuffle: bool = True,
        verbose: Int = 0,
        loss: str = "hinge",
        n_jobs: int | None = None,
        random_state: RandomState | None | Int = None,
        warm_start: bool = False,
        class_weight: str | None | Mapping[str, float] = None,
        average: bool | int = False,
    ) -> None:
        ...

    def partial_fit(
        self, X: MatrixLike | ArrayLike, y: ArrayLike, classes: None | ArrayLike = None
    ) -> Any:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        coef_init: None | MatrixLike = None,
        intercept_init: None | ArrayLike = None,
    ) -> Any:
        ...


class PassiveAggressiveRegressor(BaseSGDRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        C: Float = 1.0,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: None | Float = 1e-3,
        early_stopping: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: Int = 5,
        shuffle: bool = True,
        verbose: Int = 0,
        loss: str = "epsilon_insensitive",
        epsilon: Float = ...,
        random_state: RandomState | None | Int = None,
        warm_start: bool = False,
        average: bool | int = False,
    ) -> None:
        ...

    def partial_fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        coef_init: None | ArrayLike = None,
        intercept_init: None | ArrayLike = None,
    ) -> Any:
        ...
