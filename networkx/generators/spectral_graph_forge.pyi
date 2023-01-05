from ..classes.graph import Graph

from ..classes.graph import Graph
from ..utils import np_random_state

__all__ = ["spectral_graph_forge"]

@np_random_state(3)
def spectral_graph_forge(
    G: Graph, alpha: float, transformation: str = "identity", seed=None
) -> Graph: ...
