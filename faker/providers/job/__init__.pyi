from .. import BaseProvider as BaseProvider
from typing import Any

localized: bool

class Provider(BaseProvider):
    jobs: Any = ...
    def job(self): ...
