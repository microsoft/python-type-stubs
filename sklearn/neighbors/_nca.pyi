from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import softmax as softmax
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Int, MatrixLike, Float, ArrayLike
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_array as check_array,
)
from ..decomposition import PCA as PCA
from numpy import ndarray
from ..utils.random import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real
from scipy.optimize import minimize as minimize
from warnings import warn as warn
from ..metrics import pairwise_distances as pairwise_distances
import numpy as np
import sys
import time


class NeighborhoodComponentsAnalysis(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        init: Literal["auto", "pca", "lda", "identity", "random", "auto"]
        | MatrixLike = "auto",
        warm_start: bool = False,
        max_iter: Int = 50,
        tol: Float = 1e-5,
        callback: None | Callable = None,
        verbose: Int = 0,
        random_state: int | RandomState | None = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
