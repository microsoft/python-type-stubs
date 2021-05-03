from typing import Any

from matplotlib.artist import Artist
from matplotlib.cm import ScalarMappable


class Collection(Artist, ScalarMappable):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class _CollectionWithSizes(Collection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class LineCollection(Collection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class PolyCollection(_CollectionWithSizes):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class BrokenBarHCollection(PolyCollection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class EventCollection(LineCollection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class QuadMesh(Collection):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class PathCollection(_CollectionWithSizes):
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
