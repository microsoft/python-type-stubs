from collections.abc import Generator, Iterable
from typing import Iterator, List, Optional, Tuple, Type, Union, Any, Callable
from numpy.typing import ArrayLike
from numpy.random import RandomState

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Raghav RV <rvraghav93@gmail.com>
#         Leandro Hermida <hermidal@cs.umd.edu>
#         Rodion Martynov <marrodion@gmail.com>
# License: BSD 3 clause

from collections.abc import Iterable
from collections import defaultdict
import warnings
from itertools import chain, combinations
from math import ceil, floor
import numbers
from abc import ABCMeta, abstractmethod
from inspect import signature

import numpy as np
from scipy.special import comb

from ..utils import indexable, check_random_state, _safe_indexing
from ..utils import _approximate_mode
from ..utils.validation import _num_samples, column_or_1d
from ..utils.validation import check_array
from ..utils.multiclass import type_of_target
from ..base import _pprint
from numpy import float64, ndarray
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix

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
        self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...

    # Since subclasses must implement either _iter_test_masks or
    # _iter_test_indices, neither can be abstract.
    def _iter_test_masks(
        self,
        X: Optional[ndarray] = None,
        y: Optional[ndarray] = None,
        groups: Optional[ndarray] = None,
    ) -> Iterator[ndarray]: ...
    def _iter_test_indices(self, X=None, y=None, groups=None): ...
    @abstractmethod
    def get_n_splits(self, X=None, y=None, groups=None): ...
    def __repr__(self): ...

class LeaveOneOut(BaseCrossValidator):
    def _iter_test_indices(self, X, y=None, groups=None): ...
    def get_n_splits(self, X: ArrayLike, y: Any = None, groups: Any = None) -> int: ...

class LeavePOut(BaseCrossValidator):
    def __init__(self, p: int): ...
    def _iter_test_indices(self, X, y=None, groups=None): ...
    def get_n_splits(self, X: ArrayLike, y: Any = None, groups: Any = None): ...

