from pandas._libs.tslibs.frequencies import FreqGroup as FreqGroup, get_base_alias as get_base_alias, get_freq as get_freq, is_subperiod as is_subperiod, is_superperiod as is_superperiod
from pandas._libs.tslibs.period import Period as Period
from pandas.core.dtypes.generic import ABCDatetimeIndex as ABCDatetimeIndex, ABCPeriodIndex as ABCPeriodIndex, ABCTimedeltaIndex as ABCTimedeltaIndex
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.converter import TimeSeries_DateFormatter as TimeSeries_DateFormatter, TimeSeries_DateLocator as TimeSeries_DateLocator, TimeSeries_TimedeltaFormatter as TimeSeries_TimedeltaFormatter
from pandas.tseries.offsets import DateOffset as DateOffset
from typing import Any

def format_dateaxis(subplot: Any, freq: Any, index: Any) -> None: ...
