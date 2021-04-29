from typing import Any

class TickHelper:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Formatter(TickHelper):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Locator(TickHelper):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

def __getattr__(name: str) -> Any: ...  # incomplete
