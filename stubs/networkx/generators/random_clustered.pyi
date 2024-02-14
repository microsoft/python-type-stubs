from ..classes.graph import Graph
from ..classes.multigraph import MultiGraph
from ..utils import py_random_state

__all__ = ["random_clustered_graph"]

@py_random_state(2)
def random_clustered_graph(joint_degree_sequence, create_using=None, seed=None) -> MultiGraph: ...
