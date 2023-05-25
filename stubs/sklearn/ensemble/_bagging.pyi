from typing import Any, ClassVar, TypeVar
from warnings import warn as warn
from numpy.random import RandomState
from ..base import BaseEstimator
from ..utils.random import sample_without_replacement as sample_without_replacement
from ..metrics import r2_score as r2_score, accuracy_score as accuracy_score
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.validation import (
    has_fit_parameter as has_fit_parameter,
    check_is_fitted as check_is_fitted,
)
from abc import ABCMeta, abstractmethod
from ..tree import (
    DecisionTreeClassifier as DecisionTreeClassifier,
    DecisionTreeRegressor as DecisionTreeRegressor,
)
from numpy import ndarray
from ..utils._param_validation import (
    Interval as Interval,
    HasMethods as HasMethods,
    StrOptions as StrOptions,
)
from numbers import Integral as Integral, Real as Real
from functools import partial as partial
from ..base import ClassifierMixin, RegressorMixin
from ..utils import (
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    indices_to_mask as indices_to_mask,
)
from ._base import BaseEnsemble
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..utils.metaestimators import available_if as available_if
from .._typing import MatrixLike, ArrayLike, Int

BaseBagging_Self = TypeVar("BaseBagging_Self", bound="BaseBagging")


# Author: Gilles Louppe <g.louppe@gmail.com>
# License: BSD 3 clause


import itertools
import numbers
import numpy as np


__all__ = ["BaggingClassifier", "BaggingRegressor"]

MAX_INT = ...


class BaseBagging(BaseEnsemble, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        estimator=None,
        n_estimators: int = 10,
        *,
        max_samples: float = 1.0,
        max_features: float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        base_estimator: str = "deprecated",
    ) -> None:
        ...

    def fit(
        self: BaseBagging_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> BaggingRegressor | BaseBagging_Self:
        ...

    def estimators_samples_(self):
        ...


class BaggingClassifier(ClassifierMixin, BaseBagging):
    oob_decision_function_: ndarray = ...
    oob_score_: float = ...
    n_classes_: list | int = ...
    classes_: ndarray = ...
    estimators_features_: list[ArrayLike] = ...
    estimators_samples_: list[ArrayLike] = ...
    estimators_: list[BaseEstimator] = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    base_estimator_: BaseEstimator = ...
    estimator_: BaseEstimator = ...

    def __init__(
        self,
        estimator: Any = None,
        n_estimators: Int = 10,
        *,
        max_samples: float | int = 1.0,
        max_features: float | int = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class BaggingRegressor(RegressorMixin, BaseBagging):
    oob_prediction_: ndarray = ...
    oob_score_: float = ...
    estimators_features_: list[ArrayLike] = ...
    estimators_samples_: list[ArrayLike] = ...
    estimators_: list[BaseEstimator] = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    base_estimator_: BaseEstimator = ...
    estimator_: BaseEstimator = ...

    def __init__(
        self,
        estimator: Any = None,
        n_estimators: Int = 10,
        *,
        max_samples: float | int = 1.0,
        max_features: float | int = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
