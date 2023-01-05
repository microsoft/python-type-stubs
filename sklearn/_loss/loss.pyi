from numpy import float64, ndarray
from sklearn._typing import Scalar
from typing import Optional, Tuple, Type, Union, Literal
from numpy.typing import NDArray, ArrayLike

# Goals:
# - Provide a common private module for loss functions/classes.
# - To be used in:
#   - LogisticRegression
#   - PoissonRegressor, GammaRegressor, TweedieRegressor
#   - HistGradientBoostingRegressor, HistGradientBoostingClassifier
#   - GradientBoostingRegressor, GradientBoostingClassifier
#   - SGDRegressor, SGDClassifier
# - Replace link module of GLMs.

import numbers
import numpy as np
from scipy.special import xlogy

from .link import (
    Interval,
    IdentityLink,
    LogLink,
    LogitLink,
    MultinomialLogit,
)
from ..utils import check_scalar
from ..utils.stats import _weighted_percentile
from sklearn._loss.link import IdentityLink, LogLink, LogitLink, MultinomialLogit

class CyLossFunction:
    def cy_loss(self, y_true: float, raw_prediction: float) -> float: ...
    def cy_gradient(self, y_true: float, raw_prediction: float) -> float: ...
    def cy_grad_hess(self, y_true: float, raw_prediction: float) -> tuple[float, float]: ...

class CyHalfSquaredError(CyLossFunction): ...
class CyAbsoluteError(CyLossFunction): ...
class CyPinballLoss(CyLossFunction): ...
class CyHalfPoissonLoss(CyLossFunction): ...
class CyHalfGammaLoss(CyLossFunction): ...
class CyHalfTweedieLoss(CyLossFunction): ...
class CyHalfTweedieLossIdentity(CyLossFunction): ...
class CyHalfBinomialLoss(CyLossFunction): ...
class CyHalfMultinomialLoss(CyLossFunction): ...

# Note: The shape of raw_prediction for multiclass classifications are
# - GradientBoostingClassifier: (n_samples, n_classes)
# - HistGradientBoostingClassifier: (n_classes, n_samples)
#
# Note: Instead of inheritance like
#
#    class BaseLoss(BaseLink, CyLossFunction):
#    ...
#
#    # Note: Naturally, we would inherit in the following order
#    #     class HalfSquaredError(IdentityLink, CyHalfSquaredError, BaseLoss)
#    #   But because of https://github.com/cython/cython/issues/4350 we set BaseLoss as
#    #   the last one. This, of course, changes the MRO.
#    class HalfSquaredError(IdentityLink, CyHalfSquaredError, BaseLoss):
#
# we use composition. This way we improve maintainability by avoiding the above
# mentioned Cython edge case and have easier to understand code (which method calls
# which code).
class BaseLoss:

    # For decision trees:
    # This variable indicates whether the loss requires the leaves values to
    # be updated once the tree has been trained. The trees are trained to
    # predict a Newton-Raphson step (see grower._finalize_leaf()). But for
    # some losses (e.g. least absolute deviation) we need to adjust the tree
    # values to account for the "line search" of the gradient descent
    # procedure. See the original paper Greedy Function Approximation: A
    # Gradient Boosting Machine by Friedman
    # (https://statweb.stanford.edu/~jhf/ftp/trebst.pdf) for the theory.
    need_update_leaves_values: bool = ...
    differentiable: bool = ...
    is_multiclass: bool = ...

    def __init__(
        self,
        closs: Union[
            CyHalfPoissonLoss,
            CyHalfMultinomialLoss,
            CyHalfBinomialLoss,
            CyPinballLoss,
            CyHalfSquaredError,
        ],
        link: Union[LogitLink, IdentityLink, MultinomialLogit, LogLink],
        n_classes: int | None = None,
    ) -> None: ...
    def in_y_true_range(self, y: NDArray) -> bool: ...
    def in_y_pred_range(self, y: NDArray): ...
    def loss(
        self,
        y_true: NDArray,
        raw_prediction: NDArray,
        sample_weight: NDArray | None = None,
        loss_out: NDArray | None = None,
        n_threads: int = 1,
    ) -> ArrayLike: ...
    def loss_gradient(
        self,
        y_true: NDArray,
        raw_prediction: NDArray,
        sample_weight: NDArray | None = None,
        loss_out: NDArray | None = None,
        gradient_out: NDArray | None = None,
        n_threads: int = 1,
    ) -> tuple[ArrayLike, ArrayLike]: ...
    def gradient(
        self,
        y_true: NDArray,
        raw_prediction: NDArray,
        sample_weight: NDArray | None = None,
        gradient_out: NDArray | None = None,
        n_threads: int = 1,
    ) -> ArrayLike: ...
    def gradient_hessian(
        self,
        y_true: NDArray,
        raw_prediction: NDArray,
        sample_weight: NDArray | None = None,
        gradient_out: NDArray | None = None,
        hessian_out: NDArray | None = None,
        n_threads: int = 1,
    ) -> tuple[NDArray, NDArray]: ...
    def __call__(
        self,
        y_true: NDArray,
        raw_prediction: NDArray,
        sample_weight: NDArray | None = None,
        n_threads: int = 1,
    ) -> float: ...
    def fit_intercept_only(self, y_true: ArrayLike, sample_weight: ArrayLike | None = None) -> Scalar | NDArray: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...
    def init_gradient_and_hessian(
        self,
        n_samples: int,
        dtype: float64 | np.float32 = ...,
        order: Literal["C", "F"] = "F",
    ) -> tuple[NDArray, NDArray]: ...

