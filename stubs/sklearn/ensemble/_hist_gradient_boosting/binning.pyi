from typing import Sequence, TypeVar

from numpy import ndarray, uint8
from numpy.random import RandomState

from ..._typing import ArrayLike, Int, MatrixLike
from ...base import BaseEstimator, TransformerMixin
from ...utils import check_array as check_array, check_random_state as check_random_state
from ...utils.fixes import percentile as percentile
from ...utils.validation import check_is_fitted as check_is_fitted
from ._bitset import set_bitset_memoryview as set_bitset_memoryview
from .common import (
    ALMOST_INF as ALMOST_INF,
    X_BINNED_DTYPE as X_BINNED_DTYPE,
    X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE,
    X_DTYPE as X_DTYPE,
)

_BinMapper_Self = TypeVar("_BinMapper_Self", bound=_BinMapper)

# Author: Nicolas Hug

import numpy as np

class _BinMapper(TransformerMixin, BaseEstimator):
    missing_values_bin_idx_: uint8 = ...
    is_categorical_: ndarray = ...
    n_bins_non_missing_: ndarray = ...
    bin_thresholds_: list[ndarray] = ...

    def __init__(
        self,
        n_bins: Int = 256,
        subsample: None | int = ...,
        is_categorical: None | ArrayLike = None,
        known_categories: Sequence[None | ArrayLike] | None | ArrayLike = None,
        random_state: RandomState | None | Int = None,
        n_threads: None | Int = None,
    ) -> None: ...
    def fit(self: _BinMapper_Self, X: MatrixLike, y=None) -> _BinMapper_Self: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
    def make_known_categories_bitsets(self) -> tuple[ndarray, ndarray]: ...
