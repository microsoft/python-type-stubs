from sklearn.base import BaseEstimator
from sklearn.utils._bunch import Bunch
from sklearn.inspection import PartialDependenceDisplay
from numpy.typing import ArrayLike
from typing import List, Union, Literal, Mapping, Sequence
import numbers
import warnings
from itertools import chain
from math import ceil

import numpy as np
from numpy.random import RandomState
from matplotlib.axes import Axes
from scipy import sparse
from scipy.stats.mstats import mquantiles

from .. import partial_dependence
from ...base import is_regressor
from ...utils import Bunch
from ...utils import check_array
from ...utils import deprecated
from ...utils import check_matplotlib_support  # noqa
from ...utils import check_random_state
from ...utils import _safe_indexing
from ...utils.fixes import delayed
from numpy import ndarray
from pandas.core.frame import DataFrame
from sklearn.ensemble._forest import RandomForestRegressor
from sklearn.ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from sklearn.pipeline import Pipeline
from sklearn.tree._classes import DecisionTreeRegressor

@deprecated(
    "Function `plot_partial_dependence` is deprecated in 1.0 and will be "
    "removed in 1.2. Use PartialDependenceDisplay.from_estimator instead"
)
def plot_partial_dependence(
    estimator: BaseEstimator,
    X: ArrayLike | DataFrame,
    features: Sequence[int | str | tuple[int, int] | tuple[str, str]],
    *,
    feature_names: ArrayLike | None = None,
    target: int | None = None,
    response_method: Literal["auto", "predict_proba", "decision_function"] = "auto",
    n_cols: int = 3,
    grid_resolution: int = 100,
    percentiles: tuple[float, ...] = ...,
    method: str = "auto",
    n_jobs: int | None = None,
    verbose: int = 0,
    line_kw: Mapping | None = None,
    ice_lines_kw: Mapping | None = None,
    pd_line_kw: Mapping | None = None,
    contour_kw: Mapping | None = None,
    ax: Axes | Sequence[Axes] | None = None,
    kind: Literal["average", "individual", "both"] | Sequence[str] = "average",
    subsample: float | int | None = 1000,
    random_state: int | RandomState | None = None,
    centered: bool = False,
) -> PartialDependenceDisplay: ...

# TODO: Move into PartialDependenceDisplay.from_estimator in 1.2
def _plot_partial_dependence(
    estimator: Union[
        DecisionTreeRegressor,
        HistGradientBoostingRegressor,
        Pipeline,
        RandomForestRegressor,
    ],
    X: Union[DataFrame, ndarray],
    features: List[Union[int, str]],
    *,
    feature_names=None,
    target=None,
    response_method="auto",
    n_cols=3,
    grid_resolution=100,
    percentiles=(0.05, 0.95),
    method="auto",
    n_jobs=None,
    verbose=0,
    line_kw=None,
    ice_lines_kw=None,
    pd_line_kw=None,
    contour_kw=None,
    ax=None,
    kind="average",
    subsample=1000,
    random_state=None,
    centered=False,
) -> "PartialDependenceDisplay": ...

class PartialDependenceDisplay:
    def __init__(
        self,
        pd_results: ArrayLike,
        *,
        features: list | Sequence[tuple[int, int]],
        feature_names: ArrayLike,
        target_idx: int,
        deciles: Mapping,
        pdp_lim: Mapping | None | str = "deprecated",
        kind: Literal["average", "individual", "both"] | Sequence[str] = "average",
        subsample: float | int | None = 1000,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: ArrayLike | DataFrame,
        features: Sequence[int | str | tuple[int, int] | tuple[str, str]],
        *,
        feature_names: ArrayLike | None = None,
        target: int | None = None,
        response_method: Literal["auto", "predict_proba", "decision_function"] = "auto",
        n_cols: int = 3,
        grid_resolution: int = 100,
        percentiles: tuple[float, ...] = ...,
        method: str = "auto",
        n_jobs: int | None = None,
        verbose: int = 0,
        line_kw: Mapping | None = None,
        ice_lines_kw: Mapping | None = None,
        pd_line_kw: Mapping | None = None,
        contour_kw: Mapping | None = None,
        ax: Axes | Sequence[Axes] | None = None,
        kind: Literal["average", "individual", "both"] = "average",
        centered: bool = False,
        subsample: float | int | None = 1000,
        random_state: int | RandomState | None = None,
    ) -> PartialDependenceDisplay: ...
    def _get_sample_count(self, n_samples: int) -> int: ...
    def _plot_ice_lines(
        self,
        preds,
        feature_values,
        n_ice_to_plot,
        ax,
        pd_plot_idx,
        n_total_lines_by_plot,
        individual_line_kw,
    ): ...
    def _plot_average_dependence(
        self,
        avg_preds,
        feature_values,
        ax,
        pd_line_idx,
        line_kw,
    ): ...
    def _plot_one_way_partial_dependence(
        self,
        kind,
        preds,
        avg_preds,
        feature_values,
        feature_idx,
        n_ice_lines,
        ax,
        n_cols,
        pd_plot_idx,
        n_lines,
        ice_lines_kw,
        pd_line_kw,
        pdp_lim,
    ): ...
    def _plot_two_way_partial_dependence(
        self,
        avg_preds,
        feature_values,
        feature_idx,
        ax,
        pd_plot_idx,
        Z_level,
        contour_kw,
    ): ...
    def plot(
        self,
        *,
        ax: Axes | Sequence[Axes] | None = None,
        n_cols: int = 3,
        line_kw: Mapping | None = None,
        ice_lines_kw: Mapping | None = None,
        pd_line_kw: Mapping | None = None,
        contour_kw: Mapping | None = None,
        pdp_lim: Mapping | None = None,
        centered: bool = False,
    ) -> PartialDependenceDisplay: ...
