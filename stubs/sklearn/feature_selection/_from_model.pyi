from copy import deepcopy as deepcopy
from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, TypeVar

from numpy import ndarray

from .._typing import ArrayLike, MatrixLike
from ..base import BaseEstimator, MetaEstimatorMixin, clone as clone
from ..exceptions import NotFittedError as NotFittedError
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval, Options as Options
from ..utils.metaestimators import available_if as available_if
from ..utils.validation import check_is_fitted as check_is_fitted, check_scalar as check_scalar
from ._base import SelectorMixin

SelectFromModel_Self = TypeVar("SelectFromModel_Self", bound="SelectFromModel")

# Authors: Gilles Louppe, Mathieu Blondel, Maheshakya Wijewardena
# License: BSD 3 clause

import numpy as np

class SelectFromModel(MetaEstimatorMixin, SelectorMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    max_features_: int = ...
    estimator_: BaseEstimator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: Any,
        *,
        threshold: float | None | str = None,
        prefit: bool = False,
        norm_order: float | int = 1,
        max_features: None | Callable | int = None,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    def fit(
        self: SelectFromModel_Self,
        X: MatrixLike,
        y: None | ArrayLike = None,
        **fit_params,
    ) -> SelectFromModel_Self: ...
    @property
    def threshold_(self) -> float: ...
    def partial_fit(
        self: SelectFromModel_Self,
        X: MatrixLike,
        y: None | ArrayLike = None,
        **fit_params,
    ) -> SelectFromModel_Self: ...
    @property
    def n_features_in_(self) -> int: ...
