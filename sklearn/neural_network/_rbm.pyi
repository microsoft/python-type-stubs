from sklearn.neural_network._rbm import BernoulliRBM
from numpy.typing import ArrayLike, NDArray

# Authors: Yann N. Dauphin <dauphiya@iro.umontreal.ca>
#          Vlad Niculae
#          Gabriel Synnaeve
#          Lars Buitinck
# License: BSD 3 clause

import time

import numpy as np
import scipy.sparse as sp
from scipy.special import expit  # logistic function

from ..base import BaseEstimator
from ..base import TransformerMixin
from ..base import _ClassNamePrefixFeaturesOutMixin
from ..utils import check_random_state
from ..utils import gen_even_slices
from ..utils.extmath import safe_sparse_dot
from ..utils.extmath import log_logistic
from ..utils.validation import check_is_fitted
from numpy import ndarray
from numpy.random import RandomState
from typing import Optional

class BernoulliRBM(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int = 256,
        *,
        learning_rate: float = 0.1,
        batch_size: int = 10,
        n_iter: int = 10,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _mean_hiddens(self, v: ndarray) -> ndarray: ...
    def _sample_hiddens(self, v, rng): ...
    def _sample_visibles(self, h: ndarray, rng: RandomState) -> ndarray: ...
    def _free_energy(self, v: ndarray) -> ndarray: ...
    def gibbs(self, v: NDArray) -> NDArray: ...
    def partial_fit(self, X: NDArray, y: ArrayLike | None = None) -> BernoulliRBM: ...
    def _fit(self, v_pos: ndarray, rng: RandomState) -> None: ...
    def score_samples(self, X: NDArray | ArrayLike) -> NDArray: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike | None = None) -> BernoulliRBM: ...
    def _more_tags(self): ...
