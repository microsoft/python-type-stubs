from collections import Counter, defaultdict
from collections.abc import Iterable

from ..classes.graph import Graph

__all__ = ["dedensify", "snap_aggregation"]

def dedensify(G: Graph, threshold: int, prefix=None, copy=True): ...
def snap_aggregation(
    G: Graph,
    node_attributes,
    edge_attributes: Iterable = ...,
    prefix: str = "Supernode-",
    supernode_attribute: str = "group",
    superedge_attribute: str = "types",
): ...
