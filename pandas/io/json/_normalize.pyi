from pandas import DataFrame as DataFrame
#from pandas._libs.writers import convert_json_to_lines as convert_json_to_lines
from pandas._typing import Scalar as Scalar
from pandas.util._decorators import deprecate as deprecate
from typing import Any, Optional

def convert_to_line_delimits(s: Any): ...
def nested_to_record(ds: Any, prefix: str=..., sep: str=..., level: int=..., max_level: Optional[int]=...) -> Any: ...

json_normalize: Any
