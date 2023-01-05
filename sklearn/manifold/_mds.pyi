from typing import Literal, Any
from numpy.typing import NDArray, ArrayLike

# author: Nelle Varoquaux <nelle.varoquaux@gmail.com>
# License: BSD

import numpy as np
from numpy.random import RandomState

import warnings

from ..base import BaseEstimator
from ..metrics import euclidean_distances
from ..utils import check_random_state, check_array, check_symmetric
from ..isotonic import IsotonicRegression
from ..utils.fixes import delayed

def _smacof_single(
    dissimilarities,
    metric=True,
    n_components=2,
    init=None,
    max_iter=300,
    verbose=0,
    eps=1e-3,
    random_state=None,
): ...
def smacof(
    dissimilarities: NDArray,
    *,
    metric: bool = True,
    n_components: int = 2,
    init: NDArray | None = None,
    n_init: int = 8,
    n_jobs: int | None = None,
    max_iter: int = 300,
    verbose: int = 0,
    eps: float = 1e-3,
    random_state: int | RandomState | None = None,
    return_n_iter: bool = False,
) -> tuple[NDArray, float, int]: ...

class MDS(BaseEstimator):
    def __init__(
        self,
        n_components: int = 2,
        *,
        metric: bool = True,
        n_init: int = 4,
        max_iter: int = 300,
        verbose: int = 0,
        eps: float = 1e-3,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        dissimilarity: Literal["euclidean", "precomputed"] = "euclidean",
    ): ...
    def _more_tags(self): ...
    def fit(self, X: ArrayLike, y=None, init: NDArray | None = None) -> Any: ...
    def fit_transform(self, X: ArrayLike, y=None, init: NDArray | None = None) -> NDArray: ...
