from .exceptions import InvalidTimezone as InvalidTimezone, InvalidZoneinfoFile as InvalidZoneinfoFile
from .posix_timezone import PosixTimezone as PosixTimezone, posix_spec as posix_spec
from .timezone import Timezone as Timezone
from .transition import Transition as Transition
from .transition_type import TransitionType as TransitionType
from collections import namedtuple
from pendulum.utils._compat import PY2 as PY2

_offset = namedtuple('offset', 'utc_total_offset is_dst abbr_idx')

header = namedtuple('header', 'version utclocals stdwalls leaps transitions types abbr_size')

class Reader:
    def __init__(self, extend: bool=...) -> None: ...
    def read_for(self, timezone: str) -> Timezone: ...
    def read(self, file_path: str) -> Timezone: ...
