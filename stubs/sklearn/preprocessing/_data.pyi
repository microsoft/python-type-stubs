from typing import Any, ClassVar, Literal, TypeVar
from ..utils.sparsefuncs import (
    inplace_column_scale as inplace_column_scale,
    mean_variance_axis as mean_variance_axis,
    incr_mean_variance_axis as incr_mean_variance_axis,
    min_max_axis as min_max_axis,
)
from numpy.random import RandomState
from scipy.special import boxcox as boxcox
from scipy import sparse as sparse, stats as stats, optimize as optimize
from ..utils.sparsefuncs_fast import (
    inplace_csr_row_normalize_l1 as inplace_csr_row_normalize_l1,
    inplace_csr_row_normalize_l2 as inplace_csr_row_normalize_l2,
)
from ._encoders import OneHotEncoder
from numpy import ndarray
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms
from numbers import Integral as Integral, Real as Real
from pandas.core.series import Series
from ..base import (
    BaseEstimator,
    TransformerMixin,
    OneToOneFeatureMixin,
    ClassNamePrefixFeaturesOutMixin,
)
from scipy.sparse import spmatrix
from scipy.sparse._csr import csr_matrix
from .._typing import MatrixLike, ArrayLike, Int, Float
from ..utils import check_array as check_array
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
    FLOAT_DTYPES as FLOAT_DTYPES,
)

RobustScaler_Self = TypeVar("RobustScaler_Self", bound="RobustScaler")
KernelCenterer_Self = TypeVar("KernelCenterer_Self", bound="KernelCenterer")
Binarizer_Self = TypeVar("Binarizer_Self", bound="Binarizer")
QuantileTransformer_Self = TypeVar(
    "QuantileTransformer_Self", bound="QuantileTransformer"
)
MaxAbsScaler_Self = TypeVar("MaxAbsScaler_Self", bound="MaxAbsScaler")
StandardScaler_Self = TypeVar("StandardScaler_Self", bound="StandardScaler")
MinMaxScaler_Self = TypeVar("MinMaxScaler_Self", bound="MinMaxScaler")
Normalizer_Self = TypeVar("Normalizer_Self", bound="Normalizer")
PowerTransformer_Self = TypeVar("PowerTransformer_Self", bound="PowerTransformer")

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
) -> ndarray | spmatrix:
    ...


class MinMaxScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_samples_seen_: int = ...
    n_features_in_: int = ...
    data_range_: ndarray = ...
    data_max_: ndarray = ...
    data_min_: ndarray = ...
    scale_: ndarray = ...
    min_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        feature_range: tuple[int, int] = ...,
        *,
        copy: bool = True,
        clip: bool = False,
    ) -> None:
        ...

    def fit(
        self: MinMaxScaler_Self, X: MatrixLike, y: Series | None | ndarray = None
    ) -> MinMaxScaler_Self:
        ...

    def partial_fit(
        self: MinMaxScaler_Self, X: MatrixLike, y: Series | None | ndarray = None
    ) -> MinMaxScaler_Self:
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
    n_samples_seen_: ndarray | int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    var_: None | ndarray = ...
    mean_: None | ndarray = ...
    scale_: None | ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, *, copy: bool = True, with_mean: bool = True, with_std: bool = True
    ) -> None:
        ...

    def fit(
        self: StandardScaler_Self,
        X: MatrixLike | ArrayLike,
        y: Series | None | ndarray | list[int] = None,
        sample_weight: None | ArrayLike = None,
    ) -> StandardScaler_Self:
        ...

    def partial_fit(
        self: StandardScaler_Self,
        X: MatrixLike | ArrayLike,
        y: Series | None | ndarray | list[int] = None,
        sample_weight: None | ArrayLike = None,
    ) -> StandardScaler_Self:
        ...

    def transform(self, X: MatrixLike, copy: None | bool = None) -> ndarray | spmatrix:
        ...

    def inverse_transform(
        self, X: MatrixLike | ArrayLike, copy: None | bool = None
    ) -> ndarray | spmatrix:
        ...


class MaxAbsScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    n_samples_seen_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    max_abs_: ndarray = ...
    scale_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, copy: bool = True) -> None:
        ...

    def fit(
        self: MaxAbsScaler_Self, X: MatrixLike | ArrayLike, y=None
    ) -> MaxAbsScaler_Self:
        ...

    def partial_fit(
        self: MaxAbsScaler_Self, X: MatrixLike | ArrayLike, y=None
    ) -> MaxAbsScaler_Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...


def maxabs_scale(X: MatrixLike | ArrayLike, *, axis: Int = 0, copy: bool = True):
    ...


class RobustScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    scale_: ndarray = ...
    center_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: RobustScaler_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> RobustScaler_Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
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
) -> ndarray | spmatrix:
    ...


def normalize(
    X: MatrixLike | ArrayLike,
    norm: Literal["l1", "l2", "max", "l2"] = "l2",
    *,
    axis: int = 1,
    copy: bool = True,
    return_norm: bool = False,
) -> csr_matrix | tuple[ndarray | spmatrix, ndarray] | ndarray:
    ...


class Normalizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, norm: Literal["l1", "l2", "max", "l2"] = "l2", *, copy: bool = True
    ) -> None:
        ...

    def fit(
        self: Normalizer_Self, X: MatrixLike | ArrayLike, y: Any = None
    ) -> Normalizer_Self:
        ...

    def transform(
        self, X: MatrixLike | ArrayLike, copy: None | bool = None
    ) -> ndarray | spmatrix:
        ...


def binarize(
    X: MatrixLike | ArrayLike, *, threshold: Float = 0.0, copy: bool = True
) -> ndarray | spmatrix:
    ...


class Binarizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, threshold: Float = 0.0, copy: bool = True) -> None:
        ...

    def fit(self: Binarizer_Self, X: MatrixLike | ArrayLike, y=None) -> Binarizer_Self:
        ...

    def transform(
        self, X: MatrixLike | ArrayLike, copy: None | bool = None
    ) -> ndarray | spmatrix:
        ...


class KernelCenterer(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    K_fit_all_: float = ...
    K_fit_rows_: ndarray = ...

    def __init__(self) -> None:
        ...

    def fit(self: KernelCenterer_Self, K: MatrixLike, y=None) -> KernelCenterer_Self:
        ...

    def transform(self, K: MatrixLike, copy: bool = True) -> ndarray:
        ...


def add_dummy_feature(
    X: MatrixLike | ArrayLike, value: Float = 1.0
) -> ndarray | spmatrix:
    ...


class QuantileTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    references_: ndarray = ...
    quantiles_: ndarray = ...
    n_quantiles_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: QuantileTransformer_Self,
        X: MatrixLike | ArrayLike,
        y: Series | None = None,
    ) -> QuantileTransformer_Self:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
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
) -> ndarray | spmatrix:
    ...


class PowerTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    lambdas_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        method: Literal["yeo-johnson", "box-cox", "yeo-johnson"] = "yeo-johnson",
        *,
        standardize: bool = True,
        copy: bool = True,
    ) -> None:
        ...

    def fit(
        self: PowerTransformer_Self, X: MatrixLike, y=None
    ) -> PowerTransformer_Self:
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
