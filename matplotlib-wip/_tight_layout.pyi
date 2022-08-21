from typing import Sequence
from .gridspec import SubplotSpec
from .backend_bases import RendererBase
from .figure import Figure
from .axes import Axes, SubplotBase

def auto_adjust_subplotpars(
    fig,
    renderer,
    nrows_ncols: tuple[int, int],
    num1num2_list: Sequence[tuple[int, int]],
    subplot_list: Sequence[SubplotBase],
    ax_bbox_list=...,
    pad: float = ...,
    h_pad: float = ...,
    w_pad: float = ...,
    rect: tuple[float, float, float, float] = ...,
) -> dict | None: ...
def get_subplotspec_list(axes_list, grid_spec=...) -> list[SubplotSpec]: ...
def get_tight_layout_figure(
    fig: Figure,
    axes_list: list[Axes],
    subplotspec_list: list,
    renderer: RendererBase,
    pad: float = ...,
    h_pad: float = ...,
    w_pad: float = ...,
    rect: tuple[float, float, float, float] = ...,
) -> SubplotSpec | None: ...
