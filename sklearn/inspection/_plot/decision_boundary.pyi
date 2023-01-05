from typing import Callable, Literal, Any
from numpy.typing import NDArray, ArrayLike
from sklearn.inspection import DecisionBoundaryDisplay
from functools import reduce

import numpy as np

from ...preprocessing import LabelEncoder
from ...utils import check_matplotlib_support
from ...utils import _safe_indexing
from ...base import is_regressor
from ...utils.validation import check_is_fitted, _is_arraylike_not_scalar
from numpy import ndarray
from pandas import DataFrame
from matplotlib.axes import Axes
from sklearn.base import BaseEstimator

def _check_boundary_response_method(estimator: BaseEstimator, response_method: str) -> Callable: ...

class DecisionBoundaryDisplay:
    def __init__(
        self,
        *,
        xx0: NDArray,
        xx1: NDArray,
        response: NDArray,
        xlabel: str | None = None,
        ylabel: str | None = None,
    ) -> None: ...
    def plot(
        self,
        plot_method: Literal["contourf", "contour", "pcolormesh"] = "contourf",
        ax: Axes | None = None,
        xlabel: str | None = None,
        ylabel: str | None = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: ArrayLike | DataFrame,
        *,
        grid_resolution: int = 100,
        eps: float = 1.0,
        plot_method: Literal["contourf", "contour", "pcolormesh"] = "contourf",
        response_method: Literal["auto", "predict_proba", "decision_function", "predict"] = "auto",
        xlabel: str | None = None,
        ylabel: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay: ...
