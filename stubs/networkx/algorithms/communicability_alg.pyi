from collections.abc import Mapping

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["communicability", "communicability_exp"]

def communicability(G: Graph) -> dict[dict, dict]: ...
def communicability_exp(G: Graph) -> dict[dict, dict]: ...
