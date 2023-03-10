from typing import Any, Literal
from ..utils._param_validation import StrOptions as StrOptions, Hidden as Hidden
from .._typing import Int, MatrixLike, ArrayLike
from scipy import sparse as sp
from ..base import BaseEstimator, TransformerMixin
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    FLOAT_DTYPES as FLOAT_DTYPES,
)
from collections import Counter as Counter
from numpy import ndarray
from ..utils import is_scalar_nan as is_scalar_nan
from scipy.sparse import spmatrix

# Authors: Nicolas Tresegnie <nicolas.tresegnie@gmail.com>
#          Sergey Feldman <sergeyfeldman@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np
import numpy.ma as ma


class _BaseImputer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        missing_values=...,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None:
        ...


class SimpleImputer(_BaseImputer):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        missing_values: int | float | None | str = ...,
        strategy: str = "mean",
        fill_value: int | str | None | float = None,
        verbose: str | Int = "deprecated",
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> spmatrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class MissingIndicator(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        missing_values: int | float | None | str = ...,
        features: Literal["missing-only", "all", "missing-only"] = "missing-only",
        sparse: bool | Literal["auto", "auto"] = "auto",
        error_on_new: bool = True,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...

    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> spmatrix:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
