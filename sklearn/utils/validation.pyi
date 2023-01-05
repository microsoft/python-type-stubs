from numpy import float64, int64, uint64, ndarray
from typing import Dict, List, Optional, Tuple, Type, Union, Literal, Any, Callable
from numpy.typing import ArrayLike, NDArray

# Authors: Olivier Grisel
#          Gael Varoquaux
#          Andreas Mueller
#          Lars Buitinck
#          Alexandre Gramfort
#          Nicolas Tresegnie
#          Sylvain Marie
# License: BSD 3 clause

from functools import wraps
import warnings
import numbers
import operator

import numpy as np
import scipy.sparse as sp
from inspect import signature, isclass, Parameter

# mypy error: Module 'numpy.core.numeric' has no attribute 'ComplexWarning'
from numpy.core.numeric import ComplexWarning  # type: ignore
import joblib

from contextlib import suppress

from .fixes import _object_dtype_isnan
from .. import get_config as _get_config
from ..exceptions import PositiveSpectrumWarning
from ..exceptions import NotFittedError
from ..exceptions import DataConversionWarning
from joblib.memory import Memory
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from random.mtrand import RandomState
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.compose._column_transformer import ColumnTransformer
from sklearn.linear_model._base import LinearRegression
from sklearn.preprocessing._data import StandardScaler
from sklearn.preprocessing._encoders import OneHotEncoder
from sklearn.tree._classes import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeRegressor,
)

FLOAT_DTYPES = ...

# This function is not used anymore at this moment in the code base but we keep it in
# case that we merge a new public function without kwarg only by mistake, which would
# require a deprecation cycle to fix.
def _deprecate_positional_args(func=None, *, version="1.3"): ...
def _assert_all_finite(
    X: ndarray,
    allow_nan: bool = False,
    msg_dtype: None = None,
    estimator_name: Optional[str] = None,
    input_name: str = "",
) -> None: ...
def assert_all_finite(
    X: NDArray,
    *,
    allow_nan: bool = False,
    estimator_name: str | None = None,
    input_name: str = "",
) -> None: ...
def as_float_array(
    X: NDArray | ArrayLike,
    *,
    copy: bool = True,
    force_all_finite: bool | Literal["allow-nan"] = True,
) -> NDArray: ...
def _is_arraylike(x: Union[int64, ndarray, str, int]) -> bool: ...
def _is_arraylike_not_scalar(array: Union[int64, ndarray, str, int]) -> bool: ...
def _num_features(X: Union[DataFrame, csc_matrix, csr_matrix, ndarray]) -> int: ...
def _num_samples(x: Any) -> int: ...
def check_memory(memory: None | str | Memory) -> Memory: ...
def check_consistent_length(*arrays) -> None: ...
def _make_indexable(iterable: Any) -> Any: ...
def indexable(*iterables) -> list[NDArray | DataFrame] | None: ...
def _ensure_sparse_format(
    spmatrix: Union[csc_matrix, csr_matrix, coo_matrix],
    accept_sparse: Union[Tuple[str, str], List[str], str, bool],
    dtype: Optional[Union[Type[float64], Type[float32], Type[int], Type[float]]],
    copy: bool,
    force_all_finite: bool,
    accept_large_sparse: bool,
    estimator_name: Optional[str] = None,
    input_name: str = "",
) -> Union[csc_matrix, csr_matrix, coo_matrix]: ...
def _ensure_no_complex_data(array: Union[csc_matrix, csr_matrix, coo_matrix, ndarray]) -> None: ...
def _check_estimator_name(estimator: Any) -> Optional[str]: ...
def _pandas_dtype_needs_early_conversion(pd_dtype): ...
def check_array(
    array: Any,
    accept_sparse: str | bool | Sequence[str] | tuple[str, ...] = False,
    *,
    accept_large_sparse: bool = True,
    dtype: type | Sequence[type] | Literal["numeric"] | None = "numeric",
    order: Literal["F", "C"] | None = None,
    copy: bool = False,
    force_all_finite: bool | Literal["allow-nan"] = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    ensure_min_samples: int = 1,
    ensure_min_features: int = 1,
    estimator: str | Estimator | None = None,
    input_name: str = "",
) -> Union[ndarray, csr_matrix, coo_matrix, csc_matrix]: ...
def _check_large_sparse(X: Union[csc_matrix, csr_matrix, coo_matrix], accept_large_sparse: bool = False) -> None: ...
def check_X_y(
    X: NDArray | list,
    y: NDArray | list,
    accept_sparse: str | bool | ArrayLike = False,
    *,
    accept_large_sparse: bool = True,
    dtype: type | Sequence[type] | Literal["numeric"] | None = "numeric",
    order: Literal["F", "C"] | None = None,
    copy: bool = False,
    force_all_finite: bool | Literal["allow-nan"] = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    multi_output: bool = False,
    ensure_min_samples: int = 1,
    ensure_min_features: int = 1,
    y_numeric: bool = False,
    estimator: str | Estimator | None = None,
) -> tuple[Any, Any]: ...
def _check_y(
    y: Union[Series, ndarray, List[int64], List[Union[int, float]], List[int]],
    multi_output: bool = False,
    y_numeric: bool = False,
    estimator: Optional[Any] = None,
) -> ndarray: ...
def column_or_1d(y: ArrayLike, *, warn: bool = False) -> NDArray: ...
def check_random_state(seed: int | RandomState | None) -> RandomState: ...
def has_fit_parameter(
    estimator: Union[
        DecisionTreeRegressor,
        DecisionTreeClassifier,
        LinearRegression,
        ExtraTreeRegressor,
    ],
    parameter: str,
) -> bool: ...
def check_symmetric(
    array: NDArray,
    *,
    tol: float = 1e-10,
    raise_warning: bool = True,
    raise_exception: bool = False,
) -> NDArray: ...
def check_is_fitted(
    estimator: Estimator,
    attributes: str | ArrayLike | tuple[str, ...] | None = None,
    *,
    msg: str | None = None,
    all_or_any: Callable = ...,
) -> None: ...
def check_non_negative(X: NDArray | ArrayLike, whom: str) -> None: ...
def check_scalar(
    x: Union[bool, float, float64, Tuple[int, int], int],
    name: str,
    target_type: type | tuple,
    *,
    min_val: float | int | None = None,
    max_val: float | int | None = None,
    include_boundaries: Literal["left", "right", "both", "neither"] = "both",
) -> Number: ...
def _check_psd_eigenvalues(lambdas: ndarray, enable_warnings: bool = False) -> ndarray: ...
def _check_sample_weight(
    sample_weight: Optional[ndarray],
    X: Union[ndarray, csr_matrix, csc_matrix],
    dtype: Optional[Type[float64]] = None,
    copy: bool = False,
    only_non_negative: bool = False,
) -> ndarray: ...
def _allclose_dense_sparse(x, y, rtol=1e-7, atol=1e-9): ...
def _check_fit_params(
    X: Union[ndarray, List[str]],
    fit_params: Dict[Any, Any],
    indices: Optional[ndarray] = None,
) -> Dict[Any, Any]: ...
def _get_feature_names(X: Any) -> Optional[ndarray]: ...
def _check_feature_names_in(
    estimator: Union[ColumnTransformer, OneHotEncoder, StandardScaler],
    input_features: Optional[ndarray] = None,
    *,
    generate_names=True,
) -> ndarray: ...
def _generate_get_feature_names_out(estimator, n_features_out, input_features=None): ...
