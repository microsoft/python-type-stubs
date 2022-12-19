from typing import Tuple, Callable, Literal
import numpy as np

from ...utils.validation import check_consistent_length, check_array
from numpy import float64, ndarray

__all__ = ["consensus_score"]

def _check_rows_and_columns(
    a: Tuple[ndarray, ndarray], b: Tuple[ndarray, ndarray]
) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
def _jaccard(a_rows: ndarray, a_cols: ndarray, b_rows: ndarray, b_cols: ndarray) -> float64: ...
def _pairwise_similarity(a: Tuple[ndarray, ndarray], b: Tuple[ndarray, ndarray], similarity: Callable) -> ndarray: ...
def consensus_score(a: tuple, b: tuple, *, similarity: Callable | Literal["jaccard"] = "jaccard") -> float64: ...
