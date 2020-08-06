#from pandas.core.dtypes.common import is_list_like as is_list_like, is_scalar as is_scalar
from typing import Any, NamedTuple

class OutputKey(NamedTuple):
    label: str
    position: int

class GroupByMixin: ...

plotting_methods: Any
common_apply_whitelist: Any
series_apply_whitelist: Any
dataframe_apply_whitelist: Any
cythonized_kernels: Any
cython_cast_blacklist: Any
reduction_kernels: Any
transformation_kernels: Any
groupby_other_methods: Any
transform_kernel_whitelist: Any
