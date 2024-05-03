__all__ = ["generate_adjlist", "write_adjlist", "parse_adjlist", "read_adjlist"]

from ..classes.graph import Graph
from ..utils import open_file

def generate_adjlist(G: Graph, delimiter: str = " ") -> str: ...
def write_adjlist(G: Graph, path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8"): ...
def parse_adjlist(
    lines,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
): ...
def read_adjlist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    encoding="utf-8",
): ...
