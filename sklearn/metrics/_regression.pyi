from numpy import float64, ndarray
from typing import Tuple, Literal
from numpy.typing import ArrayLike

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Arnaud Joly <a.joly@ulg.ac.be>
#          Jochen Wersdorfer <jochen@wersdoerfer.de>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
#          Karan Desai <karandesai281196@gmail.com>
#          Noel Dawe <noel@dawe.me>
#          Manoj Kumar <manojkumarsivaraj334@gmail.com>
#          Michael Eickenberg <michael.eickenberg@gmail.com>
#          Konstantin Shmelkov <konstantin.shmelkov@polytechnique.edu>
#          Christian Lorentzen <lorentzen.ch@gmail.com>
#          Ashutosh Hathidara <ashutoshhathidara98@gmail.com>
#          Uttam kumar <bajiraouttamsinha@gmail.com>
#          Sylvain Marie <sylvain.marie@se.com>
#          Ohad Michel <ohadmich@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np
from scipy.special import xlogy

from ..exceptions import UndefinedMetricWarning
from ..utils.validation import (
    check_array,
    check_consistent_length,
    check_scalar,
    _num_samples,
    column_or_1d,
    _check_sample_weight,
)
from ..utils.stats import _weighted_percentile

__ALL__: list = ...

def _check_reg_targets(
    y_true: ndarray, y_pred: ndarray, multioutput: str, dtype: str = "numeric"
) -> Tuple[str, ndarray, ndarray, str]: ...
def mean_absolute_error(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
) -> float | np.ndarray: ...
def mean_pinball_loss(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    alpha: float = 0.5,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
) -> float | np.ndarray: ...
def mean_absolute_percentage_error(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
) -> float | np.ndarray: ...
def mean_squared_error(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
    squared: bool = True,
) -> float | np.ndarray: ...
def mean_squared_log_error(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
    squared: bool = True,
) -> float | np.ndarray: ...
def median_absolute_error(
    y_true: ArrayLike | tuple[int, int],
    y_pred: ArrayLike | tuple[int, int],
    *,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
    sample_weight: ArrayLike | None = None,
) -> float | np.ndarray: ...
def _assemble_r2_explained_variance(
    numerator: ndarray,
    denominator: ndarray,
    n_outputs: int,
    multioutput: str,
    force_finite: bool,
) -> float64: ...
def explained_variance_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average", "variance_weighted"] | ArrayLike = "uniform_average",
    force_finite: bool = True,
) -> float | np.ndarray: ...
def r2_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average", "variance_weighted"] | ArrayLike | None = "uniform_average",
    force_finite: bool = True,
) -> float | np.ndarray: ...
def max_error(y_true: ArrayLike, y_pred: ArrayLike) -> float: ...
def _mean_tweedie_deviance(y_true, y_pred, sample_weight, power): ...
def mean_tweedie_deviance(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    power: float = 0,
) -> float: ...
def mean_poisson_deviance(y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: ArrayLike | None = None) -> float: ...
def mean_gamma_deviance(y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: ArrayLike | None = None) -> float: ...
def d2_tweedie_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    power: float = 0,
) -> float | np.ndarray: ...
def d2_pinball_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    alpha: float = 0.5,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
) -> float | np.ndarray: ...
def d2_absolute_error_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    multioutput: Literal["raw_values", "uniform_average"] | ArrayLike = "uniform_average",
) -> float | np.ndarray: ...
