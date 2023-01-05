from numpy import ndarray
from sklearn._typing import Scalar
from numpy.typing import NDArray

import warnings
import numpy as np
from scipy.linalg import inv, eigh, cho_factor, cho_solve, cholesky, LinAlgError
from scipy.sparse.linalg import aslinearoperator
from numpy import block as bmat

__all__ = ["lobpcg"]

def _report_nonhermitian(M, name): ...
def _as2d(ar): ...
def _makeOperator(operatorInput, expectedShape): ...
def _applyConstraints(blockVectorV, factYBY, blockVectorBY, blockVectorY): ...
def _b_orthonormalize(B, blockVectorV, blockVectorBV=None, retInvR=False): ...
def _get_indx(_lambda, num, largest): ...
def lobpcg(
    A,
    X: NDArray | float,
    B: NDArray | LinearOperator | None = None,
    M: NDArray | LinearOperator | None = None,
    Y: NDArray | float | None = None,
    tol: Scalar | None = None,
    maxiter: int | None = None,
    largest: bool = True,
    verbosityLevel: int = 0,
    retLambdaHistory: bool = False,
    retResidualNormsHistory: bool = False,
) -> tuple[NDArray, NDArray, list[np.ndarray], list[np.ndarray]]: ...
