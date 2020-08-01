from typing import Any, Sequence

from faker.utils.loading import \
    find_available_locales as find_available_locales
from faker.utils.loading import \
    find_available_providers as find_available_providers

DEFAULT_LOCALE: str
META_PROVIDERS_MODULES: Sequence[str]
PROVIDERS: Sequence[str]
AVAILABLE_LOCALES: Sequence[str]
