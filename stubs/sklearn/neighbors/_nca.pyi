from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Literal, TypeVar
from warnings import warn as warn

from numpy import ndarray
from numpy.random import RandomState
from scipy.optimize import minimize as minimize

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..decomposition import PCA as PCA
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import pairwise_distances as pairwise_distances
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import softmax as softmax
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.random import check_random_state as check_random_state
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted

NeighborhoodComponentsAnalysis_Self = TypeVar("NeighborhoodComponentsAnalysis_Self", bound="NeighborhoodComponentsAnalysis")

import sys
import time

import numpy as np

class NeighborhoodComponentsAnalysis(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    random_state_: RandomState = ...
    n_iter_: int = ...
    n_features_in_: int = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        init: Literal["auto", "pca", "lda", "identity", "random", "auto"] | MatrixLike = "auto",
        warm_start: bool = False,
        max_iter: Int = 50,
        tol: Float = 1e-5,
        callback: None | Callable = None,
        verbose: Int = 0,
        random_state: None | RandomState | int = None,
    ) -> None: ...
    def fit(self: NeighborhoodComponentsAnalysis_Self, X: MatrixLike, y: ArrayLike) -> NeighborhoodComponentsAnalysis_Self: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
