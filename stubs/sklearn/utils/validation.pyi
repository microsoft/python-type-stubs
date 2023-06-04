from typing import Any, Callable, Literal, Sequence, Type
from ..base import BaseEstimator
from ..exceptions import (
    PositiveSpectrumWarning as PositiveSpectrumWarning,
    NotFittedError as NotFittedError,
    DataConversionWarning as DataConversionWarning,
)
from scipy.sparse._coo import coo_matrix
from numpy.random.mtrand import RandomState
from ..utils._array_api import get_namespace as get_namespace
from inspect import signature as signature, isclass as isclass, Parameter as Parameter
from contextlib import suppress as suppress
from numpy.core.numeric import ComplexWarning as ComplexWarning
from joblib.memory import Memory
from ._isfinite import cy_isfinite as cy_isfinite, FiniteStatus as FiniteStatus
from scipy.sparse import spmatrix
from .. import get_config as _get_config
from numpy import ndarray
from numbers import Real, Integral, Number
from functools import wraps as wraps
from pandas.api.types import is_sparse as is_sparse
from pandas import DataFrame
from .._typing import MatrixLike, ArrayLike, Int, Float
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
    estimator_name: None | str = None,
    input_name: str = "",
) -> None:
    ...


def as_float_array(
    X: MatrixLike | ArrayLike, *, copy: bool = True, force_all_finite: str | bool = True
) -> ndarray | spmatrix:
    ...


def check_memory(memory: None | Memory | str) -> Memory:
    ...


def check_consistent_length(*arrays) -> None:
    ...


def indexable(*iterables) -> None | list[ndarray | spmatrix | DataFrame]:
    ...


def check_array(
    array: Any,
    accept_sparse: Sequence[str] | tuple[str, str] | list[str] | str | bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: None | Sequence[type] | Literal["numeric", "numeric"] | type = "numeric",
    order: Literal["F", "C"] | None = None,
    copy: bool = False,
    force_all_finite: str | bool = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    ensure_min_samples: Int = 1,
    ensure_min_features: Int = 1,
    estimator: None | str | BaseEstimator = None,
    input_name: str = "",
) -> Any:
    ...


def check_X_y(
    X: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    accept_sparse: Sequence[str] | tuple[str, str] | list[str] | str | bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: None | Sequence[type] | Literal["numeric", "numeric"] | type = "numeric",
    order: Literal["F", "C"] | None = None,
    copy: bool = False,
    force_all_finite: str | bool = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    multi_output: bool = False,
    ensure_min_samples: Int = 1,
    ensure_min_features: Int = 1,
    y_numeric: bool = False,
    estimator: None | str | BaseEstimator = None,
) -> tuple[Any, Any]:
    ...


def column_or_1d(y: ArrayLike, *, dtype=None, warn: bool = False) -> ndarray:
    ...


def check_random_state(seed: None | Int | RandomState) -> RandomState:
    ...


def has_fit_parameter(estimator: Any, parameter: str) -> bool:
    ...


def check_symmetric(
    array: coo_matrix | MatrixLike | ArrayLike,
    *,
    tol: Float = 1e-10,
    raise_warning: bool = True,
    raise_exception: bool = False,
) -> ndarray | spmatrix:
    ...


def check_is_fitted(
    estimator: BaseEstimator,
    attributes: tuple[str, ...] | None | Sequence | list[str] | str = None,
    *,
    msg: None | str = None,
    all_or_any: Callable = ...,
) -> None:
    ...


def check_non_negative(X: MatrixLike | ArrayLike, whom: str) -> None:
    ...


def check_scalar(
    x: Any,
    name: str,
    target_type: Type[Integral] | tuple | Type[Real] | type,
    *,
    min_val: None | Float = None,
    max_val: None | Float = None,
    include_boundaries: Literal["left", "right", "both", "neither", "both"] = "both",
) -> Number | Float:
    ...
