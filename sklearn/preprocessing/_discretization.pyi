from numpy import int64, ndarray, float64, float32
from typing import Optional, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Author: Henry Lin <hlin117@gmail.com>
#         Tom Dupré la Tour

# License: BSD

import numbers
import numpy as np
import warnings

from . import OneHotEncoder

from ..base import BaseEstimator, TransformerMixin
from ..utils.validation import check_array
from ..utils.validation import check_is_fitted
from ..utils.validation import check_random_state
from ..utils.validation import _check_feature_names_in
from ..utils.validation import check_scalar
from ..utils import _safe_indexing
from scipy.sparse._csr import csr_matrix

class KBinsDiscretizer(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_bins: int | ArrayLike = 5,
        *,
        encode: Literal["onehot", "onehot-dense", "ordinal"] = "onehot",
        strategy: Literal["uniform", "quantile", "kmeans"] = "quantile",
        dtype: float64 | float32 | None = None,
        subsample: int | Literal["warn"] | None = "warn",
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "KBinsDiscretizer": ...
    def _validate_n_bins(self, n_features: int) -> ndarray: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def inverse_transform(self, Xt: ArrayLike) -> NDArray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
