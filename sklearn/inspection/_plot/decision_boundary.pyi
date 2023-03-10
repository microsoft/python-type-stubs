from typing import Any, Literal
from ...preprocessing import LabelEncoder as LabelEncoder
from ...base import is_regressor as is_regressor
from ..._typing import MatrixLike, Int, Float
from ...utils.validation import check_is_fitted as check_is_fitted
from matplotlib.axes import Axes
from ...utils import check_matplotlib_support as check_matplotlib_support
from functools import reduce as reduce

import numpy as np


class DecisionBoundaryDisplay:
    def __init__(
        self,
        *,
        xx0: MatrixLike,
        xx1: MatrixLike,
        response: MatrixLike,
        xlabel: str | None = None,
        ylabel: str | None = None,
    ) -> None:
        ...

    def plot(
        self,
        plot_method: Literal[
            "contourf", "contour", "pcolormesh", "contourf"
        ] = "contourf",
        ax: Axes | None = None,
        xlabel: str | None = None,
        ylabel: str | None = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Any,
        X: MatrixLike,
        *,
        grid_resolution: Int = 100,
        eps: Float = 1.0,
        plot_method: Literal[
            "contourf", "contour", "pcolormesh", "contourf"
        ] = "contourf",
        response_method: Literal[
            "auto", "predict_proba", "decision_function", "predict", "auto"
        ] = "auto",
        xlabel: str | None = None,
        ylabel: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay:
        ...
