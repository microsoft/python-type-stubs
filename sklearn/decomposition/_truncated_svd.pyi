from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import (
    randomized_svd as randomized_svd,
    safe_sparse_dot as safe_sparse_dot,
    svd_flip as svd_flip,
)
from scipy.sparse.linalg import svds as svds
from .._typing import Int, Float, ArrayLike, MatrixLike
from numpy.random import RandomState
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils import check_array as check_array, check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
import numpy as np
import scipy.sparse as sp

__all__ = ["TruncatedSVD"]


class TruncatedSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        algorithm: Literal["arpack", "randomized", "randomized"] = "randomized",
        n_iter: Int = 5,
        n_oversamples: Int = 10,
        power_iteration_normalizer: Literal[
            "auto", "QR", "LU", "none", "auto"
        ] = "auto",
        random_state: RandomState | None | Int = None,
        tol: Float = 0.0,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...
