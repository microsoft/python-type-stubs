from .. import BaseProvider as BaseProvider
from typing import Any

localized: bool

class Provider(BaseProvider):
    ssn_formats: Any = ...
    def ssn(self): ...
