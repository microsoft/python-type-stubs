import numpy as np
from numpy.typing import NDArray

from .._shared.filters import gaussian

def binary_blobs(
    length: int = 512,
    blob_size_fraction: float = 0.1,
    n_dim: int = 2,
    volume_fraction: float = 0.5,
    seed=None,
) -> NDArray: ...
