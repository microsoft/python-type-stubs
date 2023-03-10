from typing import Any
from .utils import check_random_state as check_random_state
from .metrics.pairwise import euclidean_distances as euclidean_distances
from .utils.parallel import delayed as delayed, Parallel as Parallel
from ._typing import Estimator, Int, ArrayLike, MatrixLike, Float
from .base import (
    BaseEstimator,
    ClassifierMixin,
    clone as clone,
    is_classifier as is_classifier,
    MultiOutputMixin,
    MetaEstimatorMixin,
    is_regressor as is_regressor,
)
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from numpy.random import RandomState
from numpy import ndarray
from .utils._param_validation import HasMethods as HasMethods, Interval as Interval
from numbers import Integral as Integral, Real as Real
from .utils.validation import check_is_fitted as check_is_fitted
from .utils.metaestimators import available_if as available_if
from .preprocessing import LabelBinarizer as LabelBinarizer

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

    _parameter_constraints: dict = ...

    def __init__(
        self, estimator: Estimator, *, n_jobs: None | Int = None, verbose: Int = 0
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: MatrixLike | ArrayLike) -> Any:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        classes: None | ArrayLike = None,
    ) -> Any:
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

    _parameter_constraints: dict = ...

    def __init__(self, estimator: Estimator, *, n_jobs: None | Int = None) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
        ...

    def partial_fit(
        self, X: MatrixLike, y: ArrayLike, classes: None | ArrayLike = None
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    @property
    def n_classes_(self) -> int:
        ...


class OutputCodeClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: Estimator,
        *,
        code_size: Float = 1.5,
        random_state: RandomState | None | Int = None,
        n_jobs: None | Int = None
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
