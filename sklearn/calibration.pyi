from typing import ClassVar, Iterable, Literal, TypeVar
from .model_selection import (
    check_cv as check_cv,
    cross_val_predict as cross_val_predict,
)
from .isotonic import IsotonicRegression
from .utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
)
from .base import BaseEstimator
from .model_selection._split import BaseShuffleSplit
from scipy.optimize import fmin_bfgs as fmin_bfgs
from inspect import signature as signature
from scipy.special import expit as expit, xlogy as xlogy
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from matplotlib.artist import Artist
from .base import (
    ClassifierMixin,
    RegressorMixin,
    clone as clone,
    MetaEstimatorMixin,
    is_classifier as is_classifier,
)
from numpy import ndarray
from matplotlib.axes import Axes
from numbers import Integral as Integral
from .svm import LinearSVC as LinearSVC
from functools import partial as partial
from .utils._param_validation import (
    StrOptions as StrOptions,
    HasMethods as HasMethods,
    Hidden as Hidden,
)
from ._typing import Int, MatrixLike, ArrayLike
from matplotlib.figure import Figure
from .preprocessing import (
    label_binarize as label_binarize,
    LabelEncoder as LabelEncoder,
)
from .utils import (
    column_or_1d as column_or_1d,
    indexable as indexable,
    check_matplotlib_support as check_matplotlib_support,
)
from math import log as log
from .utils.parallel import delayed as delayed, Parallel as Parallel
from .model_selection import BaseCrossValidator

CalibratedClassifierCV_Self = TypeVar(
    "CalibratedClassifierCV_Self", bound="CalibratedClassifierCV"
)
_SigmoidCalibration_Self = TypeVar(
    "_SigmoidCalibration_Self", bound="_SigmoidCalibration"
)

import warnings
import numpy as np


class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    calibrated_classifiers_: list = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: None | BaseEstimator = None,
        *,
        method: Literal["sigmoid", "isotonic", "sigmoid"] = "sigmoid",
        cv: int | BaseCrossValidator | Iterable | None | str | BaseShuffleSplit = None,
        n_jobs: None | Int = None,
        ensemble: bool = True,
        base_estimator: str | BaseEstimator = "deprecated",
    ) -> None:
        ...

    def fit(
        self: CalibratedClassifierCV_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
        **fit_params,
    ) -> CalibratedClassifierCV_Self:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...


class _CalibratedClassifier:
    def __init__(
        self,
        estimator: BaseEstimator,
        calibrators: list[IsotonicRegression | _SigmoidCalibration]
        | list[BaseEstimator],
        *,
        classes: ArrayLike,
        method: Literal["sigmoid", "isotonic", "sigmoid"] = "sigmoid",
    ) -> None:
        ...

    def predict_proba(self, X: ArrayLike) -> ndarray:
        ...


class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    b_: float = ...
    a_: float = ...

    def fit(
        self: _SigmoidCalibration_Self,
        X: ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> _SigmoidCalibration_Self:
        ...

    def predict(self, T: ArrayLike) -> ndarray:
        ...


def calibration_curve(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    *,
    pos_label: None | str | Int = None,
    normalize: str | bool = "deprecated",
    n_bins: Int = 5,
    strategy: Literal["uniform", "quantile", "uniform"] = "uniform",
) -> tuple[ndarray, ndarray]:
    ...


class CalibrationDisplay:
    figure_: Figure = ...
    ax_: Axes = ...
    line_: Artist = ...

    def __init__(
        self,
        prob_true: ArrayLike,
        prob_pred: ArrayLike,
        y_prob: ArrayLike,
        *,
        estimator_name: None | str = None,
        pos_label: None | str | int = None,
    ) -> None:
        ...

    def plot(
        self,
        *,
        ax: None | Axes = None,
        name: None | str = None,
        ref_line: bool = True,
        **kwargs,
    ) -> CalibrationDisplay:
        ...

    @classmethod
    def from_estimator(
        cls,
        estimator: BaseEstimator,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        *,
        n_bins: Int = 5,
        strategy: Literal["uniform", "quantile", "uniform"] = "uniform",
        pos_label: None | str | int = None,
        name: None | str = None,
        ref_line: bool = True,
        ax: None | Axes = None,
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
        pos_label: None | str | int = None,
        name: None | str = None,
        ref_line: bool = True,
        ax: None | Axes = None,
        **kwargs,
    ) -> CalibrationDisplay:
        ...
