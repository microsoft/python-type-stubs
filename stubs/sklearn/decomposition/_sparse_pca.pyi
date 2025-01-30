from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..linear_model import ridge_regression as ridge_regression
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import svd_flip as svd_flip
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted
from ._dict_learning import MiniBatchDictionaryLearning as MiniBatchDictionaryLearning, dict_learning as dict_learning

_BaseSparsePCA_Self = TypeVar("_BaseSparsePCA_Self", bound=_BaseSparsePCA)

import numpy as np

class _BaseSparsePCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | int = None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        tol: float = 1e-8,
        method: str = "lars",
        n_jobs=None,
        verbose: bool = False,
        random_state=None,
    ) -> None: ...
    def fit(self: _BaseSparsePCA_Self, X: MatrixLike, y: Any = None) -> _BaseSparsePCA_Self | MiniBatchSparsePCA: ...
    def transform(self, X: ArrayLike) -> ndarray: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...

class SparsePCA(_BaseSparsePCA):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    mean_: ndarray = ...
    n_iter_: int = ...
    n_components_: int = ...
    error_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        alpha: Float = 1,
        ridge_alpha: Float = 0.01,
        max_iter: Int = 1000,
        tol: Float = 1e-8,
        method: Literal["lars", "cd"] = "lars",
        n_jobs: None | Int = None,
        U_init: None | MatrixLike = None,
        V_init: None | MatrixLike = None,
        verbose: int | bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class MiniBatchSparsePCA(_BaseSparsePCA):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    mean_: ndarray = ...
    n_iter_: int = ...
    n_components_: int = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        alpha: Int = 1,
        ridge_alpha: Float = 0.01,
        n_iter: str | Int = "deprecated",
        max_iter: None | Int = None,
        callback: None | Callable = None,
        batch_size: Int = 3,
        verbose: int | bool = False,
        shuffle: bool = True,
        n_jobs: None | Int = None,
        method: Literal["lars", "cd"] = "lars",
        random_state: RandomState | None | Int = None,
        tol: Float = 1e-3,
        max_no_improvement: None | int = 10,
    ) -> None: ...
