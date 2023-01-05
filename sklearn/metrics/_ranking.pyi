from numpy import bool_, float64, int64, ndarray
from typing import Optional, Tuple, Union, Literal
from numpy.typing import NDArray, ArrayLike

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

import warnings
from functools import partial

import numpy as np
from scipy.sparse import csr_matrix
from scipy.stats import rankdata

from ..utils import assert_all_finite
from ..utils import check_consistent_length
from ..utils.validation import _check_sample_weight
from ..utils import column_or_1d, check_array
from ..utils.multiclass import type_of_target
from ..utils.extmath import stable_cumsum
from ..utils.sparsefuncs import count_nonzero
from ..exceptions import UndefinedMetricWarning
from ..preprocessing import label_binarize
from ..utils._encode import _encode, _unique

from ._base import (
    _average_binary_score,
    _average_multiclass_ovo_score,
    _check_pos_label_consistency,
)
from pandas.core.series import Series

def auc(x: NDArray, y: NDArray) -> float: ...
def average_precision_score(
    y_true: NDArray,
    y_score: NDArray,
    *,
    average: Literal["micro", "samples", "weighted", "macro"] | None = "macro",
    pos_label: int | str = 1,
    sample_weight: ArrayLike | None = None,
) -> float: ...
def det_curve(
    y_true: NDArray,
    y_score: NDArray,
    pos_label: int | str | None = None,
    sample_weight: ArrayLike | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: ...
def _binary_roc_auc_score(y_true: ndarray, y_score: ndarray, sample_weight: None = None, max_fpr: None = None) -> float64: ...
def roc_auc_score(
    y_true: ArrayLike,
    y_score: ArrayLike,
    *,
    average: Literal["micro", "macro", "samples", "weighted"] | None = "macro",
    sample_weight: ArrayLike | None = None,
    max_fpr: float | None = None,
    multi_class: Literal["raise", "ovr", "ovo"] = "raise",
    labels: ArrayLike | None = None,
) -> float: ...
def _multiclass_roc_auc_score(
    y_true: ndarray,
    y_score: ndarray,
    labels: None,
    multi_class: str,
    average: str,
    sample_weight: None,
): ...
def _binary_clf_curve(
    y_true: Union[ndarray, Series],
    y_score: ndarray,
    pos_label: Optional[Union[int64, int, bool_]] = None,
    sample_weight: None = None,
) -> Tuple[ndarray, ndarray, ndarray]: ...
def precision_recall_curve(
    y_true: NDArray,
    probas_pred: NDArray,
    *,
    pos_label: int | str | None = None,
    sample_weight: ArrayLike | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: ...
def roc_curve(
    y_true: NDArray,
    y_score: NDArray,
    *,
    pos_label: int | str | None = None,
    sample_weight: ArrayLike | None = None,
    drop_intermediate: bool = True,
) -> tuple[np.ndarray, np.ndarray, NDArray]: ...
def label_ranking_average_precision_score(
    y_true: NDArray, y_score: NDArray, *, sample_weight: ArrayLike | None = None
) -> float: ...
def coverage_error(y_true: NDArray, y_score: NDArray, *, sample_weight: ArrayLike | None = None) -> float: ...
def label_ranking_loss(y_true: NDArray, y_score: NDArray, *, sample_weight: ArrayLike | None = None) -> float: ...
def _dcg_sample_scores(y_true, y_score, k=None, log_base=2, ignore_ties=False): ...
def _tie_averaged_dcg(y_true, y_score, discount_cumsum): ...
def _check_dcg_target_type(y_true): ...
def dcg_score(
    y_true: NDArray,
    y_score: NDArray,
    *,
    k: int | None = None,
    log_base: float = 2,
    sample_weight: NDArray | None = None,
    ignore_ties: bool = False,
) -> float: ...
def _ndcg_sample_scores(y_true, y_score, k=None, ignore_ties=False): ...
def ndcg_score(
    y_true: NDArray,
    y_score: NDArray,
    *,
    k: int | None = None,
    sample_weight: NDArray | None = None,
    ignore_ties: bool = False,
) -> float: ...
def top_k_accuracy_score(
    y_true: ArrayLike,
    y_score: ArrayLike,
    *,
    k: int = 2,
    normalize: bool = True,
    sample_weight: ArrayLike | None = None,
    labels: ArrayLike | None = None,
) -> float: ...
