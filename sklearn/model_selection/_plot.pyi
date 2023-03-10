from typing import Callable, Iterable, Literal
from collections.abc import Iterable
from numpy.random import RandomState
from .._typing import ArrayLike, MatrixLike, Int, Float
from ..naive_bayes import GaussianNB
from matplotlib.axes import Axes
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from . import learning_curve as learning_curve
from ..utils import check_matplotlib_support as check_matplotlib_support
from ..svm._classes import SVC, SVR
from . import BaseCrossValidator
from ..kernel_ridge import KernelRidge
import numpy as np


class LearningCurveDisplay:
    def __init__(
        self,
        *,
        train_sizes: ArrayLike,
        train_scores: MatrixLike,
        test_scores: MatrixLike,
        score_name: str | None = None,
    ) -> None:
        ...

    def plot(
        self,
        ax: Axes | None = None,
        *,
        negate_score: bool = False,
        score_name: str | None = None,
        score_type: Literal["test", "train", "both", "test"] = "test",
        log_scale: bool = False,
        std_display_style: Literal["errorbar", "fill_between", "fill_between"]
        | None = "fill_between",
        line_kw: dict | None = None,
        fill_between_kw: dict | None = None,
        errorbar_kw: dict | None = None,
    ) -> LearningCurveDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: SVC | KernelRidge | SVR | GaussianNB | HistGradientBoostingRegressor,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike,
        *,
        groups: None | ArrayLike = None,
        train_sizes: ArrayLike = ...,
        cv: Iterable | BaseCrossValidator | int | None = None,
        scoring: str | None | Callable = None,
        exploit_incremental_learning: bool = False,
        n_jobs: None | Int = None,
        pre_dispatch: str | Int = "all",
        verbose: Int = 0,
        shuffle: bool = False,
        random_state: RandomState | None | Int = None,
        error_score: str | Float = ...,
        fit_params: dict | None = None,
        ax: Axes | None = None,
        negate_score: bool = False,
        score_name: str | None = None,
        score_type: Literal["test", "train", "both", "test"] = "test",
        log_scale: bool = False,
        std_display_style: Literal["errorbar", "fill_between", "fill_between"]
        | None = "fill_between",
        line_kw: dict | None = None,
        fill_between_kw: dict | None = None,
        errorbar_kw: dict | None = None,
    ) -> LearningCurveDisplay:
        ...
