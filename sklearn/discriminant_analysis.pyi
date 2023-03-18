from typing import ClassVar, Literal, TypeVar
from .covariance._shrunk_covariance import OAS
from scipy import linalg
from .base import TransformerMixin, ClassifierMixin, ClassNamePrefixFeaturesOutMixin
from .base import BaseEstimator
from .utils.multiclass import (
    unique_labels as unique_labels,
    check_classification_targets as check_classification_targets,
)
from .utils.validation import check_is_fitted as check_is_fitted
from .preprocessing import StandardScaler as StandardScaler
from .utils._array_api import get_namespace as get_namespace
from numbers import Real as Real, Integral as Integral
from .utils.extmath import softmax as softmax
from numpy import ndarray
from .covariance import (
    ledoit_wolf as ledoit_wolf,
    empirical_covariance as empirical_covariance,
    shrunk_covariance as shrunk_covariance,
)
from .utils._param_validation import (
    StrOptions as StrOptions,
    Interval as Interval,
    HasMethods as HasMethods,
)
from ._typing import ArrayLike, Int, Float, MatrixLike
from .linear_model._base import LinearClassifierMixin

LinearDiscriminantAnalysis_Self = TypeVar(
    "LinearDiscriminantAnalysis_Self", bound="LinearDiscriminantAnalysis"
)
QuadraticDiscriminantAnalysis_Self = TypeVar(
    "QuadraticDiscriminantAnalysis_Self", bound="QuadraticDiscriminantAnalysis"
)


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
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ArrayLike = ...
    xbar_: ArrayLike = ...
    scalings_: ArrayLike = ...
    priors_: ArrayLike = ...
    means_: ArrayLike = ...
    explained_variance_ratio_: ndarray = ...
    covariance_: ArrayLike = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        solver: Literal["svd", "lsqr", "eigen", "svd"] = "svd",
        shrinkage: float | None | str = None,
        priors: None | ArrayLike = None,
        n_components: None | Int = None,
        store_covariance: bool = False,
        tol: Float = 1e-4,
        covariance_estimator: None | BaseEstimator | OAS = None,
    ) -> None:
        ...

    def fit(
        self: LinearDiscriminantAnalysis_Self, X: MatrixLike, y: ArrayLike
    ) -> LinearDiscriminantAnalysis_Self:
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
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    scalings_: list[ndarray] = ...
    rotations_: list[ndarray] = ...
    priors_: ArrayLike = ...
    means_: ArrayLike = ...
    covariance_: list[ndarray] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        priors: None | ArrayLike = None,
        reg_param: Float = 0.0,
        store_covariance: bool = False,
        tol: Float = 1.0e-4
    ) -> None:
        ...

    def fit(
        self: QuadraticDiscriminantAnalysis_Self, X: MatrixLike, y: ArrayLike
    ) -> QuadraticDiscriminantAnalysis_Self:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...
