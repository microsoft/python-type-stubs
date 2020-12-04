from typing import Any

from .. import Provider as AutomotiveProvider

class Provider(AutomotiveProvider):
    license_formats: Any = ...
    def license_plate_regex_formats(self): ...
