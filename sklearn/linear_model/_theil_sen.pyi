from typing import Self
from ..utils._param_validation import Interval as Interval
from numpy.random import RandomState
from scipy.special import binom as binom
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Int, Float, ArrayLike
from scipy import linalg as linalg
from ..base import RegressorMixin
from joblib import effective_n_jobs as effective_n_jobs
from ._base import LinearModel
from itertools import combinations as combinations
from ..utils import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs

# Author: Florian Wilhelm <florian.wilhelm@gmail.com>
#
# License: BSD 3 clause


import warnings

import numpy as np

_EPSILON = ...


class TheilSenRegressor(RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_subpopulation: float | Int = 1e4,
        n_subsamples: None | Int = None,
        max_iter: Int = 300,
        tol: Float = 1.0e-3,
        random_state: RandomState | None | Int = None,
        n_jobs: None | Int = None,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(self, X: ArrayLike, y: ArrayLike) -> Self | TheilSenRegressor:
        ...
