from . import util as util
from sqlalchemy.cprocessors import (
    DecimalResultProcessor as DecimalResultProcessor,
    UnicodeResultProcessor as UnicodeResultProcessor,
    int_to_boolean as int_to_boolean,
    str_to_date as str_to_date,
    str_to_datetime as str_to_datetime,
    str_to_time as str_to_time,
    to_float as to_float,
    to_str as to_str,
)
from typing import Any, AnyStr, Callable, Dict, Optional, Pattern, Type, TypeVar, Text

_T = TypeVar("_T")


def str_to_datetime_processor_factory(regexp: Pattern[str], type_: Type[_T]) -> Callable[[AnyStr], _T]:
    ...

def py_fallback() -> Dict[str, Any]:
    ...


def to_unicode_processor_factory(encoding: str, errors: Optional[str] = ...) -> Callable[[AnyStr], Text]:
    ...


def to_conditional_unicode_processor_factory(encoding: str, errors: Optional[str] = ...) -> Callable[[AnyStr], Text]:
    ...


def to_decimal_processor_factory(target_class: Type[_T], scale: float) -> [Callable[Any]]:
    ...

