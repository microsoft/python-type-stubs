from collections import defaultdict, deque

from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...utils import py_random_state

__all__ = ["louvain_communities", "louvain_partitions"]

@py_random_state("seed")
def louvain_communities(G: Graph, weight="weight", resolution=1, threshold=0.0000001, seed=None) -> ArrayLike: ...
@py_random_state("seed")
def louvain_partitions(G: Graph, weight="weight", resolution=1, threshold=0.0000001, seed=None): ...
