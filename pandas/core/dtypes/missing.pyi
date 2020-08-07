#from pandas._config import get_option as get_option
#from pandas._libs import lib as lib
#from pandas._libs.tslibs import NaT as NaT, iNaT as iNaT
#from pandas.core.dtypes.common import ensure_object as ensure_object, is_bool_dtype as is_bool_dtype, is_complex_dtype as is_complex_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetimelike_v_numeric as is_datetimelike_v_numeric, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, is_string_like_dtype as is_string_like_dtype, is_timedelta64_dtype as is_timedelta64_dtype, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
#from pandas.core.dtypes.generic import ABCDatetimeArray as ABCDatetimeArray, ABCExtensionArray as ABCExtensionArray, ABCGeneric as ABCGeneric, ABCIndexClass as ABCIndexClass, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries, ABCTimedeltaArray as ABCTimedeltaArray
#from pandas.core.dtypes.inference import is_list_like as is_list_like
from typing import Any

isposinf_scalar: Any
isneginf_scalar: Any

def isna(obj: Any): ...
isnull = isna

def notna(obj: Any): ...
notnull = notna

def array_equivalent(left: Any, right: Any, strict_nan: bool=...) -> bool: ...
def na_value_for_dtype(dtype: Any, compat: bool=...) -> Any: ...
def remove_na_arraylike(arr: Any): ...
def is_valid_nat_for_dtype(obj: Any, dtype: Any) -> bool: ...
