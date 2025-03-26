from collections.abc import Sequence
from typing import Literal

from ._typing import *
from .artist import Artist, allow_rasterization
from .axes import Axes
from .backend_bases import MouseEvent, RendererBase
from .figure import Figure
from .font_manager import FontProperties
from .patches import Rectangle
from .path import Path
from .text import Text
from .transforms import Bbox, Transform

class Cell(Rectangle):
    PAD = ...

    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        edgecolor: Color = ...,
        facecolor: Color = ...,
        fill: bool = ...,
        text: str = ...,
        loc: Literal["left", "center", "right"] = "right",
        fontproperties: FontProperties = ...,
        *,
        visible_edges: str = "closed",
    ) -> None: ...
    def set_transform(self, trans: Transform): ...
    def set_figure(self, fig: Figure) -> None: ...
    def get_text(self) -> Text: ...
    def set_fontsize(self, size: float) -> None: ...
    def get_fontsize(self) -> float: ...
    def auto_set_font_size(self, renderer: RendererBase) -> float: ...
    @allow_rasterization
    def draw(self, renderer): ...
    def get_text_bounds(self, renderer: RendererBase): ...
    def get_required_width(self, renderer: RendererBase): ...
    def set_text_props(self, **kwargs) -> None: ...
    @property
    def visible_edges(self) -> str: ...
    @visible_edges.setter
    def visible_edges(self, value: str): ...
    def get_path(self) -> Path: ...

CustomCell = Cell

class Table(Artist):
    codes = ...
    FONTSIZE = ...
    AXESPAD = ...
    def __init__(self, ax: Axes, loc: str = ..., bbox: Bbox = ..., **kwargs) -> None: ...
    def add_cell(self, row: int, col: int, *args, **kwargs) -> Cell: ...
    def __setitem__(self, position: Sequence[int], cell: Cell) -> None: ...
    def __getitem__(self, position) -> Cell: ...
    @property
    def edges(self): ...
    @edges.setter
    def edges(self, value): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def contains(self, mouseevent: MouseEvent): ...
    def get_children(self) -> list[Artist]: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def auto_set_column_width(self, col: int) -> None: ...
    def auto_set_font_size(self, value: float = ...): ...
    def scale(self, xscale: float, yscale: float): ...
    def set_fontsize(self, size: float): ...
    def get_celld(self) -> dict[Sequence[int], Cell]: ...

def table(
    ax,
    cellText: ArrayLike = ...,
    cellColours: ArrayLike = ...,
    cellLoc: Literal["left", "center", "right"] = "right",
    colWidths: Sequence[float] = ...,
    rowLabels: Sequence[str] = ...,
    rowColours: Sequence[Color] = ...,
    rowLoc: Literal["left", "center", "right"] = "left",
    colLabels: Sequence[str] = ...,
    colColours: Sequence[Color] = ...,
    colLoc: Literal["left", "center", "right"] = "left",
    loc: str = ...,
    bbox: Bbox = ...,
    edges: str | Literal["open", "closed", "horizontal", "vertical"] = ...,
    **kwargs,
) -> Table: ...
