from abc import ABCMeta, abstractmethod
from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, TypeVar

from numpy import ndarray
from numpy.random.mtrand import RandomState

from .._typing import ArrayLike, Float, MatrixLike
from ..base import BaseEstimator, ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning, NotFittedError as NotFittedError
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    compute_class_weight as compute_class_weight,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted

BaseLibSVM_Self = TypeVar("BaseLibSVM_Self", bound=BaseLibSVM)

import warnings

import numpy as np
import scipy.sparse as sp

LIBSVM_IMPL: list = ...

class BaseLibSVM(BaseEstimator, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    # The order of these must match the integer values in LibSVM.
    # XXX These are actually the same in the dense case. Need to factor
    # this out.
    _sparse_kernels: ClassVar[list] = ...

    @abstractmethod
    def __init__(
        self,
        kernel: str | Callable,
        degree: int,
        gamma: str | Float,
        coef0: float,
        tol: float,
        C: Float,
        nu: float,
        epsilon: float,
        shrinking: bool,
        probability: bool,
        cache_size: int,
        class_weight: dict[int, int] | None | str,
        verbose: bool,
        max_iter: int,
        random_state: None | RandomState | int,
    ) -> None: ...
    def fit(
        self: BaseLibSVM_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> BaseLibSVM_Self: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    @property
    def coef_(self) -> ndarray: ...
    def n_support_(self) -> ndarray: ...

class BaseSVC(ClassifierMixin, BaseLibSVM, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        kernel: str | Callable,
        degree: int,
        gamma: str | Float,
        coef0: float,
        tol: float,
        C: Float,
        nu: float,
        shrinking: bool,
        probability: bool,
        cache_size: int,
        class_weight: dict[int, int] | None | str,
        verbose: bool,
        max_iter: int,
        decision_function_shape: str,
        random_state: None | RandomState | int,
        break_ties: bool,
    ) -> None: ...
    def decision_function(self, X: MatrixLike) -> ndarray: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
    def predict_proba(self, X: MatrixLike) -> ndarray: ...
    def predict_log_proba(self, X: MatrixLike) -> ndarray: ...
    @property
    def probA_(self) -> ndarray: ...
    @property
    def probB_(self) -> ndarray: ...
