from typing import Literal
from scipy.special import xlogy as xlogy
from ..exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from numpy import ndarray
from .._typing import MatrixLike, ArrayLike, Float
from ..utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_scalar as check_scalar,
    column_or_1d as column_or_1d,
)

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


__ALL__: list = ...


def mean_absolute_error(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
) -> ndarray | Float:
    ...


def mean_pinball_loss(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    alpha: float = 0.5,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
) -> ndarray | Float:
    ...


def mean_absolute_percentage_error(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
) -> ndarray | Float:
    ...


def mean_squared_error(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
    squared: bool = True,
) -> ndarray | Float:
    ...


def mean_squared_log_error(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
    squared: bool = True,
) -> float | ndarray:
    ...


def median_absolute_error(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
    sample_weight: None | ArrayLike = None,
) -> ndarray | Float:
    ...


def explained_variance_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: Literal[
        "raw_values", "uniform_average", "variance_weighted", "uniform_average"
    ]
    | ArrayLike = "uniform_average",
    force_finite: bool = True,
) -> float | ndarray:
    ...


def r2_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: Literal[
        "raw_values", "uniform_average", "variance_weighted", "uniform_average"
    ]
    | None
    | ArrayLike = "uniform_average",
    force_finite: bool = True,
) -> ndarray | Float:
    ...


def max_error(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    ...


def mean_tweedie_deviance(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    power: Float = 0,
) -> Float:
    ...


def mean_poisson_deviance(
    y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: None | ArrayLike = None
) -> Float:
    ...


def mean_gamma_deviance(
    y_true: ArrayLike, y_pred: ArrayLike, *, sample_weight: None | ArrayLike = None
) -> float:
    ...


def d2_tweedie_score(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    power: Float = 0,
) -> float | ndarray:
    ...


def d2_pinball_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    alpha: Float = 0.5,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
) -> float | ndarray:
    ...


def d2_absolute_error_score(
    y_true: MatrixLike | ArrayLike,
    y_pred: MatrixLike | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    multioutput: ArrayLike
    | Literal["raw_values", "uniform_average", "uniform_average"] = "uniform_average",
) -> float | ndarray:
    ...
