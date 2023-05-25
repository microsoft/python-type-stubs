from typing import Any, ClassVar, Literal, TypeVar
from scipy.special import comb as comb
from scipy import sparse
from itertools import (
    chain as chain,
    combinations as combinations,
    combinations_with_replacement as combinations_w_r,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy import ndarray
from numbers import Integral as Integral
from pandas.core.series import Series
from scipy.interpolate import BSpline as BSpline
from ..base import BaseEstimator, TransformerMixin
from scipy.sparse import spmatrix
from .._typing import ArrayLike, MatrixLike, Int
from ..utils import check_array as check_array
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    FLOAT_DTYPES as FLOAT_DTYPES,
)

SplineTransformer_Self = TypeVar("SplineTransformer_Self", bound="SplineTransformer")
PolynomialFeatures_Self = TypeVar("PolynomialFeatures_Self", bound="PolynomialFeatures")

import collections

import numpy as np


__all__ = [
    "PolynomialFeatures",
    "SplineTransformer",
]


class PolynomialFeatures(TransformerMixin, BaseEstimator):
    n_output_features_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        degree: int | tuple[int, int] = 2,
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

    def fit(
        self: PolynomialFeatures_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> PolynomialFeatures_Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...


# TODO:
# - sparse support (either scipy or own cython solution)?
class SplineTransformer(TransformerMixin, BaseEstimator):
    n_features_out_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    bsplines_: list = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_knots: Int = 5,
        degree: Int = 3,
        *,
        knots: Literal["uniform", "quantile", "uniform"] | MatrixLike = "uniform",
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
        self: SplineTransformer_Self,
        X: MatrixLike,
        y: Series | None | ndarray = None,
        sample_weight: None | ArrayLike = None,
    ) -> SplineTransformer_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
