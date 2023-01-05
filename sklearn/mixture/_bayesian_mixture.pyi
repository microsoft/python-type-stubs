from typing import Tuple, Union, Literal
from numpy.typing import ArrayLike

# Author: Wei Xue <xuewei4d@gmail.com>
#         Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import math
import numpy as np
from scipy.special import betaln, digamma, gammaln

from ._base import BaseMixture, _check_shape
from ._gaussian_mixture import _check_precision_matrix
from ._gaussian_mixture import _check_precision_positivity
from ._gaussian_mixture import _compute_log_det_cholesky
from ._gaussian_mixture import _compute_precision_cholesky
from ._gaussian_mixture import _estimate_gaussian_parameters
from ._gaussian_mixture import _estimate_log_gaussian_prob
from ..utils import check_array
from numpy import float64, ndarray
from numpy.random import RandomState

def _log_dirichlet_norm(dirichlet_concentration: ndarray) -> float64: ...
def _log_wishart_norm(degrees_of_freedom: ndarray, log_det_precisions_chol: ndarray, n_features: int) -> ndarray: ...

class BayesianGaussianMixture(BaseMixture):
    def __init__(
        self,
        *,
        n_components: int = 1,
        covariance_type: Literal["full", "tied", "diag", "spherical"] = "full",
        tol: float = 1e-3,
        reg_covar: float = 1e-6,
        max_iter: int = 100,
        n_init: int = 1,
        init_params: Literal["kmeans", "k-means++", "random", "random_from_data"] = "kmeans",
        weight_concentration_prior_type: str = "dirichlet_process",
        weight_concentration_prior: float | None = None,
        mean_precision_prior: float | None = None,
        mean_prior: ArrayLike | None = None,
        degrees_of_freedom_prior: float | None = None,
        covariance_prior: float | ArrayLike | None = None,
        random_state: int | RandomState | None = None,
        warm_start: bool = False,
        verbose: int = 0,
        verbose_interval: int = 10,
    ) -> None: ...
    def _check_parameters(self, X: ndarray) -> None: ...
    def _check_weights_parameters(self) -> None: ...
    def _check_means_parameters(self, X: ndarray) -> None: ...
    def _check_precision_parameters(self, X: ndarray) -> None: ...
    def _checkcovariance_prior_parameter(self, X: ndarray) -> None: ...
    def _initialize(self, X: ndarray, resp: ndarray) -> None: ...
    def _estimate_weights(self, nk: ndarray) -> None: ...
    def _estimate_means(self, nk: ndarray, xk: ndarray) -> None: ...
    def _estimate_precisions(self, nk: ndarray, xk: ndarray, sk: ndarray) -> None: ...
    def _estimate_wishart_full(self, nk: ndarray, xk: ndarray, sk: ndarray) -> None: ...
    def _estimate_wishart_tied(self, nk, xk, sk): ...
    def _estimate_wishart_diag(self, nk, xk, sk): ...
    def _estimate_wishart_spherical(self, nk, xk, sk): ...
    def _m_step(self, X: ndarray, log_resp: ndarray) -> None: ...
    def _estimate_log_weights(self) -> ndarray: ...
    def _estimate_log_prob(self, X: ndarray) -> ndarray: ...
    def _compute_lower_bound(self, log_resp: ndarray, log_prob_norm: float64) -> float64: ...
    def _get_parameters(
        self,
    ) -> Union[
        Tuple[ndarray, ndarray, ndarray, ndarray, ndarray, ndarray],
        Tuple[Tuple[ndarray, ndarray], ndarray, ndarray, ndarray, ndarray, ndarray],
    ]: ...
    def _set_parameters(
        self,
        params: Union[
            Tuple[ndarray, ndarray, ndarray, ndarray, ndarray, ndarray],
            Tuple[Tuple[ndarray, ndarray], ndarray, ndarray, ndarray, ndarray, ndarray],
        ],
    ) -> None: ...
