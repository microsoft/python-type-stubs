from collections import defaultdict

from ...classes.graph import Graph

__all__ = ["k_clique_communities"]

def k_clique_communities(G: Graph, k: int, cliques=None): ...
