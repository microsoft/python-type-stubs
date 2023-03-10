from typing import Callable, Literal
from numpy import ndarray
from ...utils.validation import (
    check_consistent_length as check_consistent_length,
    check_array as check_array,
)
from scipy.optimize import linear_sum_assignment as linear_sum_assignment
from ..._typing import Float
import numpy as np

__all__ = ["consensus_score"]


def consensus_score(
    a: tuple[int, int] | tuple[ndarray, ndarray],
    b: tuple[int, int] | tuple[ndarray, ndarray],
    *,
    similarity: Literal["jaccard", "jaccard"] | Callable = "jaccard"
) -> Float:
    ...
