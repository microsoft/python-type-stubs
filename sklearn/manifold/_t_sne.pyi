from typing import Dict, List, Optional, Tuple, Union, Callable, Literal, Mapping
from numpy.typing import NDArray

# Author: Alexander Fabisch  -- <afabisch@informatik.uni-bremen.de>
# Author: Christopher Moody <chrisemoody@gmail.com>
# Author: Nick Travers <nickt@squareup.com>
# License: BSD 3 clause (C) 2014

# This is the exact and Barnes-Hut t-SNE implementation. There are other
# modifications of the algorithm:
# * Fast Optimization for t-SNE:
#   https://cseweb.ucsd.edu/~lvdmaaten/workshops/nips2010/papers/vandermaaten.pdf

import warnings
from time import time
import numpy as np
from numpy.random import RandomState
from scipy import linalg
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from scipy.sparse import csr_matrix, issparse
from ..neighbors import NearestNeighbors
from ..base import BaseEstimator
from ..utils import check_random_state

from ..utils.validation import check_non_negative
from ..decomposition import PCA
from ..metrics.pairwise import pairwise_distances

# mypy error: Module 'sklearn.manifold' has no attribute '_utils'
from . import _utils  # type: ignore

# mypy error: Module 'sklearn.manifold' has no attribute '_barnes_hut_tsne'
from . import _barnes_hut_tsne  # type: ignore
import scipy.sparse._csr
from numpy import float64, ndarray

MACHINE_EPSILON = ...

def _joint_probabilities(distances, desired_perplexity, verbose): ...
def _joint_probabilities_nn(
    distances: scipy.sparse._csr.csr_matrix, desired_perplexity: int, verbose: int
) -> scipy.sparse._csr.csr_matrix: ...
def _kl_divergence(
    params,
    P,
    degrees_of_freedom,
    n_samples,
    n_components,
    skip_num_points=0,
    compute_error=True,
): ...
def _kl_divergence_bh(
    params: ndarray,
    P: scipy.sparse._csr.csr_matrix,
    degrees_of_freedom: int,
    n_samples: int,
    n_components: int,
    angle: float = 0.5,
    skip_num_points: int = 0,
    verbose: int = False,
    compute_error: bool = True,
    num_threads: int = 1,
) -> Tuple[float, ndarray]: ...
def _gradient_descent(
    objective: Callable,
    p0: ndarray,
    it: int,
    n_iter: int,
    n_iter_check: int = 1,
    n_iter_without_progress: int = 300,
    momentum: float = 0.8,
    learning_rate: Union[float, float64] = 200.0,
    min_gain: float = 0.01,
    min_grad_norm: float = 1e-7,
    verbose: int = 0,
    args: Optional[List[Union[scipy.sparse._csr.csr_matrix, int]]] = None,
    kwargs: Optional[Dict[str, Union[int, float, bool]]] = None,
) -> Tuple[ndarray, float, int]: ...
def trustworthiness(
    X: NDArray,
    X_embedded: NDArray,
    *,
    n_neighbors: int = 5,
    metric: str | Callable = "euclidean",
) -> float: ...

class TSNE(BaseEstimator):

    # Control the number of exploration iterations with early_exaggeration on
    _EXPLORATION_N_ITER: int = ...

    # Control the number of iterations between progress checks
    _N_ITER_CHECK: int = ...

    def __init__(
        self,
        n_components: int = 2,
        *,
        perplexity: float = 30.0,
        early_exaggeration: float = 12.0,
        learning_rate: float | str = "warn",
        n_iter: int = 1000,
        n_iter_without_progress: int = 300,
        min_grad_norm: float = 1e-7,
        metric: str | Callable = "euclidean",
        metric_params: Mapping | None = None,
        init: Literal["random", "pca", "warn"] | NDArray = "warn",
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        method: str = "barnes_hut",
        angle: float = 0.5,
        n_jobs: int | None = None,
        square_distances: Literal[True] | str = "deprecated",
    ) -> None: ...
    def _check_params_vs_input(self, X: ndarray) -> None: ...
    def _fit(self, X: ndarray, skip_num_points: int = 0) -> ndarray: ...
    def _tsne(
        self,
        P: scipy.sparse._csr.csr_matrix,
        degrees_of_freedom: int,
        n_samples: int,
        X_embedded: ndarray,
        neighbors: None = None,
        skip_num_points: int = 0,
    ) -> ndarray: ...
    def fit_transform(self, X: NDArray, y: None = None) -> NDArray: ...
    def fit(self, X: NDArray, y=None) -> NDArray: ...
    def _more_tags(self): ...
