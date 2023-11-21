from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Literal, Mapping, Sequence, TypeVar

from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from numpy.random import RandomState
from scipy import optimize as optimize

from .._loss.loss import HalfBinomialLoss as HalfBinomialLoss, HalfMultinomialLoss as HalfMultinomialLoss
from .._typing import ArrayLike, Float, Int, MatrixLike
from ..metrics import get_scorer as get_scorer, get_scorer_names as get_scorer_names
from ..model_selection import BaseCrossValidator, check_cv as check_cv
from ..model_selection._split import BaseShuffleSplit
from ..preprocessing import LabelBinarizer as LabelBinarizer, LabelEncoder as LabelEncoder
from ..utils import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_random_state as check_random_state,
    compute_class_weight as compute_class_weight,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms, softmax as softmax
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import BaseEstimator, LinearClassifierMixin, SparseCoefMixin
from ._glm.glm import NewtonCholeskySolver as NewtonCholeskySolver
from ._linear_loss import LinearModelLoss as LinearModelLoss
from ._sag import sag_solver as sag_solver

LogisticRegressionCV_Self = TypeVar("LogisticRegressionCV_Self", bound="LogisticRegressionCV")
LogisticRegression_Self = TypeVar("LogisticRegression_Self", bound="LogisticRegression")

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Fabian Pedregosa <f@bianp.net>
#         Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#         Manoj Kumar <manojkumarsivaraj334@gmail.com>
#         Lars Buitinck
#         Simon Wu <s8wu@uwaterloo.ca>
#         Arthur Mensch <arthur.mensch@m4x.org

import numbers
import warnings

import numpy as np

_LOGISTIC_SOLVER_CONVERGENCE_MSG: str = ...

class LogisticRegression(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    n_iter_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        penalty: Literal["l1", "l2", "elasticnet", "l2"] | None = "l2",
        *,
        dual: bool = False,
        tol: Float = 1e-4,
        C: Float = 1.0,
        fit_intercept: bool = True,
        intercept_scaling: Float = 1,
        class_weight: None | Mapping | str = None,
        random_state: RandomState | None | Int = None,
        solver: Literal["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga", "lbfgs"] = "lbfgs",
        max_iter: Int = 100,
        multi_class: Literal["auto", "ovr", "multinomial", "auto"] = "auto",
        verbose: Int = 0,
        warm_start: bool = False,
        n_jobs: None | Int = None,
        l1_ratio: None | Float = None,
    ) -> None: ...
    def fit(
        self: LogisticRegression_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LogisticRegression_Self: ...
    def predict_proba(self, X: MatrixLike) -> ndarray: ...
    def predict_log_proba(self, X: MatrixLike) -> ndarray: ...

class LogisticRegressionCV(LogisticRegression, LinearClassifierMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: ndarray = ...
    l1_ratio_: ndarray = ...
    C_: ndarray = ...
    scores_: dict = ...
    coefs_paths_: ndarray = ...
    l1_ratios_: ndarray = ...
    Cs_: ndarray = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    for param in ["C", "warm_start", "l1_ratio"]:
        pass

    def __init__(
        self,
        *,
        Cs: Sequence[float] | int = 10,
        fit_intercept: bool = True,
        cv: int | None | BaseShuffleSplit | BaseCrossValidator = None,
        dual: bool = False,
        penalty: Literal["l1", "l2", "elasticnet", "l2"] = "l2",
        scoring: None | str | Callable = None,
        solver: Literal["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga", "lbfgs"] = "lbfgs",
        tol: Float = 1e-4,
        max_iter: Int = 100,
        class_weight: None | Mapping | str = None,
        n_jobs: None | Int = None,
        verbose: Int = 0,
        refit: bool = True,
        intercept_scaling: Float = 1.0,
        multi_class: Literal["auto", "ovr", "multinomial", "auto"] = "auto",
        random_state: RandomState | None | Int = None,
        l1_ratios: None | Sequence[float] = None,
    ) -> None: ...
    def fit(
        self: LogisticRegressionCV_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LogisticRegressionCV_Self: ...
    def score(self, X: MatrixLike, y: ArrayLike, sample_weight: None | ArrayLike = None) -> float: ...