class _BaseKFold(BaseCrossValidator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, n_splits: int, *, shuffle, random_state) -> None: ...
    def split(
        self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...
    def get_n_splits(
        self,
        X: Optional[Union[ndarray, List[str]]] = None,
        y: Optional[ndarray] = None,
        groups: None = None,
    ) -> int: ...

class KFold(_BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        shuffle: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _iter_test_indices(
        self, X: ndarray, y: Optional[ndarray] = None, groups: Optional[ndarray] = None
    ) -> Iterator[ndarray]: ...

class GroupKFold(_BaseKFold):
    def __init__(self, n_splits: int = 5) -> None: ...
    def _iter_test_indices(self, X: ndarray, y: ndarray, groups: ndarray) -> Iterator[ndarray]: ...
    def split(self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None) -> Iterator[Any]: ...

class StratifiedKFold(_BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        shuffle: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _make_test_folds(self, X: Union[ndarray, List[str]], y: Optional[ndarray] = None) -> ndarray: ...
    def _iter_test_masks(
        self,
        X: Union[ndarray, List[str]],
        y: Optional[ndarray] = None,
        groups: Optional[ndarray] = None,
    ) -> Iterator[ndarray]: ...
    def split(self, X: ArrayLike, y: ArrayLike, groups: Optional[ndarray] = None) -> Iterator[Any]: ...

class StratifiedGroupKFold(_BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        shuffle: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _iter_test_indices(self, X: ndarray, y: ndarray, groups: ndarray) -> Iterator[List[int]]: ...
    def _find_best_fold(self, y_counts_per_fold: ndarray, y_cnt: ndarray, group_y_counts: ndarray) -> int: ...

class TimeSeriesSplit(_BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        max_train_size: int | None = None,
        test_size: int | None = None,
        gap: int = 0,
    ) -> None: ...
    def split(
        self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...

class LeaveOneGroupOut(BaseCrossValidator):
    def _iter_test_masks(self, X, y, groups): ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: ArrayLike | None = None) -> int: ...
    def split(self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None): ...

class LeavePGroupsOut(BaseCrossValidator):
    def __init__(self, n_groups: int): ...
    def _iter_test_masks(self, X, y, groups): ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: ArrayLike | None = None) -> int: ...
    def split(self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None): ...

class _RepeatedSplits(metaclass=ABCMeta):
    def __init__(
        self,
        cv: Callable,
        *,
        n_repeats: int = 10,
        random_state: int | RandomState | None = None,
        **cvargs,
    ) -> None: ...
    def split(
        self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...
    def get_n_splits(
        self,
        X: Optional[ndarray] = None,
        y: Optional[ndarray] = None,
        groups: ArrayLike | None = None,
    ) -> int: ...
    def __repr__(self): ...

class RepeatedKFold(_RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: int = 5,
        n_repeats: int = 10,
        random_state: int | RandomState | None = None,
    ): ...

class RepeatedStratifiedKFold(_RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: int = 5,
        n_repeats: int = 10,
        random_state: int | RandomState | None = None,
    ) -> None: ...

class BaseShuffleSplit(metaclass=ABCMeta):
    def __init__(self, n_splits: int = 10, *, test_size=None, train_size=None, random_state=None) -> None: ...
    def split(
        self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...
    @abstractmethod
    def _iter_indices(self, X, y=None, groups=None): ...
    def get_n_splits(
        self,
        X: Optional[ndarray] = None,
        y: Optional[ndarray] = None,
        groups: None = None,
    ) -> int: ...
    def __repr__(self): ...

class ShuffleSplit(BaseShuffleSplit):
    def __init__(
        self,
        n_splits: int = 10,
        *,
        test_size: float | int | None = None,
        train_size: float | int | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _iter_indices(
        self, X: ndarray, y: Optional[ndarray] = None, groups: Optional[ndarray] = None
    ) -> Iterator[Tuple[ndarray, ndarray]]: ...

class GroupShuffleSplit(ShuffleSplit):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        test_size: float | int | None = None,
        train_size: float | int | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _iter_indices(self, X: ndarray, y: ndarray, groups: ndarray) -> Iterator[Tuple[ndarray, ndarray]]: ...
    def split(self, X: ArrayLike, y: ArrayLike | None = None, groups: ArrayLike | None = None) -> Iterator[Any]: ...

class StratifiedShuffleSplit(BaseShuffleSplit):
    def __init__(
        self,
        n_splits: int = 10,
        *,
        test_size: float | int | None = None,
        train_size: float | int | None = None,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _iter_indices(self, X: ndarray, y: ndarray, groups: Optional[ndarray] = None) -> Iterator[Tuple[ndarray, ndarray]]: ...
    def split(self, X: ArrayLike, y: ArrayLike, groups: Optional[ndarray] = None) -> Iterator[Any]: ...

def _validate_shuffle_split(
    n_samples: int,
    test_size: Optional[Union[int, float]],
    train_size: Optional[Union[int, float, float64]],
    default_test_size: Optional[float] = None,
) -> Tuple[int, int]: ...

class PredefinedSplit(BaseCrossValidator):
    def __init__(self, test_fold: ArrayLike): ...
    def split(self, X: Any = None, y: Any = None, groups: Any = None): ...
    def _iter_test_masks(self): ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...

class _CVIterableWrapper(BaseCrossValidator):
    def __init__(self, cv): ...
    def get_n_splits(self, X: Any = None, y: Any = None, groups: Any = None) -> int: ...
    def split(self, X: Any = None, y: Any = None, groups: Any = None): ...

def check_cv(
    cv: int | Generator | Iterable = 5,
    y: ArrayLike | None = None,
    *,
    classifier: bool = False,
) -> BaseCrossValidator: ...
def train_test_split(
    *arrays,
    test_size: float | int | None = None,
    train_size: float | int | None = None,
    random_state: int | RandomState | None = None,
    shuffle: bool = True,
    stratify: ArrayLike | None = None,
) -> list: ...
def _build_repr(self): ...
def _yields_constant_splits(cv: Union[StratifiedKFold, KFold]) -> bool: ...
