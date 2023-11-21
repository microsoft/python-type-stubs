from enum import IntEnum

import numpy as np

class FiniteStatus(IntEnum): ...

def cy_isfinite(a: np.ndarray, allow_nan: bool = False) -> bool: ...
