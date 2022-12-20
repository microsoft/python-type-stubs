from ..classes.graph import Graph

from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = [
    "is_valid_joint_degree",
    "is_valid_directed_joint_degree",
    "joint_degree_graph",
    "directed_joint_degree_graph",
]

def is_valid_joint_degree(joint_degrees) -> bool: ...
@py_random_state(1)
def joint_degree_graph(joint_degrees, seed=None) -> Graph: ...
def is_valid_directed_joint_degree(in_degrees, out_degrees, nkk) -> bool: ...
@py_random_state(3)
def directed_joint_degree_graph(in_degrees, out_degrees, nkk, seed=None) -> Graph: ...
