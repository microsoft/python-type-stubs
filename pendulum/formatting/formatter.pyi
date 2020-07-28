import pendulum
import typing
from pendulum.locales.locale import Locale as Locale
from pendulum.utils._compat import decode as decode

class Formatter:
    def format(self, dt: pendulum.DateTime, fmt: str, locale: typing.Optional[typing.Union[str, Locale]]=...) -> str: ...
    def parse(self, time: str, fmt: str, now: pendulum.DateTime, locale: typing.Optional[str]=...) -> typing.Dict[str, typing.Any]: ...
