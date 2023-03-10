from typing import Literal
from ...ensemble._forest import RandomForestClassifier
from ..._typing import ArrayLike, Float, Estimator, MatrixLike
from matplotlib.axes import Axes
from ...utils import check_matplotlib_support as check_matplotlib_support
from ...svm._classes import SVC
from ...ensemble._gb import GradientBoostingClassifier
from .. import auc as auc, roc_curve as roc_curve
from ...pipeline import Pipeline


class RocCurveDisplay:
    def __init__(
        self,
        *,
        fpr: ArrayLike,
        tpr: ArrayLike,
        roc_auc: None | Float = None,
        estimator_name: str | None = None,
        pos_label: int | str | None = None,
    ) -> None:
        ...

    def plot(
        self, ax: Axes | None = None, *, name: str | None = None, **kwargs
    ) -> RocCurveDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Pipeline
        | SVC
        | Estimator
        | GradientBoostingClassifier
        | RandomForestClassifier,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        drop_intermediate: bool = True,
        response_method: Literal[
            "predict_proba", "decision_function", "auto", "auto"
        ] = "auto",
        pos_label: int | str | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> RocCurveDisplay:
        ...

    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        sample_weight: None | ArrayLike = None,
        drop_intermediate: bool = True,
        pos_label: int | str | None = None,
        name: str | None = None,
        ax: Axes | None = None,
        **kwargs,
    ) -> RocCurveDisplay:
        ...
