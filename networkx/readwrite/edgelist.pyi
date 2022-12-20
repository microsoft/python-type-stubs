from numpy.typing import ArrayLike

__all__ = [
    "generate_edgelist",
    "write_edgelist",
    "parse_edgelist",
    "read_edgelist",
    "read_weighted_edgelist",
    "write_weighted_edgelist",
]

from ..classes.graph import Graph
from ..utils import open_file

def generate_edgelist(G: Graph, delimiter: str = " ", data=True) -> str: ...
def write_edgelist(
    G: Graph,
    path,
    comments: str = "#",
    delimiter: str = " ",
    data: bool | ArrayLike = True,
    encoding: str = "utf-8",
): ...
def parse_edgelist(
    lines,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    data=True,
): ...
def read_edgelist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    data=True,
    edgetype=None,
    encoding: str = "utf-8",
): ...
def write_weighted_edgelist(
    G: Graph, path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8"
): ...
def read_weighted_edgelist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    encoding: str = "utf-8",
): ...
