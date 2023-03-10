from typing import Any, Callable, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from ..utils.extmath import svd_flip as svd_flip
from numpy.random import RandomState
from .._typing import MatrixLike, ArrayLike, Int, Float
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..linear_model import ridge_regression as ridge_regression
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from ..utils import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real
from ._dict_learning import (
    dict_learning as dict_learning,
    MiniBatchDictionaryLearning as MiniBatchDictionaryLearning,
)

import numpy as np


class _BaseSparsePCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: int | None = None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        tol: float = 1e-8,
        method: str = "lars",
        n_jobs=None,
        verbose: bool = False,
        random_state=None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def transform(self, X: ArrayLike) -> ndarray:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...


class SparsePCA(_BaseSparsePCA):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        alpha: Float = 1,
        ridge_alpha: Float = 0.01,
        max_iter: Int = 1000,
        tol: Float = 1e-8,
        method: Literal["lars", "cd", "lars"] = "lars",
        n_jobs: None | Int = None,
        U_init: None | MatrixLike = None,
        V_init: None | MatrixLike = None,
        verbose: int | bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...


class MiniBatchSparsePCA(_BaseSparsePCA):

    _parameter_constraints: dict = ...

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
        method: Literal["lars", "cd", "lars"] = "lars",
        random_state: RandomState | None | Int = None,
        tol: Float = 1e-3,
        max_no_improvement: int | None = 10,
    ) -> None:
        ...
