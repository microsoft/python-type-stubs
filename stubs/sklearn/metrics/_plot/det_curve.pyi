from typing import Literal
from ...base import BaseEstimator
from matplotlib.axes import Axes
from matplotlib.artist import Artist
from ...utils import check_matplotlib_support as check_matplotlib_support
from ..._typing import ArrayLike, MatrixLike
from .. import det_curve as det_curve
from matplotlib.figure import Figure
import scipy as sp


class DetCurveDisplay:
    figure_: Figure = ...
    ax_: Axes = ...
    line_: Artist = ...

    def __init__(
        self,
        *,
        fpr: ArrayLike,
        fnr: ArrayLike,
        estimator_name: None | str = None,
        pos_label: None | str | int = None,
    ) -> None:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        response_method: Literal[
            "predict_proba", "decision_function", "auto", "auto"
        ] = "auto",
        pos_label: None | str | int = None,
        name: None | str = None,
        ax: None | Axes = None,
        **kwargs,
    ) -> DetCurveDisplay:
        ...

    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        pos_label: None | str | int = None,
        name: None | str = None,
        ax: None | Axes = None,
        **kwargs,
    ) -> DetCurveDisplay:
        ...

    def plot(
        self, ax: None | Axes = None, *, name: None | str = None, **kwargs
    ) -> DetCurveDisplay:
        ...
