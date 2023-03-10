from typing import Callable, Literal, Self, Sequence
from .validation import check_array as check_array, check_is_fitted as check_is_fitted
from .._typing import Int, MatrixLike, ArrayLike, Estimator
from ..base import BaseEstimator, ClassifierMixin
from numpy import ndarray
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
    def __init__(
        self,
        *,
        check_y: None | Callable = None,
        check_y_params: dict | None = None,
        check_X: None | Callable = None,
        check_X_params: dict | None = None,
        methods_to_check: Sequence[str] | Literal["all", "all"] = "all",
        foo_param: Int = 0,
        expected_sample_weight: bool | None = None,
        expected_fit_params: Sequence[str] | None = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        **fit_params,
    ) -> Self:
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
    def __init__(self, est: Estimator | None = None) -> None:
        ...

    def fit(self, X, y):
        ...

    def predict(self, X):
        ...

    def predict_proba(self, X):
        ...
