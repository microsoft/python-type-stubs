from typing import Any

from matplotlib.artist import Artist


class Patch(Artist):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Polygon(Patch):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class FancyArrow(Polygon):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Wedge(Patch):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Rectangle(Patch):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

def __getattr__(name: str) -> Any: ...  # incomplete
