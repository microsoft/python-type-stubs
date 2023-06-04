from skimage.future.graph.rag import RAG
from numpy.typing import NDArray, ArrayLike
import networkx as nx
import numpy as np
from . import _ncut

from scipy.sparse import linalg

def cut_threshold(
    labels: NDArray, rag: RAG, thresh: float, in_place: bool = True
) -> NDArray: ...
def cut_normalized(
    labels: NDArray,
    rag: RAG,
    thresh: float = 0.001,
    num_cuts: int = 10,
    in_place: bool = True,
    max_edge: float = 1.0,
    *,
    random_state=None,
) -> NDArray: ...
def partition_by_cut(cut: ArrayLike, rag: RAG) -> RAG: ...
def get_min_ncut(
    ev: ArrayLike, d: NDArray, w: NDArray, num_cuts: int
) -> tuple[ArrayLike, float]: ...
def _label_all(rag, attr_name): ...
def _ncut_relabel(rag, thresh, num_cuts, random_state): ...