# Note: Naturally, we would inherit in the following order
#         class HalfSquaredError(IdentityLink, CyHalfSquaredError, BaseLoss)
#       But because of https://github.com/cython/cython/issues/4350 we
#       set BaseLoss as the last one. This, of course, changes the MRO.
class HalfSquaredError(BaseLoss):
    def __init__(self, sample_weight: None = None) -> None: ...

class AbsoluteError(BaseLoss):

    differentiable: bool = ...
    need_update_leaves_values: bool = ...

    def __init__(self, sample_weight=None): ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...

class PinballLoss(BaseLoss):

    differentiable: bool = ...
    need_update_leaves_values: bool = ...

    def __init__(self, sample_weight: None = None, quantile: float = 0.5) -> None: ...
    def fit_intercept_only(self, y_true: ndarray, sample_weight: None = None) -> float64: ...

class HalfPoissonLoss(BaseLoss):
    def __init__(self, sample_weight: None = None) -> None: ...
    def constant_to_optimal_zero(self, y_true: ndarray, sample_weight: None = None) -> ndarray: ...

class HalfGammaLoss(BaseLoss):
    def __init__(self, sample_weight=None): ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...

class HalfTweedieLoss(BaseLoss):
    def __init__(self, sample_weight=None, power=1.5): ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...

class HalfTweedieLossIdentity(BaseLoss):
    def __init__(self, sample_weight=None, power=1.5): ...

class HalfBinomialLoss(BaseLoss):
    def __init__(self, sample_weight: None = None) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...
    def predict_proba(self, raw_prediction: ArrayLike) -> NDArray: ...

class HalfMultinomialLoss(BaseLoss):

    is_multiclass: bool = ...

    def __init__(self, sample_weight: None = None, n_classes: int = 3) -> None: ...
    def in_y_true_range(self, y: NDArray): ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...
    def predict_proba(self, raw_prediction: ArrayLike) -> ArrayLike: ...
    def gradient_proba(
        self,
        y_true: NDArray,
        raw_prediction: ArrayLike,
        sample_weight: NDArray | None = None,
        gradient_out: ArrayLike | None = None,
        proba_out: ArrayLike | None = None,
        n_threads: int = 1,
    ) -> tuple[ArrayLike, ArrayLike]: ...

_LOSSES: dict = ...
