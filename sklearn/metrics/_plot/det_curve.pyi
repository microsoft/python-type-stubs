from typing import Literal
from ...ensemble._forest import RandomForestClassifier
from ..._typing import ArrayLike, Estimator, MatrixLike
from matplotlib.axes import Axes
from ...utils import check_matplotlib_support as check_matplotlib_support
from .. import det_curve as det_curve
from ...pipeline import Pipeline
import scipy as sp


class DetCurveDisplay:
    def __init__(
        self,
        *,
        fpr: ArrayLike,
        fnr: ArrayLike,
        estimator_name: str | None = None,
        pos_label: int | str | None = None,
    ) -> None:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Pipeline | Estimator | RandomForestClassifier,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        response_method: Literal[
            "predict_proba", "decision_function", "auto", "auto"
        ] = "auto",
        pos_label: int | str | None = None,
        name: str | None = None,
        ax: Axes | None = None,
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
        pos_label: int | str | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> DetCurveDisplay:
        ...

    def plot(
        self, ax: Axes | None = None, *, name: str | None = None, **kwargs
    ) -> DetCurveDisplay:
        ...
