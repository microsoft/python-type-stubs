from typing import Any

from faker.utils import checksums as checksums

from .. import Provider as BaseProvider

class Provider(BaseProvider):
    aadhaar_id_formats: Any = ...
    def aadhaar_id(self): ...
