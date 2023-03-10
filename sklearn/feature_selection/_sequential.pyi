from typing import Any, Callable, Iterable, Literal
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from collections.abc import Iterable
from ..linear_model._ridge import RidgeCV
from .._typing import Estimator, Float, Int, MatrixLike, ArrayLike
from ..base import BaseEstimator, MetaEstimatorMixin, clone as clone
from ..model_selection import cross_val_score as cross_val_score
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin
from numbers import Integral as Integral, Real as Real
from ..neighbors._classification import KNeighborsClassifier
from ..model_selection import BaseCrossValidator
from ..metrics import get_scorer_names as get_scorer_names

import numpy as np

import warnings


class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: RidgeCV | Estimator | KNeighborsClassifier,
        *,
        n_features_to_select: int | float | Literal["auto", "warn"] = "warn",
        tol: None | Float = None,
        direction: Literal["forward", "backward", "forward"] = "forward",
        scoring: str | None | Callable = None,
        cv: Iterable | BaseCrossValidator | int = 5,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | ArrayLike = None) -> Any:
        ...
