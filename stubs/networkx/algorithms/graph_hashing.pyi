from collections import Counter, defaultdict
from hashlib import blake2b
from typing import Mapping

from ..classes.graph import Graph

__all__ = ["weisfeiler_lehman_graph_hash", "weisfeiler_lehman_subgraph_hashes"]

def weisfeiler_lehman_graph_hash(
    G: Graph,
    edge_attr: str | None = None,
    node_attr: str | None = None,
    iterations: int = 3,
    digest_size: int = 16,
) -> str: ...
def weisfeiler_lehman_subgraph_hashes(
    G: Graph,
    edge_attr: str | None = None,
    node_attr: str | None = None,
    iterations: int = 3,
    digest_size: int = 16,
) -> Mapping: ...
