from pandas._typing import FrameOrSeries as FrameOrSeries
from pandas.core.base import PandasObject as PandasObject
from pandas.core.computation.common import result_type_many as result_type_many
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.errors import PerformanceWarning as PerformanceWarning
from typing import Any

def align_terms(terms: Any): ...
def reconstruct_object(typ: Any, obj: Any, axes: Any, dtype: Any): ...
