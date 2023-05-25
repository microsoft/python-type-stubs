from collections.abc import Iterable
from ...classes.graph import Graph
from collections import Counter, defaultdict

from ...classes.graph import Graph
from ...utils import groups, not_implemented_for, py_random_state

__all__ = ["label_propagation_communities", "asyn_lpa_communities"]

@py_random_state(2)
def asyn_lpa_communities(
    G: Graph, weight: str | None = None, seed=None
) -> Iterable: ...
def label_propagation_communities(G: Graph) -> Iterable: ...
