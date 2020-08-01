from typing import Any

from .. import Provider as GeoProvider

class Provider(GeoProvider):
    nationalities: Any = ...
    def nationality(self): ...
