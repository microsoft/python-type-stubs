from numpy import ndarray
from typing import Iterator, Optional, Union, Callable, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Peter Prettenhofer, Scott White, Gilles Louppe, Emanuele Olivetti,
#          Arnaud Joly, Jacob Schreiber
# License: BSD 3 clause

from abc import ABCMeta
from abc import abstractmethod
import warnings

from ._base import BaseEnsemble
from ..base import ClassifierMixin
from ..base import RegressorMixin
from ..base import BaseEstimator
from ..base import is_classifier
from ..utils import deprecated

import numbers
import numpy as np

from scipy.sparse import csc_matrix
from scipy.sparse import csr_matrix
from scipy.sparse import issparse

from time import time
from ..model_selection import train_test_split
from ..tree import DecisionTreeRegressor
from . import _gb_losses

from ..utils import check_random_state
from ..utils import check_array
from ..utils import check_scalar
from ..utils import column_or_1d
from ..utils.validation import check_is_fitted, _check_sample_weight
from ..utils.multiclass import check_classification_targets
from ..exceptions import NotFittedError
from numpy.random import RandomState

class VerboseReporter:
    def __init__(self, verbose: int): ...
    def init(self, est: BaseEstimator, begin_at_stage: int = 0): ...
    def update(self, j: int, est: BaseEstimator): ...

class BaseGradientBoosting(BaseEnsemble, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        *,
        loss,
        learning_rate,
        n_estimators,
        criterion,
        min_samples_split,
        min_samples_leaf,
        min_weight_fraction_leaf,
        max_depth,
        min_impurity_decrease,
        init,
        subsample,
        max_features,
        ccp_alpha,
        random_state,
        alpha=0.9,
        verbose=0,
        max_leaf_nodes=None,
        warm_start=False,
        validation_fraction=0.1,
        n_iter_no_change=None,
        tol=1e-4,
    ) -> None: ...
    @abstractmethod
    def _validate_y(self, y, sample_weight=None): ...
    def _fit_stage(
        self,
        i: int,
        X: ndarray,
        y: ndarray,
        raw_predictions: ndarray,
        sample_weight: ndarray,
        sample_mask: ndarray,
        random_state: RandomState,
        X_csc: None = None,
        X_csr: None = None,
    ) -> ndarray: ...
    def _check_params(self) -> None: ...
    def _init_state(self) -> None: ...
    def _clear_state(self) -> None: ...
    def _resize_state(self): ...
    def _is_initialized(self) -> bool: ...
    def _check_initialized(self) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
        monitor: Callable | None = None,
    ) -> Union[GradientBoostingRegressor, GradientBoostingClassifier]: ...
    def _fit_stages(
        self,
        X: ndarray,
        y: ndarray,
        raw_predictions: ndarray,
        sample_weight: ndarray,
        random_state: RandomState,
        X_val: Optional[ndarray],
        y_val: Optional[ndarray],
        sample_weight_val: Optional[ndarray],
        begin_at_stage: int = 0,
        monitor: None = None,
    ) -> int: ...
    def _make_estimator(self, append=True): ...
    def _raw_predict_init(self, X: ndarray) -> ndarray: ...
    def _raw_predict(self, X: ndarray) -> ndarray: ...
    def _staged_raw_predict(self, X: ndarray, check_input: bool = True) -> Iterator[ndarray]: ...
    @property
    def feature_importances_(self) -> NDArray: ...
    def _compute_partial_dependence_recursion(self, grid, target_features): ...
    def apply(self, X: NDArray | ArrayLike) -> ArrayLike: ...

    # TODO(1.2): Remove
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `n_features_` was deprecated in version 1.0 and will be " "removed in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...

    # TODO(1.3): Remove
    # mypy error: Decorated property not supported
    @deprecated("Attribute `loss_` was deprecated in version 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def loss_(self): ...

class GradientBoostingClassifier(ClassifierMixin, BaseGradientBoosting):

    # TODO(1.3): remove "deviance"
    _SUPPORTED_LOSS = ...

    def __init__(
        self,
        *,
        loss: Literal["log_loss", "deviance", "exponential"] = "log_loss",
        learning_rate: float = 0.1,
        n_estimators: int = 100,
        subsample: float = 1.0,
        criterion: Literal["friedman_mse", "squared_error", "mse"] = "friedman_mse",
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_depth: int = 3,
        min_impurity_decrease: float = 0.0,
        init: BaseEstimator | Literal["zero"] | None = None,
        random_state: int | RandomState | None = None,
        max_features: Literal["auto", "sqrt", "log2"] | int | float | None = None,
        verbose: int = 0,
        max_leaf_nodes: int | None = None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int | None = None,
        tol: float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def _validate_y(self, y: ndarray, sample_weight: ndarray) -> ndarray: ...
    def decision_function(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def staged_decision_function(self, X: NDArray | ArrayLike): ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def staged_predict(self, X: NDArray | ArrayLike): ...
    def predict_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def predict_log_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def staged_predict_proba(self, X: NDArray | ArrayLike) -> Iterator[ndarray]: ...

class GradientBoostingRegressor(RegressorMixin, BaseGradientBoosting):

    # TODO(1.2): remove "ls" and "lad"
    _SUPPORTED_LOSS = ...

    def __init__(
        self,
        *,
        loss: Literal["squared_error", "absolute_error", "huber", "quantile"] = "squared_error",
        learning_rate: float = 0.1,
        n_estimators: int = 100,
        subsample: float = 1.0,
        criterion: Literal["friedman_mse", "squared_error", "mse"] = "friedman_mse",
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_depth: int = 3,
        min_impurity_decrease: float = 0.0,
        init: BaseEstimator | Literal["zero"] | None = None,
        random_state: int | RandomState | None = None,
        max_features: Literal["auto", "sqrt", "log2"] | int | float | None = None,
        alpha: float = 0.9,
        verbose: int = 0,
        max_leaf_nodes: int | None = None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int | None = None,
        tol: float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def _validate_y(self, y: ndarray, sample_weight: None = None) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def staged_predict(self, X: NDArray | ArrayLike) -> Iterator[ndarray]: ...
    def apply(self, X: NDArray | ArrayLike) -> ArrayLike: ...
