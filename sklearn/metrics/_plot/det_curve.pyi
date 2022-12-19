from ...base import BaseEstimator
from sklearn.metrics import DetCurveDisplay
from numpy.typing import NDArray, ArrayLike
import scipy as sp

from .base import _get_response

from .. import det_curve
from .._base import _check_pos_label_consistency

from ...utils import check_matplotlib_support
from ...utils import deprecated
from numpy import ndarray
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.pipeline import Pipeline
from typing import Union, Sequence, Literal, Mapping
from matplotlib.axes import Axes

class DetCurveDisplay:
    def __init__(
        self,
        *,
        fpr: NDArray,
        fnr: NDArray,
        estimator_name: str | None = None,
        pos_label: str | int | None = None,
    ) -> None: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: ArrayLike | None = None,
        response_method: Literal["predict_proba", "decision_function", "auto"] = "auto",
        pos_label: str | int | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> DetCurveDisplay: ...
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
    ) -> DetCurveDisplay: ...
    def plot(self, ax: Axes | None = None, *, name: str | None = None, **kwargs) -> DetCurveDisplay: ...

@deprecated(
    "Function plot_det_curve is deprecated in 1.0 and will be "
    "removed in 1.2. Use one of the class methods: "
    "DetCurveDisplay.from_predictions or "
    "DetCurveDisplay.from_estimator."
)
def plot_det_curve(
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
) -> DetCurveDisplay: ...
