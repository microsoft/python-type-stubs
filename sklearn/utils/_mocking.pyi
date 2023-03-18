from typing import Callable, Literal, Sequence, TypeVar
from ..base import BaseEstimator
from numpy import ndarray
from ..base import ClassifierMixin
from .validation import check_array as check_array, check_is_fitted as check_is_fitted
from .._typing import Int, MatrixLike, ArrayLike

CheckingClassifier_Self = TypeVar("CheckingClassifier_Self", bound="CheckingClassifier")

import numpy as np


class ArraySlicingWrapper:
    def __init__(self, array) -> None:
        ...

    def __getitem__(self, aslice):
        ...


class MockDataFrame:

    # have shape and length but don't support indexing.

    def __init__(self, array) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __array__(self, dtype=None):
        ...

    def __eq__(self, other) -> bool:
        ...

    def __ne__(self, other) -> bool:
        ...

    def take(self, indices, axis: int = 0):
        ...


class CheckingClassifier(ClassifierMixin, BaseEstimator):
    n_features_in_: int = ...
    classes_: int = ...

    def __init__(
        self,
        *,
        check_y: None | Callable = None,
        check_y_params: None | dict = None,
        check_X: None | Callable = None,
        check_X_params: None | dict = None,
        methods_to_check: Literal["all", "all"] | Sequence[str] = "all",
        foo_param: Int = 0,
        expected_sample_weight: None | bool = None,
        expected_fit_params: None | Sequence[str] = None,
    ) -> None:
        ...

    def fit(
        self: CheckingClassifier_Self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        **fit_params,
    ) -> CheckingClassifier_Self:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def score(
        self, X: None | MatrixLike = None, Y: None | MatrixLike | ArrayLike = None
    ) -> float:
        ...


class NoSampleWeightWrapper(BaseEstimator):
    def __init__(self, est: None | BaseEstimator = None) -> None:
        ...

    def fit(self, X, y):
        ...

    def predict(self, X):
        ...

    def predict_proba(self, X):
        ...
