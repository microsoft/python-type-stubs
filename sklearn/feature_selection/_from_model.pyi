from typing import Any, Callable
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    Options as Options,
)
from ..exceptions import NotFittedError as NotFittedError
from .._typing import MatrixLike, ArrayLike
from ..base import BaseEstimator, clone as clone, MetaEstimatorMixin
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_scalar as check_scalar,
)
from ._base import SelectorMixin
from numbers import Integral as Integral, Real as Real
from copy import deepcopy as deepcopy
from ..utils.metaestimators import available_if as available_if

# Authors: Gilles Louppe, Mathieu Blondel, Maheshakya Wijewardena
# License: BSD 3 clause


import numpy as np


class SelectFromModel(MetaEstimatorMixin, SelectorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: Any,
        *,
        threshold: str | None | float = None,
        prefit: bool = False,
        norm_order: int | float = 1,
        max_features: int | None | Callable = None,
        importance_getter: str | Callable = "auto",
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | ArrayLike = None, **fit_params) -> Any:
        ...

    @property
    def threshold_(self) -> float:
        ...

    def partial_fit(
        self, X: MatrixLike, y: None | ArrayLike = None, **fit_params
    ) -> Any:
        ...

    @property
    def n_features_in_(self) -> int:
        ...
