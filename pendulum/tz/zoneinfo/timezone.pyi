from .posix_timezone import PosixTimezone as PosixTimezone
from .transition import Transition as Transition
from .transition_type import TransitionType as TransitionType
from pendulum.constants import DAYS_PER_YEAR as DAYS_PER_YEAR, SECS_PER_YEAR as SECS_PER_YEAR
from pendulum.helpers import is_leap as is_leap, local_time as local_time, timestamp as timestamp, week_day as week_day
from typing import List, Optional

class Timezone:
    def __init__(self, transitions: List[Transition], posix_rule: Optional[PosixTimezone]=..., extended: bool=...) -> None: ...
    @property
    def transitions(self) -> List[Transition]: ...
    @property
    def posix_rule(self): ...
