from typing import Any


class Widget:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class SubplotTool(Widget):
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
