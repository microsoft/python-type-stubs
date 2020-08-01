from typing import Any

from .. import Provider as SsnProvider

def checksum(sin: Any): ...

class Provider(SsnProvider):
    def ssn(self): ...
