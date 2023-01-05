from skimage.future.graph.rag import RAG
from numpy.typing import NDArray
import networkx as nx
import numpy as np
from scipy import sparse

def DW_matrices(graph: RAG): ...
def ncut_cost(cut: NDArray, D, W) -> float: ...
