from numpy import float64, ndarray
from typing import Dict, Optional, Tuple, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Vlad Niculae
#         Lars Buitinck
#         Mathieu Blondel <mathieu@mblondel.org>
#         Tom Dupre la Tour
# License: BSD 3 clause

import numbers
import numpy as np
import scipy.sparse as sp
import time
import itertools
import warnings
from math import sqrt
from scipy import linalg

from .._config import config_context
from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..exceptions import ConvergenceWarning
from ..utils import check_random_state, check_array, gen_batches
from ..utils.extmath import randomized_svd, safe_sparse_dot, squared_norm
from ..utils.validation import (
    check_is_fitted,
    check_non_negative,
)
from numpy.random import RandomState
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix

EPSILON = ...

def norm(x: ArrayLike) -> float: ...
def trace_dot(X: ArrayLike, Y: ArrayLike) -> float64: ...
def _check_init(A: ndarray, shape: Tuple[int, int], whom: str) -> None: ...
def _beta_divergence(
    X: Union[int, csr_matrix, ndarray],
    W: Union[ndarray, float64],
    H: Union[ndarray, int],
    beta: Union[int, float],
    square_root: bool = False,
) -> float64: ...
def _special_sparse_dot(W: ndarray, H: ndarray, X: csr_matrix) -> csr_matrix: ...
def _compute_regularization(
    alpha: float,
    alpha_W: float,
    alpha_H: Union[float, str],
    l1_ratio: Union[int, float],
    regularization: str,
) -> Tuple[float, float, float, float]: ...
def _beta_loss_to_float(beta_loss: Union[int, float, str]) -> Union[int, float]: ...
def _initialize_nmf(
    X: Union[ndarray, csr_matrix],
    n_components: int,
    init: Optional[str] = None,
    eps: float = 1e-6,
    random_state: Optional[int] = None,
) -> Tuple[ndarray, ndarray]: ...
def _update_coordinate_descent(
    X: Union[csc_matrix, csr_matrix, ndarray],
    W: ndarray,
    Ht: ndarray,
    l1_reg: float,
    l2_reg: float,
    shuffle: bool,
    random_state: RandomState,
) -> float: ...
def _fit_coordinate_descent(
    X: Union[ndarray, csr_matrix],
    W: ndarray,
    H: ndarray,
    tol: float = 1e-4,
    max_iter: int = 200,
    l1_reg_W: float = 0,
    l1_reg_H: float = 0,
    l2_reg_W: float = 0,
    l2_reg_H: float = 0,
    update_H: bool = True,
    verbose: int = 0,
    shuffle: bool = False,
    random_state: Optional[int] = None,
) -> Tuple[ndarray, ndarray, int]: ...
def _multiplicative_update_w(
    X: csr_matrix,
    W: ndarray,
    H: ndarray,
    beta_loss: int,
    l1_reg_W: float,
    l2_reg_W: float,
    gamma: float,
    H_sum: None = None,
    HHt: None = None,
    XHt: None = None,
    update_H: bool = True,
) -> Union[Tuple[ndarray, ndarray, None, None], Tuple[ndarray, None, ndarray, ndarray]]: ...
def _multiplicative_update_h(
    X: csr_matrix,
    W: ndarray,
    H: ndarray,
    beta_loss: int,
    l1_reg_H: float,
    l2_reg_H: float,
    gamma: float,
    A: Optional[ndarray] = None,
    B: Optional[ndarray] = None,
    rho: Optional[float] = None,
) -> ndarray: ...
def _fit_multiplicative_update(
    X: csr_matrix,
    W: ndarray,
    H: ndarray,
    beta_loss: int | str = "frobenius",
    max_iter: int = 200,
    tol: float = 1e-4,
    l1_reg_W: float = 0,
    l1_reg_H: float = 0,
    l2_reg_W: float = 0,
    l2_reg_H: float = 0,
    update_H: bool = True,
    verbose: int = 0,
) -> Tuple[ndarray, ndarray, int]: ...
def non_negative_factorization(
    X: ArrayLike,
    W: ArrayLike | None = None,
    H: ArrayLike | None = None,
    n_components: int | None = None,
    *,
    init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"] | None = None,
    update_H: bool = True,
    solver: Literal["cd", "mu"] = "cd",
    beta_loss: float | Literal["frobenius", "kullback-leibler", "itakura-saito"] = "frobenius",
    tol: float = 1e-4,
    max_iter: int = 200,
    alpha: float | str = "deprecated",
    alpha_W: float = 0.0,
    alpha_H: float | Literal["same"] = "same",
    l1_ratio: float = 0.0,
    regularization: Literal["both", "components", "transformation"] | str = "deprecated",
    random_state: int | RandomState | None = None,
    verbose: int = 0,
    shuffle: bool = False,
) -> tuple[NDArray, NDArray, int]: ...

