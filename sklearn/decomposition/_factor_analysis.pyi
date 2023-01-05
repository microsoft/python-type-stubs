from typing import Optional, Literal, Any
from numpy.typing import NDArray, ArrayLike

# Author: Christian Osendorfer <osendorf@gmail.com>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>

# License: BSD3

import warnings
from math import sqrt, log
import numpy as np
from numpy.random import RandomState
from scipy import linalg

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils import check_random_state
from ..utils.extmath import fast_logdet, randomized_svd, squared_norm
from ..utils.validation import check_is_fitted
from ..exceptions import ConvergenceWarning
from numpy import float64, int64, ndarray

class FactorAnalysis(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        tol: float = 1e-2,
        copy: bool = True,
        max_iter: int = 1000,
        noise_variance_init: NDArray | None = None,
        svd_method: Literal["lapack", "randomized"] = "randomized",
        iterated_power: int = 3,
        rotation: Literal["varimax", "quartimax"] | None = None,
        random_state: int | RandomState = 0,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "FactorAnalysis": ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def get_covariance(self) -> NDArray: ...
    def get_precision(self) -> NDArray: ...
    def score_samples(self, X: NDArray) -> NDArray: ...
    def score(self, X: NDArray, y: None = None) -> float: ...
    def _rotate(self, components: ndarray, n_components: None = None, tol: float = 1e-6) -> ndarray: ...
    @property
    def _n_features_out(self): ...

def _ortho_rotation(components: ndarray, method: str = "varimax", tol: float = 1e-6, max_iter: int = 100) -> ndarray: ...
