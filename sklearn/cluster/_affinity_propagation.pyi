from numpy import bool_, ndarray
from typing import Tuple, Union, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort alexandre.gramfort@inria.fr
#        Gael Varoquaux gael.varoquaux@normalesup.org

# License: BSD 3 clause

import numbers
import warnings

import numpy as np
from numpy.random import RandomState

from ..exceptions import ConvergenceWarning
from ..base import BaseEstimator, ClusterMixin
from ..utils import as_float_array, check_random_state
from ..utils import check_scalar
from ..utils.validation import check_is_fitted
from ..metrics import euclidean_distances
from ..metrics import pairwise_distances_argmin
from .._config import config_context

def _equal_similarities_and_preferences(S: ndarray, preference: ndarray) -> bool_: ...
def affinity_propagation(
    S: ArrayLike,
    *,
    preference: ArrayLike | float | None = None,
    convergence_iter: int = 15,
    max_iter: int = 200,
    damping: float = 0.5,
    copy: bool = True,
    verbose: bool = False,
    return_n_iter: bool = False,
    random_state: int | RandomState | None = None,
) -> tuple[np.ndarray, NDArray, int]: ...

###############################################################################

class AffinityPropagation(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        *,
        damping: float = 0.5,
        max_iter: int = 200,
        convergence_iter: int = 15,
        copy: bool = True,
        preference: ArrayLike | float | None = None,
        affinity: Literal["euclidean", "precomputed"] = "euclidean",
        verbose: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _more_tags(self): ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "AffinityPropagation": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def fit_predict(self, X: NDArray | ArrayLike, y=None) -> NDArray: ...
