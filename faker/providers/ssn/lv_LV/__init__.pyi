from typing import Any

from .. import Provider as BaseProvider

class Provider(BaseProvider):
    vat_id_formats: Any = ...
    def vat_id(self): ...
