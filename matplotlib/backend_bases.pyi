from typing import Any


class Event:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class LocationEvent(Event):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class MouseEvent(LocationEvent):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class FigureManagerBase:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class RendererBase:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

def __getattr__(name: str) -> Any: ...  # incomplete
