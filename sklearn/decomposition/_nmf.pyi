from typing import Any, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from abc import ABC
from scipy import linalg as linalg
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from numpy import ndarray
from ..utils.extmath import (
    randomized_svd as randomized_svd,
    safe_sparse_dot as safe_sparse_dot,
    squared_norm as squared_norm,
)
from numbers import Integral as Integral, Real as Real
from .._config import config_context as config_context
from ..utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from math import sqrt as sqrt
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from scipy.sparse import spmatrix
from .._typing import ArrayLike, Float, MatrixLike, Int
from ..utils import (
    check_random_state as check_random_state,
    check_array as check_array,
    gen_batches as gen_batches,
)
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
)

MiniBatchNMF_Self = TypeVar("MiniBatchNMF_Self", bound="MiniBatchNMF")
_BaseNMF_Self = TypeVar("_BaseNMF_Self", bound="_BaseNMF")

import numpy as np
import scipy.sparse as sp
import time
import itertools
import warnings


EPSILON = ...


def norm(x: ArrayLike) -> float:
    ...


def trace_dot(X: ArrayLike, Y: ArrayLike) -> Float:
    ...


def non_negative_factorization(
    X: MatrixLike | ArrayLike,
    W: None | MatrixLike = None,
    H: None | ArrayLike = None,
    n_components: None | Int = None,
    *,
    init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"] | None = None,
    update_H: bool = True,
    solver: Literal["cd", "mu", "cd"] = "cd",
    beta_loss: float
    | Literal[
        "frobenius", "kullback-leibler", "itakura-saito", "frobenius"
    ] = "frobenius",
    tol: Float = 1e-4,
    max_iter: Int = 200,
    alpha_W: Float = 0.0,
    alpha_H: float | Literal["same", "same"] = "same",
    l1_ratio: Float = 0.0,
    random_state: RandomState | None | Int = None,
    verbose: Int = 0,
    shuffle: bool = False,
) -> tuple[ndarray, ndarray, int]:
    ...


class _BaseNMF(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, ABC):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | int = None,
        *,
        init=None,
        beta_loss: str = "frobenius",
        tol: float = 1e-4,
        max_iter: int = 200,
        random_state=None,
        alpha_W: float = 0.0,
        alpha_H: str = "same",
        l1_ratio: float = 0.0,
        verbose: int = 0,
    ) -> None:
        ...

    def fit(
        self: _BaseNMF_Self, X: MatrixLike | ArrayLike, y: Any = None, **params
    ) -> _BaseNMF_Self:
        ...

    def inverse_transform(self, W: MatrixLike) -> ndarray | spmatrix:
        ...


class NMF(_BaseNMF):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    reconstruction_err_: float = ...
    n_components_: int = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"]
        | None = None,
        solver: Literal["cd", "mu", "cd"] = "cd",
        beta_loss: float
        | Literal[
            "frobenius", "kullback-leibler", "itakura-saito", "frobenius"
        ] = "frobenius",
        tol: Float = 1e-4,
        max_iter: Int = 200,
        random_state: RandomState | None | Int = None,
        alpha_W: Float = 0.0,
        alpha_H: float | Literal["same", "same"] = "same",
        l1_ratio: Float = 0.0,
        verbose: Int = 0,
        shuffle: bool = False,
    ) -> None:
        ...

    def fit_transform(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        W: None | MatrixLike = None,
        H: None | ArrayLike = None,
    ) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class MiniBatchNMF(_BaseNMF):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_steps_: int = ...
    n_iter_: int = ...
    reconstruction_err_: float = ...
    n_components_: int = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"]
        | None = None,
        batch_size: Int = 1024,
        beta_loss: float
        | Literal[
            "frobenius", "kullback-leibler", "itakura-saito", "frobenius"
        ] = "frobenius",
        tol: Float = 1e-4,
        max_no_improvement: Int = 10,
        max_iter: Int = 200,
        alpha_W: Float = 0.0,
        alpha_H: float | Literal["same", "same"] = "same",
        l1_ratio: Float = 0.0,
        forget_factor: Float = 0.7,
        fresh_restarts: bool = False,
        fresh_restarts_max_iter: Int = 30,
        transform_max_iter: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: int | bool = 0,
    ) -> None:
        ...

    def fit_transform(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        W: None | MatrixLike = None,
        H: None | ArrayLike = None,
    ) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def partial_fit(
        self: MiniBatchNMF_Self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        W: None | MatrixLike = None,
        H: None | ArrayLike = None,
    ) -> MiniBatchNMF_Self:
        ...
