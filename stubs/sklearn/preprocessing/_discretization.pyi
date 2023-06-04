from typing import ClassVar, Literal, TypeVar
from numpy.random import RandomState
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    Options as Options,
)
from numbers import Integral as Integral
from pandas.core.series import Series
from ..base import BaseEstimator, TransformerMixin
from scipy.sparse import spmatrix
from ..cluster import KMeans as KMeans
from .._typing import ArrayLike, Int, Float, MatrixLike
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
)
from . import OneHotEncoder as OneHotEncoder

KBinsDiscretizer_Self = TypeVar("KBinsDiscretizer_Self", bound="KBinsDiscretizer")

# Author: Henry Lin <hlin117@gmail.com>
#         Tom Dupré la Tour

# License: BSD


import numpy as np
import warnings


class KBinsDiscretizer(TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_bins_: ndarray = ...
    bin_edges_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_bins: ArrayLike | Int = 5,
        *,
        encode: Literal["onehot", "onehot-dense", "ordinal", "onehot"] = "onehot",
        strategy: Literal["uniform", "quantile", "kmeans", "quantile"] = "quantile",
        dtype: None | Float = None,
        subsample: int | None | Literal["warn", "warn"] = "warn",
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self: KBinsDiscretizer_Self, X: MatrixLike, y: Series | None | ndarray = None
    ) -> KBinsDiscretizer_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, Xt: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
