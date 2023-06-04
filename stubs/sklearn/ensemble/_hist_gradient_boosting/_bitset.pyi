
import numpy as np
from .common import X_BINNED_DTYPE_C


def set_bitset_memoryview(bitset: np.ndarray, val: X_BINNED_DTYPE_C) -> None: ...

def set_raw_bitset_from_binned_bitset(raw_bitset: np.ndarray,
                                      binned_bitset: np.ndarray,
                                      categories: np.ndarray) -> None: ...
