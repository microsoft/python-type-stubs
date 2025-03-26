from collections.abc import Sequence
from typing import Literal

from ._typing import *
from .collections import PolyCollection

__all__ = ["stackplot"]

def stackplot(
    axes,
    x: ArrayLike,
    *args,
    labels: Sequence[str] = ...,
    colors: Sequence[Color] = ...,
    baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = ...,
    **kwargs,
) -> list[PolyCollection]: ...
