from typing import ClassVar, Literal, TypeVar
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    column_or_1d as column_or_1d,
)
from abc import abstractmethod
from ..base import ClassifierMixin, RegressorMixin, BaseEstimator
from ._base import _BaseHeterogeneousEnsemble
from ..exceptions import NotFittedError as NotFittedError
from ..utils._param_validation import StrOptions as StrOptions
from numpy import ndarray
from numbers import Integral as Integral
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..utils.metaestimators import available_if as available_if
from ..base import TransformerMixin, clone as clone
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import MatrixLike, ArrayLike, Int
from ..utils import Bunch
from ..preprocessing import LabelEncoder

VotingClassifier_Self = TypeVar("VotingClassifier_Self", bound="VotingClassifier")
VotingRegressor_Self = TypeVar("VotingRegressor_Self", bound="VotingRegressor")


import numpy as np


class _BaseVoting(TransformerMixin, _BaseHeterogeneousEnsemble):

    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def fit(self, X: ndarray, y: ndarray, sample_weight=None):
        ...

    def fit_transform(
        self, X: MatrixLike, y: None | ArrayLike = None, **fit_params
    ) -> ndarray:
        ...

    def n_features_in_(self):
        ...


class VotingClassifier(ClassifierMixin, _BaseVoting):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    le_: LabelEncoder = ...
    named_estimators_: Bunch = ...
    estimators_: list[ClassifierMixin] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimators: list[tuple[str, BaseEstimator]],
        *,
        voting: Literal["hard", "soft", "hard"] = "hard",
        weights: None | ArrayLike = None,
        n_jobs: None | Int = None,
        flatten_transform: bool = True,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(
        self: VotingClassifier_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> VotingClassifier_Self:
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
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    named_estimators_: Bunch = ...
    estimators_: list[RegressorMixin] = ...

    def __init__(
        self,
        estimators: list[tuple[str, BaseEstimator]],
        *,
        weights: None | ArrayLike = None,
        n_jobs: None | Int = None,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(
        self: VotingRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> VotingRegressor_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
