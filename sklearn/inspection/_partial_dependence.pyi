from sklearn.base import BaseEstimator
from typing import List, Tuple, Union, Literal
from sklearn.utils import Bunch
from numpy.typing import ArrayLike

# Authors: Peter Prettenhofer
#          Trevor Stephens
#          Nicolas Hug
# License: BSD 3 clause

from collections.abc import Iterable

import numpy as np
from scipy import sparse
from scipy.stats.mstats import mquantiles

from ..base import is_classifier, is_regressor
from ..utils.extmath import cartesian
from ..utils import check_array
from ..utils import check_matplotlib_support  # noqa
from ..utils import _safe_indexing
from ..utils import _determine_key_type
from ..utils import _get_column_indices
from ..utils.validation import check_is_fitted
from ..utils import Bunch
from ..tree import DecisionTreeRegressor
from ..ensemble import RandomForestRegressor
from ..exceptions import NotFittedError
from ..ensemble._gb import BaseGradientBoosting
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    BaseHistGradientBoosting,
)
import sklearn.utils._bunch
from numpy import ndarray
from pandas.core.frame import DataFrame
from sklearn.ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from sklearn.pipeline import Pipeline
from sklearn.tree._classes import DecisionTreeRegressor

__all__ = [
    "partial_dependence",
]

def _grid_from_X(
    X: Union[DataFrame, ndarray], percentiles: Tuple[float, float], grid_resolution: int
) -> Tuple[ndarray, List[ndarray]]: ...
def _partial_dependence_recursion(
    est: Union[DecisionTreeRegressor, HistGradientBoostingRegressor],
    grid: ndarray,
    features: ndarray,
) -> ndarray: ...
def _partial_dependence_brute(
    est: Pipeline, grid: ndarray, features: ndarray, X: DataFrame, response_method: str
) -> Tuple[ndarray, ndarray]: ...
def partial_dependence(
    estimator: BaseEstimator,
    X: ArrayLike | DataFrame,
    features: ArrayLike,
    *,
    response_method: Literal["auto", "predict_proba", "decision_function"] = "auto",
    percentiles: tuple[float, ...] = ...,
    grid_resolution: int = 100,
    method: Literal["auto", "recursion", "brute"] = "auto",
    kind: Literal["average", "individual", "both"] = "average",
) -> Bunch: ...
