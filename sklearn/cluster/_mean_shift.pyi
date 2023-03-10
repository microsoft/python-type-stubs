from typing import Any
from ..utils._param_validation import Interval as Interval
from numpy.random import RandomState
from .._typing import MatrixLike, Float, Int
from ..base import BaseEstimator, ClusterMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils.validation import check_is_fitted as check_is_fitted
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from collections import defaultdict as defaultdict
from numpy import ndarray
from ..utils import (
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    check_array as check_array,
)
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from numbers import Integral as Integral, Real as Real
from .._config import config_context as config_context

# Authors: Conrad Lee <conradlee@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Martino Sorbaro <martino.sorbaro@ed.ac.uk>

import numpy as np
import warnings


def estimate_bandwidth(
    X: MatrixLike,
    *,
    quantile: Float = 0.3,
    n_samples: None | Int = None,
    random_state: RandomState | Int = 0,
    n_jobs: None | Int = None,
) -> Float:
    ...


def mean_shift(
    X: MatrixLike,
    *,
    bandwidth: None | Float = None,
    seeds: None | MatrixLike = None,
    bin_seeding: bool = False,
    min_bin_freq: Int = 1,
    cluster_all: bool = True,
    max_iter: Int = 300,
    n_jobs: None | Int = None,
) -> tuple[ndarray, ndarray]:
    ...


def get_bin_seeds(X: MatrixLike, bin_size: Float, min_bin_freq: Int = 1) -> ndarray:
    ...


class MeanShift(ClusterMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        bandwidth: None | Float = None,
        seeds: None | MatrixLike = None,
        bin_seeding: bool = False,
        min_bin_freq: Int = 1,
        cluster_all: bool = True,
        n_jobs: None | Int = None,
        max_iter: Int = 300,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...
