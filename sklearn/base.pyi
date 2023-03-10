from typing import Any, Iterable
from ._typing import Estimator, MatrixLike, ArrayLike, Float, Int
from .utils._set_output import _SetOutputMixin
from ._config import get_config as get_config
from pandas.core.frame import DataFrame
from scipy.sparse._csr import csr_matrix
from collections import defaultdict as defaultdict
from .utils._estimator_html_repr import estimator_html_repr as estimator_html_repr
from .utils._param_validation import (
    validate_parameter_constraints as validate_parameter_constraints,
)
from .utils.validation import (
    check_X_y as check_X_y,
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from .metrics import accuracy_score as accuracy_score, r2_score as r2_score

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# License: BSD 3 clause

import copy
import warnings
import platform
import inspect
import re

import numpy as np


def clone(estimator: Estimator | Iterable[Estimator], *, safe: bool = True) -> Any:
    ...


class BaseEstimator:
    def get_params(self, deep: bool = True) -> dict:
        ...

    def set_params(self, **params) -> Estimator:
        ...

    def __repr__(self, N_CHAR_MAX: int = 700) -> str:
        ...

    def __getstate__(self):
        ...

    def __setstate__(
        self, state: dict[str, int | None | str | dict[Any, Any] | ndarray]
    ) -> None:
        ...


class ClassifierMixin:

    _estimator_type: str = ...

    def score(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...


class RegressorMixin:

    _estimator_type: str = ...

    def score(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...


class ClusterMixin:

    _estimator_type: str = ...

    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...


class BiclusterMixin:
    @property
    def biclusters_(self):
        ...

    def get_indices(self, i: Int) -> tuple[ndarray, ndarray]:
        ...

    def get_shape(self, i: Int) -> tuple[int, int]:
        ...

    def get_submatrix(self, i: Int, data: MatrixLike) -> ndarray:
        ...


class TransformerMixin(_SetOutputMixin):
    def fit_transform(
        self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None, **fit_params
    ) -> csr_matrix | DataFrame | ndarray:
        ...


class OneToOneFeatureMixin:
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class ClassNamePrefixFeaturesOutMixin:
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class DensityMixin:

    _estimator_type: str = ...

    def score(self, X: MatrixLike, y: Any = None) -> float:
        ...


class OutlierMixin:

    _estimator_type: str = ...

    def fit_predict(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray:
        ...


class MetaEstimatorMixin:
    _required_parameters: list = ...


class MultiOutputMixin:
    pass


class _UnstableArchMixin:
    pass


def is_classifier(estimator: Any) -> bool:
    ...


def is_regressor(estimator: Estimator) -> bool:
    ...


def is_outlier_detector(estimator: Estimator) -> bool:
    ...
