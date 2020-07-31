from .. import Provider as SsnProvider
from typing import Any

def checksum(sin: Any): ...

class Provider(SsnProvider):
    def ssn(self): ...
