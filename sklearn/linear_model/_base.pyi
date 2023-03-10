from typing import Any, Self
from scipy.special import expit as expit
from .._typing import MatrixLike, ArrayLike, Int
from ..utils._array_api import get_namespace as get_namespace
from ..utils.sparsefuncs import (
    mean_variance_axis as mean_variance_axis,
    inplace_column_scale as inplace_column_scale,
)
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from scipy.sparse.linalg import lsqr as lsqr
from abc import ABCMeta, abstractmethod
from ..utils import check_array as check_array, check_random_state as check_random_state
from scipy import linalg as linalg, optimize as optimize, sparse
from ..utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from ._stochastic_gradient import SGDClassifier
from numpy.random import RandomState
from ..base import BaseEstimator, ClassifierMixin, RegressorMixin, MultiOutputMixin
from ..utils._seq_dataset import ArrayDataset64, CSRDataset64
from numbers import Integral as Integral
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils._seq_dataset import (
    ArrayDataset32 as ArrayDataset32,
    CSRDataset32 as CSRDataset32,
)
import numbers
import warnings

import numpy as np
import scipy.sparse as sp

# TODO: bayesian_ridge_regression and bayesian_regression_ard
# should be squashed into its respective objects.

SPARSE_INTERCEPT_DECAY: float = ...


def make_dataset(
    X: MatrixLike,
    y: ArrayLike,
    sample_weight: ArrayLike,
    random_state: RandomState | None | Int = None,
) -> tuple[ArrayDataset64, float] | tuple[ArrayDataset64 | CSRDataset64, float] | tuple[
    CSRDataset64, float
]:
    ...


class LinearModel(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y):
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...


# XXX Should this derive from LinearModel? It should be a mixin, not an ABC.
# Maybe the n_features checking can be moved to LinearModel.
class LinearClassifierMixin(ClassifierMixin):
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class SparseCoefMixin:
    def densify(self) -> Self:
        ...

    def sparsify(self) -> SGDClassifier | Self:
        ...


class LinearRegression(MultiOutputMixin, RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        n_jobs: None | Int = None,
        positive: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...
