from typing import Type
from .._config import get_config as get_config
from .._typing import Float
from numpy import ndarray, int32
import numpy
import scipy.special as special


class _ArrayAPIWrapper:
    def __init__(self, array_namespace) -> None:
        ...

    def __getattr__(self, name):
        ...

    def take(self, X, indices, *, axis):
        ...


class _NumPyApiWrapper:
    def __getattr__(self, name: str):
        ...

    def astype(
        self,
        x: ndarray,
        dtype: Type[int32] | Type[int] | Type[Float],
        *,
        copy: bool = True,
        casting: str = "unsafe"
    ) -> ndarray:
        ...

    def asarray(self, x, *, dtype=None, device=None, copy=None) -> ndarray:
        ...

    def unique_inverse(self, x: ndarray) -> tuple[ndarray, ndarray]:
        ...

    def unique_counts(self, x: ndarray) -> tuple[ndarray, ndarray]:
        ...

    def unique_values(self, x: ndarray) -> ndarray:
        ...

    def concat(self, arrays: list[ndarray], *, axis=None) -> ndarray:
        ...


def get_namespace(*arrays) -> tuple[_NumPyApiWrapper, bool]:
    ...
