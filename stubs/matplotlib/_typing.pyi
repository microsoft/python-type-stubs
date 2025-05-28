import io
import typing_extensions
from decimal import Decimal as Decimal

import pandas as pd
from numpy.typing import ArrayLike as ArrayLike

PythonScalar: typing_extensions.TypeAlias = str | int | float | bool

FileLike = io.IOBase
PathLike = str

PandasScalar: typing_extensions.TypeAlias = pd.Period | pd.Timestamp | pd.Timedelta | pd.Interval
Scalar: typing_extensions.TypeAlias = PythonScalar | PandasScalar

Color: typing_extensions.TypeAlias = tuple[float, float, float] | str

__all__ = [
    "ArrayLike",
    "Color",
    "Decimal",
    "FileLike",
    "PathLike",
    "Scalar",
]
