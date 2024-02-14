from math import ceil as ceil
from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..linear_model import Lars as Lars, Lasso as Lasso, LassoLars as LassoLars, orthogonal_mp_gram as orthogonal_mp_gram
from ..utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    deprecated,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import randomized_svd as randomized_svd, row_norms as row_norms, svd_flip as svd_flip
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted

DictionaryLearning_Self = TypeVar("DictionaryLearning_Self", bound="DictionaryLearning")
SparseCoder_Self = TypeVar("SparseCoder_Self", bound="SparseCoder")
MiniBatchDictionaryLearning_Self = TypeVar("MiniBatchDictionaryLearning_Self", bound="MiniBatchDictionaryLearning")

# Author: Vlad Niculae, Gael Varoquaux, Alexandre Gramfort
# License: BSD 3 clause

import itertools
import sys
import time
import warnings

import numpy as np

# XXX : could be moved to the linear_model module
def sparse_encode(
    X: ArrayLike,
    dictionary: MatrixLike,
    *,
    gram: None | MatrixLike = None,
    cov: None | MatrixLike = None,
    algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold", "lasso_lars"] = "lasso_lars",
    n_nonzero_coefs: None | Int = None,
    alpha: None | Float = None,
    copy_cov: bool = True,
    init: None | MatrixLike = None,
    max_iter: Int = 1000,
    n_jobs: None | Int = None,
    check_input: bool = True,
    verbose: Int = 0,
    positive: bool = False,
) -> ndarray: ...
def dict_learning(
    X: ArrayLike,
    n_components: Int,
    *,
    alpha: Int,
    max_iter: Int = 100,
    tol: Float = 1e-8,
    method: Literal["lars", "cd", "lars"] = "lars",
    n_jobs: None | Int = None,
    dict_init: None | MatrixLike = None,
    code_init: None | MatrixLike = None,
    callback: None | Callable = None,
    verbose: bool = False,
    random_state: RandomState | None | Int = None,
    return_n_iter: bool = False,
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: Int = 1000,
) -> tuple[ndarray, ndarray, ndarray, int]: ...
def dict_learning_online(
    X: ArrayLike,
    n_components: None | int = 2,
    *,
    alpha: Float = 1,
    n_iter: str | Int = "deprecated",
    max_iter: None | Int = None,
    return_code: bool = True,
    dict_init: None | MatrixLike = None,
    callback: None | Callable = None,
    batch_size: str | Int = "warn",
    verbose: bool = False,
    shuffle: bool = True,
    n_jobs: None | Int = None,
    method: Literal["lars", "cd", "lars"] = "lars",
    iter_offset: str | Int = "deprecated",
    random_state: RandomState | None | Int = None,
    return_inner_stats: str | bool = "deprecated",
    inner_stats: str | tuple[ArrayLike, ArrayLike] = "deprecated",
    return_n_iter: str | bool = "deprecated",
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: Int = 1000,
    tol: Float = 1e-3,
    max_no_improvement: Int = 10,
) -> tuple[ndarray, ndarray, int]: ...

class _BaseSparseCoding(ClassNamePrefixFeaturesOutMixin, TransformerMixin):
    def __init__(
        self,
        transform_algorithm: str,
        transform_n_nonzero_coefs: None | int,
        transform_alpha: float | None | int,
        split_sign: bool,
        n_jobs,
        positive_code: bool,
        transform_max_iter: int,
    ) -> None: ...
    def transform(self, X: ArrayLike) -> ndarray: ...

class SparseCoder(_BaseSparseCoding, BaseEstimator):
    feature_names_in_: ndarray = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        dictionary: MatrixLike,
        *,
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold", "omp"] = "omp",
        transform_n_nonzero_coefs: None | Int = None,
        transform_alpha: None | Float = None,
        split_sign: bool = False,
        n_jobs: None | Int = None,
        positive_code: bool = False,
        transform_max_iter: Int = 1000,
    ) -> None: ...
    def fit(self: SparseCoder_Self, X: Any, y: Any = None) -> SparseCoder_Self: ...
    def transform(self, X: ArrayLike, y: Any = None) -> ndarray: ...
    @property
    def n_components_(self) -> int: ...
    @property
    def n_features_in_(self) -> int: ...

class DictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    error_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        alpha: Float = 1,
        max_iter: Int = 1000,
        tol: Float = 1e-8,
        fit_algorithm: Literal["lars", "cd", "lars"] = "lars",
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold", "omp"] = "omp",
        transform_n_nonzero_coefs: None | Int = None,
        transform_alpha: None | Float = None,
        n_jobs: None | int = None,
        code_init: None | MatrixLike = None,
        dict_init: None | MatrixLike = None,
        verbose: bool = False,
        split_sign: bool = False,
        random_state: RandomState | None | Int = None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: Int = 1000,
    ) -> None: ...
    def fit(self: DictionaryLearning_Self, X: MatrixLike, y: Any = None) -> DictionaryLearning_Self: ...

class MiniBatchDictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_steps_: int = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        alpha: Float = 1,
        n_iter: str | Int = "deprecated",
        max_iter: None | Int = None,
        fit_algorithm: Literal["lars", "cd", "lars"] = "lars",
        n_jobs: None | Int = None,
        batch_size: str | Int = "warn",
        shuffle: bool = True,
        dict_init: None | MatrixLike = None,
        transform_algorithm: Literal["lasso_lars", "lasso_cd", "lars", "omp", "threshold", "omp"] = "omp",
        transform_n_nonzero_coefs: None | Int = None,
        transform_alpha: None | Float = None,
        verbose: int | bool = False,
        split_sign: bool = False,
        random_state: RandomState | None | Int = None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: Int = 1000,
        callback: None | Callable = None,
        tol: Float = 1e-3,
        max_no_improvement: Int = 10,
    ) -> None: ...
    @deprecated("The attribute `iter_offset_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def iter_offset_(self) -> int: ...
    @deprecated("The attribute `random_state_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def random_state_(self) -> RandomState: ...
    @deprecated("The attribute `inner_stats_` is deprecated in 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def inner_stats_(self) -> tuple[ndarray, ndarray]: ...
    def fit(self: MiniBatchDictionaryLearning_Self, X: MatrixLike, y: Any = None) -> MiniBatchDictionaryLearning_Self: ...
    def partial_fit(
        self: MiniBatchDictionaryLearning_Self,
        X: MatrixLike,
        y: Any = None,
        iter_offset: str | Int = "deprecated",
    ) -> MiniBatchDictionaryLearning_Self: ...
