from numpy import ndarray
from scipy.sparse._csr import csr_matrix
from pandas.core.frame import DataFrame
from pandas.core.series import Series


class Bunch(dict):
    def __init__(self, **kwargs) -> None:
        ...

    def __setattr__(self, key: str, value: str | list[str] | ndarray) -> None:
        ...

    def __dir__(self) -> list[str]:
        ...

    def __getattr__(
        self, key: str
    ) -> Series | csr_matrix | int | str | list[str] | list[
        ndarray
    ] | DataFrame | float | ndarray:
        ...

    def __setstate__(self, state):
        ...
