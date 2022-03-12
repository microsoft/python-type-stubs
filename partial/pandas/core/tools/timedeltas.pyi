# def to_timedelta(arg, unit: str = ..., errors: str = ...): ...
from datetime import timedelta
from typing import Literal, Union, overload
from pandas._libs.tslibs import Timedelta
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
ErrorChoices = Literal["ignore", "raise", "coerce"]

@overload
def to_timedelta(
    arg: Union[str, int, float, timedelta], unit: UnitChoices = "ns", errors: ErrorChoices = "raise"
) -> Timedelta: ...
@overload
def to_timedelta(arg: Union[list, Series], unit: UnitChoices = "ns", errors: ErrorChoices = "raise") -> Series[Timedelta]: ...
