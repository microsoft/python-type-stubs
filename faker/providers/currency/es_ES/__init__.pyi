from .. import Provider as CurrencyProvider
from typing import Any

class Provider(CurrencyProvider):
    currencies: Any = ...
