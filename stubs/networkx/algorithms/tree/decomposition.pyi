from itertools import combinations

from networkx import Graph

from ...algorithms import chordal_graph_cliques, complete_to_chordal_graph, moral
from ...classes.graph import Graph
from ...utils import not_implemented_for

__all__ = ["junction_tree"]

def junction_tree(G: Graph) -> Graph: ...
