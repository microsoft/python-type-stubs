from typing import Any, Callable, Literal, Mapping
from ..linear_model._base import LinearClassifierMixin, SparseCoefMixin, LinearModel
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy.random import RandomState
from .._typing import Float, Int, ArrayLike, MatrixLike
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..base import BaseEstimator, RegressorMixin, OutlierMixin
from ._base import BaseSVC, BaseLibSVM
from numpy import ndarray
from ..utils import deprecated
from numbers import Integral as Integral, Real as Real

import numpy as np


class LinearSVC(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        penalty: Literal["l2", "l1", "l2"] = "l2",
        loss: Literal["hinge", "squared_hinge", "squared_hinge"] = "squared_hinge",
        *,
        dual: bool = True,
        tol: Float = 1e-4,
        C: Float = 1.0,
        multi_class: Literal["ovr", "crammer_singer", "ovr"] = "ovr",
        fit_intercept: bool = True,
        intercept_scaling: Float = 1,
        class_weight: str | Mapping | None = None,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        max_iter: Int = 1000,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class LinearSVR(RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        epsilon: Float = 0.0,
        tol: Float = 1e-4,
        C: Float = 1.0,
        loss: Literal[
            "epsilon_insensitive", "squared_epsilon_insensitive", "epsilon_insensitive"
        ] = "epsilon_insensitive",
        fit_intercept: bool = True,
        intercept_scaling: Float = 1.0,
        dual: bool = True,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        max_iter: Int = 1000,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class SVC(BaseSVC):

    _impl: str = ...

    def __init__(
        self,
        *,
        C: Float = 1.0,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed", "rbf"]
        | Callable = "rbf",
        degree: Int = 3,
        gamma: float | Literal["scale", "auto", "scale"] = "scale",
        coef0: Float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: Float = 1e-3,
        cache_size: Float = 200,
        class_weight: str | Mapping | None = None,
        verbose: bool = False,
        max_iter: Int = ...,
        decision_function_shape: Literal["ovo", "ovr", "ovr"] = "ovr",
        break_ties: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...


class NuSVC(BaseSVC):

    _impl: str = ...

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        nu: Float = 0.5,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed", "rbf"]
        | Callable = "rbf",
        degree: Int = 3,
        gamma: float | Literal["scale", "auto", "scale"] = "scale",
        coef0: Float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: Float = 1e-3,
        cache_size: Float = 200,
        class_weight: str | Mapping | None = None,
        verbose: bool = False,
        max_iter: Int = ...,
        decision_function_shape: Literal["ovo", "ovr", "ovr"] = "ovr",
        break_ties: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...


class SVR(RegressorMixin, BaseLibSVM):

    _impl: str = ...

    _parameter_constraints: dict = ...
    for unused_param in ["class_weight", "nu", "probability", "random_state"]:
        pass

    def __init__(
        self,
        *,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed", "rbf"]
        | Callable = "rbf",
        degree: Int = 3,
        gamma: float | Literal["scale", "auto", "scale"] = "scale",
        coef0: Float = 0.0,
        tol: Float = 1e-3,
        C: Float = 1.0,
        epsilon: Float = 0.1,
        shrinking: bool = True,
        cache_size: Float = 200,
        verbose: bool = False,
        max_iter: Int = ...,
    ) -> None:
        ...

    # TODO(1.4): Remove
    @deprecated(  # type: ignore
        "Attribute `class_weight_` was deprecated in version 1.2 and will be removed in"
        " 1.4."
    )
    @property
    def class_weight_(self) -> ndarray:
        ...


class NuSVR(RegressorMixin, BaseLibSVM):

    _impl: str = ...

    _parameter_constraints: dict = ...
    for unused_param in ["class_weight", "epsilon", "probability", "random_state"]:
        pass

    def __init__(
        self,
        *,
        nu: Float = 0.5,
        C: Float = 1.0,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed", "rbf"]
        | Callable = "rbf",
        degree: Int = 3,
        gamma: float | Literal["scale", "auto", "scale"] = "scale",
        coef0: Float = 0.0,
        shrinking: bool = True,
        tol: Float = 1e-3,
        cache_size: Float = 200,
        verbose: bool = False,
        max_iter: Int = ...,
    ) -> None:
        ...

    # TODO(1.4): Remove
    @deprecated(  # type: ignore
        "Attribute `class_weight_` was deprecated in version 1.2 and will be removed in"
        " 1.4."
    )
    @property
    def class_weight_(self) -> ndarray:
        ...


class OneClassSVM(OutlierMixin, BaseLibSVM):

    _impl: str = ...

    _parameter_constraints: dict = ...
    for unused_param in ["C", "class_weight", "epsilon", "probability", "random_state"]:
        pass

    def __init__(
        self,
        *,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "precomputed", "rbf"]
        | Callable = "rbf",
        degree: Int = 3,
        gamma: float | Literal["scale", "auto", "scale"] = "scale",
        coef0: Float = 0.0,
        tol: Float = 1e-3,
        nu: Float = 0.5,
        shrinking: bool = True,
        cache_size: Float = 200,
        verbose: bool = False,
        max_iter: Int = ...,
    ) -> None:
        ...

    # TODO(1.4): Remove
    @deprecated(  # type: ignore
        "Attribute `class_weight_` was deprecated in version 1.2 and will be removed in"
        " 1.4."
    )
    @property
    def class_weight_(self) -> ndarray:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def score_samples(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...
