from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    jobs: Any = ...
    def job(self): ...
