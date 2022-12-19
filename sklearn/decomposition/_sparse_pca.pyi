from typing import Literal, Any, Callable
from numpy.typing import NDArray, ArrayLike

# Author: Vlad Niculae, Gael Varoquaux, Alexandre Gramfort
# License: BSD 3 clause

import warnings

import numpy as np
from numpy.random import RandomState

from ..utils import check_random_state
from ..utils.validation import check_is_fitted
from ..linear_model import ridge_regression
from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ._dict_learning import dict_learning, dict_learning_online

class SparsePCA(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        alpha: float = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        tol: float = 1e-8,
        method: Literal["lars", "cd"] = "lars",
        n_jobs: int | None = None,
        U_init: NDArray | None = None,
        V_init: NDArray | None = None,
        verbose: int | bool = False,
        random_state: int | RandomState | None = None,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def transform(self, X: NDArray) -> NDArray: ...
    @property
    def _n_features_out(self): ...
    def _more_tags(self): ...

class MiniBatchSparsePCA(SparsePCA):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        n_iter: int = 100,
        callback: Callable | None = None,
        batch_size: int = 3,
        verbose: int | bool = False,
        shuffle: bool = True,
        n_jobs: int | None = None,
        method: Literal["lars", "cd"] = "lars",
        random_state: int | RandomState | None = None,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
