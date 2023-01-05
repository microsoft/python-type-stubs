# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Arnaud Joly <a.joly@ulg.ac.be>
#          Jochen Wersdorfer <jochen@wersdoerfer.de>
#          Lars Buitinck
#          Joel Nothman <joel.nothman@gmail.com>
#          Noel Dawe <noel@dawe.me>
# License: BSD 3 clause

from itertools import combinations

import numpy as np

from ..utils import check_array, check_consistent_length
from ..utils.multiclass import type_of_target
from functools import partial
from numpy import bool_, float64, int64, ndarray
from pandas.core.series import Series
from typing import Optional, Union

def _average_binary_score(
    binary_metric: partial,
    y_true: ndarray,
    y_score: ndarray,
    average: str,
    sample_weight: None = None,
) -> float64: ...
def _average_multiclass_ovo_score(binary_metric, y_true, y_score, average="macro"): ...
def _check_pos_label_consistency(
    pos_label: Optional[Union[int64, int, bool_]], y_true: Union[ndarray, Series]
) -> Union[int64, int, bool_]: ...
