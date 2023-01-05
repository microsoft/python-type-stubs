from ...base import BaseEstimator
from ...metrics import RocCurveDisplay
from numpy.typing import NDArray, ArrayLike
from .base import _get_response

from .. import auc
from .. import roc_curve
from .._base import _check_pos_label_consistency

from ...utils import check_matplotlib_support, deprecated
from numpy import ndarray
from pandas.core.series import Series
from ...ensemble._gb import GradientBoostingClassifier
from ...pipeline import Pipeline
from ...svm._classes import SVC
from typing import Union, Sequence, Literal, Mapping
from matplotlib.axes import Axes

class RocCurveDisplay:
    def __init__(
        self,
        *,
        fpr: NDArray,
        tpr: NDArray,
        roc_auc: float | None = None,
        estimator_name: str | None = None,
        pos_label: str | int | None = None,
    ) -> None: ...
    def plot(self, ax: Axes | None = None, *, name: str | None = None, **kwargs) -> RocCurveDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: ArrayLike | None = None,
        drop_intermediate: bool = True,
        response_method: Literal["predict_proba", "decision_function", "auto"] = "auto",
        pos_label: str | int | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> RocCurveDisplay: ...
    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        sample_weight: ArrayLike | None = None,
        drop_intermediate: bool = True,
        pos_label: str | int | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> RocCurveDisplay: ...

@deprecated(
    "Function :func:`plot_roc_curve` is deprecated in 1.0 and will be "
    "removed in 1.2. Use one of the class methods: "
    ":meth:`sklearn.metrics.RocCurveDisplay.from_predictions` or "
    ":meth:`sklearn.metrics.RocCurveDisplay.from_estimator`."
)
def plot_roc_curve(
    estimator: BaseEstimator,
    X: NDArray | ArrayLike,
    y: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    drop_intermediate: bool = True,
    response_method: Literal["predict_proba", "decision_function", "auto"] = "auto",
    name: str | None = None,
    ax: Axes | None = None,
    pos_label: str | int | None = None,
    **kwargs,
) -> RocCurveDisplay: ...
