from typing import Callable, ClassVar, Literal, Mapping, Sequence, TypeVar
from numpy.random import RandomState
from ..metrics import get_scorer_names as get_scorer_names
from scipy import optimize as optimize
from ..model_selection._split import BaseShuffleSplit
from ..utils.extmath import softmax as softmax, row_norms as row_norms
from joblib import effective_n_jobs as effective_n_jobs
from ..metrics import get_scorer as get_scorer
from ..preprocessing import (
    LabelEncoder as LabelEncoder,
    LabelBinarizer as LabelBinarizer,
)
from ._glm.glm import NewtonCholeskySolver as NewtonCholeskySolver
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils._param_validation import StrOptions as StrOptions, Interval as Interval
from numbers import Integral as Integral, Real as Real
from ._sag import sag_solver as sag_solver
from ..model_selection import check_cv as check_cv
from ..utils import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    compute_class_weight as compute_class_weight,
    check_random_state as check_random_state,
)
from ._base import LinearClassifierMixin, SparseCoefMixin, BaseEstimator
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from .._loss.loss import (
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
)
from ._linear_loss import LinearModelLoss as LinearModelLoss
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..model_selection import BaseCrossValidator

LogisticRegressionCV_Self = TypeVar(
    "LogisticRegressionCV_Self", bound="LogisticRegressionCV"
)
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
        solver: Literal[
            "lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga", "lbfgs"
        ] = "lbfgs",
        max_iter: Int = 100,
        multi_class: Literal["auto", "ovr", "multinomial", "auto"] = "auto",
        verbose: Int = 0,
        warm_start: bool = False,
        n_jobs: None | Int = None,
        l1_ratio: None | Float = None,
    ) -> None:
        ...

    def fit(
        self: LogisticRegression_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LogisticRegression_Self:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...


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
        solver: Literal[
            "lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga", "lbfgs"
        ] = "lbfgs",
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
    ) -> None:
        ...

    def fit(
        self: LogisticRegressionCV_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LogisticRegressionCV_Self:
        ...

    def score(
        self, X: MatrixLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> float:
        ...
