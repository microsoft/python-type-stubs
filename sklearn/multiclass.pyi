from numpy import int64, ndarray
from typing import Callable, List, Optional, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Mathieu Blondel <mathieu@mblondel.org>
# Author: Hamzeh Alsalhi <93hamsal@gmail.com>
#
# License: BSD 3 clause

import array
import numpy as np
import warnings
import scipy.sparse as sp
import itertools
from numpy.random import RandomState

from .base import BaseEstimator, ClassifierMixin, clone, is_classifier
from .base import MultiOutputMixin
from .base import MetaEstimatorMixin, is_regressor
from .preprocessing import LabelBinarizer
from .metrics.pairwise import euclidean_distances
from .utils import check_random_state
from .utils._tags import _safe_tags
from .utils.validation import _num_samples
from .utils.validation import check_is_fitted
from .utils.multiclass import (
    _check_partial_fit_first_call,
    check_classification_targets,
    _ovr_decision_function,
)
from .utils.metaestimators import _safe_split, available_if
from .utils.fixes import delayed
from sklearn.gaussian_process._gpc import _BinaryGaussianProcessClassifierLaplace
from sklearn.pipeline import Pipeline
from sklearn.svm._classes import SVC

__all__ = [
    "OneVsRestClassifier",
    "OneVsOneClassifier",
    "OutputCodeClassifier",
]

def _fit_binary(
    estimator: Union[Pipeline, _BinaryGaussianProcessClassifierLaplace, SVC],
    X: ndarray,
    y: ndarray,
    classes: Optional[List[Union[str, int64]]] = None,
) -> Union[Pipeline, _BinaryGaussianProcessClassifierLaplace, SVC]: ...
def _partial_fit_binary(estimator, X, y): ...
def _predict_binary(
    estimator: _BinaryGaussianProcessClassifierLaplace, X: ndarray
) -> ndarray: ...
def _threshold_for_binary_predict(estimator): ...
def _check_estimator(estimator): ...

class _ConstantPredictor(BaseEstimator):
    def fit(self, X, y): ...
    def predict(self, X): ...
    def decision_function(self, X): ...
    def predict_proba(self, X): ...

def _estimators_has(attr: str) -> Callable: ...

class OneVsRestClassifier(
    MultiOutputMixin, ClassifierMixin, MetaEstimatorMixin, BaseEstimator
):
    def __init__(
        self, estimator: BaseEstimator, *, n_jobs: int | None = None, verbose: int = 0
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "OneVsRestClassifier": ...
    @available_if(_estimators_has("partial_fit"))
    def partial_fit(
        self, X: ArrayLike, y: ArrayLike, classes: NDArray | None = None
    ) -> Any: ...
    def predict(self, X: ArrayLike) -> ArrayLike: ...
    @available_if(_estimators_has("predict_proba"))
    def predict_proba(self, X: ArrayLike) -> ArrayLike: ...
    @available_if(_estimators_has("decision_function"))
    def decision_function(self, X: ArrayLike) -> ArrayLike: ...
    @property
    def multilabel_(self) -> bool: ...
    @property
    def n_classes_(self): ...
    def _more_tags(self): ...

def _fit_ovo_binary(estimator, X, y, i, j): ...
def _partial_fit_ovo_binary(estimator, X, y, i, j): ...

class OneVsOneClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    def __init__(self, estimator: BaseEstimator, *, n_jobs: int | None = None): ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> Any: ...
    @available_if(_estimators_has("partial_fit"))
    def partial_fit(
        self, X: ArrayLike, y: ArrayLike, classes: NDArray | None = None
    ) -> Any: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def decision_function(self, X: ArrayLike) -> ArrayLike: ...
    @property
    def n_classes_(self): ...
    def _more_tags(self): ...

class OutputCodeClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        code_size: float = 1.5,
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None
    ): ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> Any: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
