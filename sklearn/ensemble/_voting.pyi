from typing import Any, Literal
from ..utils._param_validation import StrOptions as StrOptions
from ..exceptions import NotFittedError as NotFittedError
from .._typing import MatrixLike, ArrayLike, Estimator, Int
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..base import ClassifierMixin, RegressorMixin, TransformerMixin, clone as clone
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    column_or_1d as column_or_1d,
)
from abc import abstractmethod
from ._base import _BaseHeterogeneousEnsemble
from numpy import ndarray
from ..utils import Bunch as Bunch
from numbers import Integral as Integral
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import available_if as available_if

import numpy as np


class _BaseVoting(TransformerMixin, _BaseHeterogeneousEnsemble):

    _parameter_constraints: dict = ...

    @abstractmethod
    def fit(
        self, X: ndarray, y: ndarray, sample_weight=None
    ) -> VotingRegressor | VotingClassifier:
        ...

    def fit_transform(
        self, X: MatrixLike, y: None | ArrayLike = None, **fit_params
    ) -> ndarray:
        ...

    @property
    def n_features_in_(self):
        ...


class VotingClassifier(ClassifierMixin, _BaseVoting):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimators: list[tuple[str, Estimator]],
        *,
        voting: Literal["hard", "soft", "hard"] = "hard",
        weights: None | ArrayLike = None,
        n_jobs: None | Int = None,
        flatten_transform: bool = True,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ArrayLike:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike):
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class VotingRegressor(RegressorMixin, _BaseVoting):
    def __init__(
        self,
        estimators: list[tuple[str, Estimator]],
        *,
        weights: None | ArrayLike = None,
        n_jobs: None | Int = None,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
