from typing import Any

from matplotlib.artist import Artist
from matplotlib.collections import PolyCollection


class Barbs(PolyCollection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Quiver(PolyCollection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class QuiverKey(Artist):
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
