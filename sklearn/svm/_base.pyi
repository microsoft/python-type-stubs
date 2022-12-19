from numpy import float64, ndarray
from typing import Callable, Dict, List, Optional, Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray
import warnings
import numbers
from abc import ABCMeta, abstractmethod
from numpy.random import RandomState

import numpy as np
import scipy.sparse as sp

# mypy error: error: Module 'sklearn.svm' has no attribute '_libsvm'
# (and same for other imports)
from . import _libsvm as libsvm  # type: ignore
from . import _liblinear as liblinear  # type: ignore
from . import _libsvm_sparse as libsvm_sparse  # type: ignore
from ..base import BaseEstimator, ClassifierMixin
from ..preprocessing import LabelEncoder
from ..utils.multiclass import _ovr_decision_function
from ..utils import check_array, check_random_state
from ..utils import column_or_1d
from ..utils import compute_class_weight
from ..utils.metaestimators import available_if
from ..utils.extmath import safe_sparse_dot
from ..utils.validation import check_is_fitted, _check_large_sparse
from ..utils.validation import _num_samples
from ..utils.validation import _check_sample_weight, check_consistent_length
from ..utils.multiclass import check_classification_targets
from ..exceptions import ConvergenceWarning
from ..exceptions import NotFittedError
from scipy.sparse._csr import csr_matrix
from sklearn.svm._classes import NuSVC, NuSVR, OneClassSVM, SVC, SVR

LIBSVM_IMPL: list = ...

def _one_vs_one_coef(dual_coef: ndarray, n_support: ndarray, support_vectors: ndarray) -> List[ndarray]: ...

class BaseLibSVM(BaseEstimator, metaclass=ABCMeta):

    # The order of these must match the integer values in LibSVM.
    # XXX These are actually the same in the dense case. Need to factor
    # this out.
    _sparse_kernels: list = ...

    @abstractmethod
    def __init__(
        self,
        kernel: Union[Callable, str],
        degree: int,
        gamma: Union[int, float, str, float64],
        coef0: Union[int, float],
        tol: float,
        C: Union[int, float, float64],
        nu: float,
        epsilon: float,
        shrinking: bool,
        probability: bool,
        cache_size: int,
        class_weight: Optional[Union[str, Dict[int, int]]],
        verbose: bool,
        max_iter: int,
        random_state: Optional[Union[RandomState, int]],
    ) -> None: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Union[NuSVR, SVR, NuSVC, OneClassSVM, SVC]: ...
    def _validate_targets(self, y: ndarray) -> ndarray: ...
    def _warn_from_fit_status(self) -> None: ...
    def _dense_fit(
        self,
        X: ndarray,
        y: ndarray,
        sample_weight: ndarray,
        solver_type: int,
        kernel: str,
        random_seed: int,
    ) -> None: ...
    def _sparse_fit(self, X, y, sample_weight, solver_type, kernel, random_seed): ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _dense_predict(self, X: ndarray) -> ndarray: ...
    def _sparse_predict(self, X): ...
    def _compute_kernel(self, X: ndarray) -> ndarray: ...
    def _decision_function(self, X: ndarray) -> ndarray: ...
    def _dense_decision_function(self, X: ndarray) -> ndarray: ...
    def _sparse_decision_function(self, X): ...
    def _validate_for_predict(self, X: ndarray) -> ndarray: ...
    @property
    def coef_(self) -> np.ndarray: ...
    def _get_coef(self): ...
    @property
    def n_support_(self) -> ndarray: ...

class BaseSVC(ClassifierMixin, BaseLibSVM, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        kernel: Union[Callable, str],
        degree: int,
        gamma: Union[int, float, str, float64],
        coef0: Union[int, float],
        tol: float,
        C: Union[int, float, float64],
        nu: float,
        shrinking: bool,
        probability: bool,
        cache_size: int,
        class_weight: Optional[Union[str, Dict[int, int]]],
        verbose: bool,
        max_iter: int,
        decision_function_shape: str,
        random_state: Optional[Union[RandomState, int]],
        break_ties: bool,
    ) -> None: ...
    def _validate_targets(self, y: ndarray) -> ndarray: ...
    def decision_function(self, X: ArrayLike) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...

    # Hacky way of getting predict_proba to raise an AttributeError when
    # probability=False using properties. Do not use this in new code; when
    # probabilities are not available depending on a setting, introduce two
    # estimators.
    def _check_proba(self) -> bool: ...
    @available_if(_check_proba)
    def predict_proba(self, X: ArrayLike) -> np.ndarray: ...
    @available_if(_check_proba)
    def predict_log_proba(self, X: ArrayLike) -> np.ndarray: ...
    def _dense_predict_proba(self, X: ndarray) -> ndarray: ...
    def _sparse_predict_proba(self, X): ...
    def _get_coef(self) -> ndarray: ...
    @property
    def probA_(self) -> NDArray: ...
    @property
    def probB_(self) -> NDArray: ...

def _get_liblinear_solver_type(multi_class: str, penalty: str, loss: str, dual: bool) -> int: ...
def _fit_liblinear(
    X: Union[ndarray, csr_matrix],
    y: ndarray,
    C: Union[int, float, float64],
    fit_intercept: bool,
    intercept_scaling: Union[int, float],
    class_weight: None,
    penalty: str,
    dual: bool,
    verbose: int,
    max_iter: int,
    tol: float,
    random_state: Optional[Union[int, RandomState]] = None,
    multi_class: str = "ovr",
    loss: str = "logistic_regression",
    epsilon: float = 0.1,
    sample_weight: None = None,
) -> Tuple[ndarray, ndarray, ndarray]: ...
