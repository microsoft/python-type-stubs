import warnings
from contextlib import contextmanager

from ..classes.graph import Graph

__all__ = ["reversed"]

@contextmanager
def reversed(G: Graph): ...
