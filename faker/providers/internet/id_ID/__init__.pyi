from typing import Any

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    tlds: Any = ...
