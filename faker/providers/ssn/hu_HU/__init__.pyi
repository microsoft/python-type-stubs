from .. import Provider as SsnProvider
from typing import Any, Optional

def zfix(d: Any): ...

class Provider(SsnProvider):
    def ssn(self, dob: Optional[Any] = ..., gender: Optional[Any] = ...): ...
    vat_id_formats: Any = ...
    def vat_id(self): ...
