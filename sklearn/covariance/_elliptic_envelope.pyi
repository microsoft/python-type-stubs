from typing import Any
from numpy.typing import ArrayLike, NDArray

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

import numpy as np
from numpy.random import RandomState
from . import MinCovDet
from ..utils.validation import check_is_fitted
from ..metrics import accuracy_score
from ..base import OutlierMixin
from numpy import ndarray

class EllipticEnvelope(OutlierMixin, MinCovDet):
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction: float | None = None,
        contamination: float = 0.1,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "EllipticEnvelope": ...
    def decision_function(self, X: ArrayLike) -> NDArray: ...
    def score_samples(self, X: ArrayLike) -> ArrayLike: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def score(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...
