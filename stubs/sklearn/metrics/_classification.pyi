import warnings
from typing import Literal

import numpy as np
from numpy import ndarray
from scipy.sparse import coo_matrix as coo_matrix, csr_matrix as csr_matrix
from scipy.special import xlogy as xlogy

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from ..preprocessing import LabelBinarizer as LabelBinarizer, LabelEncoder as LabelEncoder
from ..utils import (
    assert_all_finite as assert_all_finite,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    column_or_1d as column_or_1d,
)
from ..utils._param_validation import validate_params as validate_params
from ..utils.multiclass import type_of_target as type_of_target, unique_labels as unique_labels
from ..utils.sparsefuncs import count_nonzero as count_nonzero

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Arnaud Joly <a.joly@ulg.ac.be>
#          Jochen Wersdorfer <jochen@wersdoerfer.de>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
#          Noel Dawe <noel@dawe.me>
#          Jatin Shah <jatindshah@gmail.com>
#          Saurabh Jha <saurabh.jhaa@gmail.com>
#          Bernardo Stein <bernardovstein@gmail.com>
#          Shangwu Yao <shangwuyao@gmail.com>
#          Michal Karbownik <michakarbownik@gmail.com>
# License: BSD 3 clause

def accuracy_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    normalize: bool = True,
    sample_weight: None | ArrayLike = None,
) -> Float: ...
def confusion_matrix(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: None | ArrayLike = None,
    sample_weight: None | ArrayLike = None,
    normalize: Literal["true", "pred", "all"] | None = None,
) -> ndarray: ...
def multilabel_confusion_matrix(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    labels: None | ArrayLike = None,
    samplewise: bool = False,
) -> ndarray: ...
def cohen_kappa_score(
    y1: ArrayLike,
    y2: ArrayLike,
    *,
    labels: None | ArrayLike = None,
    weights: None | Literal["linear", "quadratic"] = None,
    sample_weight: None | ArrayLike = None,
) -> float: ...
def jaccard_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["micro", "macro", "samples", "weighted", "binary", "binary"] = "binary",
    sample_weight: None | ArrayLike = None,
    zero_division: float | Literal["warn", "warn"] = "warn",
) -> ndarray | Float: ...
def matthews_corrcoef(y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: None | ArrayLike = None) -> float: ...
def zero_one_loss(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    normalize: bool = True,
    sample_weight: None | ArrayLike = None,
) -> Float: ...
def f1_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["micro", "macro", "samples", "weighted", "binary", "binary"] = "binary",
    sample_weight: None | ArrayLike = None,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> ndarray | Float: ...
def fbeta_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    beta: Float,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["micro", "macro", "samples", "weighted", "binary", "binary"] = "binary",
    sample_weight: None | ArrayLike = None,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> ndarray | Float: ...
def precision_recall_fscore_support(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    beta: Float = 1.0,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["binary", "micro", "macro", "samples", "weighted"] = None,
    warn_for: set | tuple = ...,
    sample_weight: None | ArrayLike = None,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> tuple[float | ndarray, float | ndarray, float | ndarray, None | ndarray]: ...
def class_likelihood_ratios(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    sample_weight: None | ArrayLike = None,
    raise_warning: bool = True,
) -> tuple[float, Float] | tuple | tuple[Float, Float]: ...
def precision_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["micro", "macro", "samples", "weighted", "binary", "binary"] = "binary",
    sample_weight: None | ArrayLike = None,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> ndarray | Float: ...
def recall_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    pos_label: str | int = 1,
    average: None | Literal["micro", "macro", "samples", "weighted", "binary", "binary"] = "binary",
    sample_weight: None | ArrayLike = None,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> ndarray | Float: ...
def balanced_accuracy_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    adjusted: bool = False,
) -> float: ...
def classification_report(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    target_names: None | ArrayLike = None,
    sample_weight: None | ArrayLike = None,
    digits: Int = 2,
    output_dict: bool = False,
    zero_division: Literal["warn", "warn"] | int = "warn",
) -> str | dict: ...
def hamming_loss(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
) -> Float: ...
def log_loss(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    eps: float | Literal["auto", "auto"] = "auto",
    normalize: bool = True,
    sample_weight: None | ArrayLike = None,
    labels: None | ArrayLike = None,
) -> Float: ...
def hinge_loss(
    y_true: ArrayLike,
    pred_decision: MatrixLike | ArrayLike,
    *,
    labels: None | ArrayLike = None,
    sample_weight: None | ArrayLike = None,
) -> float: ...
def brier_score_loss(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    pos_label: None | str | Int = None,
) -> Float: ...
