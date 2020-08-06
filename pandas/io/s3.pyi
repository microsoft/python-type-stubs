from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
#from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from typing import Any, IO, Optional, Tuple

s3fs: Any

def get_file_and_filesystem(filepath_or_buffer: FilePathOrBuffer, mode: Optional[str]=...) -> Tuple[IO, Any]: ...
def get_filepath_or_buffer(filepath_or_buffer: FilePathOrBuffer, encoding: Optional[str]=..., compression: Optional[str]=..., mode: Optional[str]=...) -> Tuple[IO, Optional[str], Optional[str], bool]: ...
