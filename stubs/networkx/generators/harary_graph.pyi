from ..classes.graph import Graph
from ..exception import NetworkXError

__all__ = ["hnm_harary_graph", "hkn_harary_graph"]

def hnm_harary_graph(n, m, create_using=None): ...
def hkn_harary_graph(k, n, create_using=None): ...
