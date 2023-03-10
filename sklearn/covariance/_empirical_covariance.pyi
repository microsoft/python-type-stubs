from typing import Any, Literal
from ..utils.extmath import fast_logdet as fast_logdet
from .._typing import MatrixLike, Float, ArrayLike
from scipy import linalg as linalg
from ..base import BaseEstimator
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from numpy import ndarray
from ..utils import check_array as check_array
from .. import config_context as config_context

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation
import warnings
import numpy as np


def log_likelihood(emp_cov: MatrixLike, precision: MatrixLike) -> Float:
    ...


def empirical_covariance(X: ArrayLike, *, assume_centered: bool = False) -> ndarray:
    ...


class EmpiricalCovariance(BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, store_precision: bool = True, assume_centered: bool = False
    ) -> None:
        ...

    def get_precision(self) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def score(self, X_test: MatrixLike, y: Any = None) -> Float:
        ...

    def error_norm(
        self,
        comp_cov: MatrixLike,
        norm: Literal["frobenius", "frobenius", "spectral"] = "frobenius",
        scaling: bool = True,
        squared: bool = True,
    ) -> Float:
        ...

    def mahalanobis(self, X: MatrixLike) -> ndarray:
        ...
