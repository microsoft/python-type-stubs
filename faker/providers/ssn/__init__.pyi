from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    ssn_formats: Any = ...
    def ssn(self): ...
