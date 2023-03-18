from typing import ClassVar, Literal, Sequence, TypeVar
from scipy import sparse
from numpy import ndarray
from ..utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    Hidden as Hidden,
)
from numbers import Integral as Integral, Real as Real
from pandas.core.series import Series
from ..base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from scipy.sparse import spmatrix
from .._typing import ArrayLike, Int, MatrixLike
from ..utils import check_array as check_array, is_scalar_nan as is_scalar_nan
from ..utils.validation import check_is_fitted as check_is_fitted

OrdinalEncoder_Self = TypeVar("OrdinalEncoder_Self", bound="OrdinalEncoder")
OneHotEncoder_Self = TypeVar("OneHotEncoder_Self", bound="OneHotEncoder")

# Authors: Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joris Van den Bossche <jorisvandenbossche@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np


__all__ = ["OneHotEncoder", "OrdinalEncoder"]


class _BaseEncoder(TransformerMixin, BaseEstimator):
    ...


class OneHotEncoder(_BaseEncoder):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    drop_idx_: ndarray = ...
    categories_: list[ArrayLike] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto", "auto"] = "auto",
        drop: None | ArrayLike | Literal["first", "if_binary"] = None,
        sparse: str | bool = "deprecated",
        sparse_output: bool = True,
        dtype=...,
        handle_unknown: Literal[
            "error", "ignore", "infrequent_if_exist", "error"
        ] = "error",
        min_frequency: float | None | int = None,
        max_categories: None | Int = None,
    ) -> None:
        ...

    @property
    def infrequent_categories_(self) -> list[ndarray]:
        ...

    def fit(
        self: OneHotEncoder_Self,
        X: MatrixLike,
        y: Series | None | ndarray | list[int] = None,
    ) -> OneHotEncoder_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class OrdinalEncoder(OneToOneFeatureMixin, _BaseEncoder):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    categories_: list[ArrayLike] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto", "auto"] = "auto",
        dtype=...,
        handle_unknown: Literal["error", "use_encoded_value", "error"] = "error",
        unknown_value: float | None | int = None,
        encoded_missing_value: float | int = ...,
    ) -> None:
        ...

    def fit(
        self: OrdinalEncoder_Self, X: MatrixLike, y: Series | None = None
    ) -> OrdinalEncoder_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...
