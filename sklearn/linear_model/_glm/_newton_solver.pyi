from abc import ABC, abstractmethod
from numpy import ndarray
from ..._loss.loss import HalfSquaredError as HalfSquaredError
from ..._typing import MatrixLike, ArrayLike, Float, Int
from .._linear_loss import LinearModelLoss
from scipy.sparse._csr import csr_matrix
from ...exceptions import ConvergenceWarning as ConvergenceWarning

# Author: Christian Lorentzen <lorentzen.ch@gmail.com>
# License: BSD 3 clause

import warnings

import numpy as np
import scipy.linalg
import scipy.optimize


class NewtonSolver(ABC):
    gradient_times_newton: float = ...
    use_fallback_lbfgs_solve: bool = ...
    iteration: int = ...
    converged: bool = ...
    raw_prediction: ndarray = ...
    loss_value_old: float = ...
    loss_value: float = ...
    gradient_old: ndarray = ...
    gradient: ndarray = ...
    coef_newton: ndarray = ...
    coef_old: ndarray = ...

    def __init__(
        self,
        *,
        coef: MatrixLike | ArrayLike,
        linear_loss: LinearModelLoss = ...,
        l2_reg_strength: Float = 0.0,
        tol: Float = 1e-4,
        max_iter: Int = 100,
        n_threads: Int = 1,
        verbose: int = 0,
    ) -> None:
        ...

    def setup(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> None:
        ...

    @abstractmethod
    def update_gradient_hessian(self, X, y, sample_weight):
        ...

    @abstractmethod
    def inner_solve(self, X, y, sample_weight):
        ...

    def fallback_lbfgs_solve(self, X, y, sample_weight):
        ...

    def line_search(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> None:
        ...

    def check_convergence(
        self, X: csr_matrix, y: ndarray, sample_weight: ndarray
    ) -> None:
        ...

    def finalize(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> None:
        ...

    def solve(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> ndarray:
        ...


class NewtonCholeskySolver(NewtonSolver):
    def setup(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> None:
        ...

    def update_gradient_hessian(
        self, X: csr_matrix, y: ndarray, sample_weight: ndarray
    ) -> None:
        ...

    def inner_solve(self, X: csr_matrix, y: ndarray, sample_weight: ndarray) -> None:
        ...
