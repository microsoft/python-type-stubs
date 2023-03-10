from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.special import comb as comb
from .._typing import ArrayLike, MatrixLike, Int
from scipy import sparse
from ..base import BaseEstimator, TransformerMixin
from scipy.interpolate import BSpline as BSpline
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    FLOAT_DTYPES as FLOAT_DTYPES,
)
from numpy import ndarray
from itertools import (
    chain as chain,
    combinations as combinations,
    combinations_with_replacement as combinations_w_r,
)
from ..utils import check_array as check_array
from numbers import Integral as Integral
from scipy.sparse import spmatrix
from pandas.core.series import Series
import collections

import numpy as np


__all__ = [
    "PolynomialFeatures",
    "SplineTransformer",
]


class PolynomialFeatures(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        degree: tuple[int, int] | int = 2,
        *,
        interaction_only: bool = False,
        include_bias: bool = True,
        order: Literal["C", "F", "C"] = "C",
    ) -> None:
        ...

    @property
    def powers_(self) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...


# TODO:
# - sparse support (either scipy or own cython solution)?
class SplineTransformer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_knots: Int = 5,
        degree: Int = 3,
        *,
        knots: MatrixLike | Literal["uniform", "quantile", "uniform"] = "uniform",
        extrapolation: Literal[
            "error", "constant", "linear", "continue", "periodic", "constant"
        ] = "constant",
        include_bias: bool = True,
        order: Literal["C", "F", "C"] = "C",
    ) -> None:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: Series | None | ndarray = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
