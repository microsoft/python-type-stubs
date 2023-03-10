from typing import Callable
from scipy.linalg import (
    inv as inv,
    eigh as eigh,
    cho_factor as cho_factor,
    cho_solve as cho_solve,
    cholesky as cholesky,
    LinAlgError as LinAlgError,
)
from scipy.sparse.linalg import LinearOperator
from .._typing import ArrayLike, MatrixLike, Float, Scalar, Int
from numpy import block as bmat, ndarray
from scipy.sparse import isspmatrix as isspmatrix
import inspect
import warnings
import numpy as np

__all__ = ["lobpcg"]


def lobpcg(
    A: LinearOperator | Callable | MatrixLike | ArrayLike,
    X: Float | ArrayLike,
    B: MatrixLike | Callable | ArrayLike | None | LinearOperator = None,
    M: MatrixLike | Callable | ArrayLike | None | LinearOperator = None,
    Y: float | None | ArrayLike = None,
    tol: Scalar | None = None,
    maxiter: int | None = None,
    largest: bool | None = True,
    verbosityLevel: Int = 0,
    retLambdaHistory: bool | None = False,
    retResidualNormsHistory: bool | None = False,
    restartControl: int | None = 20,
) -> tuple[ndarray, ndarray, ndarray, ndarray]:
    ...
