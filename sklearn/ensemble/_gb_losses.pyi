from sklearn.tree._reingold_tilford import Tree
from typing import Optional, Union, Any
from numpy.typing import NDArray

from abc import ABCMeta
from abc import abstractmethod

import numpy as np
from scipy.special import expit, logsumexp

from ..utils.stats import _weighted_percentile
from ..dummy import DummyClassifier
from ..dummy import DummyRegressor
from numpy import float64, int64, ndarray
from sklearn.dummy import DummyClassifier, DummyRegressor

class LossFunction(metaclass=ABCMeta):

    is_multi_class: bool = ...

    def __init__(self, n_classes: int) -> None: ...
    def init_estimator(self): ...
    @abstractmethod
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None): ...
    @abstractmethod
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs): ...
    def update_terminal_regions(
        self,
        tree: Tree,
        X: NDArray,
        y: NDArray,
        residual: NDArray,
        raw_predictions: NDArray,
        sample_weight: NDArray,
        sample_mask: NDArray,
        learning_rate: float = 0.1,
        k: int = 0,
    ) -> None: ...
    @abstractmethod
    def _update_terminal_region(
        self,
        tree,
        terminal_regions,
        leaf,
        X,
        y,
        residual,
        raw_predictions,
        sample_weight,
    ): ...
    @abstractmethod
    def get_init_raw_predictions(self, X: NDArray, estimator: Any) -> NDArray: ...

class RegressionLossFunction(LossFunction, metaclass=ABCMeta):
    def __init__(self) -> None: ...
    def check_init_estimator(self, estimator: Any): ...
    def get_init_raw_predictions(self, X: NDArray, estimator: DummyRegressor) -> NDArray: ...

class LeastSquaresError(RegressionLossFunction):
    def init_estimator(self) -> DummyRegressor: ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None) -> float64: ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs) -> ndarray: ...
    def update_terminal_regions(
        self,
        tree: Tree,
        X: NDArray,
        y: NDArray,
        residual: NDArray,
        raw_predictions: NDArray,
        sample_weight: NDArray,
        sample_mask: NDArray,
        learning_rate: float = 0.1,
        k: int = 0,
    ) -> None: ...
    def _update_terminal_region(
        self,
        tree,
        terminal_regions,
        leaf,
        X,
        y,
        residual,
        raw_predictions,
        sample_weight,
    ): ...

class LeastAbsoluteError(RegressionLossFunction):
    def init_estimator(self): ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None): ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs): ...
    def _update_terminal_region(
        self,
        tree,
        terminal_regions,
        leaf,
        X,
        y,
        residual,
        raw_predictions,
        sample_weight,
    ): ...

class HuberLossFunction(RegressionLossFunction):
    def __init__(self, alpha: float = 0.9): ...
    def init_estimator(self): ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None): ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None, **kargs): ...
    def _update_terminal_region(
        self,
        tree,
        terminal_regions,
        leaf,
        X,
        y,
        residual,
        raw_predictions,
        sample_weight,
    ): ...

class QuantileLossFunction(RegressionLossFunction):
    def __init__(self, alpha: float = 0.9) -> None: ...
    def init_estimator(self) -> DummyRegressor: ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None) -> float64: ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs) -> ndarray: ...
    def _update_terminal_region(
        self,
        tree: Tree,
        terminal_regions: ndarray,
        leaf: int64,
        X: ndarray,
        y: ndarray,
        residual: ndarray,
        raw_predictions: ndarray,
        sample_weight: ndarray,
    ) -> None: ...

class ClassificationLossFunction(LossFunction, metaclass=ABCMeta):
    def _raw_prediction_to_proba(self, raw_predictions): ...
    @abstractmethod
    def _raw_prediction_to_decision(self, raw_predictions): ...
    def check_init_estimator(self, estimator: Any): ...

class BinomialDeviance(ClassificationLossFunction):
    def __init__(self, n_classes: int) -> None: ...
    def init_estimator(self) -> DummyClassifier: ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None) -> float64: ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs) -> ndarray: ...
    def _update_terminal_region(
        self,
        tree: Tree,
        terminal_regions: ndarray,
        leaf: int64,
        X: ndarray,
        y: ndarray,
        residual: ndarray,
        raw_predictions: ndarray,
        sample_weight: ndarray,
    ) -> None: ...
    def _raw_prediction_to_proba(self, raw_predictions: ndarray) -> ndarray: ...
    def _raw_prediction_to_decision(self, raw_predictions: ndarray) -> ndarray: ...
    def get_init_raw_predictions(self, X: NDArray, estimator: DummyClassifier) -> NDArray: ...

class MultinomialDeviance(ClassificationLossFunction):

    is_multi_class: bool = ...

    def __init__(self, n_classes: int) -> None: ...
    def init_estimator(self) -> DummyClassifier: ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None) -> float64: ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, k: int = 0, **kwargs) -> ndarray: ...
    def _update_terminal_region(
        self,
        tree: Tree,
        terminal_regions: ndarray,
        leaf: int64,
        X: ndarray,
        y: ndarray,
        residual: ndarray,
        raw_predictions: ndarray,
        sample_weight: ndarray,
    ) -> None: ...
    def _raw_prediction_to_proba(self, raw_predictions: ndarray) -> ndarray: ...
    def _raw_prediction_to_decision(self, raw_predictions: ndarray) -> ndarray: ...
    def get_init_raw_predictions(self, X: NDArray, estimator: DummyClassifier) -> NDArray: ...

class ExponentialLoss(ClassificationLossFunction):
    def __init__(self, n_classes: int): ...
    def init_estimator(self): ...
    def __call__(self, y: NDArray, raw_predictions: NDArray, sample_weight: NDArray | None = None): ...
    def negative_gradient(self, y: NDArray, raw_predictions: NDArray, **kargs): ...
    def _update_terminal_region(
        self,
        tree,
        terminal_regions,
        leaf,
        X,
        y,
        residual,
        raw_predictions,
        sample_weight,
    ): ...
    def _raw_prediction_to_proba(self, raw_predictions): ...
    def _raw_prediction_to_decision(self, raw_predictions): ...
    def get_init_raw_predictions(self, X: NDArray, estimator: Any) -> NDArray: ...

# TODO: Remove entry 'ls' and 'lad' in version 1.2.
LOSS_FUNCTIONS: dict = ...
