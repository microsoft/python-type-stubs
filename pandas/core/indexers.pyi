import numpy as np
from typing import Any, Optional, Tuple
from pandas._typing import AnyArrayLike as AnyArrayLike
#from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like
#from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries

def is_list_like_indexer(key: Any) -> bool: ...
def is_scalar_indexer(indexer: Any, arr_value: Any) -> bool: ...
def is_empty_indexer(indexer: Any, arr_value: np.ndarray) -> bool: ...
def check_setitem_lengths(indexer: Any, value: Any, values: Any) -> None: ...
def validate_indices(indices: np.ndarray, n: int) -> None: ...
def maybe_convert_indices(indices: Any, n: int) -> Any: ...
def length_of_indexer(indexer: Any, target: Any=...) -> int: ...
def deprecate_ndim_indexing(result: Any) -> None: ...
def check_array_indexer(array: AnyArrayLike, indexer: Any) -> Any: ...

class BaseIndexer:
    def __init__(
        self, index_array: Optional[np.ndarray] = ..., window_size: int = ..., **kwargs,
    ): ...
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...

class FixedWindowIndexer(BaseIndexer):
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...

class VariableWindowIndexer(BaseIndexer):
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...

class VariableOffsetWindowIndexer(BaseIndexer):
    def __init__(
        self,
        index_array: Optional[np.ndarray] = ...,
        window_size: int = ...,
        index=...,
        offset=...,
        **kwargs,
    ): ...
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...

class ExpandingIndexer(BaseIndexer):
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...

class FixedForwardWindowIndexer(BaseIndexer):
    def get_window_bounds(
        self,
        num_values: int = ...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        closed: Optional[str] = ...,
    ) -> Tuple[np.ndarray, np.ndarray]: ...
