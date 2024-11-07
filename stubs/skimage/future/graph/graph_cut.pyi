import networkx as nx
import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.sparse import linalg

from . import _ncut
from .rag import RAG

def cut_threshold(labels: NDArray, rag: RAG, thresh: float, in_place: bool = True) -> NDArray: ...
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
def get_min_ncut(ev: ArrayLike, d: NDArray, w: NDArray, num_cuts: int) -> tuple[ArrayLike, float]: ...
def _label_all(rag, attr_name): ...
def _ncut_relabel(rag, thresh, num_cuts, random_state): ...
