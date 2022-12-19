from sklearn.utils._bunch import Bunch
from typing import Union, Any, Callable, Mapping
from numpy.typing import NDArray, ArrayLike
import numbers
import numpy as np
from numpy.random import RandomState
from pandas import DataFrame

from ..ensemble._bagging import _generate_indices
from ..metrics import check_scoring
from ..metrics._scorer import _check_multimetric_scoring, _MultimetricScorer
from ..model_selection._validation import _aggregate_score_dicts
from ..utils import Bunch, _safe_indexing
from ..utils import check_random_state
from ..utils import check_array
from ..utils.fixes import delayed
from numpy import float64, ndarray
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.ensemble._gb import GradientBoostingRegressor

def _weights_scorer(
    scorer: Callable,
    estimator: Union[RandomForestClassifier, GradientBoostingRegressor],
    X: ndarray,
    y: ndarray,
    sample_weight: None,
) -> float64: ...
def _calculate_permutation_scores(
    estimator: RandomForestClassifier,
    X: ndarray,
    y: ndarray,
    sample_weight: None,
    col_idx: int,
    random_state: int,
    n_repeats: int,
    scorer: Callable,
    max_samples: int,
) -> ndarray: ...
def _create_importances_bunch(baseline_score: float64, permuted_score: ndarray) -> Bunch: ...
def permutation_importance(
    estimator: Union[RandomForestClassifier, GradientBoostingRegressor],
    X: NDArray | DataFrame,
    y: ArrayLike | None,
    *,
    scoring: str | Callable | ArrayLike | tuple | Mapping | None = None,
    n_repeats: int = 5,
    n_jobs: int | None = None,
    random_state: int | RandomState | None = None,
    sample_weight: ArrayLike | None = None,
    max_samples: int | float = 1.0,
) -> Bunch | dict[str, Bunch]: ...
