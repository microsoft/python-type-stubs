from typing import Any
from scipy.special import logsumexp as logsumexp
from ._typing import MatrixLike, ArrayLike, Float, Int
from .base import BaseEstimator, ClassifierMixin
from abc import ABCMeta, abstractmethod as abstractmethod
from numpy import ndarray
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .utils._param_validation import (
    Interval as Interval,
    Hidden as Hidden,
    StrOptions as StrOptions,
)
from numbers import Real as Real, Integral as Integral
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
)
from .preprocessing import (
    binarize,
    LabelBinarizer as LabelBinarizer,
    label_binarize as label_binarize,
)

# Author: Vincent Michel <vincent.michel@inria.fr>
#         Minor fixes by Fabian Pedregosa
#         Amit Aides <amitibo@tx.technion.ac.il>
#         Yehuda Finkelstein <yehudaf@tx.technion.ac.il>
#         Lars Buitinck
#         Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
#         (parts based on earlier work by Mathieu Blondel)
#
# License: BSD 3 clause
import warnings

import numpy as np

__all__ = [
    "BernoulliNB",
    "GaussianNB",
    "MultinomialNB",
    "ComplementNB",
    "CategoricalNB",
]


class _BaseNB(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    def predict_joint_log_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...


class GaussianNB(_BaseNB):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, priors: None | ArrayLike = None, var_smoothing: Float = 1e-9
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> Any:
        ...

    def partial_fit(
        self,
        X: MatrixLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class _BaseDiscreteNB(_BaseNB):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        fit_prior: bool = True,
        class_prior=None,
        force_alpha: str = "warn",
    ) -> None:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class MultinomialNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: bool | str = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
    ) -> None:
        ...


class ComplementNB(_BaseDiscreteNB):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: bool | str = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
        norm: bool = False,
    ) -> None:
        ...


class BernoulliNB(_BaseDiscreteNB):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: bool | str = "warn",
        binarize: None | Float = 0.0,
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
    ) -> None:
        ...


class CategoricalNB(_BaseDiscreteNB):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        force_alpha: bool | str = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
        min_categories: None | Int | ArrayLike = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...
