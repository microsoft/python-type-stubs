from typing import Callable, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray
import warnings

import numpy as np

from ..base import MetaEstimatorMixin, clone, BaseEstimator
from ..utils.validation import check_is_fitted
from ..utils.metaestimators import available_if
from ..utils import safe_mask
from numpy import float64, ndarray
from scipy.sparse._csr import csr_matrix
from sklearn.linear_model._stochastic_gradient import SGDClassifier
from sklearn.svm._classes import SVC

__all__ = ["SelfTrainingClassifier"]

# Authors: Oliver Rausch   <rauscho@ethz.ch>
#          Patrice Becker  <beckerp@ethz.ch>
# License: BSD 3 clause

def _estimator_has(attr: str) -> Callable: ...

class SelfTrainingClassifier(MetaEstimatorMixin, BaseEstimator):

    _estimator_type: str = ...

    def __init__(
        self,
        base_estimator: Estimator,
        threshold: float = 0.75,
        criterion: Literal["threshold", "k_best"] = "threshold",
        k_best: int = 10,
        max_iter: int | None = 10,
        verbose: bool = False,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: NDArray | ArrayLike) -> "SelfTrainingClassifier": ...
    @available_if(_estimator_has("predict"))
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    @available_if(_estimator_has("predict_proba"))
    def predict_proba(self, X: NDArray | ArrayLike) -> NDArray: ...
    @available_if(_estimator_has("decision_function"))
    def decision_function(self, X: NDArray | ArrayLike) -> NDArray: ...
    @available_if(_estimator_has("predict_log_proba"))
    def predict_log_proba(self, X: NDArray | ArrayLike) -> NDArray: ...
    @available_if(_estimator_has("score"))
    def score(self, X: NDArray | ArrayLike, y: ArrayLike) -> float: ...
