from typing import Callable, Literal
from ...utils.validation import (
    check_consistent_length as check_consistent_length,
    check_array as check_array,
)
from numpy import ndarray
from ..._typing import Float
from scipy.optimize import linear_sum_assignment as linear_sum_assignment
import numpy as np

__all__ = ["consensus_score"]


def consensus_score(
    a: tuple[ndarray, ndarray] | tuple[int, int],
    b: tuple[ndarray, ndarray] | tuple[int, int],
    *,
    similarity: Literal["jaccard", "jaccard"] | Callable = "jaccard"
) -> Float:
    ...
