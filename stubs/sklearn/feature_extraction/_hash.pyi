from itertools import chain as chain
from numbers import Integral as Integral
from typing import Any, ClassVar, Iterator, TypeVar

from numpy import dtype
from scipy.sparse import spmatrix

from .._typing import Int
from ..base import BaseEstimator, TransformerMixin
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ._hashing_fast import transform as _hashing_transform

FeatureHasher_Self = TypeVar("FeatureHasher_Self", bound=FeatureHasher)

# Author: Lars Buitinck
# License: BSD 3 clause

import numpy as np
import scipy.sparse as sp

class FeatureHasher(TransformerMixin, BaseEstimator):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_features: Int = ...,
        *,
        input_type: str = "dict",
        dtype: dtype = ...,
        alternate_sign: bool = True,
    ) -> None: ...
    def fit(self: FeatureHasher_Self, X: Any = None, y: Any = None) -> FeatureHasher_Self: ...
    def transform(self, raw_X: Iterator[Any] | Iterator[Iterator]) -> spmatrix: ...
