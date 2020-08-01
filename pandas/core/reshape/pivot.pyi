from pandas import DataFrame as DataFrame
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.groupby import Grouper as Grouper
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, get_objs_combined_axis as get_objs_combined_axis
from pandas.core.reshape.concat import concat as concat
from pandas.core.reshape.util import cartesian_product as cartesian_product
from pandas.core.series import Series as Series
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any

def pivot_table(data: Any, values: Any=..., index: Any=..., columns: Any=..., aggfunc: Any=..., fill_value: Any=..., margins: Any=..., dropna: Any=..., margins_name: Any=..., observed: Any=...) -> DataFrame: ...
def pivot(data: DataFrame, index: Any=..., columns: Any=..., values: Any=...) -> DataFrame: ...
def crosstab(index: Any, columns: Any, values: Any=..., rownames: Any=..., colnames: Any=..., aggfunc: Any=..., margins: Any=..., margins_name: str=..., dropna: bool=..., normalize: Any=...) -> DataFrame: ...
