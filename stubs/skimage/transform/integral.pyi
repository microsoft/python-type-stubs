from skimage._typing import Scalar
from numpy import ndarray
from numpy.typing import NDArray
import numpy as np

def integral_image(image: NDArray, *, dtype=None) -> NDArray: ...
def integrate(ii: NDArray, start, end) -> Scalar | np.ndarray: ...
