from numpy.typing import NDArray, ArrayLike

# Author: Christian Lorentzen <lorentzen.ch@gmail.com>

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from scipy.special import expit, logit
from scipy.stats import gmean
from ..utils.extmath import softmax
from numpy import float64, ndarray
from typing import Union

@dataclass
class Interval:
    low: float = ...
    high: float = ...
    low_inclusive: bool = ...
    high_inclusive: bool = ...

    def __post_init__(self) -> None: ...
    def includes(self, x: NDArray) -> bool: ...

def _inclusive_low_high(interval, dtype=np.float64): ...

class BaseLink(ABC):

    is_multiclass: bool = ...  # used for testing only

    # Usually, raw_prediction may be any real number and y_pred is an open
    # interval.
    # interval_raw_prediction = Interval(-np.inf, np.inf, False, False)
    interval_y_pred = ...

    @abstractmethod
    def link(self, y_pred: ArrayLike, out: ArrayLike | None = None) -> ArrayLike: ...
    @abstractmethod
    def inverse(
        self, raw_prediction: ArrayLike, out: ArrayLike | None = None
    ) -> ArrayLike: ...

class IdentityLink(BaseLink):
    def link(self, y_pred: ArrayLike, out: ArrayLike | None = None) -> ArrayLike: ...

    inverse = link

class LogLink(BaseLink):

    interval_y_pred = ...

    def link(self, y_pred: ArrayLike, out: ArrayLike | None = None) -> ArrayLike: ...
    def inverse(
        self, raw_prediction: ArrayLike, out: ArrayLike | None = None
    ) -> ArrayLike: ...

class LogitLink(BaseLink):

    interval_y_pred = ...

    def link(self, y_pred: ArrayLike, out: ArrayLike | None = None) -> ArrayLike: ...
    def inverse(
        self, raw_prediction: ArrayLike, out: ArrayLike | None = None
    ) -> ArrayLike: ...

class MultinomialLogit(BaseLink):

    is_multiclass: bool = ...
    interval_y_pred = ...

    def symmetrize_raw_prediction(self, raw_prediction): ...
    def link(self, y_pred: ArrayLike, out: ArrayLike | None = None) -> ArrayLike: ...
    def inverse(
        self, raw_prediction: ArrayLike, out: ArrayLike | None = None
    ) -> ArrayLike: ...

_LINKS: dict = ...
