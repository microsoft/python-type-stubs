from typing import Literal
from ..utils._param_validation import StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms
from numpy.random import RandomState
from .._typing import Int, Float, ArrayLike, MatrixLike
from scipy import linalg as linalg
from ._base import BaseMixture
from ..utils import check_array as check_array

# Author: Wei Xue <xuewei4d@gmail.com>
# Modified by Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import numpy as np


class GaussianMixture(BaseMixture):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Int = 1,
        *,
        covariance_type: Literal["full", "tied", "diag", "spherical", "full"] = "full",
        tol: Float = 1e-3,
        reg_covar: Float = 1e-6,
        max_iter: Int = 100,
        n_init: Int = 1,
        init_params: Literal[
            "kmeans", "k-means++", "random", "random_from_data", "kmeans"
        ] = "kmeans",
        weights_init: None | ArrayLike = None,
        means_init: None | ArrayLike = None,
        precisions_init: None | ArrayLike = None,
        random_state: RandomState | None | Int = None,
        warm_start: bool = False,
        verbose: Int = 0,
        verbose_interval: Int = 10,
    ) -> None:
        ...

    def bic(self, X: MatrixLike) -> Float:
        ...

    def aic(self, X: MatrixLike) -> float:
        ...
