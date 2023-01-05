from sklearn.metrics import PrecisionRecallDisplay
from typing import Literal
from numpy.typing import NDArray, ArrayLike
from ...base import BaseEstimator, is_classifier
from .base import _get_response

from .. import average_precision_score
from .. import precision_recall_curve
from .._base import _check_pos_label_consistency
from .._classification import check_consistent_length

from ...utils import check_matplotlib_support, deprecated
from numpy import ndarray
from sklearn.pipeline import Pipeline
from matplotlib.axes import Axes

class PrecisionRecallDisplay:
    def __init__(
        self,
        precision: NDArray,
        recall: NDArray,
        *,
        average_precision: float | None = None,
        estimator_name: str | None = None,
        pos_label: str | int | None = None,
    ) -> None: ...
    def plot(self, ax: Axes | None = None, *, name: str | None = None, **kwargs) -> PrecisionRecallDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: ArrayLike | None = None,
        pos_label: str | int | None = None,
        response_method: Literal["predict_proba", "decision_function", "auto"] = "auto",
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> PrecisionRecallDisplay: ...
    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        sample_weight: ArrayLike | None = None,
        pos_label: str | int | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> PrecisionRecallDisplay: ...

@deprecated(
    "Function `plot_precision_recall_curve` is deprecated in 1.0 and will be "
    "removed in 1.2. Use one of the class methods: "
    "PrecisionRecallDisplay.from_predictions or "
    "PrecisionRecallDisplay.from_estimator."
)
def plot_precision_recall_curve(
    estimator: BaseEstimator,
    X: NDArray | ArrayLike,
    y: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    response_method: Literal["predict_proba", "decision_function", "auto"] = "auto",
    name: str | None = None,
    ax: Axes | None = None,
    pos_label: str | int | None = None,
    **kwargs,
) -> PrecisionRecallDisplay: ...
