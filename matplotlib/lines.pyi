from typing import Any, List, Literal, Optional, Tuple, Union

from matplotlib._typing import ArrayLike
from matplotlib.artist import Artist
from matplotlib.colors import _ColorLike
from matplotlib.markers import MarkerStyle

_LineStyle = Union[
    Literal['-', 'solid', '--', 'dashed', '-.', 'dashdot', ':', 'dotted', 'None', '  ', ''],
    Tuple[int, Tuple[int, ...]]
]

class Line2D(Artist):
    def __init__(
        self,
        xdata: ArrayLike,
        ydata: ArrayLike,
        linewidth: Optional[float] = ...,
        linestyle: Optional[_LineStyle] = ...,
        color: Optional[_ColorLike] = ...,
        marker: Optional[MarkerStyle] = ...,
        markersize: Optional[float] = ...,
        markeredgewidth: Optional[float] = ...,
        markeredgecolor: Optional[_ColorLike] = ...,
        markerfacecolor: Optional[_ColorLike] = ...,
        markerfacecoloralt: Optional[_ColorLike] = ...,
        fillstyle: Optional[Literal['full', 'left', 'right', 'bottom', 'top', 'none']] = ...,
        antialiased: Optional[bool] = ...,
        dash_capstyle: Optional[Literal['butt', 'round', 'projecting']] = ...,
        solid_capstyle: Optional[Literal['butt', 'round', 'projecting']] = ...,
        dash_joinstyle: Optional[Literal['miter', 'round', 'bevel']] = ...,
        solid_joinstyle: Optional[Literal['miter', 'round', 'bevel']] = ...,
        pickradius: float = ...,
        drawstyle: Optional[Literal['default', 'steps', 'steps-pre', 'steps-mid', 'steps-post']] = ...,
        markevery: Optional[Union[int, Tuple[int, int], slice, List[int], float, Tuple[float, float], List[bool]]] = ...,
        **kwargs: Any,
    ) -> None: ...

    def __getattr__(self, name: str) -> Any: ...  # incomplete


def __getattr__(name: str) -> Any: ...  # incomplete
