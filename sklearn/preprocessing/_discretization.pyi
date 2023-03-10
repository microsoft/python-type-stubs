from typing import Any, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    Options as Options,
)
from numpy.random import RandomState
from .._typing import ArrayLike, Int, Float, MatrixLike
from ..base import BaseEstimator, TransformerMixin
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
)
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from . import OneHotEncoder as OneHotEncoder
from numbers import Integral as Integral
from scipy.sparse import spmatrix
from ..cluster import KMeans as KMeans
from pandas.core.series import Series

# Author: Henry Lin <hlin117@gmail.com>
#         Tom Dupré la Tour

# License: BSD


import numpy as np
import warnings


class KBinsDiscretizer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_bins: Int | ArrayLike = 5,
        *,
        encode: Literal["onehot", "onehot-dense", "ordinal", "onehot"] = "onehot",
        strategy: Literal["uniform", "quantile", "kmeans", "quantile"] = "quantile",
        dtype: None | Float = None,
        subsample: int | None | Literal["warn", "warn"] = "warn",
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Series | None | ndarray = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> csr_matrix | spmatrix | ndarray:
        ...

    def inverse_transform(self, Xt: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
