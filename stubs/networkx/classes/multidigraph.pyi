from ..classes.multigraph import MultiGraph
from ..classes.reportviews import (
    OutMultiEdgeView,
    InMultiEdgeView,
    DiMultiDegreeView,
)
from copy import deepcopy
from functools import cached_property

from ..classes.graph import Graph
import networkx.convert as convert
from ..classes.coreviews import MultiAdjacencyView
from ..classes.digraph import DiGraph
from ..classes.multigraph import MultiGraph
from ..classes.reportviews import (
    DiMultiDegreeView,
    InMultiDegreeView,
    InMultiEdgeView,
    OutMultiDegreeView,
    OutMultiEdgeView,
)
from ..exception import NetworkXError

__all__ = ["MultiDiGraph"]

class MultiDiGraph(MultiGraph, DiGraph):

    # node_dict_factory = dict    # already assigned in Graph
    # adjlist_outer_dict_factory = dict
    # adjlist_inner_dict_factory = dict
    edge_key_dict_factory = ...
    # edge_attr_dict_factory = dict

    def __init__(self, incoming_graph_data=None, multigraph_input=None, **attr): ...
    @cached_property
    def adj(self): ...
    @cached_property
    def succ(self): ...
    @cached_property
    def pred(self): ...
    def add_edge(self, u_for_edge, v_for_edge, key=None, **attr): ...
    def remove_edge(self, u, v, key=None): ...
    @cached_property
    def edges(self) -> OutMultiEdgeView: ...

    # alias out_edges to edges
    @cached_property
    def out_edges(self) -> OutMultiEdgeView: ...

    out_edges.__doc__ = ...

    @cached_property
    def in_edges(self) -> InMultiEdgeView: ...
    @cached_property
    def degree(self) -> DiMultiDegreeView | int: ...
    @cached_property
    def in_degree(self): ...
    @cached_property
    def out_degree(self): ...
    def is_multigraph(self): ...
    def is_directed(self): ...
    def to_undirected(self, reciprocal=False, as_view=False) -> MultiGraph: ...
    def reverse(self, copy=True): ...
