from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray, ufunc
from pandas.core.frame import DataFrame

from .._typing import ArrayLike, MatrixLike
from ..base import BaseEstimator, TransformerMixin
from ..utils._param_validation import StrOptions as StrOptions
from ..utils.metaestimators import available_if as available_if
from ..utils.validation import check_array as check_array

FunctionTransformer_Self = TypeVar("FunctionTransformer_Self", bound="FunctionTransformer")

import warnings

import numpy as np

class FunctionTransformer(TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        func: ufunc | None | Callable = None,
        inverse_func: None | ufunc | Callable = None,
        *,
        validate: bool = False,
        accept_sparse: bool = False,
        check_inverse: bool = True,
        feature_names_out: None | str | Callable = None,
        kw_args: None | dict = None,
        inv_kw_args: None | dict = None,
    ) -> None: ...
    def fit(self: FunctionTransformer_Self, X: list[str] | MatrixLike, y: Any = None) -> FunctionTransformer_Self: ...
    def transform(self, X: list[str] | MatrixLike) -> ndarray | DataFrame | list[dict[str, int]]: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
    def __sklearn_is_fitted__(self): ...
    def set_output(self, *, transform: None | Literal["default", "pandas"] = None) -> BaseEstimator: ...
