from typing import Any, Callable, Literal, Mapping, Self, Sequence
from ._glm.glm import NewtonCholeskySolver as NewtonCholeskySolver
from .._typing import Float, Int, ArrayLike, MatrixLike
from .._loss.loss import (
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
)
from ..preprocessing import (
    LabelEncoder as LabelEncoder,
    LabelBinarizer as LabelBinarizer,
)
from ..model_selection import BaseCrossValidator
from ..utils._param_validation import StrOptions as StrOptions, Interval as Interval
from ..utils.extmath import softmax as softmax, row_norms as row_norms
from ._linear_loss import LinearModelLoss as LinearModelLoss
from ..model_selection import check_cv as check_cv
from joblib import effective_n_jobs as effective_n_jobs
from ._base import LinearClassifierMixin, SparseCoefMixin, BaseEstimator
from ..utils import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    compute_class_weight as compute_class_weight,
    check_random_state as check_random_state,
)
from ..metrics import get_scorer as get_scorer
from ._sag import sag_solver as sag_solver
from scipy import optimize as optimize
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from numpy.random import RandomState
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..metrics import get_scorer_names as get_scorer_names
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel

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

    _parameter_constraints: dict = ...

    def __init__(
        self,
        penalty: Literal["l1", "l2", "elasticnet", "l2"] | None = "l2",
        *,
        dual: bool = False,
        tol: Float = 1e-4,
        C: Float = 1.0,
        fit_intercept: bool = True,
        intercept_scaling: Float = 1,
        class_weight: str | Mapping | None = None,
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
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Self | LogisticRegression:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...


class LogisticRegressionCV(LogisticRegression, LinearClassifierMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    for param in ["C", "warm_start", "l1_ratio"]:
        pass

    def __init__(
        self,
        *,
        Cs: Sequence[float] | int = 10,
        fit_intercept: bool = True,
        cv: BaseCrossValidator | int | None = None,
        dual: bool = False,
        penalty: Literal["l1", "l2", "elasticnet", "l2"] = "l2",
        scoring: str | None | Callable = None,
        solver: Literal[
            "lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga", "lbfgs"
        ] = "lbfgs",
        tol: Float = 1e-4,
        max_iter: Int = 100,
        class_weight: str | Mapping | None = None,
        n_jobs: None | Int = None,
        verbose: Int = 0,
        refit: bool = True,
        intercept_scaling: Float = 1.0,
        multi_class: Literal["auto", "ovr", "multinomial", "auto"] = "auto",
        random_state: RandomState | None | Int = None,
        l1_ratios: Sequence[float] | None = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def score(
        self, X: MatrixLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> float:
        ...
