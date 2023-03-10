from typing import Any, Callable, Literal
from ..utils._param_validation import StrOptions as StrOptions
from .._typing import MatrixLike, ArrayLike, Estimator
from ..base import BaseEstimator, TransformerMixin
from ..utils.validation import check_array as check_array
from pandas.core.frame import DataFrame
from numpy import ufunc, ndarray
from ..utils.metaestimators import available_if as available_if
import warnings

import numpy as np


class FunctionTransformer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        func: ufunc | None | Callable = None,
        inverse_func: ufunc | None | Callable = None,
        *,
        validate: bool = False,
        accept_sparse: bool = False,
        check_inverse: bool = True,
        feature_names_out: str | None | Callable = None,
        kw_args: dict | None = None,
        inv_kw_args: dict | None = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | list[str], y: Any = None) -> Any:
        ...

    def transform(
        self, X: MatrixLike | list[str]
    ) -> list[dict[str, int]] | DataFrame | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def __sklearn_is_fitted__(self):
        ...

    def set_output(
        self, *, transform: Literal["default", "pandas"] | None = None
    ) -> Estimator | FunctionTransformer:
        ...
