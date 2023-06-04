from typing import ClassVar, TypeVar
from numpy.random import RandomState
from .base import (
    ClassifierMixin,
    clone as clone,
    is_classifier as is_classifier,
    MultiOutputMixin,
    MetaEstimatorMixin,
    is_regressor as is_regressor,
)
from .preprocessing import LabelBinarizer
from .base import BaseEstimator
from .utils.validation import check_is_fitted as check_is_fitted
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from .utils.metaestimators import available_if as available_if
from .utils import check_random_state as check_random_state
from .utils._param_validation import HasMethods as HasMethods, Interval as Interval
from ._typing import Int, MatrixLike, ArrayLike, Float
from .metrics.pairwise import euclidean_distances as euclidean_distances
from .utils.parallel import delayed as delayed, Parallel as Parallel

OneVsRestClassifier_Self = TypeVar(
    "OneVsRestClassifier_Self", bound="OneVsRestClassifier"
)
OneVsOneClassifier_Self = TypeVar("OneVsOneClassifier_Self", bound="OneVsOneClassifier")
OutputCodeClassifier_Self = TypeVar(
    "OutputCodeClassifier_Self", bound="OutputCodeClassifier"
)


# Author: Mathieu Blondel <mathieu@mblondel.org>
# Author: Hamzeh Alsalhi <93hamsal@gmail.com>
#
# License: BSD 3 clause

import array
import numpy as np
import warnings
import scipy.sparse as sp
import itertools

__all__ = [
    "OneVsRestClassifier",
    "OneVsOneClassifier",
    "OutputCodeClassifier",
]


class _ConstantPredictor(BaseEstimator):
    def fit(self, X, y):
        ...

    def predict(self, X):
        ...

    def decision_function(self, X):
        ...

    def predict_proba(self, X):
        ...


class OneVsRestClassifier(
    MultiOutputMixin, ClassifierMixin, MetaEstimatorMixin, BaseEstimator
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    label_binarizer_: LabelBinarizer = ...
    classes_: ndarray = ...
    estimators_: list[BaseEstimator] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, estimator: BaseEstimator, *, n_jobs: None | Int = None, verbose: Int = 0
    ) -> None:
        ...

    def fit(
        self: OneVsRestClassifier_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
    ) -> OneVsRestClassifier_Self:
        ...

    def partial_fit(
        self: OneVsRestClassifier_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        classes: None | ArrayLike = None,
    ) -> OneVsRestClassifier_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    @property
    def multilabel_(self) -> bool:
        ...

    @property
    def n_classes_(self) -> int:
        ...


class OneVsOneClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    pairwise_indices_: None | list = ...
    classes_: ndarray = ...
    estimators_: list[BaseEstimator] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, estimator: BaseEstimator, *, n_jobs: None | Int = None) -> None:
        ...

    def fit(
        self: OneVsOneClassifier_Self, X: MatrixLike | ArrayLike, y: ArrayLike
    ) -> OneVsOneClassifier_Self:
        ...

    def partial_fit(
        self: OneVsOneClassifier_Self,
        X: MatrixLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
    ) -> OneVsOneClassifier_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    @property
    def n_classes_(self) -> int:
        ...


class OutputCodeClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    code_book_: ndarray = ...
    classes_: ndarray = ...
    estimators_: list[BaseEstimator] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        code_size: Float = 1.5,
        random_state: RandomState | None | Int = None,
        n_jobs: None | Int = None
    ) -> None:
        ...

    def fit(
        self: OutputCodeClassifier_Self, X: MatrixLike | ArrayLike, y: ArrayLike
    ) -> OutputCodeClassifier_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
