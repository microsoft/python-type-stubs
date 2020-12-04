from typing import Any

from faker.providers import BaseProvider as BaseProvider

class Provider(BaseProvider):
    safe_colors: Any = ...
