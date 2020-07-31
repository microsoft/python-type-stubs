from faker import Faker as Faker, VERSION as VERSION, documentor as documentor
from faker.config import (
    AVAILABLE_LOCALES as AVAILABLE_LOCALES,
    DEFAULT_LOCALE as DEFAULT_LOCALE,
    META_PROVIDERS_MODULES as META_PROVIDERS_MODULES,
)
from typing import Any, Optional

def print_provider(
    doc: Any,
    provider: Any,
    formatters: Any,
    excludes: Optional[Any] = ...,
    output: Optional[Any] = ...,
) -> None: ...
def print_doc(
    provider_or_field: Optional[Any] = ...,
    args: Optional[Any] = ...,
    lang: Any = ...,
    output: Optional[Any] = ...,
    seed: Optional[Any] = ...,
    includes: Optional[Any] = ...,
) -> None: ...

class Command:
    argv: Any = ...
    prog_name: Any = ...
    def __init__(self, argv: Optional[Any] = ...) -> None: ...
    def execute(self) -> None: ...

def execute_from_command_line(argv: Optional[Any] = ...) -> None: ...
