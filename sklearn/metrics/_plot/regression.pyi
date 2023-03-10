from typing import Literal
from numpy.random import RandomState
from ..._typing import ArrayLike, Estimator, MatrixLike
from matplotlib.axes import Axes
from ...ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from ...utils import (
    check_matplotlib_support as check_matplotlib_support,
    check_random_state as check_random_state,
)
import numbers

import numpy as np


class PredictionErrorDisplay:
    def __init__(self, *, y_true: ArrayLike, y_pred: ArrayLike) -> None:
        ...

    def plot(
        self,
        ax: Axes | None = None,
        *,
        kind: Literal[
            "actual_vs_predicted", "residual_vs_predicted", "residual_vs_predicted"
        ] = "residual_vs_predicted",
        scatter_kwargs: dict | None = None,
        line_kwargs: dict | None = None,
    ) -> PredictionErrorDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Estimator | HistGradientBoostingRegressor,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        kind: Literal[
            "actual_vs_predicted", "residual_vs_predicted", "residual_vs_predicted"
        ] = "residual_vs_predicted",
        subsample: int | float | None = 1_000,
        random_state: int | RandomState | None = None,
        ax: Axes | None = None,
        scatter_kwargs: dict | None = None,
        line_kwargs: dict | None = None,
    ) -> PredictionErrorDisplay:
        ...

    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        kind: Literal[
            "actual_vs_predicted", "residual_vs_predicted", "residual_vs_predicted"
        ] = "residual_vs_predicted",
        subsample: int | float | None = 1_000,
        random_state: int | RandomState | None = None,
        ax: Axes | None = None,
        scatter_kwargs: dict | None = None,
        line_kwargs: dict | None = None,
    ) -> PredictionErrorDisplay:
        ...
