from ..utils.extmath import softmax as softmax
from dataclasses import dataclass
from scipy.special import expit as expit, logit as logit
from .._typing import ArrayLike, Float
from abc import ABC, abstractmethod
from scipy.stats import gmean as gmean
from numpy import ndarray

import numpy as np


@dataclass
class Interval:
    low: float = ...
    high: float = ...
    low_inclusive: bool = ...
    high_inclusive: bool = ...

    def __post_init__(self) -> None:
        ...

    def includes(self, x: ArrayLike) -> bool:
        ...


class BaseLink(ABC):

    is_multiclass: bool = ...  # used for testing only

    # Usually, raw_prediction may be any real number and y_pred is an open
    # interval.
    # interval_raw_prediction = Interval(-np.inf, np.inf, False, False)
    interval_y_pred = ...

    @abstractmethod
    def link(self, y_pred: ArrayLike, out: None | ArrayLike = None) -> ndarray:
        ...

    @abstractmethod
    def inverse(
        self, raw_prediction: ArrayLike, out: None | ArrayLike = None
    ) -> ndarray:
        ...


class IdentityLink(BaseLink):
    def link(
        self, y_pred: Float | ArrayLike, out: None | ArrayLike = None
    ) -> Float | ndarray:
        ...

    def inverse(
        self, y_pred: Float | ArrayLike, out: None | ArrayLike = None
    ) -> Float | ndarray:
        ...


class LogLink(BaseLink):

    interval_y_pred = ...

    def link(
        self, y_pred: Float | ArrayLike, out: None | ArrayLike = None
    ) -> Float | ndarray:
        ...

    def inverse(
        self, raw_prediction: ArrayLike, out: None | ArrayLike = None
    ) -> ndarray:
        ...


class LogitLink(BaseLink):

    interval_y_pred = ...

    def link(
        self, y_pred: Float | ArrayLike, out: None | ArrayLike = None
    ) -> Float | ndarray:
        ...

    def inverse(
        self, raw_prediction: ArrayLike, out: None | ArrayLike = None
    ) -> ndarray:
        ...


class MultinomialLogit(BaseLink):

    is_multiclass: bool = ...
    interval_y_pred = ...

    def symmetrize_raw_prediction(self, raw_prediction):
        ...

    def link(self, y_pred: ArrayLike, out: None | ArrayLike = None) -> ndarray:
        ...

    def inverse(
        self, raw_prediction: ArrayLike, out: None | ArrayLike = None
    ) -> ndarray:
        ...


_LINKS: dict = ...
