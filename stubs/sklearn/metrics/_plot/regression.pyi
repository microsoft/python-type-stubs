from typing import Literal
from numpy.random import RandomState
from ...base import BaseEstimator
from matplotlib.axes import Axes
from matplotlib.artist import Artist
from ...utils import (
    check_matplotlib_support as check_matplotlib_support,
    check_random_state as check_random_state,
)
from ..._typing import ArrayLike, MatrixLike
from matplotlib.figure import Figure
import numbers

import numpy as np


class PredictionErrorDisplay:
    figure_: Figure = ...
    ax_: Axes = ...
    scatter_: Artist = ...
    errors_lines_: Artist | None = ...
    line_: Artist = ...

    def __init__(self, *, y_true: ArrayLike, y_pred: ArrayLike) -> None:
        ...

    def plot(
        self,
        ax: None | Axes = None,
        *,
        kind: Literal[
            "actual_vs_predicted", "residual_vs_predicted", "residual_vs_predicted"
        ] = "residual_vs_predicted",
        scatter_kwargs: None | dict = None,
        line_kwargs: None | dict = None,
    ) -> PredictionErrorDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        kind: Literal[
            "actual_vs_predicted", "residual_vs_predicted", "residual_vs_predicted"
        ] = "residual_vs_predicted",
        subsample: float | None | int = 1_000,
        random_state: None | RandomState | int = None,
        ax: None | Axes = None,
        scatter_kwargs: None | dict = None,
        line_kwargs: None | dict = None,
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
        subsample: float | None | int = 1_000,
        random_state: None | RandomState | int = None,
        ax: None | Axes = None,
        scatter_kwargs: None | dict = None,
        line_kwargs: None | dict = None,
    ) -> PredictionErrorDisplay:
        ...
