from pandas import DataFrame as DataFrame, Int64Index as Int64Index, RangeIndex as RangeIndex
from pandas._typing import _Path_or_Buf
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.common import stringify_path as stringify_path
from typing import Any, Optional, Sequence

def to_feather(df: DataFrame, path: Any) -> Any: ...
def read_feather(p: _Path_or_Buf, columns: Optional[Sequence] = ..., use_threads: bool = ...) -> Any: ...
