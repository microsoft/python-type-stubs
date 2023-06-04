from typing import Callable
from scipy.sparse.linalg import LinearOperator
from numpy import block as bmat, ndarray
from scipy.linalg import (
    inv as inv,
    eigh as eigh,
    cho_factor as cho_factor,
    cho_solve as cho_solve,
    cholesky as cholesky,
    LinAlgError as LinAlgError,
)
from scipy.sparse import isspmatrix as isspmatrix
from .._typing import MatrixLike, ArrayLike, Float, Scalar, Int
import inspect
import warnings
import numpy as np

__all__ = ["lobpcg"]


def lobpcg(
    A: MatrixLike | LinearOperator | ArrayLike | Callable,
    X: ArrayLike | Float,
    B: ArrayLike | None | Callable | MatrixLike | LinearOperator = None,
    M: ArrayLike | None | Callable | MatrixLike | LinearOperator = None,
    Y: float | None | ArrayLike = None,
    tol: None | Scalar = None,
    maxiter: None | int = None,
    largest: None | bool = True,
    verbosityLevel: Int = 0,
    retLambdaHistory: None | bool = False,
    retResidualNormsHistory: None | bool = False,
    restartControl: None | int = 20,
) -> tuple[ndarray, ndarray, ndarray, ndarray]:
    ...
