from typing import Optional, Tuple, Callable, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: William de Vazelhes <wdevazelhes@gmail.com>
#          John Chiotellis <ioannis.chiotellis@in.tum.de>
# License: BSD 3 clause

from warnings import warn
import numpy as np
import sys
import time
import numbers
from scipy.optimize import minimize
from ..utils.extmath import softmax
from ..metrics import pairwise_distances
from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..preprocessing import LabelEncoder
from ..decomposition import PCA
from ..utils.multiclass import check_classification_targets
from ..utils.random import check_random_state
from ..utils.validation import check_is_fitted, check_array, check_scalar
from ..exceptions import ConvergenceWarning
from numpy import float64, ndarray
from numpy.random import RandomState

class NeighborhoodComponentsAnalysis(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        init: Literal["auto", "pca", "lda", "identity", "random"] | NDArray = "auto",
        warm_start: bool = False,
        max_iter: int = 50,
        tol: float = 1e-5,
        callback: Callable | None = None,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "NeighborhoodComponentsAnalysis": ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def _validate_params(self, X: ndarray, y: ndarray) -> Tuple[ndarray, ndarray, str]: ...
    def _initialize(self, X: ndarray, y: ndarray, init: str) -> ndarray: ...
    def _callback(self, transformation: ndarray) -> None: ...
    def _loss_grad_lbfgs(
        self,
        transformation: ndarray,
        X: ndarray,
        same_class_mask: ndarray,
        sign: float = 1.0,
    ) -> Tuple[float64, ndarray]: ...
    def _more_tags(self): ...
