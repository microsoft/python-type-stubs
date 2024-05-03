from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from scipy import linalg as linalg

from .. import config_context as config_context
from .._typing import ArrayLike, Float, MatrixLike
from ..base import BaseEstimator
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from ..utils import check_array as check_array
from ..utils.extmath import fast_logdet as fast_logdet

EmpiricalCovariance_Self = TypeVar("EmpiricalCovariance_Self", bound="EmpiricalCovariance")

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation
import warnings

import numpy as np

def log_likelihood(emp_cov: MatrixLike, precision: MatrixLike) -> Float: ...
def empirical_covariance(X: ArrayLike, *, assume_centered: bool = False) -> ndarray: ...

class EmpiricalCovariance(BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    precision_: ndarray = ...
    covariance_: ndarray = ...
    location_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False) -> None: ...
    def get_precision(self) -> ndarray: ...
    def fit(self: EmpiricalCovariance_Self, X: MatrixLike, y: Any = None) -> EmpiricalCovariance_Self: ...
    def score(self, X_test: MatrixLike, y: Any = None) -> Float: ...
    def error_norm(
        self,
        comp_cov: MatrixLike,
        norm: Literal["frobenius", "spectral", "frobenius"] = "frobenius",
        scaling: bool = True,
        squared: bool = True,
    ) -> Float: ...
    def mahalanobis(self, X: MatrixLike) -> ndarray: ...
