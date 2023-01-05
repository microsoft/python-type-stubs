from sklearn.metrics import ConfusionMatrixDisplay
from typing import Union, Literal, Mapping
from numpy.typing import NDArray, ArrayLike
from itertools import product

import numpy as np
from matplotlib.colors import Colormap
from matplotlib.axes import Axes

from .. import confusion_matrix
from ...utils import check_matplotlib_support
from ...utils import deprecated
from ...utils.multiclass import unique_labels
from ...base import BaseEstimator, is_classifier
from numpy import ndarray
from sklearn.model_selection._search import RandomizedSearchCV
from sklearn.svm._classes import SVC

class ConfusionMatrixDisplay:
    def __init__(self, confusion_matrix: NDArray, *, display_labels: NDArray | None = None) -> None: ...
    def plot(
        self,
        *,
        include_values: bool = True,
        cmap: str | Colormap = "viridis",
        xticks_rotation: Literal["vertical", "horizontal"] | float = "horizontal",
        values_format: str | None = None,
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: Mapping | None = None,
    ) -> ConfusionMatrixDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        *,
        labels: ArrayLike | None = None,
        sample_weight: ArrayLike | None = None,
        normalize: Literal["true", "pred", "all"] | None = None,
        display_labels: ArrayLike | None = None,
        include_values: bool = True,
        xticks_rotation: Literal["vertical", "horizontal"] | float = "horizontal",
        values_format: str | None = None,
        cmap: str | Colormap = "viridis",
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: Mapping | None = None,
    ) -> ConfusionMatrixDisplay: ...
    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        labels: ArrayLike | None = None,
        sample_weight: ArrayLike | None = None,
        normalize: Literal["true", "pred", "all"] | None = None,
        display_labels: ArrayLike | None = None,
        include_values: bool = True,
        xticks_rotation: Literal["vertical", "horizontal"] | float = "horizontal",
        values_format: str | None = None,
        cmap: str | Colormap = "viridis",
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: Mapping | None = None,
    ) -> ConfusionMatrixDisplay: ...

@deprecated(
    "Function `plot_confusion_matrix` is deprecated in 1.0 and will be "
    "removed in 1.2. Use one of the class methods: "
    "ConfusionMatrixDisplay.from_predictions or "
    "ConfusionMatrixDisplay.from_estimator."
)
def plot_confusion_matrix(
    estimator: BaseEstimator,
    X: NDArray | ArrayLike,
    y_true: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    sample_weight: ArrayLike | None = None,
    normalize: Literal["true", "pred", "all"] | None = None,
    display_labels: ArrayLike | None = None,
    include_values: bool = True,
    xticks_rotation: Literal["vertical", "horizontal"] | float = "horizontal",
    values_format: str | None = None,
    cmap: str | Colormap = "viridis",
    ax: Axes | None = None,
    colorbar: bool = True,
) -> ConfusionMatrixDisplay: ...
