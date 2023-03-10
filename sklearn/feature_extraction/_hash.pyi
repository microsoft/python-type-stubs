from typing import Any, Iterator
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ._hashing_fast import transform as _hashing_transform
from .._typing import Int
from ..base import BaseEstimator, TransformerMixin
from scipy.sparse._csr import csr_matrix
from numpy import dtype
from itertools import chain as chain
from numbers import Integral as Integral
from scipy.sparse import spmatrix

# Author: Lars Buitinck
# License: BSD 3 clause


import numpy as np
import scipy.sparse as sp


class FeatureHasher(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_features: Int = ...,
        *,
        input_type: str = "dict",
        dtype: dtype = ...,
        alternate_sign: bool = True,
    ) -> None:
        ...

    def fit(self, X: Any = None, y: Any = None) -> Any:
        ...

    def transform(
        self, raw_X: Iterator[Any] | Iterator[Iterator]
    ) -> spmatrix | csr_matrix:
        ...
