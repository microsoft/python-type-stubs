from .. import Provider as BaseProvider
from faker.utils import checksums as checksums
from typing import Any

class Provider(BaseProvider):
    aadhaar_id_formats: Any = ...
    def aadhaar_id(self): ...
