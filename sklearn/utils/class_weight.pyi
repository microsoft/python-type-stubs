from typing import Mapping
from scipy import sparse as sparse
from .._typing import ArrayLike, MatrixLike
from numpy import ndarray
from ..preprocessing import LabelEncoder as LabelEncoder

# Authors: Andreas Mueller
#          Manoj Kumar
# License: BSD 3 clause

import numpy as np


def compute_class_weight(
    class_weight: dict[int, int] | None | Mapping | str,
    *,
    classes: ArrayLike,
    y: ArrayLike
) -> ndarray:
    ...


def compute_sample_weight(
    class_weight: None | Mapping | str | ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    indices: None | ArrayLike = None
) -> ndarray:
    ...
