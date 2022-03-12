# def to_timedelta(arg, unit: str = ..., errors: str = ...): ...
from datetime import timedelta
from typing import Literal, Optional, Union, overload
from pandas._libs.tslibs import Timedelta
from pandas._typing import DateTimeErrorChoices, AnyArrayLike, ArrayLike
from pandas.core.frame import Series as Series

# Copied from pandas/_libs/tslibs/timedeltas.pyx

UnitChoices = Literal[
    "Y",
    "y",
    "M",
    "W",
    "w",
    "D",
    "d",
    "days",
    "day",
    "hours",
    "hour",
    "hr",
    "h",
    "m",
    "minute",
    "min",
    "minutes",
    "t",
    "s",
    "seconds",
    "sec",
    "second",
    "ms",
    "milliseconds",
    "millisecond",
    "milli",
    "millis",
    "l",
    "us",
    "microseconds",
    "microsecond",
    "µs",
    "micro",
    "micros",
    "u",
    "ns",
    "nanoseconds",
    "nano",
    "nanos",
    "nanosecond",
    "n",
]

@overload
def to_timedelta(
    arg: Union[str, int, float, timedelta],
    unit: Optional[UnitChoices] = ...,
    errors: DateTimeErrorChoices = ...,
) -> Timedelta: ...
@overload
def to_timedelta(
    arg: Union[list, tuple, range, AnyArrayLike, ArrayLike],
    unit: Optional[UnitChoices] = ...,
    errors: DateTimeErrorChoices = ...,
) -> Series[Timedelta]: ...
