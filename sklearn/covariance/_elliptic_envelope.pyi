from typing import Any
from ..utils._param_validation import Interval as Interval
from numpy.random import RandomState
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..base import OutlierMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from . import MinCovDet
from numbers import Real as Real
from ..metrics import accuracy_score as accuracy_score

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

import numpy as np


class EllipticEnvelope(OutlierMixin, MinCovDet):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction: None | Float = None,
        contamination: Float = 0.1,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def score_samples(self, X: MatrixLike) -> ArrayLike:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def score(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> float:
        ...
