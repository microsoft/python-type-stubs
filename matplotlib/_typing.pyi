from typing import Callable
from numpy import ndarray as ndarray
from numpy.typing import ArrayLike as ArrayLike
from numpy.typing import _ScalarLike

Scalar = _ScalarLike


# For writing stubs without numpy installed.
# from typing import Any
# ndarray = Any
# ArrayLike = Any
# Scalar = Any

_DetrendCallable = Callable[[ArrayLike], ArrayLike]
