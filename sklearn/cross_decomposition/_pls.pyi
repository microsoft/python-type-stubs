from typing import Optional, Tuple, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Edouard Duchesnay <edouard.duchesnay@cea.fr>
# License: BSD 3 clause

import numbers
import warnings
from abc import ABCMeta, abstractmethod

import numpy as np
from scipy.linalg import svd

from ..base import BaseEstimator, RegressorMixin, TransformerMixin
from ..base import MultiOutputMixin
from ..base import _ClassNamePrefixFeaturesOutMixin
from ..utils import check_array, check_scalar, check_consistent_length
from ..utils.fixes import sp_version
from ..utils.fixes import parse_version
from ..utils.extmath import svd_flip
from ..utils.validation import check_is_fitted, FLOAT_DTYPES
from ..exceptions import ConvergenceWarning
from numpy import ndarray

__all__ = ["PLSCanonical", "PLSRegression", "PLSSVD"]

def _pinv2_old(a: ndarray) -> ndarray: ...
def _get_first_singular_vectors_power_method(
    X: ndarray,
    Y: ndarray,
    mode: str = "A",
    max_iter: int = 500,
    tol: float = 1e-06,
    norm_y_weights: bool = False,
) -> Tuple[ndarray, ndarray, int]: ...
def _get_first_singular_vectors_svd(X, Y): ...
def _center_scale_xy(
    X: ndarray, Y: ndarray, scale: bool = True
) -> Tuple[ndarray, ndarray, ndarray, ndarray, ndarray, ndarray]: ...
def _svd_flip_1d(u: ndarray, v: ndarray) -> None: ...

class _PLS(
    _ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    RegressorMixin,
    MultiOutputMixin,
    BaseEstimator,
    metaclass=ABCMeta,
):
    @abstractmethod
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale=True,
        deflation_mode="regression",
        mode="A",
        algorithm="nipals",
        max_iter=500,
        tol=1e-06,
        copy=True,
    ) -> None: ...
    def fit(self, X: ArrayLike, Y: ArrayLike) -> Union[PLSCanonical, CCA, PLSRegression]: ...
    def transform(self, X: ArrayLike, Y: ArrayLike | None = None, copy: bool = True) -> ArrayLike | tuple[ArrayLike, ...]: ...
    def inverse_transform(self, X: ArrayLike, Y: ArrayLike | None = None) -> tuple[NDArray, NDArray]: ...
    def predict(self, X: ArrayLike, copy: bool = True) -> NDArray: ...
    def fit_transform(self, X: ArrayLike, y: ArrayLike | None = None) -> NDArray: ...
    @property
    def coef_(self) -> ndarray: ...
    def _more_tags(self): ...

class PLSRegression(_PLS):

    # This implementation provides the same results that 3 PLS packages
    # provided in the R language (R-project):
    #     - "mixOmics" with function pls(X, Y, mode = "regression")
    #     - "plspm " with function plsreg2(X, Y)
    #     - "pls" with function oscorespls.fit(X, Y)

    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...
    def fit(self, X: ArrayLike, Y: ArrayLike) -> "PLSRegression": ...

class PLSCanonical(_PLS):

    # This implementation provides the same results that the "plspm" package
    # provided in the R language (R-project), using the function plsca(X, Y).
    # Results are equal or collinear with the function
    # ``pls(..., mode = "canonical")`` of the "mixOmics" package. The
    # difference relies in the fact that mixOmics implementation does not
    # exactly implement the Wold algorithm since it does not normalize
    # y_weights to one.

    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        algorithm: Literal["nipals", "svd"] = "nipals",
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class CCA(_PLS):
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class PLSSVD(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(self, n_components: int = 2, *, scale: bool = True, copy: bool = True): ...
    def fit(self, X: ArrayLike, Y: ArrayLike) -> Any: ...
    def transform(self, X: ArrayLike, Y: ArrayLike | None = None) -> ArrayLike | tuple[ArrayLike, ...]: ...
    def fit_transform(self, X: ArrayLike, y: ArrayLike | None = None) -> ArrayLike | tuple[ArrayLike, ...]: ...
