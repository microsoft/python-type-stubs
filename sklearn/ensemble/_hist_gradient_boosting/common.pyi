
from numpy import float32 as G_H_DTYPE
from numpy import float32 as X_BITSET_INNER_DTYPE
from numpy import float64 as X_DTYPE
from numpy import float64 as Y_DTYPE
from numpy import uint32 as X_BINNED_DTYPE
from numpy import uint8 as X_BINNED_DTYPE_C
import numpy as np


ALMOST_INF: float = 1e300
MonotonicConstraint: int

class PREDICTOR_RECORD_DTYPE:
    value: Y_DTYPE
    count: np.uint32
    feature_idx: np.uint32
    num_threshold: X_DTYPE
    missing_go_to_left: np.uint8
    left: np.uint32
    right: np.uint32
    gain: Y_DTYPE
    depth: np.uint32
    is_leaf: np.uint8
    bin_threshold: X_BINNED_DTYPE
    is_categorical: np.uint8
    bitset_idx: np.uint32

