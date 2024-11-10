from functools import reduce as reduce
from typing import Any, Literal

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh
from matplotlib.contour import QuadContourSet
from matplotlib.figure import Figure

from ..._typing import Float, Int, MatrixLike
from ...base import is_regressor as is_regressor
from ...preprocessing import LabelEncoder as LabelEncoder
from ...utils import check_matplotlib_support as check_matplotlib_support
from ...utils.validation import check_is_fitted as check_is_fitted

class DecisionBoundaryDisplay:
    figure_: Figure = ...
    ax_: Axes = ...
    surface_: QuadContourSet | QuadMesh = ...

    def __init__(
        self,
        *,
        xx0: MatrixLike,
        xx1: MatrixLike,
        response: MatrixLike,
        xlabel: None | str = None,
        ylabel: None | str = None,
    ) -> None: ...
    def plot(
        self,
        plot_method: Literal["contourf", "contour", "pcolormesh"] = "contourf",
        ax: None | Axes = None,
        xlabel: None | str = None,
        ylabel: None | str = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: Any,
        X: MatrixLike,
        *,
        grid_resolution: Int = 100,
        eps: Float = 1.0,
        plot_method: Literal["contourf", "contour", "pcolormesh"] = "contourf",
        response_method: Literal["auto", "predict_proba", "decision_function", "predict"] = "auto",
        xlabel: None | str = None,
        ylabel: None | str = None,
        ax: None | Axes = None,
        **kwargs,
    ) -> DecisionBoundaryDisplay: ...
