from typing import Any, ClassVar
from scipy.special import expit as expit, logsumexp as logsumexp
from ..tree._tree import TREE_LEAF as TREE_LEAF
from abc import ABCMeta, abstractmethod
from numpy import ndarray
from ..dummy import DummyClassifier, DummyRegressor
from .._typing import Int, ArrayLike, MatrixLike, Float
from ..tree._tree import Tree

import numpy as np


class LossFunction(metaclass=ABCMeta):
    K: int = ...

    is_multi_class: ClassVar[bool] = ...

    def __init__(self, n_classes: Int) -> None:
        ...

    @abstractmethod
    def init_estimator(self):
        ...

    @abstractmethod
    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ):
        ...

    @abstractmethod
    def negative_gradient(self, y: ArrayLike, raw_predictions: MatrixLike, **kargs):
        ...

    def update_terminal_regions(
        self,
        tree: Tree,
        X: ArrayLike,
        y: ArrayLike,
        residual: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: ArrayLike,
        sample_mask: ArrayLike,
        learning_rate: Float = 0.1,
        k: Int = 0,
    ) -> None:
        ...

    @abstractmethod
    def get_init_raw_predictions(self, X: ArrayLike, estimator: Any) -> ndarray:
        ...


class RegressionLossFunction(LossFunction, metaclass=ABCMeta):
    def __init__(self) -> None:
        ...

    def check_init_estimator(self, estimator: Any):
        ...

    def get_init_raw_predictions(self, X: ArrayLike, estimator: Any) -> ndarray:
        ...


class LeastSquaresError(RegressionLossFunction):
    def init_estimator(self) -> DummyRegressor:
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    def negative_gradient(
        self, y: ArrayLike, raw_predictions: ArrayLike, **kargs
    ) -> ndarray:
        ...

    def update_terminal_regions(
        self,
        tree: Tree,
        X: ArrayLike,
        y: ArrayLike,
        residual: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: ArrayLike,
        sample_mask: ArrayLike,
        learning_rate: Float = 0.1,
        k: Int = 0,
    ) -> None:
        ...


class LeastAbsoluteError(RegressionLossFunction):
    def init_estimator(self):
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ):
        ...

    def negative_gradient(self, y: ArrayLike, raw_predictions: MatrixLike, **kargs):
        ...


class HuberLossFunction(RegressionLossFunction):
    def __init__(self, alpha: Float = 0.9) -> None:
        ...

    def init_estimator(self):
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ):
        ...

    def negative_gradient(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
        **kargs
    ):
        ...


class QuantileLossFunction(RegressionLossFunction):
    def __init__(self, alpha: Float = 0.9) -> None:
        ...

    def init_estimator(self) -> DummyRegressor:
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    def negative_gradient(
        self, y: ArrayLike, raw_predictions: MatrixLike, **kargs
    ) -> ndarray:
        ...


class ClassificationLossFunction(LossFunction, metaclass=ABCMeta):
    def check_init_estimator(self, estimator: Any):
        ...


class BinomialDeviance(ClassificationLossFunction):
    def __init__(self, n_classes: Int) -> None:
        ...

    def init_estimator(self) -> DummyClassifier:
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    def negative_gradient(
        self, y: ArrayLike, raw_predictions: MatrixLike, **kargs
    ) -> ndarray:
        ...

    def get_init_raw_predictions(self, X: ArrayLike, estimator: Any) -> ndarray:
        ...


class MultinomialDeviance(ClassificationLossFunction):

    is_multi_class: ClassVar[bool] = ...

    def __init__(self, n_classes: Int) -> None:
        ...

    def init_estimator(self) -> DummyClassifier:
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    def negative_gradient(
        self, y: ArrayLike, raw_predictions: MatrixLike, k: Int = 0, **kwargs
    ) -> ndarray:
        ...

    def get_init_raw_predictions(self, X: ArrayLike, estimator: Any) -> ndarray:
        ...


class ExponentialLoss(ClassificationLossFunction):
    def __init__(self, n_classes: Int) -> None:
        ...

    def init_estimator(self):
        ...

    def __call__(
        self,
        y: ArrayLike,
        raw_predictions: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ):
        ...

    def negative_gradient(self, y: ArrayLike, raw_predictions: MatrixLike, **kargs):
        ...

    def get_init_raw_predictions(self, X: ArrayLike, estimator: Any) -> ndarray:
        ...


LOSS_FUNCTIONS: dict = ...
