from typing import Literal, Mapping, Sequence
from numpy.random import RandomState
from scipy import sparse as sparse
from itertools import chain as chain
from ...base import BaseEstimator
from ...utils import (
    check_array as check_array,
    check_matplotlib_support as check_matplotlib_support,
    check_random_state as check_random_state,
)
from ...utils._bunch import Bunch
from .. import partial_dependence as partial_dependence
from ...utils.parallel import delayed as delayed, Parallel as Parallel
from matplotlib.gridspec import GridSpecFromSubplotSpec as GridSpecFromSubplotSpec
from matplotlib.axes import Axes
from numpy import ndarray
from ...base import is_regressor as is_regressor
from matplotlib.figure import Figure
from math import ceil as ceil
from scipy.stats.mstats import mquantiles as mquantiles
from ..._typing import Int, ArrayLike, MatrixLike
import numbers
import warnings

import numpy as np


class PartialDependenceDisplay:
    figure_: Figure = ...
    heatmaps_: ndarray = ...
    bars_: ndarray = ...
    contours_: ndarray = ...
    deciles_hlines_: ndarray = ...
    deciles_vlines_: ndarray = ...
    lines_: ndarray = ...
    axes_: ndarray = ...
    bounding_ax_: None | Axes = ...

    def __init__(
        self,
        pd_results: list[Bunch] | Sequence[Bunch],
        *,
        features: Sequence[int] | Sequence[tuple[int, int]],
        feature_names: Sequence[str],
        target_idx: Int,
        deciles: dict,
        pdp_lim: None | Mapping | str = "deprecated",
        kind: Sequence[Literal["average", "individual", "both"]]
        | Literal["average", "individual", "both", "average"] = "average",
        subsample: float | None | int = 1000,
        random_state: RandomState | None | Int = None,
        is_categorical: None | ArrayLike = None,
    ) -> None:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: MatrixLike,
        features: list[int | str | tuple[str, str]]
        | Sequence[int | str | Sequence[int | str]],
        *,
        categorical_features: None | MatrixLike | ArrayLike = None,
        feature_names: None | ArrayLike = None,
        target: None | Int = None,
        response_method: Literal[
            "auto", "predict_proba", "decision_function", "auto"
        ] = "auto",
        n_cols: Int = 3,
        grid_resolution: Int = 100,
        percentiles: tuple[float, ...] = ...,
        method: str = "auto",
        n_jobs: None | Int = None,
        verbose: Int = 0,
        line_kw: None | dict = None,
        ice_lines_kw: None | dict = None,
        pd_line_kw: None | dict = None,
        contour_kw: None | dict = None,
        ax: None | Sequence[Axes] | Axes = None,
        kind: Literal["average", "individual", "both", "average"] = "average",
        centered: bool = False,
        subsample: float | None | int = 1000,
        random_state: RandomState | None | Int = None,
    ) -> PartialDependenceDisplay:
        ...

    def plot(
        self,
        *,
        ax: None | Sequence[Axes] | Axes = None,
        n_cols: Int = 3,
        line_kw: None | dict = None,
        ice_lines_kw: None | dict = None,
        pd_line_kw: None | dict = None,
        contour_kw: None | dict = None,
        bar_kw: None | dict = None,
        heatmap_kw: None | dict = None,
        pdp_lim: None | dict = None,
        centered: bool = False,
    ) -> PartialDependenceDisplay:
        ...
