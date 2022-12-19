from numpy import ndarray
from typing import Optional, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Clemens Brunner
#          Martin Billinger
#          Matthieu Perrot
#          Mathieu Blondel

# License: BSD 3-Clause

import warnings
import numpy as np
from scipy import linalg
from scipy.special import expit
from numbers import Real

from .base import BaseEstimator, TransformerMixin, ClassifierMixin
from .base import _ClassNamePrefixFeaturesOutMixin
from .linear_model._base import LinearClassifierMixin
from .covariance import ledoit_wolf, empirical_covariance, shrunk_covariance
from .utils.multiclass import unique_labels
from .utils.validation import check_is_fitted
from .utils.multiclass import check_classification_targets
from .utils.extmath import softmax
from .preprocessing import StandardScaler
from sklearn.covariance._shrunk_covariance import OAS

__all__ = ["LinearDiscriminantAnalysis", "QuadraticDiscriminantAnalysis"]

def _cov(
    X: ndarray,
    shrinkage: Optional[str] = None,
    covariance_estimator: Optional[OAS] = None,
) -> ndarray: ...
def _class_means(X: ndarray, y: ndarray) -> ndarray: ...
def _class_cov(
    X: ndarray,
    y: ndarray,
    priors: ndarray,
    shrinkage: Optional[str] = None,
    covariance_estimator: Optional[OAS] = None,
) -> ndarray: ...

class LinearDiscriminantAnalysis(
    _ClassNamePrefixFeaturesOutMixin,
    LinearClassifierMixin,
    TransformerMixin,
    BaseEstimator,
):
    def __init__(
        self,
        solver: Literal["svd", "lsqr", "eigen"] = "svd",
        shrinkage: float | Literal["auto"] | None = None,
        priors: ArrayLike | None = None,
        n_components: int | None = None,
        store_covariance: bool = False,
        tol: float = 1e-4,
        covariance_estimator: Estimator | None = None,
    ) -> None: ...
    def _solve_lsqr(
        self,
        X: ndarray,
        y: ndarray,
        shrinkage: Optional[str],
        covariance_estimator: Optional[OAS],
    ) -> None: ...
    def _solve_eigen(self, X, y, shrinkage, covariance_estimator): ...
    def _solve_svd(self, X: ndarray, y: ndarray) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "LinearDiscriminantAnalysis": ...
    def transform(self, X: ArrayLike) -> ndarray: ...
    def predict_proba(self, X: ArrayLike) -> np.ndarray: ...
    def predict_log_proba(self, X: ArrayLike) -> np.ndarray: ...
    def decision_function(self, X: ArrayLike) -> NDArray: ...

class QuadraticDiscriminantAnalysis(ClassifierMixin, BaseEstimator):
    def __init__(
        self, *, priors: NDArray | None = None, reg_param: float = 0.0, store_covariance: bool = False, tol: float = 1.0e-4
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "QuadraticDiscriminantAnalysis": ...
    def _decision_function(self, X: ndarray) -> ndarray: ...
    def decision_function(self, X: ArrayLike) -> NDArray: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def predict_proba(self, X: ArrayLike) -> np.ndarray: ...
    def predict_log_proba(self, X: ArrayLike) -> np.ndarray: ...
