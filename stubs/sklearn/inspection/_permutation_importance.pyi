import numbers
from typing import Any, Callable, Mapping

import numpy as np
from numpy.random import RandomState

from .._typing import ArrayLike, Int, MatrixLike
from ..metrics import check_scoring as check_scoring
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils._bunch import Bunch
from ..utils.parallel import Parallel as Parallel, delayed as delayed

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
    max_samples: float = 1.0,
) -> Bunch | dict[str, Bunch]: ...
