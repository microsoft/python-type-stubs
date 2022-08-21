from .font_manager import FontProperties
from typing import Literal, Sequence
from .transforms import Bbox, BboxBase, Transform
from .text import Text
from .backend_bases import Event, RendererBase
from .patches import Patch, Rectangle
from .lines import Line2D
from .figure import Figure
from .axes import Axes
from .artist import Artist, allow_rasterization
from .offsetbox import DraggableOffsetBox

class DraggableLegend(DraggableOffsetBox):
    def __init__(
        self, legend: Legend, use_blit: bool = ..., update: Literal["loc", "bbox"] = ...
    ) -> None:
        """
        Wrapper around a `.Legend` to support mouse dragging.

        Parameters
        ----------
        legend : `.Legend`
            The `.Legend` instance to wrap.
        use_blit : bool, optional
            Use blitting for faster image composition. For details see
            :ref:`func-animation`.
        update : {'loc', 'bbox'}, optional
            If "loc", update the *loc* parameter of the legend upon finalizing.
            If "bbox", update the *bbox_to_anchor* parameter.
        """
        ...
    def finalize_offset(self): ...

class Legend(Artist):
    """
    Place a legend on the axes at location loc.
    """

    codes = ...
    zorder = ...
    def __str__(self) -> str: ...
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
        ncol=...
    ) -> None:
        """
        Parameters
        ----------
        parent : `~Axes` or `.Figure`
            The artist that contains the legend.

        handles : list of `.Artist`
            A list of Artists (lines, patches) to be added to the legend.

        labels : list of str
            A list of labels to show next to the artists. The length of handles
            and labels should be the same. If they are not, they are truncated
            to the smaller of both lengths.

        Other Parameters
        ----------------
        %(_legend_kw_doc)s

        Notes
        -----
        Users can specify any arbitrary location for the legend using the
        *bbox_to_anchor* keyword argument. *bbox_to_anchor* can be a
        `.BboxBase` (or derived there from) or a tuple of 2 or 4 floats.
        See `set_bbox_to_anchor` for more detail.

        The legend location can be specified by setting *loc* with a tuple of
        2 floats, which is interpreted as the lower-left corner of the legend
        in the normalized axes coordinate.
        """
        ...
    def set_ncols(self, ncols: int) -> None:
        """Set the number of columns."""
        ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    @classmethod
    def get_default_handler_map(cls):
        """Return the global default handler map, shared by all legends."""
        ...
    @classmethod
    def set_default_handler_map(cls, handler_map: dict):
        """Set the global default handler map, shared by all legends."""
        ...
    @classmethod
    def update_default_handler_map(cls, handler_map: dict):
        """Update the global default handler map, shared by all legends."""
        ...
    def get_legend_handler_map(self) -> dict:
        """Return this legend instance's handler map."""
        ...
    @staticmethod
    def get_legend_handler(legend_handler_map: dict, orig_handle):
        """
        Return a legend handler from *legend_handler_map* that
        corresponds to *orig_handler*.

        *legend_handler_map* should be a dictionary object (that is
        returned by the get_legend_handler_map method).

        It first checks if the *orig_handle* itself is a key in the
        *legend_handler_map* and return the associated value.
        Otherwise, it checks for each of the classes in its
        method-resolution-order. If no matching key is found, it
        returns ``None``.
        """
        ...
    def get_children(self): ...
    def get_frame(self) -> Rectangle:
        """Return the `~.patches.Rectangle` used to frame the legend."""
        ...
    def get_lines(self) -> list[Line2D]:
        r"""Return the list of `~.lines.Line2D`\s in the legend."""
        ...
    def get_patches(self) -> list[Patch]:
        r"""Return the list of `~.patches.Patch`\s in the legend."""
        ...
    def get_texts(self) -> list[Text]:
        r"""Return the list of `~.text.Text`\s in the legend."""
        ...
    def set_title(self, title, prop: FontProperties = ...):
        """
        Set the legend title. Fontproperties can be optionally set
        with *prop* parameter.
        """
        ...
    def get_title(self) -> Text:
        """Return the `.Text` instance for the legend title."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
    def get_frame_on(self) -> bool:
        """Get whether the legend box patch is drawn."""
        ...
    def set_frame_on(self, b: bool) -> None:
        """
        Set whether the legend box patch is drawn.

        Parameters
        ----------
        b : bool
        """
        ...
    draw_frame = ...
    def get_bbox_to_anchor(self) -> Bbox:
        """Return the bbox that the legend will be anchored to."""
        ...
    def set_bbox_to_anchor(
        self, bbox: BboxBase | Sequence[float] | None, transform: Transform = ...
    ) -> None:
        """
        Set the bbox that the legend will be anchored to.

        Parameters
        ----------
        bbox : `~BboxBase` or tuple
            The bounding box can be specified in the following ways:

            - A `.BboxBase` instance
            - A tuple of ``(left, bottom, width, height)`` in the given
              transform (normalized axes coordinate if None)
            - A tuple of ``(left, bottom)`` where the width and height will be
              assumed to be zero.
            - *None*, to remove the bbox anchoring, and use the parent bbox.

        transform : `~Transform`, optional
            A transform to apply to the bounding box. If not specified, this
            will use a transform to the bounding box of the parent.
        """
        ...
    def contains(self, event: Event) -> bool: ...
    def set_draggable(
        self, state: bool, use_blit: bool = ..., update: Literal["loc", "bbox"] = ...
    ) -> DraggableLegend:
        """
        Enable or disable mouse dragging support of the legend.

        Parameters
        ----------
        state : bool
            Whether mouse dragging is enabled.
        use_blit : bool, optional
            Use blitting for faster image composition. For details see
            :ref:`func-animation`.
        update : {'loc', 'bbox'}, optional
            The legend parameter to be changed when dragged:

            - 'loc': update the *loc* parameter of the legend
            - 'bbox': update the *bbox_to_anchor* parameter of the legend

        Returns
        -------
        `.DraggableLegend` or *None*
            If *state* is ``True`` this returns the `.DraggableLegend` helper
            instance. Otherwise this returns *None*.
        """
        ...
    def get_draggable(self) -> bool:
        """Return ``True`` if the legend is draggable, ``False`` otherwise."""
        ...
