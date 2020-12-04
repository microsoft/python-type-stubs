from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    license_formats: Any = ...
    def license_plate(self): ...
