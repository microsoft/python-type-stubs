from typing import Any


class Artist:
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
