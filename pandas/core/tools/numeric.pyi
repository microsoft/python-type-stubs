from pandas._libs import lib as lib
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import ensure_object as ensure_object, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_decimal as is_decimal, is_number as is_number, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from typing import Any, Optional

def to_numeric(arg: Any, errors: str = ..., downcast: Optional[Any] = ...): ...
