from scipy.special import xlogy as xlogy
from collections import namedtuple as namedtuple
from abc import ABCMeta, abstractmethod
from numpy import ndarray
from .._typing import ArrayLike, Float
import numbers

import numpy as np


DistributionBoundary = ...


class ExponentialDispersionModel(metaclass=ABCMeta):
    def in_y_range(self, y: ArrayLike):
        ...

    @abstractmethod
    def unit_variance(self, y_pred: ArrayLike):
        ...

    @abstractmethod
    def unit_deviance(
        self, y: ArrayLike, y_pred: ArrayLike, check_input: bool = False
    ) -> ndarray:
        ...

    def unit_deviance_derivative(self, y: ArrayLike, y_pred: ArrayLike):
        ...

    def deviance(self, y: ArrayLike, y_pred: ArrayLike, weights: ArrayLike | int = 1):
        ...

    def deviance_derivative(
        self, y: ArrayLike, y_pred: ArrayLike, weights: ArrayLike | int = 1
    ):
        ...


class TweedieDistribution(ExponentialDispersionModel):
    def __init__(self, power: Float = 0) -> None:
        ...

    @property
    def power(self):
        ...

    @power.setter
    def power(self, power):
        ...

    def unit_variance(self, y_pred: ArrayLike):
        ...

    def unit_deviance(
        self, y: ArrayLike, y_pred: ArrayLike, check_input: bool = False
    ) -> ndarray:
        ...


class NormalDistribution(TweedieDistribution):
    def __init__(self) -> None:
        ...


class PoissonDistribution(TweedieDistribution):
    def __init__(self) -> None:
        ...


class GammaDistribution(TweedieDistribution):
    def __init__(self) -> None:
        ...


class InverseGaussianDistribution(TweedieDistribution):
    def __init__(self) -> None:
        ...


EDM_DISTRIBUTIONS: dict = ...
