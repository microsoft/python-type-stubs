from numpy.typing import ArrayLike
from ...classes.graph import Graph

__all__ = ["generate_edgelist", "write_edgelist", "parse_edgelist", "read_edgelist"]

from ...utils import not_implemented_for, open_file

def write_edgelist(
    G: Graph,
    path,
    comments: str = "#",
    delimiter: str = " ",
    data: bool | ArrayLike = True,
    encoding: str = "utf-8",
): ...
def generate_edgelist(G: Graph, delimiter: str = " ", data=True) -> str: ...
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
