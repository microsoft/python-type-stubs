import numbers
import warnings
from abc import ABCMeta, abstractmethod
from collections import defaultdict as defaultdict
from collections.abc import Iterable
from inspect import signature as signature
from itertools import chain as chain, combinations as combinations
from math import ceil as ceil, floor as floor
from typing import Any, Callable, Iterable, Iterator

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from scipy.special import comb as comb

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..utils import check_random_state as check_random_state, indexable as indexable
from ..utils.multiclass import type_of_target as type_of_target
from ..utils.validation import check_array as check_array, column_or_1d as column_or_1d

__all__ = [
    "BaseCrossValidator",
    "KFold",
    "GroupKFold",
    "LeaveOneGroupOut",
    "LeaveOneOut",
    "LeavePGroupsOut",
    "LeavePOut",
    "RepeatedStratifiedKFold",
    "RepeatedKFold",
    "ShuffleSplit",
    "GroupShuffleSplit",
    "StratifiedKFold",
    "StratifiedGroupKFold",
    "StratifiedShuffleSplit",
    "PredefinedSplit",
    "train_test_split",
    "check_cv",
]

class BaseCrossValidator(metaclass=ABCMeta):
    def split(
        self,
        X: list[str] | MatrixLike,
        y: None | ArrayLike = None,
        groups: None | ArrayLike = None,
    ) -> Iterator[tuple[ndarray, ndarray]]: ...
    @abstractmethod
    def get_n_splits(self, X=None, y=None, groups=None) -> int: ...

class LeaveOneOut(BaseCrossValidator):
    def get_n_splits(self, X: MatrixLike, y: Any = None, groups: Any = None) -> int: ...

class LeavePOut(BaseCrossValidator):
    def __init__(self, p: Int) -> None: ...
    def get_n_splits(self, X: MatrixLike, y: Any = None, groups: Any = None): ...

class _BaseKFold(BaseCrossValidator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, n_splits: int, *, shuffle, random_state) -> None: ...
    def split(
        self,
        X: list[str] | MatrixLike,
        y: None | ArrayLike = None,
        groups: None | ArrayLike = None,
    ) -> Iterator[tuple[ndarray, ndarray]]: ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...

class KFold(_BaseKFold):
    def __init__(
        self,
        n_splits: Int = 5,
        *,
        shuffle: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class GroupKFold(_BaseKFold):
    def __init__(self, n_splits: Int = 5) -> None: ...
    def split(self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None) -> Iterator[Any]: ...

class StratifiedKFold(_BaseKFold):
    def __init__(
        self,
        n_splits: Int = 5,
        *,
        shuffle: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def split(self, X: list[str] | MatrixLike, y: ArrayLike, groups: Any = None) -> Iterator[Any]: ...

class StratifiedGroupKFold(_BaseKFold):
    def __init__(
        self,
        n_splits: Int = 5,
        shuffle: bool = False,
        random_state: None | RandomState | int = None,
    ) -> None: ...

class TimeSeriesSplit(_BaseKFold):
    def __init__(
        self,
        n_splits: Int = 5,
        *,
        max_train_size: None | Int = None,
        test_size: None | Int = None,
        gap: Int = 0,
    ) -> None: ...
    def split(
        self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None
    ) -> Iterator[tuple[ndarray, ndarray]]: ...

class LeaveOneGroupOut(BaseCrossValidator):
    def get_n_splits(self, X: Any = None, y: Any = None, groups: None | ArrayLike = None) -> int: ...
    def split(self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None): ...

class LeavePGroupsOut(BaseCrossValidator):
    def __init__(self, n_groups: Int) -> None: ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: None | ArrayLike = None) -> int: ...
    def split(self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None): ...

class _RepeatedSplits(BaseCrossValidator, metaclass=ABCMeta):
    def __init__(
        self,
        cv: Callable,
        *,
        n_repeats: Int = 10,
        random_state: RandomState | None | Int = None,
        **cvargs,
    ) -> None: ...
    def split(
        self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None
    ) -> Iterator[tuple[ndarray, ndarray]]: ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: None | ArrayLike = None) -> int: ...

class RepeatedKFold(_RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: Int = 5,
        n_repeats: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class RepeatedStratifiedKFold(_RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: Int = 5,
        n_repeats: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class BaseShuffleSplit(BaseCrossValidator, metaclass=ABCMeta):
    def __init__(self, n_splits: int = 10, *, test_size=None, train_size=None, random_state=None) -> None: ...
    def split(
        self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None
    ) -> Iterator[tuple[ndarray, ndarray]]: ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...

class ShuffleSplit(BaseShuffleSplit):
    def __init__(
        self,
        n_splits: Int = 10,
        *,
        test_size: None | Float = None,
        train_size: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class GroupShuffleSplit(ShuffleSplit):
    def __init__(
        self,
        n_splits: Int = 5,
        *,
        test_size: float | None = None,
        train_size: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def split(self, X: MatrixLike, y: None | ArrayLike = None, groups: None | ArrayLike = None) -> Iterator[Any]: ...

class StratifiedShuffleSplit(BaseShuffleSplit):
    def __init__(
        self,
        n_splits: Int = 10,
        *,
        test_size: None | Float = None,
        train_size: None | Float = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def split(self, X: MatrixLike, y: ArrayLike, groups: Any = None) -> Iterator[Any]: ...

class PredefinedSplit(BaseCrossValidator):
    def __init__(self, test_fold: ArrayLike) -> None: ...
    def split(self, X: Any = None, y: Any = None, groups: Any = None): ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...

class _CVIterableWrapper(BaseCrossValidator):
    def __init__(self, cv) -> None: ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...
    def split(self, X: Any = None, y: Any = None, groups: Any = None): ...

def check_cv(
    cv: Iterable | int | BaseCrossValidator | None = 5,
    y: None | ArrayLike = None,
    *,
    classifier: bool = False,
) -> BaseCrossValidator: ...
def train_test_split(
    *arrays,
    test_size: None | Float = None,
    train_size: None | Float = None,
    random_state: RandomState | None | Int = None,
    shuffle: bool = True,
    stratify: None | ArrayLike = None,
) -> list: ...
