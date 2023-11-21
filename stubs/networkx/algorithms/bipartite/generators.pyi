import math
import numbers
from functools import reduce

from numpy.typing import ArrayLike

from ...classes.graph import Graph
from ...utils import nodes_or_number, py_random_state

__all__ = [
    "configuration_model",
    "havel_hakimi_graph",
    "reverse_havel_hakimi_graph",
    "alternating_havel_hakimi_graph",
    "preferential_attachment_graph",
    "random_graph",
    "gnmk_random_graph",
    "complete_bipartite_graph",
]

def complete_bipartite_graph(n1, n2, create_using=None): ...
@py_random_state(3)
def configuration_model(aseq: ArrayLike, bseq: ArrayLike, create_using=None, seed=None): ...
def havel_hakimi_graph(aseq: ArrayLike, bseq: ArrayLike, create_using=None): ...
def reverse_havel_hakimi_graph(aseq: ArrayLike, bseq: ArrayLike, create_using=None): ...
def alternating_havel_hakimi_graph(aseq: ArrayLike, bseq: ArrayLike, create_using=None): ...
@py_random_state(3)
def preferential_attachment_graph(aseq: ArrayLike, p: float, create_using=None, seed=None): ...
@py_random_state(3)
def random_graph(n: int, m: int, p: float, seed=None, directed=False): ...
@py_random_state(3)
def gnmk_random_graph(n: int, m: int, k: int, seed=None, directed=False): ...
