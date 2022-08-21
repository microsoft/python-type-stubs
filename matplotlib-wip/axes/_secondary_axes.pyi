import numpy as np
from typing import Callable, Literal
from matplotlib._typing import *
from matplotlib.axes._base import _AxesBase
from matplotlib.transforms import Transform

class SecondaryAxis(_AxesBase):
    def __init__(self, parent, orientation, location, functions, **kwargs) -> None:
        """
        See `.secondary_xaxis` and `.secondary_yaxis` for the doc string.
        """
        ...
    def set_alignment(
        self, align: Literal["top", "bottom", "left", "right"]
    ) -> None: ...
    def set_location(
        self, location: Literal["top", "bottom", "left", "right"] | float
    ) -> None: ...
    def apply_aspect(self, position=...): ...
    def set_ticks(
        self,
        ticks: list[float],
        labels: list[str] = ...,
        *,
        minor: bool = ...,
        **kwargs
    ): ...
    def set_functions(
        self, functions: tuple[Callable, Callable] | Transform
    ) -> None: ...
    def draw(self, *args, **kwargs) -> None: ...
    def set_aspect(self, *args, **kwargs) -> None: ...
    def set_color(self, color: Color) -> None: ...
