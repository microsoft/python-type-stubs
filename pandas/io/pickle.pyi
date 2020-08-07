import sys
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
#from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer, get_handle as get_handle
from typing import Any, Optional
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

def to_pickle(obj: Any, filepath_or_buffer: FilePathOrBuffer, compression: Optional[str]=..., protocol: int=...) -> Any: ...
def read_pickle(
    filepath_or_buffer_or_reader: FilePathOrBuffer,
    compression: Optional[Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
) -> Any: ...
