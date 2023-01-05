from numpy import float64, ndarray
from typing import Optional, Tuple, Union, Callable, Any
from numpy.typing import ArrayLike, NDArray

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

import warnings
import numbers
import numpy as np
from scipy import linalg

from . import empirical_covariance, EmpiricalCovariance
from ..utils.extmath import fast_logdet
from ..utils import check_random_state, check_array
from numpy.random import RandomState
from sklearn.covariance._elliptic_envelope import EllipticEnvelope

# Minimum Covariance Determinant
#   Implementing of an algorithm by Rousseeuw & Van Driessen described in
#   (A Fast Algorithm for the Minimum Covariance Determinant Estimator,
#   1999, American Statistical Association and the American Society
#   for Quality, TECHNOMETRICS)
# XXX Is this really a public function? It's not listed in the docs or
# exported by sklearn.covariance. Deprecate?
def c_step(
    X: ArrayLike,
    n_support: int,
    remaining_iterations: int = 30,
    initial_estimates: tuple | None = None,
    verbose: bool = False,
    cov_computation_method: Callable = ...,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray, NDArray]: ...
def _c_step(
    X: ndarray,
    n_support: int,
    random_state: RandomState,
    remaining_iterations: int = 30,
    initial_estimates: Optional[Tuple[ndarray, ndarray]] = None,
    verbose: bool = False,
    cov_computation_method: Callable = empirical_covariance,
) -> Tuple[ndarray, ndarray, float64, ndarray, ndarray]: ...
def select_candidates(
    X: ArrayLike,
    n_support: int,
    n_trials: int | tuple,
    select: int = 1,
    n_iter: int = 30,
    verbose: bool = False,
    cov_computation_method: Callable = ...,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: ...
def fast_mcd(
    X: ArrayLike,
    support_fraction: float | None = None,
    cov_computation_method: Callable = ...,
    random_state: int | RandomState | None = None,
) -> tuple[NDArray, NDArray, np.ndarray]: ...

class MinCovDet(EmpiricalCovariance):

    _nonrobust_covariance = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction: float | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> Union[MinCovDet, EllipticEnvelope]: ...
    def correct_covariance(self, data: ArrayLike) -> NDArray: ...
    def reweight_covariance(self, data: ArrayLike) -> tuple[NDArray, NDArray, np.ndarray]: ...
