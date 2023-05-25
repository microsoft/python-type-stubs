from typing import Callable, ClassVar, Iterable, Literal, TypeVar
from ..model_selection import BaseCrossValidator
from ..base import BaseEstimator
from ._base import SelectorMixin
from ..model_selection._split import BaseShuffleSplit
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from ..base import MetaEstimatorMixin, clone as clone
from ..model_selection import cross_val_score as cross_val_score
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..metrics import get_scorer_names as get_scorer_names
from ..utils.validation import check_is_fitted as check_is_fitted

SequentialFeatureSelector_Self = TypeVar(
    "SequentialFeatureSelector_Self", bound="SequentialFeatureSelector"
)


import numpy as np

import warnings


class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    support_: ndarray = ...
    n_features_to_select_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        n_features_to_select: float | int | Literal["auto", "warn"] = "warn",
        tol: None | Float = None,
        direction: Literal["forward", "backward", "forward"] = "forward",
        scoring: None | str | Callable = None,
        cv: Iterable | int | BaseShuffleSplit | BaseCrossValidator = 5,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: SequentialFeatureSelector_Self, X: MatrixLike, y: None | ArrayLike = None
    ) -> SequentialFeatureSelector_Self:
        ...
