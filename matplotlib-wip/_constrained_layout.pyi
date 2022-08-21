from .figure import Figure
from .axes import Axes
from .transforms import Bbox

def do_constrained_layout(
    fig: Figure,
    h_pad: float,
    w_pad: float,
    hspace: float = ...,
    wspace: float = ...,
    rect: tuple = ...,
    compress: bool = ...,
): ...
def make_layoutgrids(fig, layoutgrids, rect=...): ...
def make_layoutgrids_gs(layoutgrids, gs): ...
def check_no_collapsed_axes(layoutgrids, fig): ...
def compress_fixed_aspect(layoutgrids, fig): ...
def get_margin_from_padding(obj, *, w_pad=..., h_pad=..., hspace=..., wspace=...): ...
def make_layout_margins(
    layoutgrids, fig, renderer, *, w_pad=..., h_pad=..., hspace=..., wspace=...
): ...
def make_margin_suptitles(layoutgrids, fig, renderer, *, w_pad=..., h_pad=...): ...
def match_submerged_margins(layoutgrids, fig): ...
def get_cb_parent_spans(cbax): ...
def get_pos_and_bbox(ax: Axes, renderer) -> tuple[Bbox, Bbox]: ...
def reposition_axes(
    layoutgrids, fig: Figure, renderer, *, w_pad=..., h_pad=..., hspace=..., wspace=...
): ...
def reposition_colorbar(layoutgrids, cbax: Axes, renderer, *, offset=...): ...
def reset_margins(layoutgrids, fig: Figure): ...
def colorbar_get_pad(layoutgrids, cax): ...
