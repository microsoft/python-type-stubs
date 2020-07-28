import typing
from .date import Date as Date
from .datetime import DateTime as DateTime
from .time import Duration as Duration, Time as Time
from .tz import UTC as UTC

def parse(text: str, **options: typing.Any) -> typing.Union[Date, Time, DateTime, Duration]: ...
