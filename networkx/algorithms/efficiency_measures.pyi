from ..classes.graph import Graph
from ..exception import NetworkXNoPath

from ..utils import not_implemented_for

__all__ = ["efficiency", "local_efficiency", "global_efficiency"]

def efficiency(G: Graph, u, v) -> float: ...
def global_efficiency(G: Graph) -> float: ...
def local_efficiency(G: Graph) -> float: ...
