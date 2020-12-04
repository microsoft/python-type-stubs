from typing import Any

from .. import BaseProvider as BaseProvider

class Provider(BaseProvider):
    jobs: Any = ...
    def job(self): ...
