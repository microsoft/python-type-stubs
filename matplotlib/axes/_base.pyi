from typing import Any


class _AxesBase:
    def __getattr__(self, name: str) -> Any: ...  # incomplete
    def __getitem__(self, key): ... # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
