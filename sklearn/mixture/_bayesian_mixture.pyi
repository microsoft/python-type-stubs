from typing import Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy.random import RandomState
from scipy.special import betaln as betaln, digamma as digamma, gammaln as gammaln
from .._typing import Int, Float, ArrayLike
from ._base import BaseMixture
from ..utils import check_array as check_array
from numbers import Real as Real

# Author: Wei Xue <xuewei4d@gmail.com>
#         Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import math
import numpy as np


class BayesianGaussianMixture(BaseMixture):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        n_components: Int = 1,
        covariance_type: Literal["full", "tied", "diag", "spherical", "full"] = "full",
        tol: Float = 1e-3,
        reg_covar: Float = 1e-6,
        max_iter: Int = 100,
        n_init: Int = 1,
        init_params: Literal[
            "kmeans", "k-means++", "random", "random_from_data", "kmeans"
        ] = "kmeans",
        weight_concentration_prior_type: Literal[
            "dirichlet_process", "dirichlet_distribution", "dirichlet_process"
        ] = "dirichlet_process",
        weight_concentration_prior: None | Float = None,
        mean_precision_prior: None | Float = None,
        mean_prior: None | ArrayLike = None,
        degrees_of_freedom_prior: None | Float = None,
        covariance_prior: float | None | ArrayLike = None,
        random_state: RandomState | None | Int = None,
        warm_start: bool = False,
        verbose: Int = 0,
        verbose_interval: Int = 10,
    ) -> None:
        ...
