from typing import Any, Optional

from .. import BaseProvider as BaseProvider

class Provider(BaseProvider):
    def simple_profile(self, sex: Optional[Any] = ...): ...
    def profile(self, fields: Optional[Any] = ..., sex: Optional[Any] = ...): ...
