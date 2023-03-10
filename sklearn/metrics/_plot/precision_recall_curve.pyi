from typing import Literal
from ...base import is_classifier as is_classifier
from ..._typing import ArrayLike, Float, Estimator, MatrixLike
from matplotlib.axes import Axes
from ...utils import check_matplotlib_support as check_matplotlib_support
from .._classification import check_consistent_length as check_consistent_length
from .. import (
    average_precision_score as average_precision_score,
    precision_recall_curve as precision_recall_curve,
)
from ...pipeline import Pipeline


class PrecisionRecallDisplay:
    def __init__(
        self,
        precision: ArrayLike,
        recall: ArrayLike,
        *,
        average_precision: None | Float = None,
        estimator_name: str | None = None,
        pos_label: int | str | None = None,
    ) -> None:
        ...

    def plot(
        self, ax: Axes | None = None, *, name: str | None = None, **kwargs
    ) -> PrecisionRecallDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Pipeline | Estimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        pos_label: int | str | None = None,
        response_method: Literal[
            "predict_proba", "decision_function", "auto", "auto"
        ] = "auto",
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> PrecisionRecallDisplay:
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
    ) -> PrecisionRecallDisplay:
        ...
