from ..constants import HOURS_PER_DAY as HOURS_PER_DAY, MINUTES_PER_HOUR as MINUTES_PER_HOUR, MONTHS_OFFSETS as MONTHS_OFFSETS, SECONDS_PER_MINUTE as SECONDS_PER_MINUTE
from ..duration import Duration as Duration
from ..helpers import days_in_year as days_in_year, is_leap as is_leap, is_long_year as is_long_year, week_day as week_day
from ..tz.timezone import FixedTimezone as FixedTimezone, UTC as UTC
from .exceptions import ParserError as ParserError
from typing import Any

ISO8601_DT: Any
ISO8601_DURATION: Any

def parse_iso8601(text: Any): ...
