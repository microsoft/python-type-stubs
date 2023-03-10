from typing import Any, Literal
from scipy.special import boxcox as boxcox
from .._typing import ArrayLike, MatrixLike, Int, Float
from scipy.sparse import spmatrix
from ..utils.sparsefuncs import (
    inplace_column_scale as inplace_column_scale,
    mean_variance_axis as mean_variance_axis,
    incr_mean_variance_axis as incr_mean_variance_axis,
    min_max_axis as min_max_axis,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms
from ..utils.sparsefuncs_fast import (
    inplace_csr_row_normalize_l1 as inplace_csr_row_normalize_l1,
    inplace_csr_row_normalize_l2 as inplace_csr_row_normalize_l2,
)
from ._encoders import OneHotEncoder
from ..utils import check_array as check_array
from pandas.core.series import Series
from scipy import sparse as sparse, stats as stats, optimize as optimize
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
    FLOAT_DTYPES as FLOAT_DTYPES,
)
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from numpy.random import RandomState
from ..base import (
    BaseEstimator,
    TransformerMixin,
    OneToOneFeatureMixin,
    ClassNamePrefixFeaturesOutMixin,
)
from numbers import Integral as Integral, Real as Real

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Eric Martin <eric@ericmart.in>
#          Giorgio Patrini <giorgio.patrini@anu.edu.au>
#          Eric Chang <ericchang2017@u.northwestern.edu>
# License: BSD 3 clause


import warnings

import numpy as np


BOUNDS_THRESHOLD: float = ...

__all__ = [
    "Binarizer",
    "KernelCenterer",
    "MinMaxScaler",
    "MaxAbsScaler",
    "Normalizer",
    "OneHotEncoder",
    "RobustScaler",
    "StandardScaler",
    "QuantileTransformer",
    "PowerTransformer",
    "add_dummy_feature",
    "binarize",
    "normalize",
    "scale",
    "robust_scale",
    "maxabs_scale",
    "minmax_scale",
    "quantile_transform",
    "power_transform",
]


def scale(
    X: MatrixLike | ArrayLike,
    *,
    axis: Int = 0,
    with_mean: bool = True,
    with_std: bool = True,
    copy: bool = True,
) -> spmatrix | ndarray:
    ...


class MinMaxScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        feature_range: tuple[int, int] = ...,
        *,
        copy: bool = True,
        clip: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Series | None | ndarray = None) -> Any:
        ...

    def partial_fit(self, X: MatrixLike, y: Series | None | ndarray = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...


def minmax_scale(
    X: MatrixLike,
    feature_range: tuple[int, int] = ...,
    *,
    axis: Int = 0,
    copy: bool = True,
) -> ndarray:
    ...


class StandardScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, copy: bool = True, with_mean: bool = True, with_std: bool = True
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ndarray | list[int] | None | Series = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: Series | list[int] | None | ndarray = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def transform(self, X: MatrixLike, copy: bool | None = None) -> spmatrix | ndarray:
        ...

    def inverse_transform(
        self, X: MatrixLike | ArrayLike, copy: bool | None = None
    ) -> spmatrix:
        ...


class MaxAbsScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(self, *, copy: bool = True) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y=None) -> Any:
        ...

    def partial_fit(self, X: MatrixLike | ArrayLike, y=None) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> spmatrix:
        ...


def maxabs_scale(X: MatrixLike | ArrayLike, *, axis: Int = 0, copy: bool = True):
    ...


class RobustScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        with_centering: bool = True,
        with_scaling: bool = True,
        quantile_range: tuple[float, float] = ...,
        copy: bool = True,
        unit_variance: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> spmatrix:
        ...


def robust_scale(
    X: MatrixLike,
    *,
    axis: Int = 0,
    with_centering: bool = True,
    with_scaling: bool = True,
    quantile_range: tuple[float, float] = ...,
    copy: bool = True,
    unit_variance: bool = False,
) -> spmatrix:
    ...


def normalize(
    X: MatrixLike | ArrayLike,
    norm: Literal["l1", "l2", "max", "l2"] = "l2",
    *,
    axis: int = 1,
    copy: bool = True,
    return_norm: bool = False,
) -> csr_matrix | tuple[spmatrix, ndarray] | ndarray:
    ...


class Normalizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, norm: Literal["l1", "l2", "max", "l2"] = "l2", *, copy: bool = True
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def transform(
        self, X: MatrixLike | ArrayLike, copy: bool | None = None
    ) -> spmatrix | ndarray:
        ...


def binarize(
    X: MatrixLike | ArrayLike, *, threshold: Float = 0.0, copy: bool = True
) -> spmatrix | csr_matrix:
    ...


class Binarizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(self, *, threshold: Float = 0.0, copy: bool = True) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y=None) -> Any:
        ...

    def transform(
        self, X: MatrixLike | ArrayLike, copy: bool | None = None
    ) -> spmatrix:
        ...


class KernelCenterer(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(self) -> None:
        ...

    def fit(self, K: MatrixLike, y=None) -> Any:
        ...

    def transform(self, K: MatrixLike, copy: bool = True) -> ndarray:
        ...


def add_dummy_feature(X: MatrixLike | ArrayLike, value: Float = 1.0) -> spmatrix:
    ...


class QuantileTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        n_quantiles: Int = 1000,
        output_distribution: Literal["uniform", "normal", "uniform"] = "uniform",
        ignore_implicit_zeros: bool = False,
        subsample: Int = 10_000,
        random_state: RandomState | None | Int = None,
        copy: bool = True,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: None | Series = None) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...


def quantile_transform(
    X: MatrixLike | ArrayLike,
    *,
    axis: Int = 0,
    n_quantiles: Int = 1000,
    output_distribution: Literal["uniform", "normal", "uniform"] = "uniform",
    ignore_implicit_zeros: bool = False,
    subsample: Int = ...,
    random_state: RandomState | None | Int = None,
    copy: bool = True,
) -> spmatrix | ndarray:
    ...


class PowerTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        method: Literal["yeo-johnson", "yeo-johnson", "box-cox"] = "yeo-johnson",
        *,
        standardize: bool = True,
        copy: bool = True,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y=None) -> Any:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...


def power_transform(
    X: MatrixLike,
    method: Literal["yeo-johnson", "box-cox", "yeo-johnson"] = "yeo-johnson",
    *,
    standardize: bool = True,
    copy: bool = True,
) -> ndarray:
    ...
