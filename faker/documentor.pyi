# pyright: strict

from faker.providers import BaseProvider
from typing import Any, Mapping, Optional, Sequence, Tuple


class Documentor:
    generator: Any = ...
    max_name_len: int = ...
    already_generated: Any = ...

    def __init__(self, generator: Any) -> None:
        ...

    def get_formatters(
        self,
        locale: Optional[str] = ...,
        excludes: Optional[Sequence[str]] = ...,
        **kwargs: Any
    ) -> Sequence[Tuple[BaseProvider, Mapping[str, str]]]:
        ...

    def get_provider_formatters(
        self,
        provider: Any,
        prefix: str = ...,
        with_args: bool = ...,
        with_defaults: bool = ...,
    ) -> Mapping[str, str]:
        ...

    @staticmethod
    def get_provider_name(provider_class: BaseProvider) -> str:
        ...

