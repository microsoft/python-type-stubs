from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms
from ._kd_tree import KDTree as KDTree
from ..neighbors._base import VALID_METRICS as VALID_METRICS
from scipy.special import gammainc as gammainc
from .._typing import Float, Int, MatrixLike, ArrayLike
from numpy.random import RandomState
from ..base import BaseEstimator
from ._ball_tree import BallTree as BallTree, DTYPE as DTYPE
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real

# Author: Jake Vanderplas <jakevdp@cs.washington.edu>
import itertools

import numpy as np


VALID_KERNELS: list = ...

TREE_DICT: dict = ...


# TODO: implement a brute force version for testing purposes
# TODO: create a density estimation base class?
class KernelDensity(BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        bandwidth: float | Literal["scott", "silverman"] = 1.0,
        algorithm: Literal["kd_tree", "ball_tree", "auto", "auto"] = "auto",
        kernel: Literal[
            "gaussian",
            "tophat",
            "epanechnikov",
            "exponential",
            "linear",
            "cosine",
            "gaussian",
        ] = "gaussian",
        metric: str = "euclidean",
        atol: Float = 0,
        rtol: Float = 0,
        breadth_first: bool = True,
        leaf_size: Int = 40,
        metric_params: dict | None = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y=None, sample_weight: None | ArrayLike = None) -> Any:
        ...

    def score_samples(self, X: MatrixLike) -> ndarray:
        ...

    def score(self, X: MatrixLike, y=None) -> Float:
        ...

    def sample(
        self, n_samples: Int = 1, random_state: RandomState | None | Int = None
    ) -> ndarray:
        ...
