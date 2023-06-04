from typing import Callable, Iterable, Literal
from . import BaseCrossValidator
from numpy.random import RandomState
from matplotlib.figure import Figure
from ._split import BaseShuffleSplit
from matplotlib.axes import Axes
from matplotlib.artist import Artist
from .._typing import ArrayLike, MatrixLike, Int, Float
from ..utils import check_matplotlib_support as check_matplotlib_support
from . import learning_curve as learning_curve
import numpy as np


class LearningCurveDisplay:
    fill_between_: Artist | None = ...
    lines_: Artist | None = ...
    errorbar_: Artist | None = ...
    figure_: Figure = ...
    ax_: Axes = ...

    def __init__(
        self,
        *,
        train_sizes: ArrayLike,
        train_scores: MatrixLike,
        test_scores: MatrixLike,
        score_name: None | str = None,
    ) -> None:
        ...

    def plot(
        self,
        ax: None | Axes = None,
        *,
        negate_score: bool = False,
        score_name: None | str = None,
        score_type: Literal["test", "train", "both", "test"] = "test",
        log_scale: bool = False,
        std_display_style: None
        | Literal["errorbar", "fill_between", "fill_between"] = "fill_between",
        line_kw: None | dict = None,
        fill_between_kw: None | dict = None,
        errorbar_kw: None | dict = None,
    ) -> LearningCurveDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike,
        *,
        groups: None | ArrayLike = None,
        train_sizes: ArrayLike = ...,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        scoring: None | str | Callable = None,
        exploit_incremental_learning: bool = False,
        n_jobs: None | Int = None,
        pre_dispatch: str | Int = "all",
        verbose: Int = 0,
        shuffle: bool = False,
        random_state: RandomState | None | Int = None,
        error_score: str | Float = ...,
        fit_params: None | dict = None,
        ax: None | Axes = None,
        negate_score: bool = False,
        score_name: None | str = None,
        score_type: Literal["test", "train", "both", "test"] = "test",
        log_scale: bool = False,
        std_display_style: None
        | Literal["errorbar", "fill_between", "fill_between"] = "fill_between",
        line_kw: None | dict = None,
        fill_between_kw: None | dict = None,
        errorbar_kw: None | dict = None,
    ) -> LearningCurveDisplay:
        ...
