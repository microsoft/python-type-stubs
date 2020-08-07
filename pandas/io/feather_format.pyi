#from pandas import DataFrame as DataFrame, Int64Index as Int64Index, RangeIndex as RangeIndex
from pandas.core.frame import DataFrame as DataFrame
from pandas._typing import FilePathOrBuffer
#from pandas.compat._optional import import_optional_dependency as import_optional_dependency
#from pandas.io.common import stringify_path as stringify_path
from typing import Any, Optional, Sequence

def to_feather(df: DataFrame, path: Any) -> Any: ...
def read_feather(p: FilePathOrBuffer, columns: Optional[Sequence] = ..., use_threads: bool = ...) -> Any: ...
