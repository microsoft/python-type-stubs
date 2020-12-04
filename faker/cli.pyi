from typing import Any, Mapping, Optional, Sequence, TextIO

from faker import VERSION as VERSION
from faker import Faker as Faker
from faker.config import AVAILABLE_LOCALES as AVAILABLE_LOCALES
from faker.config import DEFAULT_LOCALE as DEFAULT_LOCALE
from faker.config import META_PROVIDERS_MODULES as META_PROVIDERS_MODULES
from faker.documentor import Documentor
from faker.providers import BaseProvider

def print_provider(
    doc: Documentor,
    provider: BaseProvider,
    formatters: Mapping[str, str],
    excludes: Optional[Sequence[str]] = ...,
    output: Optional[TextIO] = ...,
) -> None: ...
def print_doc(
    provider_or_field: Optional[Any] = ...,
    args: Optional[Sequence[Any]] = ...,
    lang: str = ...,
    output: Optional[TextIO] = ...,
    seed: Optional[Any] = ...,
    includes: Optional[Sequence[str]] = ...,
) -> None: ...

class Command:
    argv: Sequence[str] = ...
    prog_name: str = ...
    def __init__(self, argv: Optional[Sequence[str]] = ...) -> None: ...
    def execute(self) -> None: ...

def execute_from_command_line(argv: Optional[Any] = ...) -> None: ...
