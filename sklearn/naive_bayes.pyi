from typing import ClassVar, TypeVar
from scipy.special import logsumexp as logsumexp
from abc import ABCMeta, abstractmethod as abstractmethod
from .base import BaseEstimator, ClassifierMixin
from .preprocessing import (
    binarize,
    LabelBinarizer as LabelBinarizer,
    label_binarize as label_binarize,
)
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
)
from numpy import ndarray
from numbers import Real as Real, Integral as Integral
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .utils._param_validation import (
    Interval as Interval,
    Hidden as Hidden,
    StrOptions as StrOptions,
)
from ._typing import MatrixLike, ArrayLike, Float, Int

_BaseDiscreteNB_Self = TypeVar("_BaseDiscreteNB_Self", bound="_BaseDiscreteNB")
GaussianNB_Self = TypeVar("GaussianNB_Self", bound="GaussianNB")
CategoricalNB_Self = TypeVar("CategoricalNB_Self", bound="CategoricalNB")


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
    theta_: ndarray = ...
    var_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    epsilon_: float = ...
    classes_: ndarray = ...
    class_prior_: ndarray = ...
    class_count_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, *, priors: None | ArrayLike = None, var_smoothing: Float = 1e-9
    ) -> None:
        ...

    def fit(
        self: GaussianNB_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> GaussianNB_Self:
        ...

    def partial_fit(
        self: GaussianNB_Self,
        X: MatrixLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> GaussianNB_Self:
        ...


class _BaseDiscreteNB(_BaseNB):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        fit_prior: bool = True,
        class_prior=None,
        force_alpha: str = "warn",
    ) -> None:
        ...

    def partial_fit(
        self: _BaseDiscreteNB_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> MultinomialNB | _BaseDiscreteNB_Self:
        ...

    def fit(
        self: _BaseDiscreteNB_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> _BaseDiscreteNB_Self | BernoulliNB | ComplementNB:
        ...


class MultinomialNB(_BaseDiscreteNB):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_log_prob_: ndarray = ...
    feature_count_: ndarray = ...
    classes_: ndarray = ...
    class_log_prior_: ndarray = ...
    class_count_: ndarray = ...

    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: str | bool = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
    ) -> None:
        ...


class ComplementNB(_BaseDiscreteNB):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_log_prob_: ndarray = ...
    feature_count_: ndarray = ...
    feature_all_: ndarray = ...
    classes_: ndarray = ...
    class_log_prior_: ndarray = ...
    class_count_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: str | bool = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
        norm: bool = False,
    ) -> None:
        ...


class BernoulliNB(_BaseDiscreteNB):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_log_prob_: ndarray = ...
    feature_count_: ndarray = ...
    classes_: ndarray = ...
    class_log_prior_: ndarray = ...
    class_count_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: float | ArrayLike = 1.0,
        force_alpha: str | bool = "warn",
        binarize: None | Float = 0.0,
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
    ) -> None:
        ...


class CategoricalNB(_BaseDiscreteNB):
    n_categories_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_log_prob_: list[ArrayLike] = ...
    classes_: ndarray = ...
    class_log_prior_: ndarray = ...
    class_count_: ndarray = ...
    category_count_: list[ArrayLike] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        force_alpha: str | bool = "warn",
        fit_prior: bool = True,
        class_prior: None | ArrayLike = None,
        min_categories: None | ArrayLike | Int = None,
    ) -> None:
        ...

    def fit(
        self: CategoricalNB_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> CategoricalNB_Self:
        ...

    def partial_fit(
        self: CategoricalNB_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        classes: None | ArrayLike = None,
        sample_weight: None | ArrayLike = None,
    ) -> CategoricalNB_Self:
        ...
