from itertools import combinations

from numpy.typing import ArrayLike

from ..algorithms.simple_paths import is_simple_path as is_path
from ..classes.digraph import DiGraph
from ..classes.graph import Graph
from ..utils import arbitrary_element, not_implemented_for, py_random_state

__all__ = [
    "hamiltonian_path",
    "is_reachable",
    "is_strongly_connected",
    "is_tournament",
    "random_tournament",
    "score_sequence",
]

def index_satisfying(iterable, condition): ...
def is_tournament(G: Graph) -> bool: ...
def hamiltonian_path(G: Graph) -> ArrayLike: ...
@py_random_state(1)
def random_tournament(n: int, seed=None) -> DiGraph: ...
def score_sequence(G: Graph) -> ArrayLike: ...
def tournament_matrix(G: Graph): ...
def is_reachable(G: Graph, s, t) -> bool: ...
def is_strongly_connected(G: Graph) -> bool: ...
