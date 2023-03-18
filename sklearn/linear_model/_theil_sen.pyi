from typing import ClassVar, TypeVar
from numpy.random import RandomState
from scipy.special import binom as binom
from scipy import linalg as linalg
from itertools import combinations as combinations
from ._base import LinearModel
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils._param_validation import Interval as Interval
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from scipy.linalg.lapack import get_lapack_funcs as get_lapack_funcs
from joblib import effective_n_jobs as effective_n_jobs
from ..base import RegressorMixin
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import Int, Float, ArrayLike
from ..utils import check_random_state as check_random_state

TheilSenRegressor_Self = TypeVar("TheilSenRegressor_Self", bound="TheilSenRegressor")


# Author: Florian Wilhelm <florian.wilhelm@gmail.com>
#
# License: BSD 3 clause


import warnings

import numpy as np

_EPSILON = ...


class TheilSenRegressor(RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_subpopulation_: int = ...
    n_iter_: int = ...
    breakdown_: float = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: TheilSenRegressor_Self, X: ArrayLike, y: ArrayLike
    ) -> TheilSenRegressor_Self:
        ...
