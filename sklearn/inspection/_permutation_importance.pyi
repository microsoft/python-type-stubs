from typing import Any, Callable, Mapping
from numpy.random import RandomState
from ..utils import check_random_state as check_random_state, check_array as check_array
from ..utils._bunch import Bunch
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import MatrixLike, ArrayLike, Int
from ..metrics import check_scoring as check_scoring
import numbers
import numpy as np


def permutation_importance(
    estimator: Any,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike,
    *,
    scoring: ArrayLike | None | tuple | Callable | Mapping | str = None,
    n_repeats: Int = 5,
    n_jobs: None | int = None,
    random_state: RandomState | None | Int = None,
    sample_weight: None | ArrayLike = None,
    max_samples: float | int = 1.0,
) -> Bunch | dict[str, Bunch]:
    ...
