from collections.abc import Mapping

from .classes.graph import Graph

__all__ = ["convert_node_labels_to_integers", "relabel_nodes"]

def relabel_nodes(G: Graph, mapping: Mapping, copy=True): ...
def convert_node_labels_to_integers(G: Graph, first_label=0, ordering: str = "default", label_attribute=None): ...
