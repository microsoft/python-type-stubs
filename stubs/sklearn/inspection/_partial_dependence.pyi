from typing import Literal, Sequence
from ..utils import (
    check_array as check_array,
    check_matplotlib_support as check_matplotlib_support,
)
from ..ensemble import RandomForestRegressor as RandomForestRegressor
from scipy import sparse as sparse
from ..tree import DecisionTreeRegressor as DecisionTreeRegressor
from ..ensemble._gb import BaseGradientBoosting as BaseGradientBoosting
from ..exceptions import NotFittedError as NotFittedError
from ..base import BaseEstimator
from ..utils.extmath import cartesian as cartesian
from ..base import is_classifier as is_classifier, is_regressor as is_regressor
from ..utils._bunch import Bunch
from scipy.stats.mstats import mquantiles as mquantiles
from .._typing import MatrixLike, ArrayLike, Int
from collections.abc import Iterable as Iterable
from ..utils.validation import check_is_fitted as check_is_fitted
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    BaseHistGradientBoosting as BaseHistGradientBoosting,
)

import numpy as np


__all__ = [
    "partial_dependence",
]


def partial_dependence(
    estimator: BaseEstimator,
    X: MatrixLike,
    features: tuple[int]
    | Sequence[tuple[int, str]]
    | tuple[str, str]
    | tuple[int, int],
    *,
    categorical_features: None | MatrixLike | ArrayLike = None,
    feature_names: None | ArrayLike = None,
    response_method: Literal[
        "auto", "predict_proba", "decision_function", "auto"
    ] = "auto",
    percentiles: tuple[float, ...] = ...,
    grid_resolution: Int = 100,
    method: Literal["auto", "recursion", "brute", "auto"] = "auto",
    kind: Literal["average", "individual", "both", "average"] = "average",
) -> Bunch:
    ...
