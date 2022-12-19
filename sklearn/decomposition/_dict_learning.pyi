from numpy import float64, ndarray
from typing import Optional, Union, Literal, Callable, Any
from numpy.typing import NDArray, ArrayLike

# Author: Vlad Niculae, Gael Varoquaux, Alexandre Gramfort
# License: BSD 3 clause

import time
import sys
import itertools
import warnings

from math import ceil

import numpy as np
from scipy import linalg

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils import check_array, check_random_state, gen_even_slices, gen_batches
from ..utils import deprecated
from ..utils.extmath import randomized_svd, row_norms, svd_flip
from ..utils.validation import check_is_fitted
from ..utils.validation import check_scalar
from ..utils.fixes import delayed
from ..linear_model import Lasso, orthogonal_mp_gram, LassoLars, Lars
from numpy.random import RandomState

def _check_positive_coding(method: str, positive: bool) -> None: ...
def _sparse_encode(
    X: ndarray,
    dictionary: ndarray,
    gram: Optional[ndarray],
    cov: Optional[ndarray] = None,
    algorithm: str = "lasso_lars",
    regularization: Optional[Union[int, float]] = None,
    copy_cov: bool = True,
    init: None = None,
    max_iter: int = 1000,
    check_input: bool = True,
    verbose: Union[int, bool] = 0,
    positive: bool = False,
) -> ndarray: ...

# XXX : could be moved to the linear_model module
def sparse_encode(
    X: NDArray,
    dictionary: NDArray,
    *,
    gram: NDArray | None = None,
    cov: NDArray | None = None,
    algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold"] = "lasso_lars",
    n_nonzero_coefs: int | None = None,
    alpha: float | None = None,
    copy_cov: bool = True,
    init: NDArray | None = None,
    max_iter: int = 1000,
    n_jobs: int | None = None,
    check_input: bool = True,
    verbose: int = 0,
    positive: bool = False,
) -> NDArray: ...
def _update_dict(
    dictionary: ndarray,
    Y: ndarray,
    code: ndarray,
    A: Optional[ndarray] = None,
    B: Optional[ndarray] = None,
    verbose: bool = False,
    random_state: Optional[RandomState] = None,
    positive: bool = False,
) -> None: ...
def dict_learning(
    X: NDArray,
    n_components: int,
    *,
    alpha: int,
    max_iter: int = 100,
    tol: float = 1e-8,
    method: Literal["lars", "cd"] = "lars",
    n_jobs: int | None = None,
    dict_init: NDArray | None = None,
    code_init: NDArray | None = None,
    callback: Callable | None = None,
    verbose: bool = False,
    random_state: int | RandomState | None = None,
    return_n_iter: bool = False,
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: int = 1000,
) -> tuple[NDArray, NDArray, ArrayLike, int]: ...
def _check_warn_deprecated(param, name, default, additional_message=None): ...
def dict_learning_online(
    X: NDArray,
    n_components: int | None = 2,
    *,
    alpha: float = 1,
    n_iter: int | str = "deprecated",
    max_iter: int | None = None,
    return_code: bool = True,
    dict_init: NDArray | None = None,
    callback: Callable | None = None,
    batch_size: int | str = "warn",
    verbose: bool = False,
    shuffle: bool = True,
    n_jobs: int | None = None,
    method: Literal["lars", "cd"] = "lars",
    iter_offset: int | str = "deprecated",
    random_state: int | RandomState | None = None,
    return_inner_stats: bool | str = "deprecated",
    inner_stats: tuple[NDArray, ...] | str = "deprecated",
    return_n_iter: bool | str = "deprecated",
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: int = 1000,
    tol: float = 1e-3,
    max_no_improvement: int = 10,
) -> tuple[NDArray, NDArray, int]: ...

class _BaseSparseCoding(_ClassNamePrefixFeaturesOutMixin, TransformerMixin):
    def __init__(
        self,
        transform_algorithm: str,
        transform_n_nonzero_coefs: Optional[int],
        transform_alpha: Optional[int],
        split_sign: bool,
        n_jobs: None,
        positive_code: bool,
        transform_max_iter: int,
    ) -> None: ...
    def _transform(self, X: ndarray, dictionary: ndarray) -> ndarray: ...
    def transform(self, X: NDArray) -> NDArray: ...

class SparseCoder(_BaseSparseCoding, BaseEstimator):

    _required_parameters: list = ...

    def __init__(
        self,
        dictionary: NDArray,
        *,
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold"] = "omp",
        transform_n_nonzero_coefs: int | None = None,
        transform_alpha: float | None = None,
        split_sign: bool = False,
        n_jobs: int | None = None,
        positive_code: bool = False,
        transform_max_iter: int = 1000,
    ) -> None: ...
    def fit(self, X, y=None) -> Any: ...
    def transform(self, X: NDArray, y: None = None) -> NDArray: ...
    def _more_tags(self): ...
    @property
    def n_components_(self): ...
    @property
    def n_features_in_(self) -> int: ...
    @property
    def _n_features_out(self): ...

class DictionaryLearning(_BaseSparseCoding, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        alpha: float = 1,
        max_iter: int = 1000,
        tol: float = 1e-8,
        fit_algorithm: Literal["lars", "cd"] = "lars",
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold"] = "omp",
        transform_n_nonzero_coefs: int | None = None,
        transform_alpha: float | None = None,
        n_jobs: int | None = None,
        code_init: NDArray | None = None,
        dict_init: NDArray | None = None,
        verbose: bool = False,
        split_sign: bool = False,
        random_state: int | RandomState | None = None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: int = 1000,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    @property
    def _n_features_out(self): ...
    def _more_tags(self): ...

class MiniBatchDictionaryLearning(_BaseSparseCoding, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        alpha: float = 1,
        n_iter: int | str = "deprecated",
        max_iter: int | None = None,
        fit_algorithm: Literal["lars", "cd"] = "lars",
        n_jobs: int | None = None,
        batch_size: int | str = "warn",
        shuffle: bool = True,
        dict_init: NDArray | None = None,
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold"] = "omp",
        transform_n_nonzero_coefs: int | None = None,
        transform_alpha: float | None = None,
        verbose: bool | int = False,
        split_sign: bool = False,
        random_state: int | RandomState | None = None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: int = 1000,
        callback: Callable | None = None,
        tol: float = 1e-3,
        max_no_improvement: int = 10,
    ) -> None: ...
    @deprecated("The attribute `iter_offset_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def iter_offset_(self): ...
    @deprecated("The attribute `random_state_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def random_state_(self): ...
    @deprecated("The attribute `inner_stats_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def inner_stats_(self): ...
    def _check_params(self, X: ndarray) -> None: ...
    def _initialize_dict(self, X: ndarray, random_state: RandomState) -> ndarray: ...
    def _update_inner_stats(self, X: ndarray, code: ndarray, batch_size: int, step: int) -> None: ...
    def _minibatch_step(self, X: ndarray, dictionary: ndarray, random_state: RandomState, step: int) -> float64: ...
    def _check_convergence(
        self,
        X: ndarray,
        batch_cost: float64,
        new_dict: ndarray,
        old_dict: ndarray,
        n_samples: int,
        step: int,
        n_steps: int,
    ) -> bool: ...
    def fit(self, X: ArrayLike, y: None = None) -> "MiniBatchDictionaryLearning": ...
    def partial_fit(self, X: ArrayLike, y=None, iter_offset: int | str = "deprecated") -> Any: ...
    @property
    def _n_features_out(self): ...
    def _more_tags(self): ...
