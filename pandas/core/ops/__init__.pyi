from pandas import DataFrame as DataFrame
from pandas._libs import Timedelta as Timedelta, Timestamp as Timestamp, lib as lib
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op as maybe_dispatch_ufunc_to_dunder_op
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import is_list_like as is_list_like, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCExtensionArray as ABCExtensionArray, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.ops.array_ops import arithmetic_op as arithmetic_op, comp_method_OBJECT_ARRAY as comp_method_OBJECT_ARRAY, comparison_op as comparison_op, define_na_arithmetic_op as define_na_arithmetic_op, get_array_op as get_array_op, logical_op as logical_op
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.ops.dispatch import should_series_dispatch as should_series_dispatch
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison
from pandas.core.ops.mask_ops import kleene_and as kleene_and, kleene_or as kleene_or, kleene_xor as kleene_xor
from pandas.core.ops.methods import add_flex_arithmetic_methods as add_flex_arithmetic_methods, add_special_arithmetic_methods as add_special_arithmetic_methods
from pandas.core.ops.roperator import radd as radd, rand_ as rand_, rdiv as rdiv, rdivmod as rdivmod, rfloordiv as rfloordiv, rmod as rmod, rmul as rmul, ror_ as ror_, rpow as rpow, rsub as rsub, rtruediv as rtruediv, rxor as rxor
from pandas.util._decorators import Appender as Appender
from typing import Any, Optional, Set, Tuple

ARITHMETIC_BINOPS: Set[str]
COMPARISON_BINOPS: Set[str]

def get_op_result_name(left: Any, right: Any): ...
def maybe_upcast_for_op(obj: Any, shape: Tuple[int, ...]) -> Any: ...
def fill_binop(left: Any, right: Any, fill_value: Any): ...
def dispatch_to_series(left: Any, right: Any, func: Any, str_rep: Optional[Any] = ..., axis: Optional[Any] = ...): ...
