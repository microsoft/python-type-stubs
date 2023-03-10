from typing import Any, Literal, Self, Sequence
from ..utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    Hidden as Hidden,
)
from .._typing import ArrayLike, Int, MatrixLike
from scipy import sparse
from ..base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from ..utils import check_array as check_array, is_scalar_nan as is_scalar_nan
from numbers import Integral as Integral, Real as Real
from scipy.sparse import spmatrix
from pandas.core.series import Series

# Authors: Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joris Van den Bossche <jorisvandenbossche@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np


__all__ = ["OneHotEncoder", "OrdinalEncoder"]


class _BaseEncoder(TransformerMixin, BaseEstimator):
    pass


class OneHotEncoder(_BaseEncoder):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto", "auto"] = "auto",
        drop: Literal["first", "if_binary"] | None | ArrayLike = None,
        sparse: bool | str = "deprecated",
        sparse_output: bool = True,
        dtype=...,
        handle_unknown: Literal[
            "error", "ignore", "infrequent_if_exist", "error"
        ] = "error",
        min_frequency: int | float | None = None,
        max_categories: None | Int = None,
    ) -> None:
        ...

    @property
    def infrequent_categories_(self) -> list[ndarray]:
        ...

    def fit(
        self, X: MatrixLike, y: Series | list[int] | None | ndarray = None
    ) -> OneHotEncoder | Self:
        ...

    def transform(self, X: MatrixLike) -> csr_matrix | spmatrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class OrdinalEncoder(OneToOneFeatureMixin, _BaseEncoder):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto", "auto"] = "auto",
        dtype=...,
        handle_unknown: Literal["error", "use_encoded_value", "error"] = "error",
        unknown_value: int | float | None = None,
        encoded_missing_value: int | float = ...,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | Series = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...
