from typing import Mapping

# This module uses material from the Wikipedia article Hopcroft--Karp algorithm
# <https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>, accessed on
# January 3, 2015, which is released under the Creative Commons
# Attribution-Share-Alike License 3.0
# <http://creativecommons.org/licenses/by-sa/3.0/>. That article includes
# pseudocode, which has been translated into the corresponding Python code.
#
# Portions of this module use code from David Eppstein's Python Algorithms and
# Data Structures (PADS) library, which is dedicated to the public domain (for
# proof, see <http://www.ics.uci.edu/~eppstein/PADS/ABOUT-PADS.txt>).
import collections
import itertools

from .matrix import biadjacency_matrix
from ...classes.graph import Graph

__all__ = [
    "maximum_matching",
    "hopcroft_karp_matching",
    "eppstein_matching",
    "to_vertex_cover",
    "minimum_weight_full_matching",
]

INFINITY = ...

def hopcroft_karp_matching(G: Graph, top_nodes=None) -> Mapping: ...
def eppstein_matching(G: Graph, top_nodes=None) -> Mapping: ...
def to_vertex_cover(G: Graph, matching: Mapping, top_nodes=None): ...

#: Returns the maximum cardinality matching in the given bipartite graph.
#:
#: This function is simply an alias for :func:`hopcroft_karp_matching`.
maximum_matching = ...

def minimum_weight_full_matching(
    G: Graph, top_nodes=None, weight="weight"
) -> Mapping: ...
