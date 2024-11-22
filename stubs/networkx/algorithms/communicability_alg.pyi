
from ..classes.graph import Graph

__all__ = ["communicability", "communicability_exp"]

def communicability(G: Graph) -> dict[dict, dict]: ...
def communicability_exp(G: Graph) -> dict[dict, dict]: ...
