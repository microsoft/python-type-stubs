from numpy.typing import NDArray

# Author: Florian Wilhelm <florian.wilhelm@gmail.com>
#
# License: BSD 3 clause

import warnings
import numbers
from itertools import combinations

import numpy as np
from scipy import linalg
from scipy.special import binom
from scipy.linalg.lapack import get_lapack_funcs

from ._base import LinearModel
from ..base import RegressorMixin
from ..utils import check_random_state
from ..utils.validation import check_scalar
from ..utils.fixes import delayed
from ..exceptions import ConvergenceWarning
from numpy import ndarray
from numpy.random import RandomState
from typing import Tuple

_EPSILON = ...

def _modified_weiszfeld_step(X: ndarray, x_old: ndarray) -> ndarray: ...
def _spatial_median(X: ndarray, max_iter: int = 300, tol: float = 1.0e-3) -> Tuple[int, ndarray]: ...
def _breakdown_point(n_samples: int, n_subsamples: int) -> float: ...
def _lstsq(X: ndarray, y: ndarray, indices: ndarray, fit_intercept: bool) -> ndarray: ...

class TheilSenRegressor(RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_subpopulation: int | float = 1e4,
        n_subsamples: int | None = None,
        max_iter: int = 300,
        tol: float = 1.0e-3,
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None,
        verbose: bool = False,
    ) -> None: ...
    def _check_subparams(self, n_samples: int, n_features: int) -> Tuple[int, int]: ...
    def fit(self, X: NDArray, y: NDArray) -> "TheilSenRegressor": ...
