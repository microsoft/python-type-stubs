from typing import Any, ClassVar, TypeVar
from numpy.random import RandomState
from numpy import ndarray
from ..utils._param_validation import Interval as Interval
from numbers import Real as Real
from ..base import OutlierMixin
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..metrics import accuracy_score as accuracy_score
from ..utils.validation import check_is_fitted as check_is_fitted
from . import MinCovDet

EllipticEnvelope_Self = TypeVar("EllipticEnvelope_Self", bound="EllipticEnvelope")

# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
#
# License: BSD 3 clause

import numpy as np


class EllipticEnvelope(OutlierMixin, MinCovDet):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dist_: ndarray = ...
    raw_support_: ndarray = ...
    raw_covariance_: ndarray = ...
    raw_location_: ndarray = ...
    offset_: float = ...
    support_: ndarray = ...
    precision_: ndarray = ...
    covariance_: ndarray = ...
    location_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: EllipticEnvelope_Self, X: MatrixLike, y: Any = None
    ) -> EllipticEnvelope_Self:
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
