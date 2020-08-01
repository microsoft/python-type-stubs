#from pandas._libs.lib import item_from_zerodim as item_from_zerodim
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from typing import Any

def unpack_zerodim_and_defer(name: str) -> Any: ...
