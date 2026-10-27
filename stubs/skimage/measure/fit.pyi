import math
import sys
from typing import Any, Protocol, TypeVar, overload, runtime_checkable
from typing_extensions import Self
from warnings import warn

import numpy as np
from numpy.linalg import inv
from numpy.typing import ArrayLike, NDArray
from scipy import optimize, spatial

if sys.version_info >= (3, 11):
    from .._shared.utils import FailedEstimation

    @runtime_checkable
    class RansacModelProtocol(Protocol):
        @classmethod
        def from_estimate(cls, *data: NDArray) -> Self | FailedEstimation: ...
        def residuals(self, *data: NDArray) -> NDArray[np.floating]: ...

    _ModelT = TypeVar("_ModelT")

    def add_from_estimate(cls: type[_ModelT]) -> type[_ModelT]: ...

def _check_data_dim(data, dim): ...
def _check_data_atleast_2D(data): ...

class BaseModel:
    def __init__(self) -> None: ...

if sys.version_info >= (3, 11):
    class _BaseModel:
        @classmethod
        def from_estimate(cls, data: NDArray) -> Self | FailedEstimation: ...

    _ModelBase = _BaseModel
else:
    _ModelBase = BaseModel

class LineModelND(_ModelBase):
    if sys.version_info >= (3, 11):
        origin: NDArray | None
        direction: NDArray | None
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, origin: ArrayLike, direction: ArrayLike) -> None: ...
        @property
        def params(self) -> tuple[NDArray | None, NDArray | None]: ...
    def estimate(self, data: NDArray) -> bool: ...
    def residuals(self, data: NDArray, params: tuple[ArrayLike, ArrayLike] | None = ...) -> NDArray[np.floating]: ...
    def predict(self, x: ArrayLike, axis: int = 0, params: tuple[ArrayLike, ArrayLike] | None = ...) -> NDArray: ...
    def predict_x(self, y: ArrayLike, params: tuple[ArrayLike, ArrayLike] | None = ...) -> NDArray: ...
    def predict_y(self, x: ArrayLike, params: tuple[ArrayLike, ArrayLike] | None = ...) -> NDArray: ...

class CircleModel(_ModelBase):
    if sys.version_info >= (3, 11):
        center: NDArray | None
        radius: float | None
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, center: ArrayLike, radius: float) -> None: ...
        @property
        def params(self) -> NDArray: ...
    def estimate(self, data: NDArray) -> bool: ...
    def residuals(self, data: NDArray) -> NDArray[np.floating]: ...
    def predict_xy(self, t: ArrayLike, params: ArrayLike | None = ...) -> NDArray: ...

class EllipseModel(_ModelBase):
    if sys.version_info >= (3, 11):
        center: NDArray | None
        axis_lengths: NDArray | None
        theta: float | None
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, center: ArrayLike, axis_lengths: ArrayLike, theta: float) -> None: ...
        @property
        def params(self) -> NDArray: ...
    def estimate(self, data: NDArray) -> bool: ...
    def residuals(self, data: NDArray) -> NDArray[np.float64]: ...
    def predict_xy(self, t: ArrayLike, params: ArrayLike | None = ...) -> NDArray: ...

def _dynamic_max_trials(n_inliers, n_samples, min_samples, probability): ...
def ransac(
    data,
    model_class: Any,
    min_samples,
    residual_threshold,
    is_data_valid=None,
    is_model_valid=None,
    max_trials: int = 100,
    stop_sample_num: int = ...,
    stop_residuals_sum: float = 0,
    stop_probability=1,
    random_state=None,
    initial_inliers=None,
): ...
