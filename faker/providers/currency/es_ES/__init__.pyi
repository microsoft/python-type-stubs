from typing import Any

from .. import Provider as CurrencyProvider

class Provider(CurrencyProvider):
    currencies: Any = ...
