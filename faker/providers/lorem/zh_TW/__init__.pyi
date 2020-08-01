from typing import Any

from .. import Provider as LoremProvider

class Provider(LoremProvider):
    word_connector: str = ...
    word_list: Any = ...
