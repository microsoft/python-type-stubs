from collections.abc import Iterable

from numpy.typing import ArrayLike

from ...exception import NetworkXAlgorithmError
from ...utils import not_implemented_for

__all__ = [
    "project",
    "projected_graph",
    "weighted_projected_graph",
    "collaboration_weighted_projected_graph",
    "overlap_weighted_projected_graph",
    "generic_weighted_projected_graph",
]

def projected_graph(B, nodes: ArrayLike | Iterable, multigraph=False): ...
def weighted_projected_graph(B, nodes: ArrayLike | Iterable, ratio=False): ...
def collaboration_weighted_projected_graph(B, nodes: ArrayLike | Iterable): ...
def overlap_weighted_projected_graph(B, nodes: ArrayLike | Iterable, jaccard=True): ...
def generic_weighted_projected_graph(B, nodes: ArrayLike | Iterable, weight_function=None): ...
def project(B, nodes, create_using=None): ...
