from typing import Literal, Mapping, Any
from numpy.typing import ArrayLike, NDArray

# Author: Jake Vanderplas <jakevdp@cs.washington.edu>

import numpy as np
from scipy.special import gammainc
from ..base import BaseEstimator
from ..utils import check_random_state
from ..utils.validation import _check_sample_weight, check_is_fitted

from ..utils.extmath import row_norms
from numpy import ndarray
from numpy.random import RandomState

VALID_KERNELS: list = ...
TREE_DICT: dict = ...

# TODO: implement a brute force version for testing purposes
# TODO: bandwidth estimation
# TODO: create a density estimation base class?
class KernelDensity(BaseEstimator):
    def __init__(
        self,
        *,
        bandwidth: float = 1.0,
        algorithm: Literal["kd_tree", "ball_tree", "auto"] = "auto",
        kernel: Literal["gaussian", "tophat", "epanechnikov", "exponential", "linear", "cosine"] = "gaussian",
        metric: str = "euclidean",
        atol: float = 0,
        rtol: float = 0,
        breadth_first: bool = True,
        leaf_size: int = 40,
        metric_params: Mapping | None = None,
    ) -> None: ...
    def _choose_algorithm(self, algorithm: str, metric: str) -> str: ...
    def fit(self, X: ArrayLike, y: None = None, sample_weight: ArrayLike | None = None) -> "KernelDensity": ...
    def score_samples(self, X: ArrayLike) -> NDArray: ...
    def score(self, X: ArrayLike, y=None) -> float: ...
    def sample(self, n_samples: int = 1, random_state: int | RandomState | None = None) -> ArrayLike: ...
    def _more_tags(self): ...
