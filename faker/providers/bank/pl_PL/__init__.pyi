from typing import Any

from .. import Provider as BankProvider

class Provider(BankProvider):
    bban_format: Any = ...
    country_code: str = ...
