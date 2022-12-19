from numpy import ndarray
from typing import Optional, Literal, Sequence, Any
from numpy.typing import ArrayLike, NDArray
import collections
import numbers
from itertools import chain, combinations
from itertools import combinations_with_replacement as combinations_w_r

import numpy as np
from scipy import sparse
from scipy.interpolate import BSpline
from scipy.special import comb

from ..base import BaseEstimator, TransformerMixin
from ..utils import check_array
from ..utils.deprecation import deprecated
from ..utils.validation import check_is_fitted, FLOAT_DTYPES, _check_sample_weight
from ..utils.validation import _check_feature_names_in
from ..utils.stats import _weighted_percentile

from ._csr_polynomial_expansion import _csr_polynomial_expansion

__all__ = [
    "PolynomialFeatures",
    "SplineTransformer",
]

class PolynomialFeatures(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        degree: int | tuple[int, int] = 2,
        *,
        interaction_only: bool = False,
        include_bias: bool = True,
        order: Literal["C", "F"] = "C",
    ) -> None: ...
    @staticmethod
    def _combinations(n_features, min_degree, max_degree, interaction_only, include_bias): ...
    @staticmethod
    def _num_combinations(
        n_features: int,
        min_degree: int,
        max_degree: int,
        interaction_only: bool,
        include_bias: bool,
    ) -> int: ...
    @property
    def powers_(self): ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self, input_features: Sequence[str] | None = None) -> list[str]: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def fit(self, X: NDArray | ArrayLike, y: Optional[ndarray] = None) -> "PolynomialFeatures": ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated("The attribute `n_input_features_` was " "deprecated in version 1.0 and will be removed in 1.2.")  # type: ignore
    @property
    def n_input_features_(self): ...

# TODO:
# - sparse support (either scipy or own cython solution)?
class SplineTransformer(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_knots: int = 5,
        degree: int = 3,
        *,
        knots: Literal["uniform", "quantile"] | ArrayLike = "uniform",
        extrapolation: Literal["error", "constant", "linear", "continue", "periodic"] = "constant",
        include_bias: bool = True,
        order: Literal["C", "F"] = "C",
    ) -> None: ...
    @staticmethod
    def _get_base_knot_positions(
        X: ndarray,
        n_knots: int = 10,
        knots: str = "uniform",
        sample_weight: None = None,
    ) -> ndarray: ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self, input_features: Sequence[str] | None = None) -> list[str]: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def fit(
        self,
        X: ArrayLike,
        y: Optional[ndarray] = None,
        sample_weight: ArrayLike | None = None,
    ) -> "SplineTransformer": ...
    def transform(self, X: ArrayLike) -> np.ndarray: ...
