from pandas._typing import _Path_or_Buf
from pandas.io.common import stringify_path as stringify_path
from typing import Any, Optional, Sequence

def read_sas(
    path: _Path_or_Buf,
    format: Optional[str] = ...,
    index: Optional[Sequence[Any]] = ...,
    encoding: Optional[str] = ...,
    chunksize: Optional[int] = ...,
    iterator: bool = ...,
) -> Any: ...
