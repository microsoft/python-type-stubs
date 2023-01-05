from typing import Literal, Mapping
from numpy.typing import NDArray, ArrayLike

# Authors: Andreas Mueller
#          Manoj Kumar
# License: BSD 3 clause

import numpy as np

from scipy import sparse

def compute_class_weight(class_weight: Mapping | Literal["balanced"] | None, *, classes: NDArray, y: ArrayLike) -> NDArray: ...
def compute_sample_weight(
    class_weight: dict | Sequence[dicts] | Literal["balanced"] | None, y: NDArray | ArrayLike, *, indices: ArrayLike | None = None
) -> NDArray: ...
