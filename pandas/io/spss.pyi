from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
#from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.frame import DataFrame as DataFrame
#from pandas.core.dtypes.inference import is_list_like as is_list_like
#from pathlib import Path as Path
from typing import Optional, Sequence

def read_spss(
    path: FilePathOrBuffer, usecols: Optional[Sequence[str]] = ..., convert_categoricals: bool = ...,
) -> DataFrame: ...
