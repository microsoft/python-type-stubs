from logging import Logger
from typing import Any, Optional, Sequence

from faker.generator import Generator as Generator
from faker.utils.loading import list_module as list_module

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
    ) -> Generator: ...
