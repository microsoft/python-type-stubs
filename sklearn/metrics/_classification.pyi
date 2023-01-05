from numpy import float64, ndarray
from typing import List, Optional, Tuple, Union, Literal, Sequence
from numpy.typing import ArrayLike, NDArray

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

import warnings
import numpy as np

from scipy.sparse import coo_matrix
from scipy.sparse import csr_matrix

from ..preprocessing import LabelBinarizer
from ..preprocessing import LabelEncoder
from ..utils import assert_all_finite
from ..utils import check_array
from ..utils import check_consistent_length
from ..utils import column_or_1d
from ..utils.multiclass import unique_labels
from ..utils.multiclass import type_of_target
from ..utils.validation import _num_samples
from ..utils.sparsefuncs import count_nonzero
from ..exceptions import UndefinedMetricWarning

from ._base import _check_pos_label_consistency
from pandas.core.series import Series

def _check_zero_division(zero_division: str) -> None: ...
def _check_targets(
    y_true: Union[List[int], ndarray, Series], y_pred: Union[List[int], ndarray]
) -> Tuple[str, ndarray, ndarray]: ...
def _weighted_sum(sample_score: ndarray, sample_weight: Optional[ndarray], normalize: bool = False) -> float64: ...
def accuracy_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    normalize: bool = True,
    sample_weight: ArrayLike | None = None,
) -> float: ...
def confusion_matrix(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    sample_weight: ArrayLike | None = None,
    normalize: Literal["true", "pred", "all"] | None = None,
) -> NDArray: ...
def multilabel_confusion_matrix(
    y_true: NDArray | ArrayLike,
    y_pred: NDArray | ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    labels: ArrayLike | None = None,
    samplewise: bool = False,
) -> np.ndarray: ...
def cohen_kappa_score(
    y1: ArrayLike,
    y2: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    weights: Literal["linear", "quadratic"] | None = None,
    sample_weight: ArrayLike | None = None,
) -> float: ...
def jaccard_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["micro", "macro", "samples", "weighted", "binary"] | None = "binary",
    sample_weight: ArrayLike | None = None,
    zero_division: float | Literal["warn"] = "warn",
) -> float | np.ndarray: ...
def matthews_corrcoef(y_true: NDArray, y_pred: NDArray, *, sample_weight: ArrayLike | None = None) -> float: ...
def zero_one_loss(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    normalize: bool = True,
    sample_weight: ArrayLike | None = None,
) -> float | int: ...
def f1_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["micro", "macro", "samples", "weighted", "binary"] | None = "binary",
    sample_weight: ArrayLike | None = None,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> float | NDArray: ...
def fbeta_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    beta: float,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["micro", "macro", "samples", "weighted", "binary"] | None = "binary",
    sample_weight: ArrayLike | None = None,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> float | NDArray: ...
def _prf_divide(
    numerator: ndarray,
    denominator: ndarray,
    metric: str,
    modifier: str,
    average: Optional[str],
    warn_for: Union[Tuple[str], Tuple[str, str, str]],
    zero_division: str = "warn",
) -> ndarray: ...
def _warn_prf(average, modifier, msg_start, result_size): ...
def _check_set_wise_labels(
    y_true: ndarray,
    y_pred: ndarray,
    average: Optional[str],
    labels: Optional[ndarray],
    pos_label: int,
) -> Optional[Union[List[int], ndarray]]: ...
def precision_recall_fscore_support(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    beta: float = 1.0,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["binary", "micro", "macro", "samples", "weighted"] | None = None,
    warn_for: tuple | set = ...,
    sample_weight: ArrayLike | None = None,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> tuple[float | NDArray, float | NDArray, float | NDArray, None | NDArray]: ...
def precision_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["micro", "macro", "samples", "weighted", "binary"] | None = "binary",
    sample_weight: ArrayLike | None = None,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> float | NDArray: ...
def recall_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    pos_label: str | int = 1,
    average: Literal["micro", "macro", "samples", "weighted", "binary"] | None = "binary",
    sample_weight: ArrayLike | None = None,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> float | NDArray: ...
def balanced_accuracy_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    adjusted: bool = False,
) -> float: ...
def classification_report(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    target_names: Sequence[str] | None = None,
    sample_weight: ArrayLike | None = None,
    digits: int = 2,
    output_dict: bool = False,
    zero_division: Literal["warn", 0, 1] = "warn",
) -> str | dict: ...
def hamming_loss(y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: ArrayLike | None = None) -> float | int: ...
def log_loss(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    eps: float = 1e-15,
    normalize: bool = True,
    sample_weight: ArrayLike | None = None,
    labels: ArrayLike | None = None,
) -> float: ...
def hinge_loss(
    y_true: ArrayLike,
    pred_decision: ArrayLike,
    *,
    labels: ArrayLike | None = None,
    sample_weight: ArrayLike | None = None,
) -> float: ...
def brier_score_loss(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    pos_label: int | str | None = None,
) -> float: ...
