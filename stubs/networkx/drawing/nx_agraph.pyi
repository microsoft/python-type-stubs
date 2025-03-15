import os
import tempfile
from collections.abc import Mapping
from typing import Callable

from ..classes.graph import Graph

__all__ = [
    "from_agraph",
    "to_agraph",
    "write_dot",
    "read_dot",
    "graphviz_layout",
    "pygraphviz_layout",
    "view_pygraphviz",
]

def from_agraph(A, create_using=None): ...
def to_agraph(N): ...
def write_dot(G: Graph, path): ...
def read_dot(path): ...
def graphviz_layout(G: Graph, prog: str = "neato", root: str | None = None, args: str = ""): ...
def pygraphviz_layout(G: Graph, prog: str = "neato", root: str | None = None, args: str = "") -> Mapping: ...
def view_pygraphviz(
    G: Graph,
    edgelabel: str | Callable | None = None,
    prog: str = "dot",
    args: str = "",
    suffix: str = "",
    path: str | None = None,
    show: bool = True,
): ...
def display_pygraphviz(graph, path, format: str | None = None, prog: str | None = None, args: str = ""): ...
