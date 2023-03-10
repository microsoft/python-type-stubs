from typing import Any, Literal
from .linear_model._base import LinearClassifierMixin
from ._typing import ArrayLike, Int, Float, Estimator, MatrixLike
from .covariance import (
    ledoit_wolf as ledoit_wolf,
    empirical_covariance as empirical_covariance,
    shrunk_covariance as shrunk_covariance,
)
from scipy import linalg
from .base import (
    BaseEstimator,
    TransformerMixin,
    ClassifierMixin,
    ClassNamePrefixFeaturesOutMixin,
)
from .utils.multiclass import (
    unique_labels as unique_labels,
    check_classification_targets as check_classification_targets,
)
from numpy import ndarray
from .utils.extmath import softmax as softmax
from .utils._array_api import get_namespace as get_namespace
from numbers import Real as Real, Integral as Integral
from .utils.validation import check_is_fitted as check_is_fitted
from .utils._param_validation import (
    StrOptions as StrOptions,
    Interval as Interval,
    HasMethods as HasMethods,
)
from .preprocessing import StandardScaler as StandardScaler
from .covariance._shrunk_covariance import OAS

# Authors: Clemens Brunner
#          Martin Billinger
#          Matthieu Perrot
#          Mathieu Blondel

# License: BSD 3-Clause

import warnings
import numpy as np
import scipy.linalg


__all__ = ["LinearDiscriminantAnalysis", "QuadraticDiscriminantAnalysis"]


class LinearDiscriminantAnalysis(
    ClassNamePrefixFeaturesOutMixin,
    LinearClassifierMixin,
    TransformerMixin,
    BaseEstimator,
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        solver: Literal["svd", "svd", "lsqr", "eigen"] = "svd",
        shrinkage: float | None | str = None,
        priors: None | ArrayLike = None,
        n_components: None | Int = None,
        store_covariance: bool = False,
        tol: Float = 1e-4,
        covariance_estimator: OAS | Estimator | None = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...


class QuadraticDiscriminantAnalysis(ClassifierMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        priors: None | ArrayLike = None,
        reg_param: Float = 0.0,
        store_covariance: bool = False,
        tol: Float = 1.0e-4
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...
