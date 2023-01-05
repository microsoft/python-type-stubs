from numpy import ndarray
from typing import Dict, Optional, Tuple, Literal, Callable, Mapping, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Pierre Lafaye de Micheaux, Stefan van der Walt, Gael Varoquaux,
#          Bertrand Thirion, Alexandre Gramfort, Denis A. Engemann
# License: BSD 3 clause

import warnings

import numpy as np
from numpy.random import RandomState
from scipy import linalg

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..exceptions import ConvergenceWarning

from ..utils import check_array, as_float_array, check_random_state
from ..utils.validation import check_is_fitted

__all__ = ["fastica", "FastICA"]

def _gs_decorrelation(w, W, j): ...
def _sym_decorrelation(W: ndarray) -> ndarray: ...
def _ica_def(X, tol, g, fun_args, max_iter, w_init): ...
def _ica_par(
    X: ndarray,
    tol: float,
    g: Callable,
    fun_args: Dict[Any, Any],
    max_iter: int,
    w_init: ndarray,
) -> Tuple[ndarray, int]: ...

# Some standard non-linear functions.
# XXX: these should be optimized, as they can be a bottleneck.
def _logcosh(x: ndarray, fun_args: Optional[Dict[Any, Any]] = None) -> Tuple[ndarray, ndarray]: ...
def _exp(x, fun_args): ...
def _cube(x, fun_args): ...
def fastica(
    X: ArrayLike,
    n_components: int | None = None,
    *,
    algorithm: Literal["parallel", "deflation"] = "parallel",
    whiten: str | bool = "warn",
    fun: Literal["logcosh", "exp", "cube"] | Callable = "logcosh",
    fun_args: Mapping | None = None,
    max_iter: int = 200,
    tol: float = 1e-04,
    w_init: NDArray | None = None,
    random_state: int | RandomState | None = None,
    return_X_mean: bool = False,
    compute_sources: bool = True,
    return_n_iter: bool = False,
) -> tuple[NDArray | None, NDArray, NDArray | None, NDArray, int]: ...

class FastICA(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        algorithm: Literal["parallel", "deflation"] = "parallel",
        whiten: str | bool = "warn",
        fun: Literal["logcosh", "exp", "cube"] | Callable = "logcosh",
        fun_args: Mapping | None = None,
        max_iter: int = 200,
        tol: float = 1e-4,
        w_init: NDArray | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _fit(self, X: ndarray, compute_sources: bool = False) -> Optional[ndarray]: ...
    def fit_transform(self, X: ArrayLike, y: None = None) -> NDArray: ...
    def fit(self, X: ArrayLike, y: None = None) -> "FastICA": ...
    def transform(self, X: ArrayLike, copy: bool = True) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike, copy: bool = True) -> NDArray: ...
    @property
    def _n_features_out(self): ...
    def _more_tags(self): ...
