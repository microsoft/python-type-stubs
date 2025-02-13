from networkx import DiGraph

# See https://github.com/networkx/networkx/pull/1474
# Copyright 2011 Reya Group <http://www.reyagroup.com>
# Copyright 2011 Alex Levenson <alex@isnotinvain.com>
# Copyright 2011 Diederik van Liere <diederik.vanliere@rotman.utoronto.ca>

__all__ = ["triad_graph"]

#: Dictionary mapping triad name to list of directed edges in the
#: digraph representation of that triad (with nodes 'a', 'b', and 'c').
TRIAD_EDGES: dict = ...

def triad_graph(triad_name: str) -> DiGraph: ...
