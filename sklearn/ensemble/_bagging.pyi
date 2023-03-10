from typing import Any
from .._typing import ArrayLike, MatrixLike, Int
from ..utils.random import sample_without_replacement as sample_without_replacement
from ..utils._param_validation import (
    Interval as Interval,
    HasMethods as HasMethods,
    StrOptions as StrOptions,
)
from abc import ABCMeta, abstractmethod
from ._base import BaseEnsemble
from ..utils import (
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    indices_to_mask as indices_to_mask,
)
from ..tree._classes import DecisionTreeRegressor, ExtraTreeRegressor
from ..metrics import r2_score as r2_score, accuracy_score as accuracy_score
from ..utils.validation import (
    has_fit_parameter as has_fit_parameter,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from warnings import warn as warn
from numpy.random import RandomState
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..base import ClassifierMixin, RegressorMixin
from ..tree import DecisionTreeClassifier as DecisionTreeClassifier
from functools import partial as partial
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import available_if as available_if

# Author: Gilles Louppe <g.louppe@gmail.com>
# License: BSD 3 clause


import itertools
import numbers
import numpy as np


__all__ = ["BaggingClassifier", "BaggingRegressor"]

MAX_INT = ...


class BaseBagging(BaseEnsemble, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        estimator: ExtraTreeRegressor | None | DecisionTreeRegressor = None,
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
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    @property
    def estimators_samples_(self):
        ...


class BaggingClassifier(ClassifierMixin, BaseBagging):
    def __init__(
        self,
        estimator: Any = None,
        n_estimators: Int = 10,
        *,
        max_samples: int | float = 1.0,
        max_features: int | float = 1.0,
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
    def __init__(
        self,
        estimator: Any = None,
        n_estimators: Int = 10,
        *,
        max_samples: int | float = 1.0,
        max_features: int | float = 1.0,
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
