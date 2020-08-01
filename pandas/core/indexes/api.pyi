from pandas._libs import NaT as NaT
from pandas.core.indexes.base import Index as Index, InvalidIndexError as InvalidIndexError, _new_Index as _new_Index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.indexes.category import CategoricalIndex as CategoricalIndex
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.interval import IntervalIndex as IntervalIndex
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.numeric import Float64Index as Float64Index, Int64Index as Int64Index, NumericIndex as NumericIndex, UInt64Index as UInt64Index
from pandas.core.indexes.period import PeriodIndex as PeriodIndex
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from typing import Any

def get_objs_combined_axis(objs: Any, intersect: bool=..., axis: Any=..., sort: bool=...) -> Index: ...
def union_indexes(indexes: Any, sort: Any=...) -> Index: ...
def get_consensus_names(indexes: Any): ...
def all_indexes_same(indexes: Any): ...
