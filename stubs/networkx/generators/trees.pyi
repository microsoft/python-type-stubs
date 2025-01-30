from collections import defaultdict

from ..classes.digraph import DiGraph
from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = ["prefix_tree", "random_tree", "prefix_tree_recursive"]

def prefix_tree(paths) -> DiGraph: ...
def prefix_tree_recursive(paths) -> DiGraph: ...

# From the Wikipedia article on Prüfer sequences:
#
# > Generating uniformly distributed random Prüfer sequences and
# > converting them into the corresponding trees is a straightforward
# > method of generating uniformly distributed random labelled trees.
#
@py_random_state(1)
def random_tree(n: int, seed=None, create_using=None): ...
