from pandas.core.frame import DataFrame as DataFrame
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
#from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer
from typing import List, Optional

def read_orc(path: FilePathOrBuffer, columns: Optional[List[str]] = ..., **kwargs) -> DataFrame: ...
