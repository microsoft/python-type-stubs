from collections import OrderedDict
#from pandas._libs.lib import is_bool as is_bool, is_integer as is_integer
from pandas.errors import UnsupportedFunctionCall as UnsupportedFunctionCall
from pandas.util._validators import validate_args as validate_args, validate_args_and_kwargs as validate_args_and_kwargs, validate_kwargs as validate_kwargs
from typing import Any, Dict, Optional, Union

class CompatValidator:
    fname: Any = ...
    method: Any = ...
    defaults: Any = ...
    max_fname_arg_count: Any = ...
    def __init__(self, defaults: Any, fname: Optional[Any] = ..., method: Optional[Any] = ..., max_fname_arg_count: Optional[Any] = ...) -> None: ...
    def __call__(self, args: Any, kwargs: Any, fname: Optional[Any] = ..., max_fname_arg_count: Optional[Any] = ..., method: Optional[Any] = ...) -> None: ...

ARGMINMAX_DEFAULTS: Any
validate_argmin: Any
validate_argmax: Any

def process_skipna(skipna: Any, args: Any): ...
def validate_argmin_with_skipna(skipna: Any, args: Any, kwargs: Any): ...
def validate_argmax_with_skipna(skipna: Any, args: Any, kwargs: Any): ...

ARGSORT_DEFAULTS: OrderedDict[str, Optional[Union[int, str]]]
validate_argsort: Any
ARGSORT_DEFAULTS_KIND: OrderedDict[str, Optional[int]]
validate_argsort_kind: Any

def validate_argsort_with_ascending(ascending: Any, args: Any, kwargs: Any): ...

CLIP_DEFAULTS: Any
validate_clip: Any

def validate_clip_with_axis(axis: Any, args: Any, kwargs: Any): ...

CUM_FUNC_DEFAULTS: OrderedDict[str, Any]
validate_cum_func: Any
validate_cumsum: Any

def validate_cum_func_with_skipna(skipna: Any, args: Any, kwargs: Any, name: Any): ...

ALLANY_DEFAULTS: OrderedDict[str, Optional[bool]]
validate_all: Any
validate_any: Any
LOGICAL_FUNC_DEFAULTS: Any
validate_logical_func: Any
MINMAX_DEFAULTS: Any
validate_min: Any
validate_max: Any
RESHAPE_DEFAULTS: Dict[str, str]
validate_reshape: Any
REPEAT_DEFAULTS: Dict[str, Any]
validate_repeat: Any
ROUND_DEFAULTS: Dict[str, Any]
validate_round: Any
SORT_DEFAULTS: OrderedDict[str, Optional[Union[int, str]]]
validate_sort: Any
STAT_FUNC_DEFAULTS: OrderedDict[str, Optional[Any]]
PROD_DEFAULTS: Any
SUM_DEFAULTS: Any
MEDIAN_DEFAULTS: Any
validate_stat_func: Any
validate_sum: Any
validate_prod: Any
validate_mean: Any
validate_median: Any
STAT_DDOF_FUNC_DEFAULTS: OrderedDict[str, Optional[bool]]
validate_stat_ddof_func: Any
TAKE_DEFAULTS: OrderedDict[str, Optional[str]]
validate_take: Any

def validate_take_with_convert(convert: Any, args: Any, kwargs: Any): ...

TRANSPOSE_DEFAULTS: Any
validate_transpose: Any

def validate_window_func(name: Any, args: Any, kwargs: Any) -> None: ...
def validate_rolling_func(name: Any, args: Any, kwargs: Any) -> None: ...
def validate_expanding_func(name: Any, args: Any, kwargs: Any) -> None: ...
def validate_groupby_func(name: Any, args: Any, kwargs: Any, allowed: Optional[Any] = ...) -> None: ...

RESAMPLER_NUMPY_OPS: Any

def validate_resampler_func(method: Any, args: Any, kwargs: Any) -> None: ...
def validate_minmax_axis(axis: Any) -> None: ...
