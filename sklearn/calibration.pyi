from numpy import float64, ndarray
from sklearn.calibration import CalibrationDisplay
from typing import Callable, List, Optional, Tuple, Union, Literal, Any, Sequence
from numpy.typing import ArrayLike, NDArray
from typing import Generator, Iterable
from matplotlib.axes import Axes

# Author: Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#         Balazs Kegl <balazs.kegl@gmail.com>
#         Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
#         Mathieu Blondel <mathieu@mblondel.org>
#
# License: BSD 3 clause

import warnings
from inspect import signature
from functools import partial

from math import log
import numpy as np

from scipy.special import expit
from scipy.special import xlogy
from scipy.optimize import fmin_bfgs

from .base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    clone,
    MetaEstimatorMixin,
    is_classifier,
)
from .preprocessing import label_binarize, LabelEncoder
from .utils import (
    column_or_1d,
    indexable,
    check_matplotlib_support,
)

from .utils.multiclass import check_classification_targets
from .utils.fixes import delayed
from .utils.validation import (
    _check_fit_params,
    _check_sample_weight,
    _num_samples,
    check_consistent_length,
    check_is_fitted,
)
from .utils import _safe_indexing
from .isotonic import IsotonicRegression
from .svm import LinearSVC
from .model_selection import check_cv, cross_val_predict
from .metrics._base import _check_pos_label_consistency
from .metrics._plot.base import _get_response
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.naive_bayes import GaussianNB

class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    def __init__(
        self,
        base_estimator: BaseEstimator | None = None,
        *,
        method: Literal["sigmoid", "isotonic"] = "sigmoid",
        cv: int | Generator | Iterable | Literal["prefit"] | None = None,
        n_jobs: int | None = None,
        ensemble: bool = True,
    ) -> None: ...
    def fit(
        self,
        X: ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
        **fit_params,
    ) -> "CalibratedClassifierCV": ...
    def predict_proba(self, X: ArrayLike) -> np.ndarray: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

def _fit_classifier_calibrator_pair(
    estimator: GaussianNB,
    X: ndarray,
    y: ndarray,
    train: ndarray,
    test: ndarray,
    supports_sw: bool,
    method: str,
    classes: ndarray,
    sample_weight: Optional[ndarray] = None,
    **fit_params,
) -> "_CalibratedClassifier": ...
def _get_prediction_method(clf: Union[GaussianNB, RandomForestClassifier]) -> Tuple[Callable, str]: ...
def _compute_predictions(pred_method: Callable, method_name: str, X: ndarray, n_classes: int) -> ndarray: ...
def _fit_calibrator(
    clf: Union[GaussianNB, RandomForestClassifier],
    predictions: ndarray,
    y: ndarray,
    classes: ndarray,
    method: str,
    sample_weight: Optional[ndarray] = None,
) -> "_CalibratedClassifier": ...

class _CalibratedClassifier:
    def __init__(
        self,
        base_estimator: BaseEstimator,
        calibrators: Sequence[BaseEstimator],
        *,
        classes: ArrayLike,
        method: Literal["sigmoid", "isotonic"] = "sigmoid",
    ) -> None: ...
    def predict_proba(self, X: NDArray) -> NDArray: ...

def _sigmoid_calibration(
    predictions: ndarray, y: ndarray, sample_weight: Optional[ndarray] = None
) -> Tuple[float64, float64]: ...

class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    def fit(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> "_SigmoidCalibration": ...
    def predict(self, T: ArrayLike) -> NDArray: ...

def calibration_curve(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    *,
    pos_label: int | str | None = None,
    normalize: bool | str = "deprecated",
    n_bins: int = 5,
    strategy: Literal["uniform", "quantile"] = "uniform",
) -> tuple[NDArray, NDArray]: ...

class CalibrationDisplay:
    def __init__(
        self,
        prob_true: NDArray,
        prob_pred: NDArray,
        y_prob: NDArray,
        *,
        estimator_name: str | None = None,
        pos_label: str | int | None = None,
    ) -> None: ...
    def plot(
        self,
        *,
        ax: Axes | None = None,
        name: str | None = None,
        ref_line: bool = True,
        **kwargs,
    ) -> CalibrationDisplay: ...
    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        *,
        n_bins: int = 5,
        strategy: Literal["uniform", "quantile"] = "uniform",
        pos_label: str | int | None = None,
        name: str | None = None,
        ref_line: bool = True,
        ax: Axes | None = None,
        **kwargs,
    ) -> CalibrationDisplay: ...
    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_prob: ArrayLike,
        *,
        n_bins: int = 5,
        strategy: Literal["uniform", "quantile"] = "uniform",
        pos_label: str | int | None = None,
        name: str | None = None,
        ref_line: bool = True,
        ax: Axes | None = None,
        **kwargs,
    ) -> CalibrationDisplay: ...
