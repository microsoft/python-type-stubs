from typing import List, Optional, Tuple, Union, Literal, Mapping, Callable, Any
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

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
from scipy import optimize

from ._base import LinearClassifierMixin, SparseCoefMixin, BaseEstimator
from ._linear_loss import LinearModelLoss
from ._sag import sag_solver
from .._loss.loss import HalfBinomialLoss, HalfMultinomialLoss
from ..preprocessing import LabelEncoder, LabelBinarizer
from ..svm._base import _fit_liblinear
from ..utils import check_array, check_consistent_length, compute_class_weight
from ..utils import check_random_state
from ..utils.extmath import softmax
from ..utils.extmath import row_norms
from ..utils.optimize import _newton_cg, _check_optimize_result
from ..utils.validation import check_is_fitted, _check_sample_weight
from ..utils.multiclass import check_classification_targets
from ..utils.fixes import delayed
from ..model_selection import check_cv
from ..metrics import get_scorer
from numpy import float64, int64, ndarray
from scipy.sparse._csr import csr_matrix

_LOGISTIC_SOLVER_CONVERGENCE_MSG: str = ...

def _check_solver(solver: str, penalty: str, dual: bool) -> str: ...
def _check_multi_class(multi_class: str, solver: str, n_classes: int) -> str: ...
def _logistic_regression_path(
    X: Union[ndarray, csr_matrix],
    y: ndarray,
    pos_class: Optional[Union[int64, float64]] = None,
    Cs: List[Union[float64, int, float]] = ...,
    fit_intercept: bool = True,
    max_iter: int = 100,
    tol: Union[int, float] = 1e-4,
    verbose: int = 0,
    solver: str = "lbfgs",
    coef: None = None,
    class_weight: None = None,
    dual: bool = False,
    penalty: str = "l2",
    intercept_scaling: float = 1.0,
    multi_class: str = "auto",
    random_state: Optional[int] = None,
    check_input: bool = True,
    max_squared_sum: Optional[float64] = None,
    sample_weight: None = None,
    l1_ratio: Optional[float] = None,
    n_threads: int = 1,
) -> Tuple[ndarray, ndarray, ndarray]: ...

# helper function for LogisticCV
def _log_reg_scoring_path(
    X,
    y,
    train,
    test,
    pos_class=None,
    Cs=10,
    scoring=None,
    fit_intercept=False,
    max_iter=100,
    tol=1e-4,
    class_weight=None,
    verbose=0,
    solver="lbfgs",
    penalty="l2",
    dual=False,
    intercept_scaling=1.0,
    multi_class="auto",
    random_state=None,
    max_squared_sum=None,
    sample_weight=None,
    l1_ratio=None,
): ...

class LogisticRegression(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    def __init__(
        self,
        penalty: Literal["l1", "l2", "elasticnet", "none"] = "l2",
        *,
        dual: bool = False,
        tol: float = 1e-4,
        C: float = 1.0,
        fit_intercept: bool = True,
        intercept_scaling: float = 1,
        class_weight: Mapping | Literal["balanced"] | None = None,
        random_state: int | RandomState | None = None,
        solver: Literal["newton-cg", "lbfgs", "liblinear", "sag", "saga"] = "lbfgs",
        max_iter: int = 100,
        multi_class: Literal["auto", "ovr", "multinomial"] = "auto",
        verbose: int = 0,
        warm_start: bool = False,
        n_jobs: int | None = None,
        l1_ratio: float | None = None,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "LogisticRegression": ...
    def predict_proba(self, X: ArrayLike) -> ArrayLike: ...
    def predict_log_proba(self, X: ArrayLike) -> ArrayLike: ...

class LogisticRegressionCV(LogisticRegression, LinearClassifierMixin, BaseEstimator):
    def __init__(
        self,
        *,
        Cs: int | ArrayLike = 10,
        fit_intercept: bool = True,
        cv=None,
        dual: bool = False,
        penalty: Literal["l1", "l2", "elasticnet"] = "l2",
        scoring: str | Callable | None = None,
        solver: Literal["newton-cg", "lbfgs", "liblinear", "sag", "saga"] = "lbfgs",
        tol: float = 1e-4,
        max_iter: int = 100,
        class_weight: Mapping | Literal["balanced"] | None = None,
        n_jobs: int | None = None,
        verbose: int = 0,
        refit: bool = True,
        intercept_scaling: float = 1.0,
        multi_class="auto",
        random_state: int | RandomState | None = None,
        l1_ratios: ArrayLike | None = None,
    ): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def score(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...
    def _more_tags(self): ...
