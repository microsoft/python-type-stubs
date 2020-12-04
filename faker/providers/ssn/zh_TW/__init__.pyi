from typing import Any

from .. import Provider as SsnProvider

class Provider(SsnProvider):
    ssn_formats: Any = ...
    def ssn(self): ...
