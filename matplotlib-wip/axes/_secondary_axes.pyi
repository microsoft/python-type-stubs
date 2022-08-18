import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.transforms import Transform
from matplotlib.axis import Axis
from matplotlib.axes import Axes

"""
This type stub file was generated by pyright.
"""

from matplotlib import _docstring
from matplotlib.axes._base import _AxesBase
from matplotlib.axis import Axis

class SecondaryAxis(_AxesBase):
    """
    General class to hold a Secondary_X/Yaxis.
    """

    def __init__(self, parent, orientation, location, functions, **kwargs) -> None:
        """
        See `.secondary_xaxis` and `.secondary_yaxis` for the doc string.
        While there is no need for this to be private, it should really be
        called by those higher level functions.
        """
        ...
    def set_alignment(self, align: str):  # -> None:
        """
        Set if axes spine and labels are drawn at top or bottom (or left/right)
        of the axes.

        Parameters
        ----------
        align : str
            either 'top' or 'bottom' for orientation='x' or
            'left' or 'right' for orientation='y' axis.
        """
        ...
    def set_location(
        self, location: Literal["top", "bottom", "left", "right"] | float
    ):  # -> None:
        """
        Set the vertical or horizontal location of the axes in
        parent-normalized coordinates.

        Parameters
        ----------
        location : {'top', 'bottom', 'left', 'right'} or float
            The position to put the secondary axis.  Strings can be 'top' or
            'bottom' for orientation='x' and 'right' or 'left' for
            orientation='y'. A float indicates the relative position on the
            parent axes to put the new axes, 0.0 being the bottom (or left)
            and 1.0 being the top (or right).
        """
        ...
    def apply_aspect(self, position=...): ...
    def set_ticks(
        self,
        ticks: list[float],
        labels: list[str] = ...,
        *,
        minor: bool = ...,
        **kwargs
    ): ...
    def set_functions(self, functions):  # -> None:
        """
        Set how the secondary axis converts limits from the parent axes.

        Parameters
        ----------
        functions : 2-tuple of func, or `Transform` with an inverse.
            Transform between the parent axis values and the secondary axis
            values.

            If supplied as a 2-tuple of functions, the first function is
            the forward transform function and the second is the inverse
            transform.

            If a transform is supplied, then the transform must have an
            inverse.
        """
        ...
    def draw(self, *args, **kwargs):  # -> None:
        """
        Draw the secondary axes.

        Consults the parent axes for its limits and converts them
        using the converter specified by
        `~.axes._secondary_axes.set_functions` (or *functions*
        parameter when axes initialized.)
        """
        ...
    def set_aspect(self, *args, **kwargs):  # -> None:
        """
        Secondary axes cannot set the aspect ratio, so calling this just
        sets a warning.
        """
        ...
    def set_color(self, color: Color):  # -> None:
        """
        Change the color of the secondary axes and all decorators.

        Parameters
        ----------
        color : color
        """
        ...
