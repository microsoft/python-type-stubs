# This is a modified file from scipy.optimize
# Original authors: Travis Oliphant, Eric Jones
# Modifications by Gael Varoquaux, Mathieu Blondel and Tom Dupre la Tour
# License: BSD

import numpy as np
import warnings

from .fixes import line_search_wolfe1, line_search_wolfe2
from ..exceptions import ConvergenceWarning
from numpy import float64, ndarray
from scipy.optimize._optimize import OptimizeResult
from typing import Callable, Optional, Tuple, Union

class _LineSearchError(RuntimeError):
    pass

def _line_search_wolfe12(
    f: Callable,
    fprime: Callable,
    xk: ndarray,
    pk: ndarray,
    gfk: ndarray,
    old_fval: Union[float, float64],
    old_old_fval: Optional[Union[float, float64]],
    **kwargs,
) -> Union[Tuple[float, int, int, float, float, ndarray], Tuple[float, int, int, float, float64, ndarray],]: ...
def _cg(fhess_p: Callable, fgrad: ndarray, maxiter: int, tol: float64) -> ndarray: ...
def _newton_cg(
    grad_hess: Callable,
    func: Callable,
    grad: Callable,
    x0: ndarray,
    args: Tuple[ndarray, ndarray, ndarray, float, int] = (),
    tol: int = 1e-4,
    maxiter: int = 100,
    maxinner: int = 200,
    line_search: bool = True,
    warn: bool = True,
) -> Tuple[ndarray, int]: ...
def _check_optimize_result(
    solver: str,
    result: OptimizeResult,
    max_iter: Optional[int] = None,
    extra_warning_msg: Optional[str] = None,
) -> int: ...
