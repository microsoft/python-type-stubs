import warnings
from functools import partial as partial
from typing import Literal

import numpy as np
from numpy import ndarray
from scipy.sparse import csr_matrix as csr_matrix, issparse as issparse
from scipy.stats import rankdata as rankdata

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from ..preprocessing import label_binarize as label_binarize
from ..utils import (
    assert_all_finite as assert_all_finite,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    column_or_1d as column_or_1d,
)
from ..utils.extmath import stable_cumsum as stable_cumsum
from ..utils.multiclass import type_of_target as type_of_target
from ..utils.sparsefuncs import count_nonzero as count_nonzero

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Arnaud Joly <a.joly@ulg.ac.be>
#          Jochen Wersdorfer <jochen@wersdoerfer.de>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
#          Noel Dawe <noel@dawe.me>
#          Michal Karbownik <michakarbownik@gmail.com>
# License: BSD 3 clause

def auc(x: ArrayLike, y: ArrayLike) -> Float: ...
def average_precision_score(
    y_true: MatrixLike | ArrayLike,
    y_score: MatrixLike | ArrayLike,
    *,
    average: None | Literal["micro", "samples", "weighted", "macro"] = "macro",
    pos_label: str | Int = 1,
    sample_weight: None | ArrayLike = None,
) -> Float: ...
def det_curve(
    y_true: ArrayLike,
    y_score: ArrayLike,
    pos_label: None | str | Int = None,
    sample_weight: None | ArrayLike = None,
) -> tuple[ndarray, ndarray, ndarray]: ...
def roc_auc_score(
    y_true: MatrixLike | ArrayLike,
    y_score: MatrixLike | ArrayLike,
    *,
    average: Literal["micro", "macro", "samples", "weighted"] | None = "macro",
    sample_weight: None | ArrayLike = None,
    max_fpr: float | None = None,
    multi_class: Literal["raise", "ovr", "ovo"] = "raise",
    labels: None | ArrayLike = None,
) -> Float: ...
def precision_recall_curve(
    y_true: ArrayLike,
    probas_pred: ArrayLike,
    *,
    pos_label: None | str | Int = None,
    sample_weight: None | ArrayLike = None,
) -> tuple[ndarray, ndarray, ndarray]: ...
def roc_curve(
    y_true: ArrayLike,
    y_score: ArrayLike,
    *,
    pos_label: None | str | Int = None,
    sample_weight: None | ArrayLike = None,
    drop_intermediate: bool = True,
) -> tuple[ndarray, ndarray, ndarray]: ...
def label_ranking_average_precision_score(
    y_true: MatrixLike, y_score: MatrixLike, *, sample_weight: None | ArrayLike = None
) -> float: ...
def coverage_error(y_true: MatrixLike, y_score: MatrixLike, *, sample_weight: None | ArrayLike = None) -> float: ...
def label_ranking_loss(y_true: MatrixLike, y_score: MatrixLike, *, sample_weight: None | ArrayLike = None) -> float: ...
def dcg_score(
    y_true: MatrixLike,
    y_score: MatrixLike,
    *,
    k: None | Int = None,
    log_base: Float = 2,
    sample_weight: None | ArrayLike = None,
    ignore_ties: bool = False,
) -> float: ...
def ndcg_score(
    y_true: MatrixLike,
    y_score: MatrixLike,
    *,
    k: None | Int = None,
    sample_weight: None | ArrayLike = None,
    ignore_ties: bool = False,
) -> float: ...
def top_k_accuracy_score(
    y_true: ArrayLike,
    y_score: MatrixLike | ArrayLike,
    *,
    k: Int = 2,
    normalize: bool = True,
    sample_weight: None | ArrayLike = None,
    labels: None | ArrayLike = None,
) -> float: ...
