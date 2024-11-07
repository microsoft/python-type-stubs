import networkx as nx
import numpy as np
from numpy.typing import NDArray
from scipy import sparse

from .rag import RAG

def DW_matrices(graph: RAG): ...
def ncut_cost(cut: NDArray, D, W) -> float: ...
