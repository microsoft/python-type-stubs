from numpy.typing import ArrayLike
import gzip
import os
import os.path
from itertools import islice

from ..classes.graph import Graph

__all__ = ["graph_atlas", "graph_atlas_g"]

#: The total number of graphs in the atlas.
#:
#: The graphs are labeled starting from 0 and extending to (but not
#: including) this number.
NUM_GRAPHS: int = ...

#: The absolute path representing the directory containing this file.
THIS_DIR = ...

#: The path to the data file containing the graph edge lists.
#:
#: This is the absolute path of the gzipped text file containing the
#: edge list for each graph in the atlas. The file contains one entry
#: per graph in the atlas, in sequential order, starting from graph
#: number 0 and extending through graph number 1252 (see
#: :data:`NUM_GRAPHS`). Each entry looks like
#:
#: .. sourcecode:: text
#:
#:    GRAPH 6
#:    NODES 3
#:    0 1
#:    0 2
#:
#: where the first two lines are the graph's index in the atlas and the
#: number of nodes in the graph, and the remaining lines are the edge
#: list.
#:
#: This file was generated from a Python list of graphs via code like
#: the following::
#:
#:     import gzip
#:     from networkx.generators.atlas import graph_atlas_g
#:     from networkx.readwrite.edgelist import write_edgelist
#:
#:     with gzip.open('atlas.dat.gz', 'wb') as f:
#:         for i, G in enumerate(graph_atlas_g()):
#:             f.write(bytes(f'GRAPH {i}\n', encoding='utf-8'))
#:             f.write(bytes(f'NODES {len(G:Graph)}\n', encoding='utf-8'))
#:             write_edgelist(G:Graph, f, data=False)
#:
ATLAS_FILE = ...

def graph_atlas(i: int) -> ArrayLike: ...
def graph_atlas_g() -> ArrayLike: ...
