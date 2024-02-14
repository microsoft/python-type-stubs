from typing import Any, Callable, ClassVar, TypeVar

from numpy import ndarray

from .._typing import ArrayLike, MatrixLike
from ..base import BaseEstimator, RegressorMixin, clone as clone
from ..exceptions import NotFittedError as NotFittedError
from ..linear_model import LinearRegression as LinearRegression
from ..preprocessing import FunctionTransformer as FunctionTransformer
from ..utils import check_array as check_array
from ..utils._param_validation import HasMethods as HasMethods
from ..utils.validation import check_is_fitted as check_is_fitted

TransformedTargetRegressor_Self = TypeVar("TransformedTargetRegressor_Self", bound="TransformedTargetRegressor")

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
    ) -> None: ...
    def fit(
        self: TransformedTargetRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        **fit_params,
    ) -> TransformedTargetRegressor_Self: ...
    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray: ...
    @property
    def n_features_in_(self) -> int: ...
