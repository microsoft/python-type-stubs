from numpy import ndarray
from numpy.typing import ArrayLike, NDArray

# Author: Christian Lorentzen <lorentzen.ch@googlemail.com>
# License: BSD 3 clause
#
# TODO(1.3): remove file
#       This is only used for backward compatibility in _GeneralizedLinearRegressor
#       for the deprecated family attribute.

from abc import ABCMeta, abstractmethod
from collections import namedtuple
import numbers

import numpy as np
from scipy.special import xlogy

DistributionBoundary = ...

class ExponentialDispersionModel(metaclass=ABCMeta):
    def in_y_range(self, y: ArrayLike): ...
    @abstractmethod
    def unit_variance(self, y_pred: ArrayLike): ...
    @abstractmethod
    def unit_deviance(
        self, y: ArrayLike, y_pred: ArrayLike, check_input: bool = False
    ) -> ArrayLike: ...
    def unit_deviance_derivative(self, y: ArrayLike, y_pred: ArrayLike): ...
    def deviance(self, y: ArrayLike, y_pred: ArrayLike, weights: NDArray | int = 1): ...
    def deviance_derivative(
        self, y: NDArray, y_pred: NDArray, weights: NDArray | int = 1
    ): ...

class TweedieDistribution(ExponentialDispersionModel):
    def __init__(self, power: float = 0): ...
    @property
    def power(self): ...
    @power.setter
    def power(self, power): ...
    def unit_variance(self, y_pred: ArrayLike): ...
    def unit_deviance(
        self, y: ArrayLike, y_pred: ArrayLike, check_input: bool = False
    ) -> ArrayLike: ...

class NormalDistribution(TweedieDistribution):
    def __init__(self): ...

class PoissonDistribution(TweedieDistribution):
    def __init__(self): ...

class GammaDistribution(TweedieDistribution):
    def __init__(self): ...

class InverseGaussianDistribution(TweedieDistribution):
    def __init__(self): ...

EDM_DISTRIBUTIONS: dict = ...
