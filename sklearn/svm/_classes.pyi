from typing import Dict, Union, Literal, Mapping, Any, Callable
from numpy.typing import ArrayLike, NDArray
import numpy as np
import warnings
from numpy.random import RandomState

from ._base import _fit_liblinear, BaseSVC, BaseLibSVM
from ..base import BaseEstimator, RegressorMixin, OutlierMixin
from ..linear_model._base import LinearClassifierMixin, SparseCoefMixin, LinearModel
from ..utils.validation import _num_samples
from ..utils.multiclass import check_classification_targets
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

class LinearSVC(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    def __init__(
        self,
        penalty: Literal["l1", "l2"] = "l2",
        loss: Literal["hinge", "squared_hinge"] = "squared_hinge",
        *,
        dual: bool = True,
        tol: float = 1e-4,
        C: float = 1.0,
        multi_class: Literal["ovr", "crammer_singer"] = "ovr",
        fit_intercept: bool = True,
        intercept_scaling: float = 1,
        class_weight: Mapping | Literal["balanced"] | None = None,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        max_iter: int = 1000,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "LinearSVC": ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...

class LinearSVR(RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        epsilon: float = 0.0,
        tol: float = 1e-4,
        C: float = 1.0,
        loss: Literal["epsilon_insensitive", "squared_epsilon_insensitive"] = "epsilon_insensitive",
        fit_intercept: bool = True,
        intercept_scaling: float = 1.0,
        dual: bool = True,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        max_iter: int = 1000,
    ): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def _more_tags(self): ...

class SVC(BaseSVC):

    _impl: str = ...

    def __init__(
        self,
        *,
        C: float = 1.0,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed"] | Callable = "rbf",
        degree: int = 3,
        gamma: Literal["scale", "auto"] | float = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: float = 1e-3,
        cache_size: float = 200,
        class_weight: Mapping | Literal["balanced"] | None = None,
        verbose: bool = False,
        max_iter: int = ...,
        decision_function_shape: Literal["ovo", "ovr"] = "ovr",
        break_ties: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...

class NuSVC(BaseSVC):

    _impl: str = ...

    def __init__(
        self,
        *,
        nu: float = 0.5,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed"] | Callable = "rbf",
        degree: int = 3,
        gamma: Literal["scale", "auto"] | float = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: float = 1e-3,
        cache_size: float = 200,
        class_weight=None,
        verbose: bool = False,
        max_iter: int = ...,
        decision_function_shape: Literal["ovo", "ovr"] = "ovr",
        break_ties: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _more_tags(self): ...

class SVR(RegressorMixin, BaseLibSVM):

    _impl: str = ...

    def __init__(
        self,
        *,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed"] | Callable = "rbf",
        degree: int = 3,
        gamma: Literal["scale", "auto"] | float = "scale",
        coef0: float = 0.0,
        tol: float = 1e-3,
        C: float = 1.0,
        epsilon: float = 0.1,
        shrinking: bool = True,
        cache_size: float = 200,
        verbose: bool = False,
        max_iter: int = ...,
    ) -> None: ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...

class NuSVR(RegressorMixin, BaseLibSVM):

    _impl: str = ...

    def __init__(
        self,
        *,
        nu: float = 0.5,
        C: float = 1.0,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed"] | Callable = "rbf",
        degree: int = 3,
        gamma: Literal["scale", "auto"] | float = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        tol: float = 1e-3,
        cache_size: float = 200,
        verbose: bool = False,
        max_iter: int = ...,
    ) -> None: ...
    def _more_tags(self): ...

class OneClassSVM(OutlierMixin, BaseLibSVM):

    _impl: str = ...

    def __init__(
        self,
        *,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed"] | Callable = "rbf",
        degree: int = 3,
        gamma: Literal["scale", "auto"] | float = "scale",
        coef0: float = 0.0,
        tol: float = 1e-3,
        nu: float = 0.5,
        shrinking: bool = True,
        cache_size: float = 200,
        verbose: bool = False,
        max_iter: int = ...,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
        **params,
    ) -> "OneClassSVM": ...
    def decision_function(self, X: ArrayLike) -> NDArray: ...
    def score_samples(self, X: ArrayLike) -> NDArray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...
