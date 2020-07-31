from .. import Provider as ColorProvider
from typing import Any

localized: bool

class Provider(ColorProvider):
    all_colors: Any = ...
    safe_colors: Any = ...
