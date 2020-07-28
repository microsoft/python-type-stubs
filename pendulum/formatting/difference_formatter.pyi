import pendulum
import typing
from ..locales.locale import Locale as Locale
from pendulum.utils._compat import decode as decode

class DifferenceFormatter:
    def __init__(self, locale: str = ...) -> None: ...
    def format(self, diff: pendulum.Period, is_now: bool=..., absolute: bool=..., locale: typing.Optional[str]=...) -> str: ...
