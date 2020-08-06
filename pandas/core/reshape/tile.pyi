#from pandas import Categorical as Categorical, Index as Index, IntervalIndex as IntervalIndex, to_datetime as to_datetime, to_timedelta as to_timedelta
#from pandas._libs import Timedelta as Timedelta, Timestamp as Timestamp
#from pandas._libs.lib import infer_dtype as infer_dtype
#from pandas.core.dtypes.common import ensure_int64 as ensure_int64, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype
#from pandas.core.dtypes.generic import ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import isna as isna
from typing import Any

def cut(x: Any, bins: Any, right: bool=..., labels: Any=..., retbins: bool=..., precision: int=..., include_lowest: bool=..., duplicates: str=...) -> Any: ...
def qcut(x: Any, q: Any, labels: Any=..., retbins: bool=..., precision: int=..., duplicates: str=...) -> Any: ...
