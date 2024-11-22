
from numpy.typing import ArrayLike

from ...classes.graph import Graph

__all__ = [
    "greedy_modularity_communities",
    "naive_greedy_modularity_communities",
    "_naive_greedy_modularity_communities",
]

def greedy_modularity_communities(
    G: Graph, weight=None, resolution=1, cutoff=1, best_n=None, n_communities=None
) -> ArrayLike: ...
def naive_greedy_modularity_communities(G: Graph, resolution=1, weight=None) -> ArrayLike: ...

# old name
_naive_greedy_modularity_communities = ...
