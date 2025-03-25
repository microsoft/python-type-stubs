from collections.abc import Mapping
from itertools import chain, count

from ...classes.graph import Graph

__all__ = ["node_link_data", "node_link_graph"]

_attrs = ...

def node_link_data(
    G: Graph,
    attrs: Mapping | None = None,
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    link: str = "links",
) -> Mapping: ...
def node_link_graph(
    data: Mapping,
    directed: bool = False,
    multigraph: bool = True,
    attrs: Mapping | None = None,
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    link: str = "links",
): ...
