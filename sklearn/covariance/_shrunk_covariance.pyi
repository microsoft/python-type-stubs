from typing import Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation
import warnings
import numpy as np

from . import empirical_covariance, EmpiricalCovariance
from .._config import config_context
from ..utils import check_array
from numpy import float64, ndarray

# ShrunkCovariance estimator

def shrunk_covariance(emp_cov: ArrayLike, shrinkage: float = 0.1) -> NDArray: ...

class ShrunkCovariance(EmpiricalCovariance):
    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False, shrinkage: float = 0.1) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "ShrunkCovariance": ...

# Ledoit-Wolf estimator

def ledoit_wolf_shrinkage(X: ArrayLike, assume_centered: bool = False, block_size: int = 1000) -> float: ...
def ledoit_wolf(X: ArrayLike, *, assume_centered: bool = False, block_size: int = 1000) -> tuple[NDArray, float]: ...

class LedoitWolf(EmpiricalCovariance):
    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False, block_size: int = 1000) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "LedoitWolf": ...

# OAS estimator
def oas(X: ArrayLike, *, assume_centered: bool = False) -> tuple[ArrayLike, float]: ...

class OAS(EmpiricalCovariance):
    def fit(self, X: ArrayLike, y: None = None) -> "OAS": ...
