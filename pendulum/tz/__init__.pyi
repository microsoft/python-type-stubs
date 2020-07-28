from .local_timezone import get_local_timezone as get_local_timezone, set_local_timezone as set_local_timezone, test_local_timezone as test_local_timezone
from .timezone import FixedTimezone as _FixedTimezone, Timezone as _Timezone, UTC as UTC
from typing import Tuple, Union

PRE_TRANSITION: str
POST_TRANSITION: str
TRANSITION_ERROR: str
timezones: Tuple[str, ...]

def timezone(name: Union[str, int], extended: bool=...) -> _Timezone: ...
def fixed_timezone(offset: int) -> _FixedTimezone: ...
def local_timezone() -> _Timezone: ...
