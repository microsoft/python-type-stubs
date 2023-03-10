from typing import Any, Iterable, Literal, Sequence
from .._typing import ArrayLike, MatrixLike, Estimator, Int
from ..preprocessing import LabelEncoder as LabelEncoder
from ..model_selection import BaseCrossValidator
from ..utils._param_validation import HasMethods as HasMethods, StrOptions as StrOptions
from ..linear_model._ridge import RidgeCV
from ..model_selection import (
    cross_val_predict as cross_val_predict,
    check_cv as check_cv,
)
from abc import ABCMeta, abstractmethod
from ._base import _BaseHeterogeneousEnsemble
from ..utils import Bunch as Bunch
from copy import deepcopy as deepcopy
from ..pipeline import Pipeline
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    column_or_1d as column_or_1d,
)
from numpy import ndarray
from ._forest import RandomForestClassifier
from ..linear_model._logistic import LogisticRegression
from ..exceptions import NotFittedError as NotFittedError
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
    type_of_target as type_of_target,
)
from ..base import (
    clone as clone,
    ClassifierMixin,
    RegressorMixin,
    TransformerMixin,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
)
from numbers import Integral as Integral
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import available_if as available_if

import numpy as np
import scipy.sparse as sparse


class _BaseStacking(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        estimators: list[tuple[str, RandomForestClassifier] | tuple[str, Pipeline]],
        final_estimator: RidgeCV | None | LogisticRegression = None,
        *,
        cv=None,
        stack_method: str = "auto",
        n_jobs=None,
        verbose: int = 0,
        passthrough: bool = False,
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
    def n_features_in_(self):
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray:
        ...


class StackingClassifier(ClassifierMixin, _BaseStacking):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimators: Sequence[tuple[str, Estimator]]
        | list[tuple[str, RandomForestClassifier] | tuple[str, Pipeline]],
        final_estimator: Estimator | None | LogisticRegression = None,
        *,
        cv: BaseCrossValidator | int | str | Iterable | None = None,
        stack_method: Literal[
            "auto", "predict_proba", "decision_function", "predict", "auto"
        ] = "auto",
        n_jobs: None | Int = None,
        passthrough: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> list[ndarray] | ndarray:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike):
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class StackingRegressor(RegressorMixin, _BaseStacking):
    def __init__(
        self,
        estimators: Sequence[tuple[str, Estimator]] | list[tuple[str, Pipeline]],
        final_estimator: RidgeCV | Estimator | None = None,
        *,
        cv: BaseCrossValidator | int | str | Iterable | None = None,
        n_jobs: None | Int = None,
        passthrough: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
