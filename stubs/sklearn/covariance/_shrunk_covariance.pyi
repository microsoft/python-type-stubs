import warnings
from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar
from typing_extensions import Self

import numpy as np
from numpy import ndarray

from .._config import config_context as config_context
from .._typing import Float, Int, MatrixLike
from ..utils import check_array as check_array
from ..utils._param_validation import Interval as Interval
from . import EmpiricalCovariance, empirical_covariance as empirical_covariance

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

# avoid division truncation

# ShrunkCovariance estimator

def shrunk_covariance(emp_cov: MatrixLike, shrinkage: Float = 0.1) -> ndarray: ...

class ShrunkCovariance(EmpiricalCovariance):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    precision_: ndarray = ...
    location_: ndarray = ...
    covariance_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False, shrinkage: Float = 0.1) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...

# Ledoit-Wolf estimator

def ledoit_wolf_shrinkage(X: MatrixLike, assume_centered: bool = False, block_size: Int = 1000) -> Float: ...
def ledoit_wolf(
    X: MatrixLike, *, assume_centered: bool = False, block_size: Int = 1000
) -> tuple[ndarray, Float] | tuple[ndarray, float]: ...

class LedoitWolf(EmpiricalCovariance):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    shrinkage_: float = ...
    precision_: ndarray = ...
    location_: ndarray = ...
    covariance_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, store_precision: bool = True, assume_centered: bool = False, block_size: Int = 1000) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...

# OAS estimator
def oas(X: MatrixLike, *, assume_centered: bool = False) -> tuple[ndarray, Float] | tuple[ndarray, float]: ...

class OAS(EmpiricalCovariance):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    shrinkage_: float = ...
    precision_: ndarray = ...
    location_: ndarray = ...
    covariance_: ndarray = ...

    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
