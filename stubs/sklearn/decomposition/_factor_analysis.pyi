from math import log as log, sqrt as sqrt
from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import fast_logdet as fast_logdet, randomized_svd as randomized_svd, squared_norm as squared_norm
from ..utils.validation import check_is_fitted as check_is_fitted

FactorAnalysis_Self = TypeVar("FactorAnalysis_Self", bound="FactorAnalysis")

# Author: Christian Osendorfer <osendorf@gmail.com>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>

# License: BSD3

import warnings

import numpy as np

class FactorAnalysis(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    mean_: ndarray = ...
    n_iter_: int = ...
    noise_variance_: ndarray = ...
    loglike_: list = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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
        random_state: None | RandomState | int = 0,
    ) -> None: ...
    def fit(self: FactorAnalysis_Self, X: MatrixLike, y: Any = None) -> FactorAnalysis_Self: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
    def get_covariance(self) -> ndarray: ...
    def get_precision(self) -> ndarray: ...
    def score_samples(self, X: ArrayLike) -> ndarray: ...
    def score(self, X: ArrayLike, y: Any = None) -> float: ...
