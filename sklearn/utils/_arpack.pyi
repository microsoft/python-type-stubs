from .validation import check_random_state
from numpy import ndarray
from numpy.random.mtrand import RandomState
from typing import Optional

def _init_arpack_v0(size: int, random_state: Optional[RandomState]) -> ndarray: ...
