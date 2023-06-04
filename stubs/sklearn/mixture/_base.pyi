from typing import Any, ClassVar, TypeVar
from ..utils import check_random_state as check_random_state
from scipy.special import logsumexp as logsumexp
from abc import ABCMeta, abstractmethod as abstractmethod
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from numpy import ndarray
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from numpy.random.mtrand import RandomState
from ..base import BaseEstimator, DensityMixin
from ..cluster import kmeans_plusplus as kmeans_plusplus
from time import time as time
from .._typing import MatrixLike, Float, Int
from .. import cluster as cluster
from ..utils.validation import check_is_fitted as check_is_fitted

BaseMixture_Self = TypeVar("BaseMixture_Self", bound="BaseMixture")


# Author: Wei Xue <xuewei4d@gmail.com>
# Modified by Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import warnings

import numpy as np


class BaseMixture(DensityMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: int,
        tol: float,
        reg_covar: float | int,
        max_iter: int,
        n_init: int,
        init_params: str,
        random_state: None | RandomState | int,
        warm_start: bool,
        verbose: int,
        verbose_interval: int,
    ) -> None:
        ...

    def fit(self: BaseMixture_Self, X: MatrixLike, y: Any = None) -> BaseMixture_Self:
        ...

    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...

    def score_samples(self, X: MatrixLike) -> ndarray:
        ...

    def score(self, X: MatrixLike, y: Any = None) -> Float:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def sample(self, n_samples: Int = 1) -> tuple[ndarray, ndarray]:
        ...
