from skimage.future.graph.rag import RAG
from numpy.typing import NDArray
from typing import Callable
import numpy as np
import heapq

def _revalidate_node_edges(rag, node, heap_list): ...
def _rename_node(graph, node_id, copy_id): ...
def _invalidate_edge(graph, n1, n2): ...
def merge_hierarchical(
    labels: NDArray,
    rag: RAG,
    thresh: float,
    rag_copy: bool,
    in_place_merge: bool,
    merge_func: Callable,
    weight_func: Callable,
) -> NDArray: ...
