from typing import Any, Callable, ClassVar
from typing_extensions import Self

from numpy import ndarray
from numpy.random import RandomState

from .._typing import Float, Int, MatrixLike
from . import EmpiricalCovariance

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

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
) -> tuple[ndarray, ndarray, ndarray]: ...
def select_candidates(
    X: MatrixLike,
    n_support: Int,
    n_trials: int | tuple[ndarray, ndarray] | tuple[Any, Any],
    select: Int = 1,
    n_iter: Int = 30,
    verbose: bool = False,
    cov_computation_method: Callable = ...,
    random_state: None | Int | RandomState = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray] | tuple[ndarray, ndarray, ndarray]: ...
def fast_mcd(
    X: MatrixLike,
    support_fraction: None | Float = None,
    cov_computation_method: Callable = ...,
    random_state: None | Int | RandomState = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray] | tuple[ndarray, ndarray, ndarray]: ...

class MinCovDet(EmpiricalCovariance):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dist_: ndarray = ...
    support_: ndarray = ...
    precision_: ndarray = ...
    covariance_: ndarray = ...
    location_: ndarray = ...
    raw_support_: ndarray = ...
    raw_covariance_: ndarray = ...
    raw_location_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...
    _nonrobust_covariance = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def correct_covariance(self, data: MatrixLike) -> ndarray: ...
    def reweight_covariance(self, data: MatrixLike) -> tuple[ndarray, ndarray, ndarray]: ...
