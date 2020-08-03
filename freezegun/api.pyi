import datetime
import numbers
import types
from typing import (
    Any,
    Awaitable,
    Callable,
    Generator,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

_T = TypeVar("_T")

class TickingDateTimeFactory(object):
    def __init__(
        self, time_to_freeze: datetime.datetime, start: datetime.datetime
    ) -> None:
        self.time_to_freeze: datetime.datetime = ...
        self.start: datetime.datetime = ...
    def __call__(self) -> datetime.datetime: ...

class FrozenDateTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime) -> None:
        self.time_to_freeze: datetime.datetime = ...
    def __call__(self) -> datetime.datetime: ...
    def tick(
        self, delta: Union[float, numbers.Real, datetime.timedelta] = ...
    ) -> None: ...
    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ) -> None:
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...

class StepTickTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime, step_width: float) -> None:
        self.time_to_freeze: datetime.datetime = ...
        self.step_width: float = ...
    def __call__(self) -> datetime.datetime: ...
    def tick(self, delta: Optional[datetime.timedelta] = ...) -> None: ...
    def update_step_width(self, step_width: float) -> None:
        self.step_width = ...
    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ) -> None:
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...

class _freeze_time:
    time_to_freeze: datetime.datetime = ...
    tz_offset: float = ...
    ignore: Sequence[str] = ...
    tick: bool = ...
    auto_tick_seconds: float = ...
    undo_changes: Sequence[Tuple[types.ModuleType, str, Any]] = ...
    modules_at_start: Sequence[str] = ...
    as_arg: bool = ...
    def __init__(
        self,
        time_to_freeze_str: Union[
            None, str, datetime.datetime, datetime.date, datetime.timedelta
        ],
        tz_offset: float,
        ignore: Sequence[str],
        tick: bool,
        as_arg: bool,
        auto_tick_seconds: float,
    ) -> None: ...
    @overload
    def __call__(self, func: Type[_T]) -> Type[_T]: ...
    @overload
    def __call__(
        self, func: Callable[..., Awaitable[_T]]
    ) -> Callable[..., Awaitable[_T]]: ...
    @overload
    def __call__(self, func: Callable[..., _T]) -> Callable[..., _T]: ...
    def __enter__(
        self,
    ) -> Union[StepTickTimeFactory, TickingDateTimeFactory, FrozenDateTimeFactory]: ...
    def __exit__(self, *args: Any) -> None: ...
    def start(
        self,
    ) -> Union[StepTickTimeFactory, TickingDateTimeFactory, FrozenDateTimeFactory]: ...
    def stop(self) -> None: ...
    def decorate_class(self, klass: Type[_T]) -> _T: ...
    def decorate_coroutine(self, coroutine: _T) -> _T: ...
    def decorate_callable(self, func: Callable[..., _T],) -> Callable[..., _T]: ...

def freeze_time(
    time_to_freeze: Optional[
        Union[
            str,
            datetime.datetime,
            datetime.date,
            datetime.timedelta,
            Callable[..., Any],
            Generator,
        ]
    ] = ...,
    tz_offset: Optional[float] = ...,
    ignore: Optional[Sequence[str]] = ...,
    tick: Optional[bool] = ...,
    as_arg: Optional[bool] = ...,
    auto_tick_seconds: Optional[float] = ...,
) -> _freeze_time: ...
