from typing import Any
from ..utils._param_validation import Interval as Interval
from .._typing import MatrixLike, Float, Int
from numpy import ndarray
from . import empirical_covariance as empirical_covariance, EmpiricalCovariance
from ..utils import check_array as check_array
from numbers import Real as Real, Integral as Integral
from .._config import config_context as config_context

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation
import warnings
import numpy as np


# ShrunkCovariance estimator


def shrunk_covariance(emp_cov: MatrixLike, shrinkage: Float = 0.1) -> ndarray:
    ...


class ShrunkCovariance(EmpiricalCovariance):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        shrinkage: Float = 0.1
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...


# Ledoit-Wolf estimator


def ledoit_wolf_shrinkage(
    X: MatrixLike, assume_centered: bool = False, block_size: Int = 1000
) -> Float:
    ...


def ledoit_wolf(
    X: MatrixLike, *, assume_centered: bool = False, block_size: Int = 1000
) -> tuple[ndarray, float] | tuple[ndarray, Float]:
    ...


class LedoitWolf(EmpiricalCovariance):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        block_size: Int = 1000
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...


# OAS estimator
def oas(
    X: MatrixLike, *, assume_centered: bool = False
) -> tuple[ndarray, float] | tuple[ndarray, Float]:
    ...


class OAS(EmpiricalCovariance):
    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...
