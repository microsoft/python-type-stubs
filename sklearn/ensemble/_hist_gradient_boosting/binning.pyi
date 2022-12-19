from numpy import uint64, ndarray
from typing import Optional, Tuple, Sequence, Any
from numpy.typing import NDArray, ArrayLike

# Author: Nicolas Hug

import numpy as np
from numpy.random import RandomState

from ...utils import check_random_state, check_array
from ...base import BaseEstimator, TransformerMixin
from ...utils.validation import check_is_fitted

def _find_binning_thresholds(col_data: ndarray, max_bins: int) -> ndarray: ...

class _BinMapper(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_bins: int = 256,
        subsample: int | None = ...,
        is_categorical: NDArray | None = None,
        known_categories: Sequence[NDArray | None] | None = None,
        random_state: int | RandomState | None = None,
        n_threads: int | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "_BinMapper": ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def make_known_categories_bitsets(self) -> tuple[NDArray, NDArray]: ...
