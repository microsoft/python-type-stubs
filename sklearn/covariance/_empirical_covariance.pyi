from typing import Any, Literal
from numpy.typing import NDArray, ArrayLike

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation
import warnings
import numpy as np
from scipy import linalg

from .. import config_context
from ..base import BaseEstimator
from ..utils import check_array
from ..utils.extmath import fast_logdet
from ..metrics.pairwise import pairwise_distances
from numpy import float64, ndarray

def log_likelihood(emp_cov: NDArray, precision: NDArray) -> float: ...
def empirical_covariance(X: NDArray, *, assume_centered: bool = False) -> NDArray: ...

class EmpiricalCovariance(BaseEstimator):
    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False) -> None: ...
    def _set_covariance(self, covariance: ndarray) -> None: ...
    def get_precision(self) -> ArrayLike: ...
    def fit(self, X: ArrayLike, y: None = None) -> "EmpiricalCovariance": ...
    def score(self, X_test: ArrayLike, y: None = None) -> float: ...
    def error_norm(
        self,
        comp_cov: ArrayLike,
        norm: Literal["frobenius", "spectral"] = "frobenius",
        scaling: bool = True,
        squared: bool = True,
    ) -> float: ...
    def mahalanobis(self, X: ArrayLike) -> NDArray: ...
