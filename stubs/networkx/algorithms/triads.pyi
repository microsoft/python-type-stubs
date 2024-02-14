from collections import defaultdict
from itertools import combinations, permutations
from random import sample
from typing import Mapping

from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..utils import not_implemented_for

# See https://github.com/networkx/networkx/pull/1474
# Copyright 2011 Reya Group <http://www.reyagroup.com>
# Copyright 2011 Alex Levenson <alex@isnotinvain.com>
# Copyright 2011 Diederik van Liere <diederik.vanliere@rotman.utoronto.ca>

__all__ = [
    "triadic_census",
    "is_triad",
    "all_triplets",
    "all_triads",
    "triads_by_type",
    "triad_type",
    "random_triad",
]

#: The integer codes representing each type of triad.
#:
#: Triads that are the same up to symmetry have the same code.
TRICODES = ...

#: The names of each type of triad. The order of the elements is
#: important: it corresponds to the tricodes given in :data:`TRICODES`.
TRIAD_NAMES = ...

#: A dictionary mapping triad code to triad name.
TRICODE_TO_NAME: dict = ...

def triadic_census(G: Graph, nodelist: ArrayLike | None = None) -> Mapping: ...
def is_triad(G: Graph) -> bool: ...
def all_triplets(G: Graph): ...
def all_triads(G: Graph): ...
def triads_by_type(G: Graph) -> Mapping: ...
def triad_type(G: Graph) -> str: ...
def random_triad(G: Graph): ...
