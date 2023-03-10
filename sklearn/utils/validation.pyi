from typing import Any, Callable, Literal, Sequence, Type
from .._typing import ArrayLike, MatrixLike, Int, Estimator, Float
from ..utils._array_api import get_namespace as get_namespace
from scipy.sparse import spmatrix
from pandas.api.types import is_sparse as is_sparse
from contextlib import suppress as suppress
from joblib import Memory
from ._isfinite import cy_isfinite as cy_isfinite, FiniteStatus as FiniteStatus 
from numpy.core.numeric import ComplexWarning as ComplexWarning
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from .. import get_config as _get_config
from inspect import signature as signature, isclass as isclass, Parameter as Parameter
from numpy.random import RandomState
from ..exceptions import (
    PositiveSpectrumWarning as PositiveSpectrumWarning,
    NotFittedError as NotFittedError,
    DataConversionWarning as DataConversionWarning,
)
from functools import wraps as wraps
from pandas.core.frame import DataFrame
from numbers import Real, Integral, Number
import warnings
import numbers
import operator

import numpy as np
import scipy.sparse as sp
import joblib

FLOAT_DTYPES = ...


def assert_all_finite(
    X: MatrixLike | ArrayLike,
    *,
    allow_nan: bool = False,
    estimator_name: str | None = None,
    input_name: str = "",
) -> None:
    ...


def as_float_array(
    X: MatrixLike | ArrayLike, *, copy: bool = True, force_all_finite: bool | str = True
) -> spmatrix | ndarray:
    ...


def check_memory(memory: Memory | str | None) -> Memory:
    ...


def check_consistent_length(*arrays) -> None:
    ...


def indexable(
    *iterables,
) -> list[DataFrame | None | ndarray | csr_matrix | Series | list[str]] | None | list[
    ndarray | spmatrix | DataFrame
]:
    ...


def check_array(
    array: Any,
    accept_sparse: Sequence[str] | str | tuple[str, str] | list[str] | bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: None | type | Sequence[type] | Literal["numeric", "numeric"] = "numeric",
    order: None | Literal["F", "C"] = None,
    copy: bool = False,
    force_all_finite: bool | str = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    ensure_min_samples: Int = 1,
    ensure_min_features: Int = 1,
    estimator: Estimator | str | None = None,
    input_name: str = "",
) -> Any:
    ...


def check_X_y(
    X: coo_matrix | MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    accept_sparse: Sequence[str] | str | tuple[str, str] | list[str] | bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: None | type | Sequence[type] | Literal["numeric", "numeric"] = "numeric",
    order: None | Literal["F", "C"] = None,
    copy: bool = False,
    force_all_finite: bool | str = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    multi_output: bool = False,
    ensure_min_samples: Int = 1,
    ensure_min_features: Int = 1,
    y_numeric: bool = False,
    estimator: Estimator | str | None = None,
) -> tuple[Any, Any]:
    ...


def column_or_1d(y: ArrayLike, *, dtype=None, warn: bool = False) -> ndarray:
    ...


def check_random_state(seed: RandomState | None | Int) -> RandomState:
    ...


def has_fit_parameter(estimator: Any, parameter: str) -> bool:
    ...


def check_symmetric(
    array: coo_matrix | MatrixLike | ArrayLike,
    *,
    tol: Float = 1e-10,
    raise_warning: bool = True,
    raise_exception: bool = False,
) -> csr_matrix | coo_matrix | spmatrix | ndarray:
    ...


def check_is_fitted(
    estimator: Estimator,
    attributes=None,
    *,
    msg: str | None = None,
    all_or_any: Callable = ...,
) -> None:
    ...


def check_non_negative(X: MatrixLike | ArrayLike, whom: str) -> None:
    ...


def check_scalar(
    x: Any,
    name: str,
    target_type: tuple | Type[Integral] | Type[Real] | type,
    *,
    min_val: None | Float = None,
    max_val: None | Float = None,
    include_boundaries: Literal["left", "right", "both", "neither", "both"] = "both",
) -> Number | Float:
    ...
