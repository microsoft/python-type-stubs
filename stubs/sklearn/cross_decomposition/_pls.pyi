import warnings
from abc import ABCMeta, abstractmethod
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Literal, TypeVar

import numpy as np
from numpy import ndarray

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, MultiOutputMixin, RegressorMixin, TransformerMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_array as check_array, check_consistent_length as check_consistent_length
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import svd_flip as svd_flip
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted

PLSSVD_Self = TypeVar("PLSSVD_Self", bound=PLSSVD)
PLSRegression_Self = TypeVar("PLSRegression_Self", bound=PLSRegression)
_PLS_Self = TypeVar("_PLS_Self", bound=_PLS)

__all__ = ["PLSCanonical", "PLSRegression", "PLSSVD"]

class _PLS(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    RegressorMixin,
    MultiOutputMixin,
    BaseEstimator,
    metaclass=ABCMeta,
):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        deflation_mode: str = "regression",
        mode: str = "A",
        algorithm: str = "nipals",
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...
    def fit(self: _PLS_Self, X: MatrixLike, Y: MatrixLike | ArrayLike) -> _PLS_Self: ...
    def transform(
        self, X: MatrixLike, Y: None | MatrixLike = None, copy: bool = True
    ) -> tuple[ndarray, ...] | ndarray | tuple[ndarray, ndarray]: ...
    def inverse_transform(self, X: MatrixLike, Y: None | MatrixLike = None) -> tuple[ndarray, ndarray]: ...
    def predict(self, X: MatrixLike, copy: bool = True) -> ndarray: ...
    def fit_transform(self, X: MatrixLike, y: None | MatrixLike = None) -> ndarray: ...
    def coef_(self) -> ndarray: ...

class PLSRegression(_PLS):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: list = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...
    y_rotations_: ndarray = ...
    x_rotations_: ndarray = ...
    y_scores_: ndarray = ...
    x_scores_: ndarray = ...
    y_loadings_: ndarray = ...
    x_loadings_: ndarray = ...
    y_weights_: ndarray = ...
    x_weights_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    # This implementation provides the same results that 3 PLS packages
    # provided in the R language (R-project):
    #     - "mixOmics" with function pls(X, Y, mode = "regression")
    #     - "plspm " with function plsreg2(X, Y)
    #     - "pls" with function oscorespls.fit(X, Y)

    def __init__(
        self,
        n_components: Int = 2,
        *,
        scale: bool = True,
        max_iter: Int = 500,
        tol: Float = 1e-06,
        copy: bool = True,
    ) -> None: ...
    def fit(self: PLSRegression_Self, X: MatrixLike, Y: MatrixLike | ArrayLike) -> PLSRegression_Self: ...

class PLSCanonical(_PLS):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: list = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...
    y_rotations_: ndarray = ...
    x_rotations_: ndarray = ...
    y_loadings_: ndarray = ...
    x_loadings_: ndarray = ...
    y_weights_: ndarray = ...
    x_weights_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    # This implementation provides the same results that the "plspm" package
    # provided in the R language (R-project), using the function plsca(X, Y).
    # Results are equal or collinear with the function
    # ``pls(..., mode = "canonical")`` of the "mixOmics" package. The
    # difference relies in the fact that mixOmics implementation does not
    # exactly implement the Wold algorithm since it does not normalize
    # y_weights to one.

    def __init__(
        self,
        n_components: Int = 2,
        *,
        scale: bool = True,
        algorithm: Literal["nipals", "svd"] = "nipals",
        max_iter: Int = 500,
        tol: Float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class CCA(_PLS):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: list = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...
    y_rotations_: ndarray = ...
    x_rotations_: ndarray = ...
    y_loadings_: ndarray = ...
    x_loadings_: ndarray = ...
    y_weights_: ndarray = ...
    x_weights_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        scale: bool = True,
        max_iter: Int = 500,
        tol: Float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class PLSSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    y_weights_: ndarray = ...
    x_weights_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, n_components: Int = 2, *, scale: bool = True, copy: bool = True) -> None: ...
    def fit(self: PLSSVD_Self, X: MatrixLike, Y: MatrixLike | ArrayLike) -> PLSSVD_Self: ...
    def transform(self, X: MatrixLike, Y: None | MatrixLike | ArrayLike = None) -> ndarray | tuple[ndarray, ndarray]: ...
    def fit_transform(self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None) -> ndarray | tuple[ndarray, ndarray]: ...
