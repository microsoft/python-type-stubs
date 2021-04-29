from typing import Any


class MarkerStyle:
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
