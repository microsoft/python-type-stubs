__all__ = [
    "generate_multiline_adjlist",
    "write_multiline_adjlist",
    "parse_multiline_adjlist",
    "read_multiline_adjlist",
]

from ..classes.graph import Graph
from ..utils import open_file

def generate_multiline_adjlist(G: Graph, delimiter: str = " ") -> str: ...
def write_multiline_adjlist(G: Graph, path, delimiter: str = " ", comments: str = "#", encoding: str = "utf-8"): ...
def parse_multiline_adjlist(
    lines,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    edgetype=None,
): ...
def read_multiline_adjlist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    edgetype=None,
    encoding="utf-8",
): ...
