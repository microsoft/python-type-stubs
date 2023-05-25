from ..classes.multigraph import MultiGraph
from typing import Mapping
from ..classes.multidigraph import MultiDiGraph
from ..classes.graph import Graph
import warnings
from locale import getpreferredencoding

from ..classes.graph import Graph
from ..utils import open_file

__all__ = [
    "write_dot",
    "read_dot",
    "graphviz_layout",
    "pydot_layout",
    "to_pydot",
    "from_pydot",
]

def write_dot(G: Graph, path): ...
def read_dot(path) -> MultiGraph | MultiDiGraph: ...
def from_pydot(P): ...
def to_pydot(N): ...
def graphviz_layout(G: Graph, prog="neato", root=None): ...
def pydot_layout(G: Graph, prog="neato", root=None) -> Mapping: ...
