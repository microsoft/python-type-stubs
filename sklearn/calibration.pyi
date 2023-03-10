from typing import Any, Iterable, Literal
from scipy.special import expit as expit, xlogy as xlogy
from ._typing import Estimator, Int, MatrixLike, ArrayLike
from .base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    clone as clone,
    MetaEstimatorMixin,
    is_classifier as is_classifier,
)
from .model_selection import BaseCrossValidator
from .svm import LinearSVC as LinearSVC
from scipy.optimize import fmin_bfgs as fmin_bfgs
from .utils import (
    column_or_1d as column_or_1d,
    indexable as indexable,
    check_matplotlib_support as check_matplotlib_support,
)
from .isotonic import IsotonicRegression
from .naive_bayes import GaussianNB
from matplotlib.axes import Axes
from numpy import ndarray
from .utils.parallel import delayed as delayed, Parallel as Parallel
from .preprocessing import (
    label_binarize as label_binarize,
    LabelEncoder as LabelEncoder,
)
from .ensemble._forest import RandomForestClassifier
from inspect import signature as signature
from math import log as log
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from functools import partial as partial
from .utils._param_validation import (
    StrOptions as StrOptions,
    HasMethods as HasMethods,
    Hidden as Hidden,
)
from numbers import Integral as Integral
from .utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
)
from .model_selection import (
    check_cv as check_cv,
    cross_val_predict as cross_val_predict,
)
import warnings
import numpy as np


class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: GaussianNB | Estimator | None | RandomForestClassifier = None,
        *,
        method: Literal["sigmoid", "isotonic", "sigmoid"] = "sigmoid",
        cv: BaseCrossValidator | int | str | Iterable | None = None,
        n_jobs: None | Int = None,
        ensemble: bool = True,
        base_estimator: Estimator | str = "deprecated",
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
        **fit_params,
    ) -> Any:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...


class _CalibratedClassifier:
    def __init__(
        self,
        estimator: GaussianNB | Estimator | RandomForestClassifier,
        calibrators: list[_SigmoidCalibration | IsotonicRegression]
        | list[Estimator]
        | list[IsotonicRegression | _SigmoidCalibration],
        *,
        classes: ArrayLike,
        method: Literal["sigmoid", "isotonic", "sigmoid"] = "sigmoid",
    ) -> None:
        ...

    def predict_proba(self, X: ArrayLike) -> ndarray:
        ...


class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    def fit(
        self, X: ArrayLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> Any:
        ...

    def predict(self, T: ArrayLike) -> ndarray:
        ...


def calibration_curve(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    *,
    pos_label: str | None | Int = None,
    normalize: bool | str = "deprecated",
    n_bins: Int = 5,
    strategy: Literal["uniform", "quantile", "uniform"] = "uniform",
) -> tuple[ndarray, ndarray]:
    ...


class CalibrationDisplay:
    def __init__(
        self,
        prob_true: ArrayLike,
        prob_pred: ArrayLike,
        y_prob: ArrayLike,
        *,
        estimator_name: str | None = None,
        pos_label: int | str | None = None,
    ) -> None:
        ...

    def plot(
        self,
        *,
        ax: Axes | None = None,
        name: str | None = None,
        ref_line: bool = True,
        **kwargs,
    ) -> CalibrationDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: Estimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        n_bins: Int = 5,
        strategy: Literal["uniform", "quantile", "uniform"] = "uniform",
        pos_label: int | str | None = None,
        name: str | None = None,
        ref_line: bool = True,
        ax: Axes | None = None,
        **kwargs,
    ) -> CalibrationDisplay:
        ...

    @classmethod
    def from_predictions(
        cls,
        y_true: ArrayLike,
        y_prob: ArrayLike,
        *,
        n_bins: Int = 5,
        strategy: Literal["uniform", "quantile", "uniform"] = "uniform",
        pos_label: int | str | None = None,
        name: str | None = None,
        ref_line: bool = True,
        ax: Axes | None = None,
        **kwargs,
    ) -> CalibrationDisplay:
        ...
