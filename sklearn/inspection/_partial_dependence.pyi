from typing import Literal, Sequence
from ..utils.extmath import cartesian as cartesian
from collections.abc import Iterable as Iterable
from ..utils._bunch import Bunch
from ..exceptions import NotFittedError as NotFittedError
from .._typing import Estimator, MatrixLike, ArrayLike, Int
from scipy import sparse as sparse
from ..base import is_classifier as is_classifier, is_regressor as is_regressor
from scipy.stats.mstats import mquantiles as mquantiles
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    BaseHistGradientBoosting as BaseHistGradientBoosting,
)
from ..utils.validation import check_is_fitted as check_is_fitted
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from ..ensemble._gb import BaseGradientBoosting as BaseGradientBoosting
from ..utils import (
    check_array as check_array,
    check_matplotlib_support as check_matplotlib_support,
)
from ..ensemble import RandomForestRegressor as RandomForestRegressor
from ..pipeline import Pipeline
from ..tree._classes import DecisionTreeRegressor

import numpy as np


__all__ = [
    "partial_dependence",
]


def partial_dependence(
    estimator: Pipeline
    | Estimator
    | HistGradientBoostingRegressor
    | DecisionTreeRegressor,
    X: MatrixLike,
    features: tuple[int, int]
    | Sequence[tuple[int, str]]
    | tuple[str, str]
    | tuple[int],
    *,
    categorical_features: None | MatrixLike | ArrayLike = None,
    feature_names: None | ArrayLike = None,
    response_method: Literal[
        "auto", "predict_proba", "decision_function", "auto"
    ] = "auto",
    percentiles=...,
    grid_resolution: Int = 100,
    method: Literal["auto", "recursion", "brute", "auto"] = "auto",
    kind: Literal["average", "individual", "both", "average"] = "average",
) -> Bunch:
    ...
