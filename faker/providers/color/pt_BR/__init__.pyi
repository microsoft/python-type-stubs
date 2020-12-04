from typing import Any

from .. import Provider as ColorProvider

localized: bool

class Provider(ColorProvider):
    all_colors: Any = ...
    safe_colors: Any = ...
