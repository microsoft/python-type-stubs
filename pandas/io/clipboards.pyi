#from pandas.core.frame import DataFrame
#from pandas import get_option as get_option, option_context as option_context
from pandas.core.frame import DataFrame as DataFrame
from typing import Any, Optional

def read_clipboard(sep: str = ..., **kwargs: Any) -> DataFrame: ...
def to_clipboard(obj: Any, excel: bool = ..., sep: Optional[Any] = ..., **kwargs: Any) -> None: ...
