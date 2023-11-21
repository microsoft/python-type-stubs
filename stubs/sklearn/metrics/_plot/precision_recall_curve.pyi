from typing import Literal

from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from ..._typing import ArrayLike, Float, MatrixLike
from ...base import BaseEstimator, is_classifier as is_classifier
from ...utils import check_matplotlib_support as check_matplotlib_support
from .. import average_precision_score as average_precision_score, precision_recall_curve as precision_recall_curve
from .._classification import check_consistent_length as check_consistent_length

class PrecisionRecallDisplay:
    figure_: Figure = ...
    ax_: Axes = ...
    line_: Artist = ...

    def __init__(
        self,
        precision: ArrayLike,
        recall: ArrayLike,
        *,
        average_precision: None | Float = None,
        estimator_name: None | str = None,
        pos_label: None | str | int = None,
    ) -> None: ...
    def plot(self, ax: None | Axes = None, *, name: None | str = None, **kwargs) -> PrecisionRecallDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        pos_label: None | str | int = None,
        response_method: Literal["predict_proba", "decision_function", "auto", "auto"] = "auto",
        name: None | str = None,
        ax: None | Axes = None,
        **kwargs,
    ) -> PrecisionRecallDisplay: ...
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
    ) -> PrecisionRecallDisplay: ...
