# pyright: strict

from faker.config import (
    AVAILABLE_LOCALES as AVAILABLE_LOCALES,
    DEFAULT_LOCALE as DEFAULT_LOCALE,
    PROVIDERS as PROVIDERS,
)
from faker.generator import Generator as Generator
from faker.utils.loading import list_module as list_module
from logging import Logger
from typing import Any, Optional, Sequence

logger: Logger
inREPL: bool


class Factory:
    @classmethod
    def create(
        cls,
        locale: Optional[str] = ...,
        providers: Optional[Sequence[str]] = ...,
        generator: Optional[Sequence[Generator]] = ...,
        includes: Optional[Sequence[str]] = ...,
        **config: Any
    ) -> Generator:
        ...
