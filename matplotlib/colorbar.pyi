from typing import Any


class ColorbarBase:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Colorbar(ColorbarBase):
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
