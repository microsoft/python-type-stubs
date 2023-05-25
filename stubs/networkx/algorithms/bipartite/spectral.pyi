__all__ = ["spectral_bipartivity"]

from ...classes.graph import Graph

def spectral_bipartivity(G: Graph, nodes=None, weight="weight") -> float | dict: ...
