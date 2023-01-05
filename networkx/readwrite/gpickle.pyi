__all__ = ["read_gpickle", "write_gpickle"]

import pickle
import warnings

from ..classes.graph import Graph
from ..utils import open_file

def write_gpickle(G: Graph, path, protocol=...): ...
def read_gpickle(path): ...
