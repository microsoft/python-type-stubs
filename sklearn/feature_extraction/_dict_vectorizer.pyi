from typing import Any, Iterable, Iterator, Mapping
from collections.abc import Iterable
from .._typing import ArrayLike, MatrixLike
from ..base import BaseEstimator, TransformerMixin
from operator import itemgetter as itemgetter
from scipy.sparse._csr import csr_matrix
from array import array as array
from numpy import ndarray
from ..utils import check_array as check_array
from numbers import Number as Number
from scipy.sparse import spmatrix

# Authors: Lars Buitinck
#          Dan Blanchard <dblanchard@ets.org>
# License: BSD 3 clause


import numpy as np
import scipy.sparse as sp


class DictVectorizer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, dtype=..., separator: str = "=", sparse: bool = True, sort: bool = True
    ) -> None:
        ...

    def fit(self, X: Mapping | Iterable[Mapping], y: Any = None) -> Any:
        ...

    def fit_transform(
        self,
        X: list[dict[str, int]] | Iterator[Any] | Mapping | Iterable[Mapping],
        y: Any = None,
    ) -> spmatrix | ndarray | csr_matrix:
        ...

    def inverse_transform(
        self, X: MatrixLike | ArrayLike, dict_type=...
    ) -> list[Mapping]:
        ...

    def transform(
        self, X: Mapping[str, ArrayLike] | Iterator[Mapping[str, ArrayLike]] | ArrayLike
    ) -> spmatrix | ndarray | csr_matrix:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def restrict(self, support: ArrayLike, indices: bool = False) -> Any:
        ...
