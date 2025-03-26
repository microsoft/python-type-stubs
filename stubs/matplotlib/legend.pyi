from collections.abc import Sequence
from typing import Literal

from .artist import Artist, allow_rasterization
from .axes import Axes
from .backend_bases import Event, RendererBase
from .figure import Figure
from .font_manager import FontProperties
from .lines import Line2D
from .offsetbox import DraggableOffsetBox
from .patches import Patch, Rectangle
from .text import Text
from .transforms import Bbox, BboxBase, Transform

class DraggableLegend(DraggableOffsetBox):
    def __init__(self, legend: Legend, use_blit: bool = ..., update: Literal["loc", "bbox"] = ...) -> None: ...
    def finalize_offset(self): ...

class Legend(Artist):
    codes = ...
    zorder = ...
    def __init__(
        self,
        parent: Axes | Figure,
        handles: Sequence[Artist],
        labels: Sequence[str],
        loc=...,
        numpoints=...,
        markerscale=...,
        markerfirst=...,
        scatterpoints=...,
        scatteryoffsets=...,
        prop=...,
        fontsize=...,
        labelcolor=...,
        borderpad=...,
        labelspacing=...,
        handlelength=...,
        handleheight=...,
        handletextpad=...,
        borderaxespad=...,
        columnspacing=...,
        ncols=...,
        mode=...,
        fancybox=...,
        shadow=...,
        title=...,
        title_fontsize=...,
        framealpha=...,
        edgecolor=...,
        facecolor=...,
        bbox_to_anchor=...,
        bbox_transform=...,
        frameon=...,
        handler_map=...,
        title_fontproperties=...,
        *,
        ncol=...,
    ) -> None: ...
    def set_ncols(self, ncols: int) -> None: ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    @classmethod
    def get_default_handler_map(cls): ...
    @classmethod
    def set_default_handler_map(cls, handler_map: dict): ...
    @classmethod
    def update_default_handler_map(cls, handler_map: dict): ...
    def get_legend_handler_map(self) -> dict: ...
    @staticmethod
    def get_legend_handler(legend_handler_map: dict, orig_handle): ...
    def get_children(self): ...
    def get_frame(self) -> Rectangle: ...
    def get_lines(self) -> list[Line2D]: ...
    def get_patches(self) -> list[Patch]: ...
    def get_texts(self) -> list[Text]: ...
    def set_title(self, title, prop: FontProperties = ...) -> None: ...
    def get_title(self) -> Text: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
    def get_frame_on(self) -> bool: ...
    def set_frame_on(self, b: bool) -> None: ...
    draw_frame = ...
    def get_bbox_to_anchor(self) -> Bbox: ...
    def set_bbox_to_anchor(self, bbox: BboxBase | Sequence[float] | None, transform: Transform = ...) -> None: ...
    def contains(self, event: Event) -> bool: ...
    def set_draggable(self, state: bool, use_blit: bool = ..., update: Literal["loc", "bbox"] = ...) -> DraggableLegend: ...
    def get_draggable(self) -> bool: ...
