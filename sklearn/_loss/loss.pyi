from typing import Literal, Type
from .link import IdentityLink, LogLink, LogitLink, MultinomialLogit
from scipy.special import xlogy as xlogy
from ._loss import (
    CyHalfSquaredError,
    CyAbsoluteError as CyAbsoluteError,
    CyPinballLoss as CyPinballLoss,
    CyHalfPoissonLoss as CyHalfPoissonLoss,
    CyHalfGammaLoss as CyHalfGammaLoss,
    CyHalfTweedieLoss as CyHalfTweedieLoss,
    CyHalfTweedieLossIdentity as CyHalfTweedieLossIdentity,
    CyHalfBinomialLoss as CyHalfBinomialLoss,
    CyHalfMultinomialLoss as CyHalfMultinomialLoss,
)
from .._typing import ArrayLike, MatrixLike, Int, Float, Scalar
from ..utils._readonly_array_wrapper import ReadonlyArrayWrapper as ReadonlyArrayWrapper
from numpy import ndarray
from ..utils import check_scalar as check_scalar
from .link import Interval as Interval

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
        closs,
        link: IdentityLink | MultinomialLogit | LogitLink | LogLink,
        n_classes: int | None = None,
    ) -> None:
        ...

    def in_y_true_range(self, y: ArrayLike) -> bool:
        ...

    def in_y_pred_range(self, y: ArrayLike):
        ...

    def loss(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        loss_out: None | ArrayLike = None,
        n_threads: Int = 1,
    ) -> ndarray:
        ...

    def loss_gradient(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        loss_out: None | ArrayLike = None,
        gradient_out: None | MatrixLike | ArrayLike = None,
        n_threads: Int = 1,
    ) -> tuple[ndarray, ndarray]:
        ...

    def gradient(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        gradient_out: None | MatrixLike | ArrayLike = None,
        n_threads: Int = 1,
    ) -> ndarray:
        ...

    def gradient_hessian(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        gradient_out: None | MatrixLike | ArrayLike = None,
        hessian_out: None | MatrixLike | ArrayLike = None,
        n_threads: Int = 1,
    ) -> tuple[ndarray, ndarray]:
        ...

    def __call__(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        n_threads: Int = 1,
    ) -> Float:
        ...

    def fit_intercept_only(
        self, y_true: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> Scalar | Float | ndarray:
        ...

    def constant_to_optimal_zero(self, y_true, sample_weight=None):
        ...

    def init_gradient_and_hessian(
        self,
        n_samples: Int,
        dtype: Float | Type[Float] = ...,
        order: Literal["C", "F", "F"] = "F",
    ) -> tuple[ndarray, ndarray]:
        ...


# Note: Naturally, we would inherit in the following order
#         class HalfSquaredError(IdentityLink, CyHalfSquaredError, BaseLoss)
#       But because of https://github.com/cython/cython/issues/4350 we
#       set BaseLoss as the last one. This, of course, changes the MRO.
class HalfSquaredError(BaseLoss):
    def __init__(self, sample_weight=None) -> None:
        ...


class AbsoluteError(BaseLoss):

    differentiable: bool = ...
    need_update_leaves_values: bool = ...

    def __init__(self, sample_weight=None) -> None:
        ...

    def fit_intercept_only(self, y_true, sample_weight=None):
        ...


class PinballLoss(BaseLoss):

    differentiable: bool = ...
    need_update_leaves_values: bool = ...

    def __init__(self, sample_weight=None, quantile: float = 0.5) -> None:
        ...

    def fit_intercept_only(self, y_true: ndarray, sample_weight=None) -> Float:
        ...


class HalfPoissonLoss(BaseLoss):
    def __init__(self, sample_weight: None | ndarray = None) -> None:
        ...

    def constant_to_optimal_zero(self, y_true: ndarray, sample_weight=None) -> ndarray:
        ...


class HalfGammaLoss(BaseLoss):
    def __init__(self, sample_weight=None) -> None:
        ...

    def constant_to_optimal_zero(self, y_true: ndarray, sample_weight=None) -> ndarray:
        ...


class HalfTweedieLoss(BaseLoss):
    def __init__(self, sample_weight=None, power: float = 1.5) -> None:
        ...

    def constant_to_optimal_zero(self, y_true: ndarray, sample_weight=None) -> ndarray:
        ...


class HalfTweedieLossIdentity(BaseLoss):
    def __init__(self, sample_weight=None, power: float = 1.5) -> None:
        ...


class HalfBinomialLoss(BaseLoss):
    def __init__(self, sample_weight=None) -> None:
        ...

    def constant_to_optimal_zero(self, y_true, sample_weight=None):
        ...

    def predict_proba(self, raw_prediction: MatrixLike | ArrayLike) -> ndarray:
        ...


class HalfMultinomialLoss(BaseLoss):

    is_multiclass: bool = ...

    def __init__(self, sample_weight=None, n_classes: int = 3) -> None:
        ...

    def in_y_true_range(self, y: ArrayLike):
        ...

    def fit_intercept_only(self, y_true, sample_weight=None):
        ...

    def predict_proba(self, raw_prediction: MatrixLike) -> ndarray:
        ...

    def gradient_proba(
        self,
        y_true: ArrayLike,
        raw_prediction: MatrixLike,
        sample_weight: None | ArrayLike = None,
        gradient_out: None | MatrixLike = None,
        proba_out: None | MatrixLike = None,
        n_threads: Int = 1,
    ) -> tuple[ndarray, ndarray]:
        ...


_LOSSES: dict = ...
