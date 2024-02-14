import warnings
from numbers import Integral as Integral, Real as Real
from time import time as time
from typing import Callable, ClassVar, Literal

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg
from scipy.sparse import csr_matrix as csr_matrix, issparse as issparse
from scipy.spatial.distance import pdist as pdist, squareform as squareform

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator
from ..decomposition import PCA as PCA
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_non_negative as check_non_negative

# Author: Alexander Fabisch  -- <afabisch@informatik.uni-bremen.de>
# Author: Christopher Moody <chrisemoody@gmail.com>
# Author: Nick Travers <nickt@squareup.com>
# License: BSD 3 clause (C) 2014

# This is the exact and Barnes-Hut t-SNE implementation. There are other
# modifications of the algorithm:
# * Fast Optimization for t-SNE:
#   https://cseweb.ucsd.edu/~lvdmaaten/workshops/nips2010/papers/vandermaaten.pdf

MACHINE_EPSILON = ...

def trustworthiness(
    X: MatrixLike,
    X_embedded: MatrixLike,
    *,
    n_neighbors: Int = 5,
    metric: str | Callable = "euclidean",
) -> float: ...

class TSNE(BaseEstimator):
    n_iter_: int = ...
    learning_rate_: float = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    kl_divergence_: float = ...
    embedding_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    # Control the number of exploration iterations with early_exaggeration on
    _EXPLORATION_N_ITER: ClassVar[int] = ...

    # Control the number of iterations between progress checks
    _N_ITER_CHECK: ClassVar[int] = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        perplexity: Float = 30.0,
        early_exaggeration: Float = 12.0,
        learning_rate: float | Literal["auto", "auto"] = "auto",
        n_iter: Int = 1000,
        n_iter_without_progress: Int = 300,
        min_grad_norm: Float = 1e-7,
        metric: str | Callable = "euclidean",
        metric_params: None | dict = None,
        init: MatrixLike | Literal["random", "pca", "pca"] = "pca",
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        method: Literal["barnes_hut", "exact", "barnes_hut"] = "barnes_hut",
        angle: Float = 0.5,
        n_jobs: None | Int = None,
        square_distances: str | bool = "deprecated",
    ) -> None: ...
    def fit_transform(self, X: MatrixLike, y: None | ndarray = None) -> ndarray: ...
    def fit(self, X: MatrixLike, y=None) -> ndarray: ...
