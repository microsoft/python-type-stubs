from collections import Counter as Counter
from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from scipy import sparse as sp
from scipy.sparse import spmatrix

from .._typing import ArrayLike, Int, MatrixLike
from ..base import BaseEstimator, TransformerMixin
from ..utils import is_scalar_nan as is_scalar_nan
from ..utils._param_validation import Hidden as Hidden, StrOptions as StrOptions
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted

SimpleImputer_Self = TypeVar("SimpleImputer_Self", bound=SimpleImputer)
MissingIndicator_Self = TypeVar("MissingIndicator_Self", bound=MissingIndicator)

# Authors: Nicolas Tresegnie <nicolas.tresegnie@gmail.com>
#          Sergey Feldman <sergeyfeldman@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np
import numpy.ma as ma

class _BaseImputer(TransformerMixin, BaseEstimator):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        missing_values=...,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...

class SimpleImputer(_BaseImputer):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    indicator_: MissingIndicator = ...
    statistics_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        missing_values: float | None | str = ...,
        strategy: str = "mean",
        fill_value: float | None | str = None,
        verbose: str | Int = "deprecated",
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    def fit(self: SimpleImputer_Self, X: MatrixLike, y: Any = None) -> SimpleImputer_Self: ...
    def transform(self, X: MatrixLike) -> ndarray | spmatrix: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...

class MissingIndicator(TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    features_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        missing_values: float | None | str = ...,
        features: Literal["missing-only", "all"] = "missing-only",
        sparse: Literal["auto"] | bool = "auto",
        error_on_new: bool = True,
    ) -> None: ...
    def fit(self: MissingIndicator_Self, X: MatrixLike | ArrayLike, y: Any = None) -> MissingIndicator_Self: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix: ...
    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray | spmatrix: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
