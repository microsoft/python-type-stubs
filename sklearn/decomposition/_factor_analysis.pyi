from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import (
    fast_logdet as fast_logdet,
    randomized_svd as randomized_svd,
    squared_norm as squared_norm,
)
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Int, Float, ArrayLike, MatrixLike
from math import sqrt as sqrt, log as log
from scipy import linalg as linalg
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real

# Author: Christian Osendorfer <osendorf@gmail.com>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>

# License: BSD3

import warnings
import numpy as np


class FactorAnalysis(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        tol: Float = 1e-2,
        copy: bool = True,
        max_iter: Int = 1000,
        noise_variance_init: None | ArrayLike = None,
        svd_method: Literal["lapack", "randomized", "randomized"] = "randomized",
        iterated_power: Int = 3,
        rotation: None | Literal["varimax", "quartimax"] = None,
        random_state: int | RandomState | None = 0,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_covariance(self) -> ndarray:
        ...

    def get_precision(self) -> ndarray:
        ...

    def score_samples(self, X: ArrayLike) -> ndarray:
        ...

    def score(self, X: ArrayLike, y: Any = None) -> float:
        ...