class NMF(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"] | None = None,
        solver: Literal["cd", "mu"] = "cd",
        beta_loss: float | Literal["frobenius", "kullback-leibler", "itakura-saito"] = "frobenius",
        tol: float = 1e-4,
        max_iter: int = 200,
        random_state: int | RandomState | None = None,
        alpha: float | str = "deprecated",
        alpha_W: float = 0.0,
        alpha_H: float | Literal["same"] = "same",
        l1_ratio: float = 0.0,
        verbose: int = 0,
        shuffle: bool = False,
        regularization: None | Literal["both", "components", "transformation"] | str = "deprecated",
    ) -> None: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def _check_params(self, X: Union[ndarray, csr_matrix]) -> Union[NMF, MiniBatchNMF]: ...
    def _check_w_h(
        self,
        X: Union[ndarray, csr_matrix],
        W: None,
        H: Optional[ndarray],
        update_H: bool,
    ) -> Tuple[ndarray, ndarray]: ...
    def _scale_regularization(self, X: Union[ndarray, csr_matrix]) -> Tuple[float, float, float, float]: ...
    def fit_transform(
        self,
        X: NDArray | ArrayLike,
        y: Optional[ndarray] = None,
        W: ArrayLike | None = None,
        H: ArrayLike | None = None,
    ) -> NDArray: ...
    def _fit_transform(
        self,
        X: Union[ndarray, csr_matrix],
        y: None = None,
        W: None = None,
        H: Optional[ndarray] = None,
        update_H: bool = True,
    ) -> Tuple[ndarray, ndarray, int]: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None, **params) -> Union[NMF, MiniBatchNMF]: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, W: NDArray) -> NDArray: ...
    @property
    def _n_features_out(self): ...

class MiniBatchNMF(NMF):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        init: Literal["random", "nndsvd", "nndsvda", "nndsvdar", "custom"] | None = None,
        batch_size: int = 1024,
        beta_loss: float | Literal["frobenius", "kullback-leibler", "itakura-saito"] = "frobenius",
        tol: float = 1e-4,
        max_no_improvement: int = 10,
        max_iter: int = 200,
        alpha_W: float = 0.0,
        alpha_H: float | Literal["same"] = "same",
        l1_ratio: float = 0.0,
        forget_factor: float = 0.7,
        fresh_restarts: bool = False,
        fresh_restarts_max_iter: int = 30,
        transform_max_iter: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: bool = False,
    ) -> None: ...
    def _check_params(self, X: csr_matrix) -> "MiniBatchNMF": ...
    def _solve_W(self, X, H, max_iter): ...
    def _minibatch_step(self, X: csr_matrix, W: ndarray, H: ndarray, update_H: bool) -> float64: ...
    def _minibatch_convergence(
        self,
        X: csr_matrix,
        batch_cost: float64,
        H: ndarray,
        H_buffer: ndarray,
        n_samples: int,
        step: int,
        n_steps: int,
    ) -> bool: ...
    def fit_transform(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        W: ArrayLike | None = None,
        H: ArrayLike | None = None,
    ) -> NDArray: ...
    def _fit_transform(
        self, X: csr_matrix, W: None = None, H: None = None, update_H: bool = True
    ) -> Tuple[ndarray, ndarray, int, int]: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y=None,
        W: ArrayLike | None = None,
        H: ArrayLike | None = None,
    ): ...
