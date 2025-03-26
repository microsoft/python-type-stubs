import warnings
from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg

from .._typing import Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import as_float_array as as_float_array, check_array as check_array, check_random_state as check_random_state
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted

# Authors: Pierre Lafaye de Micheaux, Stefan van der Walt, Gael Varoquaux,
#          Bertrand Thirion, Alexandre Gramfort, Denis A. Engemann
# License: BSD 3 clause

__all__ = ["fastica", "FastICA"]

def fastica(
    X: MatrixLike,
    n_components: None | Int = None,
    *,
    algorithm: Literal["parallel", "deflation"] = "parallel",
    whiten: str | bool = "warn",
    fun: Literal["logcosh", "exp", "cube"] | Callable = "logcosh",
    fun_args: None | dict = None,
    max_iter: Int = 200,
    tol: Float = 1e-04,
    w_init: None | MatrixLike = None,
    whiten_solver: Literal["eigh", "svd"] = "svd",
    random_state: RandomState | None | Int = None,
    return_X_mean: bool = False,
    compute_sources: bool = True,
    return_n_iter: bool = False,
) -> tuple[ndarray | None, ndarray, ndarray | None, ndarray, int]: ...

class FastICA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    whitening_: ndarray = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    mean_: ndarray = ...
    mixing_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        algorithm: Literal["parallel", "deflation"] = "parallel",
        whiten: str | bool = "warn",
        fun: Literal["logcosh", "exp", "cube"] | Callable = "logcosh",
        fun_args: None | dict = None,
        max_iter: Int = 200,
        tol: Float = 1e-4,
        w_init: None | MatrixLike = None,
        whiten_solver: Literal["eigh", "svd"] = "svd",
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def transform(self, X: MatrixLike, copy: bool = True) -> ndarray: ...
    def inverse_transform(self, X: MatrixLike, copy: bool = True) -> ndarray: ...
