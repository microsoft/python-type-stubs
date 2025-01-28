import warnings
from collections.abc import Collection, Generator, Iterator, Mapping

from numpy.typing import ArrayLike

from ._typing import Scalar
from .classes.graph import Graph

__all__ = [
    "to_networkx_graph",
    "from_dict_of_dicts",
    "to_dict_of_dicts",
    "from_dict_of_lists",
    "to_dict_of_lists",
    "from_edgelist",
    "to_edgelist",
]

def to_networkx_graph(data, create_using=None, multigraph_input=False): ...
def to_dict_of_lists(G: Graph, nodelist: ArrayLike | None = None): ...
def from_dict_of_lists(d, create_using=None): ...
def to_dict_of_dicts(G: Graph, nodelist: ArrayLike | None = None, edge_data: Scalar | None = None) -> Mapping: ...
def from_dict_of_dicts(d: dict[dict, dict], create_using=None, multigraph_input=False): ...
def to_edgelist(G: Graph, nodelist: ArrayLike | None = None): ...
def from_edgelist(edgelist, create_using=None): ...
