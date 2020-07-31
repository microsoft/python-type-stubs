from .. import BaseProvider as BaseProvider
from typing import Any

localized: bool

class Provider(BaseProvider):
    license_formats: Any = ...
    def license_plate(self): ...
