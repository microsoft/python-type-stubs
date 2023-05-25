from typing import Any, ClassVar, Literal, TypeVar
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from numpy.random import RandomState
from scipy.sparse.linalg import svds as svds
from numpy import ndarray
from ..utils.extmath import (
    randomized_svd as randomized_svd,
    safe_sparse_dot as safe_sparse_dot,
    svd_flip as svd_flip,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from .._typing import Int, Float, MatrixLike, ArrayLike
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils.validation import check_is_fitted as check_is_fitted

TruncatedSVD_Self = TypeVar("TruncatedSVD_Self", bound="TruncatedSVD")

import numpy as np
import scipy.sparse as sp

__all__ = ["TruncatedSVD"]


class TruncatedSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    singular_values_: ndarray = ...
    explained_variance_ratio_: ndarray = ...
    explained_variance_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: TruncatedSVD_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> TruncatedSVD_Self:
        ...

    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...
