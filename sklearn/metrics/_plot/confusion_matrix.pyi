from typing import Literal
from ...base import is_classifier as is_classifier
from .. import confusion_matrix
from ...model_selection._search import RandomizedSearchCV
from ..._typing import MatrixLike, ArrayLike, Estimator
from matplotlib.axes import Axes
from matplotlib.colors import Colormap
from ...utils import check_matplotlib_support as check_matplotlib_support
from itertools import product as product
from ...svm._classes import SVC
from ...utils.multiclass import unique_labels as unique_labels

import numpy as np


class ConfusionMatrixDisplay:
    def __init__(
        self, confusion_matrix: MatrixLike, *, display_labels: None | ArrayLike = None
    ) -> None:
        ...

    def plot(
        self,
        *,
        include_values: bool = True,
        cmap: Colormap | str = "viridis",
        xticks_rotation: Literal["vertical", "horizontal", "horizontal"]
        | float = "horizontal",
        values_format: str | None = None,
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: dict | None = None,
        text_kw: dict | None = None,
    ) -> ConfusionMatrixDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: SVC | Estimator | RandomizedSearchCV,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        labels: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
        normalize: None | Literal["true", "pred", "all"] = None,
        display_labels: None | ArrayLike = None,
        include_values: bool = True,
        xticks_rotation: Literal["vertical", "horizontal", "horizontal"]
        | float = "horizontal",
        values_format: str | None = None,
        cmap: Colormap | str = "viridis",
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: dict | None = None,
        text_kw: dict | None = None,
    ) -> ConfusionMatrixDisplay:
        ...

    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_pred: ArrayLike,
        *,
        labels: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
        normalize: None | Literal["true", "pred", "all"] = None,
        display_labels: None | ArrayLike = None,
        include_values: bool = True,
        xticks_rotation: Literal["vertical", "horizontal", "horizontal"]
        | float = "horizontal",
        values_format: str | None = None,
        cmap: Colormap | str = "viridis",
        ax: Axes | None = None,
        colorbar: bool = True,
        im_kw: dict | None = None,
        text_kw: dict | None = None,
    ) -> ConfusionMatrixDisplay:
        ...
