from typing import Any, Callable, ClassVar, TypeVar
from ..preprocessing import FunctionTransformer as FunctionTransformer
from ..linear_model import LinearRegression as LinearRegression
from ..exceptions import NotFittedError as NotFittedError
from numpy import ndarray
from ..utils._param_validation import HasMethods as HasMethods
from ..base import BaseEstimator, RegressorMixin, clone as clone
from .._typing import MatrixLike, ArrayLike
from ..utils import check_array as check_array
from ..utils.validation import check_is_fitted as check_is_fitted

TransformedTargetRegressor_Self = TypeVar(
    "TransformedTargetRegressor_Self", bound="TransformedTargetRegressor"
)

# Authors: Andreas Mueller <andreas.mueller@columbia.edu>
#          Guillaume Lemaitre <guillaume.lemaitre@inria.fr>
# License: BSD 3 clause

import warnings

import numpy as np

__all__ = ["TransformedTargetRegressor"]


class TransformedTargetRegressor(RegressorMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    transformer_: Any = ...
    regressor_: Any = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        regressor: Any = None,
        *,
        transformer: Any = None,
        func: None | Callable = None,
        inverse_func: None | Callable = None,
        check_inverse: bool = True,
    ) -> None:
        ...

    def fit(
        self: TransformedTargetRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        **fit_params,
    ) -> TransformedTargetRegressor_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray:
        ...

    @property
    def n_features_in_(self) -> int:
        ...
