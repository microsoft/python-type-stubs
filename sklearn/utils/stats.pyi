import numpy as np

from .extmath import stable_cumsum
from numpy import float64, ndarray

def _weighted_percentile(array: ndarray, sample_weight: ndarray, percentile: float = 50) -> float64: ...
