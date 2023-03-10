from typing import Literal, Mapping, Sequence
from ...base import is_regressor as is_regressor
from matplotlib.gridspec import GridSpecFromSubplotSpec as GridSpecFromSubplotSpec
from ...utils._bunch import Bunch
from numpy.random import RandomState
from ..._typing import Int, ArrayLike, Estimator, MatrixLike
from math import ceil as ceil
from scipy import sparse as sparse
from scipy.stats.mstats import mquantiles as mquantiles
from ...utils.parallel import delayed as delayed, Parallel as Parallel
from matplotlib.axes import Axes
from ...utils import (
    check_array as check_array,
    check_matplotlib_support as check_matplotlib_support,
    check_random_state as check_random_state,
)
from itertools import chain as chain
from .. import partial_dependence as partial_dependence
import numbers
import warnings

import numpy as np


class PartialDependenceDisplay:
    def __init__(
        self,
        pd_results: list[Bunch] | Sequence[Bunch],
        *,
        features: Sequence[int] | Sequence[tuple[int, int]],
        feature_names: Sequence[str],
        target_idx: Int,
        deciles: dict,
        pdp_lim: str | Mapping | None = "deprecated",
        kind: Literal["average", "individual", "both", "average"]
        | Sequence[Literal["average", "individual", "both"]] = "average",
        subsample: int | float | None = 1000,
        random_state: RandomState | None | Int = None,
        is_categorical: None | ArrayLike = None,
    ) -> None:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Estimator,
        X: MatrixLike,
        features: Sequence[int | str | Sequence[int | str]]
        | list[str | tuple[str, str] | int],
        *,
        categorical_features: None | MatrixLike | ArrayLike = None,
        feature_names: None | ArrayLike = None,
        target: None | Int = None,
        response_method: Literal[
            "auto", "predict_proba", "decision_function", "auto"
        ] = "auto",
        n_cols: Int = 3,
        grid_resolution: Int = 100,
        percentiles=...,
        method: str = "auto",
        n_jobs: None | Int = None,
        verbose: Int = 0,
        line_kw: dict | None = None,
        ice_lines_kw: dict | None = None,
        pd_line_kw: dict | None = None,
        contour_kw: dict | None = None,
        ax: Axes | None | Sequence[Axes] = None,
        kind: Literal["average", "individual", "both", "average"] = "average",
        centered: bool = False,
        subsample: int | float | None = 1000,
        random_state: RandomState | None | Int = None,
    ) -> PartialDependenceDisplay:
        ...

    def plot(
        self,
        *,
        ax: Axes | None | Sequence[Axes] = None,
        n_cols: Int = 3,
        line_kw: dict | None = None,
        ice_lines_kw: dict | None = None,
        pd_line_kw: dict | None = None,
        contour_kw: dict | None = None,
        bar_kw: dict | None = None,
        heatmap_kw: dict | None = None,
        pdp_lim: dict | None = None,
        centered: bool = False,
    ) -> PartialDependenceDisplay:
        ...
