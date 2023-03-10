from typing import Any, Callable
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import fast_logdet as fast_logdet
from numpy.random import RandomState
from .._typing import MatrixLike, Int, Float
from scipy import linalg as linalg
from scipy.stats import chi2 as chi2
from numpy import ndarray
from . import empirical_covariance as empirical_covariance, EmpiricalCovariance
from ..utils import check_random_state as check_random_state, check_array as check_array
from numbers import Integral as Integral, Real as Real

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

import warnings
import numpy as np


# Minimum Covariance Determinant
#   Implementing of an algorithm by Rousseeuw & Van Driessen described in
#   (A Fast Algorithm for the Minimum Covariance Determinant Estimator,
#   1999, American Statistical Association and the American Society
#   for Quality, TECHNOMETRICS)
# XXX Is this really a public function? It's not listed in the docs or
# exported by sklearn.covariance. Deprecate?
def c_step(
    X: MatrixLike,
    n_support: Int,
    remaining_iterations: Int = 30,
    initial_estimates: None | tuple[Any, Any] = None,
    verbose: bool = False,
    cov_computation_method: Callable = ...,
    random_state: RandomState | None | Int = None,
) -> tuple[ndarray, ndarray, ndarray]:
    ...


def select_candidates(
    X: MatrixLike,
    n_support: Int,
    n_trials: int | tuple[Any, Any] | tuple[ndarray, ndarray],
    select: Int = 1,
    n_iter: Int = 30,
    verbose: bool = False,
    cov_computation_method: Callable = ...,
    random_state: RandomState | None | Int = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray] | tuple[ndarray, ndarray, ndarray]:
    ...


def fast_mcd(
    X: MatrixLike,
    support_fraction: None | Float = None,
    cov_computation_method: Callable = ...,
    random_state: RandomState | None | Int = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray] | tuple[ndarray, ndarray, ndarray]:
    ...


class MinCovDet(EmpiricalCovariance):

    _parameter_constraints: dict = ...
    _nonrobust_covariance = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def correct_covariance(self, data: MatrixLike) -> ndarray:
        ...

    def reweight_covariance(self, data: MatrixLike) -> tuple[ndarray, ndarray, ndarray]:
        ...
