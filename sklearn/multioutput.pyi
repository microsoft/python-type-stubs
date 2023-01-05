from numpy import ndarray
from typing import Callable, Sequence, Any
from numpy.typing import ArrayLike, NDArray

# Author: Tim Head <betatim@gmail.com>
# Author: Hugo Bowne-Anderson <hugobowne@gmail.com>
# Author: Chris Rivera <chris.richard.rivera@gmail.com>
# Author: Michael Williamson
# Author: James Ashton Nichols <james.ashton.nichols@gmail.com>
#
# License: BSD 3 clause

import numpy as np
import scipy.sparse as sp
from joblib import Parallel

from abc import ABCMeta, abstractmethod
from .base import BaseEstimator, clone, MetaEstimatorMixin
from .base import RegressorMixin, ClassifierMixin, is_classifier
from .model_selection import cross_val_predict
from .utils.metaestimators import available_if
from .utils import check_random_state
from .utils.validation import check_is_fitted, has_fit_parameter, _check_fit_params
from .utils.multiclass import check_classification_targets
from .utils.fixes import delayed
from sklearn.ensemble._forest import RandomForestRegressor

__all__ = [
    "MultiOutputRegressor",
    "MultiOutputClassifier",
    "ClassifierChain",
    "RegressorChain",
]

def _fit_estimator(
    estimator: RandomForestRegressor, X: ndarray, y: ndarray, sample_weight: None = None, **fit_params
) -> RandomForestRegressor: ...
def _partial_fit_estimator(estimator, X, y, classes=None, sample_weight=None, first_time=True): ...
def _available_if_estimator_has(attr: str) -> Callable: ...

class _MultiOutputEstimator(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, estimator: RandomForestRegressor, *, n_jobs=None) -> None: ...
    @_available_if_estimator_has("partial_fit")
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray | ArrayLike,
        classes: Sequence[NDArray] | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def fit(
        self, X: NDArray | ArrayLike, y: NDArray | ArrayLike, sample_weight: ArrayLike | None = None, **fit_params
    ) -> "MultiOutputRegressor": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray | ArrayLike: ...
    def _more_tags(self): ...

class MultiOutputRegressor(RegressorMixin, _MultiOutputEstimator):
    def __init__(self, estimator: Estimator, *, n_jobs: int | None = None) -> None: ...
    @_available_if_estimator_has("partial_fit")
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray | ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...

class MultiOutputClassifier(ClassifierMixin, _MultiOutputEstimator):
    def __init__(self, estimator: Estimator, *, n_jobs: int | None = None): ...
    def fit(self, X: NDArray | ArrayLike, Y: ArrayLike, sample_weight: ArrayLike | None = None, **fit_params) -> Any: ...
    def _check_predict_proba(self): ...
    @available_if(_check_predict_proba)
    def predict_proba(self, X: ArrayLike) -> NDArray | list[NDArray]: ...
    def score(self, X: ArrayLike, y: ArrayLike) -> float: ...
    def _more_tags(self): ...

def _available_if_base_estimator_has(attr: str) -> Callable: ...

class _BaseChain(BaseEstimator, metaclass=ABCMeta):
    def __init__(self, base_estimator, *, order=None, cv=None, random_state=None): ...
    @abstractmethod
    def fit(self, X: NDArray | ArrayLike, Y: ArrayLike, **fit_params) -> Any: ...
    def predict(self, X: NDArray | ArrayLike) -> ArrayLike: ...

class ClassifierChain(MetaEstimatorMixin, ClassifierMixin, _BaseChain):
    def fit(self, X: NDArray | ArrayLike, Y: ArrayLike) -> Any: ...
    @_available_if_base_estimator_has("predict_proba")
    def predict_proba(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    @_available_if_base_estimator_has("decision_function")
    def decision_function(self, X: ArrayLike) -> ArrayLike: ...
    def _more_tags(self): ...

class RegressorChain(MetaEstimatorMixin, RegressorMixin, _BaseChain):
    def fit(self, X: NDArray | ArrayLike, Y: ArrayLike, **fit_params) -> Any: ...
    def _more_tags(self): ...
