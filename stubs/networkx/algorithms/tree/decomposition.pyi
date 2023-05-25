from networkx import Graph

from itertools import combinations

from ...classes.graph import Graph
from ...algorithms import chordal_graph_cliques, complete_to_chordal_graph, moral
from ...utils import not_implemented_for

__all__ = ["junction_tree"]

def junction_tree(G: Graph) -> Graph: ...
