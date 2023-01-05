from numpy import float64, int64, ndarray
from typing import Dict, List, Optional, Tuple, Type, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray

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
from scipy import sparse
from scipy import stats
from scipy import optimize
from scipy.special import boxcox

from ..base import (
    BaseEstimator,
    TransformerMixin,
    _OneToOneFeatureMixin,
    _ClassNamePrefixFeaturesOutMixin,
)
from ..utils import check_array
from ..utils.extmath import _incremental_mean_and_var, row_norms

from ..utils.sparsefuncs import (
    inplace_column_scale,
    mean_variance_axis,
    incr_mean_variance_axis,
    min_max_axis,
)
from ..utils.validation import (
    check_is_fitted,
    check_random_state,
    _check_sample_weight,
    FLOAT_DTYPES,
)

from ._encoders import OneHotEncoder
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix
from numpy.random import RandomState

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

def _is_constant_feature(var: ndarray, mean: ndarray, n_samples: Union[int64, int]) -> ndarray: ...
def _handle_zeros_in_scale(
    scale: Union[ndarray, float64],
    copy: bool = True,
    constant_mask: Optional[ndarray] = None,
) -> Union[ndarray, float64]: ...
def scale(
    X: NDArray | ArrayLike,
    *,
    axis: int = 0,
    with_mean: bool = True,
    with_std: bool = True,
    copy: bool = True,
) -> NDArray: ...

class MinMaxScaler(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        feature_range: tuple[float, float] = ...,
        *,
        copy: bool = True,
        clip: bool = False,
    ) -> None: ...
    def _reset(self) -> None: ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "MinMaxScaler": ...
    def partial_fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "MinMaxScaler": ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

def minmax_scale(
    X: ArrayLike,
    feature_range: tuple[float, float] = ...,
    *,
    axis: int = 0,
    copy: bool = True,
) -> ndarray: ...

class StandardScaler(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(self, *, copy: bool = True, with_mean: bool = True, with_std: bool = True) -> None: ...
    def _reset(self) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: Optional[Union[ndarray, List[int], Series]] = None,
        sample_weight: ArrayLike | None = None,
    ) -> "StandardScaler": ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: Optional[Union[List[int], ndarray, Series]] = None,
        sample_weight: ArrayLike | None = None,
    ) -> "StandardScaler": ...
    def transform(self, X: ArrayLike, copy: bool | None = None) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike, copy: bool | None = None) -> NDArray: ...
    def _more_tags(
        self,
    ) -> Dict[str, Union[bool, List[Union[Type[float64], Type[np.float32]]]]]: ...

class MaxAbsScaler(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(self, *, copy: bool = True) -> None: ...
    def _reset(self) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "MaxAbsScaler": ...
    def partial_fit(self, X: NDArray | ArrayLike, y: None = None) -> "MaxAbsScaler": ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

def maxabs_scale(X: NDArray | ArrayLike, *, axis: int = 0, copy: bool = True): ...

class RobustScaler(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        with_centering: bool = True,
        with_scaling: bool = True,
        quantile_range: tuple[float, float] = ...,
        copy: bool = True,
        unit_variance: bool = False,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "RobustScaler": ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

def robust_scale(
    X: NDArray | ArrayLike,
    *,
    axis: int = 0,
    with_centering: bool = True,
    with_scaling: bool = True,
    quantile_range: tuple[float, float] = ...,
    copy: bool = True,
    unit_variance: bool = False,
) -> NDArray: ...
def normalize(
    X: NDArray | ArrayLike,
    norm: Literal["l1", "l2", "max"] = "l2",
    *,
    axis: Literal[0, 1] = 1,
    copy: bool = True,
    return_norm: bool = False,
) -> Union[ndarray, csr_matrix]: ...

class Normalizer(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(self, norm: Literal["l1", "l2", "max"] = "l2", *, copy: bool = True) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "Normalizer": ...
    def transform(self, X: NDArray | ArrayLike, copy: bool | None = None) -> NDArray: ...
    def _more_tags(self): ...

def binarize(X: NDArray | ArrayLike, *, threshold: float = 0.0, copy: bool = True) -> NDArray: ...

class Binarizer(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(self, *, threshold: float = 0.0, copy: bool = True): ...
    def fit(self, X: NDArray | ArrayLike, y=None) -> Any: ...
    def transform(self, X: NDArray | ArrayLike, copy: bool | None = None) -> NDArray: ...
    def _more_tags(self): ...

class KernelCenterer(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(self) -> None: ...
    def fit(self, K: NDArray, y: None = None) -> "KernelCenterer": ...
    def transform(self, K: NDArray, copy: bool = True) -> NDArray: ...
    @property
    def _n_features_out(self): ...
    def _more_tags(self): ...

def add_dummy_feature(X: NDArray | ArrayLike, value: float = 1.0) -> NDArray: ...

class QuantileTransformer(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        n_quantiles: int = 1000,
        output_distribution: Literal["uniform", "normal"] = "uniform",
        ignore_implicit_zeros: bool = False,
        subsample: int = ...,
        random_state: int | RandomState | None = None,
        copy: bool = True,
    ) -> None: ...
    def _dense_fit(self, X: ndarray, random_state: RandomState) -> None: ...
    def _sparse_fit(self, X, random_state): ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "QuantileTransformer": ...
    def _transform_col(self, X_col: ndarray, quantiles: ndarray, inverse: bool) -> ndarray: ...
    def _check_inputs(
        self,
        X: ndarray,
        in_fit: bool,
        accept_sparse_negative: bool = False,
        copy: bool = False,
    ) -> ndarray: ...
    def _transform(self, X: ndarray, inverse: bool = False) -> ndarray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

def quantile_transform(
    X: NDArray | ArrayLike,
    *,
    axis: int = 0,
    n_quantiles: int = 1000,
    output_distribution: Literal["uniform", "normal"] = "uniform",
    ignore_implicit_zeros: bool = False,
    subsample: int = ...,
    random_state: int | RandomState | None = None,
    copy: bool = True,
) -> NDArray: ...

class PowerTransformer(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        method: Literal["yeo-johnson", "box-cox"] = "yeo-johnson",
        *,
        standardize: bool = True,
        copy: bool = True,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "PowerTransformer": ...
    def fit_transform(self, X: ArrayLike, y: None = None) -> NDArray: ...
    def _fit(self, X: ndarray, y: None = None, force_transform: bool = False) -> ndarray: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
    def _box_cox_inverse_tranform(self, x, lmbda): ...
    def _yeo_johnson_inverse_transform(self, x, lmbda): ...
    def _yeo_johnson_transform(self, x: ndarray, lmbda: Union[int, float, float64]) -> ndarray: ...
    def _box_cox_optimize(self, x: ndarray) -> float64: ...
    def _yeo_johnson_optimize(self, x: ndarray) -> float64: ...
    def _check_input(
        self,
        X: ndarray,
        in_fit: bool,
        check_positive: bool = False,
        check_shape: bool = False,
        check_method: bool = False,
    ) -> ndarray: ...
    def _more_tags(self): ...

def power_transform(
    X: ArrayLike,
    method: Literal["yeo-johnson", "box-cox"] = "yeo-johnson",
    *,
    standardize: bool = True,
    copy: bool = True,
) -> NDArray: ...
