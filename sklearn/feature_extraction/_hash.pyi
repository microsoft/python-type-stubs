from numpy import ndarray
from numpy.typing import DTypeLike, NDArray
from typing import Iterator, List, Optional, Any, Iterable

# Author: Lars Buitinck
# License: BSD 3 clause

import numbers

import numpy as np
import scipy.sparse as sp

from ..base import BaseEstimator, TransformerMixin
from scipy.sparse._csr import csr_matrix

def _iteritems(d): ...

class FeatureHasher(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_features: int = ...,
        *,
        input_type: str = "dict",
        dtype: DTypeLike = ...,
        alternate_sign: bool = True,
    ) -> None: ...
    @staticmethod
    def _validate_params(n_features: int, input_type: str) -> None: ...
    def fit(self, X: Optional[List[str]] = None, y: None = None) -> "FeatureHasher": ...
    def transform(self, raw_X: Iterable[Iterable]) -> NDArray: ...
    def _more_tags(self): ...
