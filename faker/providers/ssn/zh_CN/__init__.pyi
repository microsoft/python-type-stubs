from typing import Any

from .. import Provider as SsnProvider

class Provider(SsnProvider):
    area_codes: Any = ...
    def ssn(self, min_age: int = ..., max_age: int = ...): ...
