from .colors import Colormap, Normalize
from typing import Any, Callable, Literal, Sequence
from ._typing import *
from .transforms import Bbox, BboxBase, Transform
from .text import _AnnotationBase
from .backend_bases import Event, MouseEvent, RendererBase
from .patches import FancyBboxPatch
from .font_manager import FontProperties
from .figure import Figure
from .artist import Artist

DEBUG = ...

def bbox_artist(*args, **kwargs): ...

class OffsetBox(Artist):
    """
    The OffsetBox is a simple container artist.

    The child artists are meant to be drawn at a relative position to its
    parent.

    Being an artist itself, all parameters are passed on to `.Artist`.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, fig: Figure):
        """
        Set the `.Figure` for the `.OffsetBox` and all its children.

        Parameters
        ----------
        fig : `~Figure`
        """
        ...
    def axes(self, ax): ...
    def contains(self, mouseevent: MouseEvent) -> tuple[bool, dict]:
        """
        Delegate the mouse event contains-check to the children.

        As a container, the `.OffsetBox` does not respond itself to
        mouseevents.

        Parameters
        ----------
        mouseevent : `MouseEvent`

        Returns
        -------
        contains : bool
            Whether any values are within the radius.
        details : dict
            An artist-specific dictionary of details of the event context,
            such as which points are contained in the pick radius. See the
            individual Artist subclasses for details.

        See Also
        --------
        .Artist.contains
        """
        ...
    def set_offset(self, xy: Callable):
        """
        Set the offset.

        Parameters
        ----------
        xy : (float, float) or callable
            The (x, y) coordinates of the offset in display units. These can
            either be given explicitly as a tuple (x, y), or by providing a
            function that converts the extent into the offset. This function
            must have the signature::

                def offset(width, height, xdescent, ydescent, renderer) \
-> (float, float)
        """
        ...
    def get_offset(
        self, width, height, xdescent, ydescent, renderer: RendererBase
    ) -> tuple[float, float]:
        """
        Return the offset as a tuple (x, y).

        The extent parameters have to be provided to handle the case where the
        offset is dynamically determined by a callable (see
        `~.OffsetBox.set_offset`).

        Parameters
        ----------
        width, height, xdescent, ydescent
            Extent parameters.
        renderer : `.RendererBase` subclass

        """
        ...
    def set_width(self, width: float):
        """
        Set the width of the box.

        Parameters
        ----------
        width : float
        """
        ...
    def set_height(self, height: float):
        """
        Set the height of the box.

        Parameters
        ----------
        height : float
        """
        ...
    def get_visible_children(self) -> list[Artist]:
        r"""Return a list of the visible child `.Artist`\s."""
        ...
    def get_children(self) -> list[Artist]:
        r"""Return a list of the child `.Artist`\s."""
        ...
    def get_extent_offsets(
        self, renderer: RendererBase
    ) -> tuple[float, float, float, float, list[tuple[float, float]]]:
        """
        Update offset of the children and return the extent of the box.

        Parameters
        ----------
        renderer : `.RendererBase` subclass

        Returns
        -------
        width
        height
        xdescent
        ydescent
        list of (xoffset, yoffset) pairs
        """
        ...
    def get_extent(self, renderer: RendererBase) -> tuple[float, float, float, float]:
        """Return a tuple ``width, height, xdescent, ydescent`` of the box."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def draw(self, renderer: RendererBase):
        """
        Update the location of children if necessary and draw them
        to the given *renderer*.
        """
        ...

class PackerBase(OffsetBox):
    def __init__(
        self,
        pad: float = ...,
        sep: float = ...,
        width: float = ...,
        height: float = ...,
        align: Literal[
            "top", "bottom", "left", "right", "center", "baseline"
        ] = "baseline",
        mode: Literal["fixed", "expand", "equal"] = "fixed",
        children: list[Artist] = ...,
    ) -> None:
        """
        Parameters
        ----------
        pad : float, optional
            The boundary padding in points.

        sep : float, optional
            The spacing between items in points.

        width, height : float, optional
            Width and height of the container box in pixels, calculated if
            *None*.

        align : {'top', 'bottom', 'left', 'right', 'center', 'baseline'}, \
default: 'baseline'
            Alignment of boxes.

        mode : {'fixed', 'expand', 'equal'}, default: 'fixed'
            The packing mode.

            - 'fixed' packs the given `.Artist`\\s tight with *sep* spacing.
            - 'expand' uses the maximal available space to distribute the
              artists with equal spacing in between.
            - 'equal': Each artist an equal fraction of the available space
              and is left-aligned (or top-aligned) therein.

        children : list of `.Artist`
            The artists to pack.

        Notes
        -----
        *pad* and *sep* are in points and will be scaled with the renderer
        dpi, while *width* and *height* are in pixels.
        """
        ...

class VPacker(PackerBase):
    """
    VPacker packs its children vertically, automatically adjusting their
    relative positions at draw time.
    """

    def get_extent_offsets(self, renderer: RendererBase) -> list: ...

class HPacker(PackerBase):
    """
    HPacker packs its children horizontally, automatically adjusting their
    relative positions at draw time.
    """

    def get_extent_offsets(self, renderer: RendererBase) -> list: ...

class PaddedBox(OffsetBox):
    """
    A container to add a padding around an `.Artist`.

    The `.PaddedBox` contains a `.FancyBboxPatch` that is used to visualize
    it when rendering.
    """

    def __init__(
        self,
        child: Artist,
        pad: float = ...,
        draw_frame: bool = ...,
        patch_attrs: dict | None = ...,
    ) -> None:
        """
        Parameters
        ----------
        child : `~Artist`
            The contained `.Artist`.
        pad : float
            The padding in points. This will be scaled with the renderer dpi.
            In contrast *width* and *height* are in *pixels* and thus not
            scaled.
        draw_frame : bool
            Whether to draw the contained `.FancyBboxPatch`.
        patch_attrs : dict or None
            Additional parameters passed to the contained `.FancyBboxPatch`.
        """
        ...
    def get_extent_offsets(self, renderer: RendererBase) -> list: ...
    def draw(self, renderer: RendererBase): ...
    def update_frame(self, bbox: Bbox, fontsize: float = ...): ...
    def draw_frame(self, renderer: RendererBase): ...

class DrawingArea(OffsetBox):
    """
    The DrawingArea can contain any Artist as a child. The DrawingArea
    has a fixed width and height. The position of children relative to
    the parent is fixed. The children can be clipped at the
    boundaries of the parent.
    """

    def __init__(
        self,
        width: float,
        height: float,
        xdescent: float = ...,
        ydescent: float = ...,
        clip: bool = ...,
    ) -> None:
        """
        Parameters
        ----------
        width, height : float
            Width and height of the container box.
        xdescent, ydescent : float
            Descent of the box in x- and y-direction.
        clip : bool
            Whether to clip the children to the box.
        """
        ...
    @property
    def clip_children(self):
        """
        If the children of this DrawingArea should be clipped
        by DrawingArea bounding box.
        """
        ...
    @clip_children.setter
    def clip_children(self, val): ...
    def get_transform(self) -> Transform:
        """
        Return the `~Transform` applied to the children.
        """
        ...
    def set_transform(self, t) -> None:
        """
        set_transform is ignored.
        """
        ...
    def set_offset(self, xy: Sequence[float]) -> None:
        """
        Set the offset of the container.

        Parameters
        ----------
        xy : (float, float)
            The (x, y) coordinates of the offset in display units.
        """
        ...
    def get_offset(self) -> tuple[float, float]:
        """Return offset of the container."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase):
        """Return width, height, xdescent, ydescent of box."""
        ...
    def add_artist(self, a: Artist):
        """Add an `.Artist` to the container box."""
        ...
    def draw(self, renderer: RendererBase): ...

class TextArea(OffsetBox):
    """
    The TextArea is a container artist for a single Text instance.

    The text is placed at (0, 0) with baseline+left alignment, by default. The
    width and height of the TextArea instance is the width and height of its
    child text.
    """

    def __init__(
        self, s: str, textprops: dict = ..., multilinebaseline: bool = False
    ) -> None:
        """
        Parameters
        ----------
        s : str
            The text to be displayed.
        textprops : dict, default: {}
            Dictionary of keyword parameters to be passed to the `.Text`
            instance in the TextArea.
        multilinebaseline : bool, default: False
            Whether the baseline for multiline text is adjusted so that it
            is (approximately) center-aligned with single-line text.
        """
        ...
    def set_text(self, s: str):
        """Set the text of this area as a string."""
        ...
    def get_text(self) -> str:
        """Return the string representation of this area's text."""
        ...
    def set_multilinebaseline(self, t: bool):
        """
        Set multilinebaseline.

        If True, the baseline for multiline text is adjusted so that it is
        (approximately) center-aligned with single-line text.  This is used
        e.g. by the legend implementation so that single-line labels are
        baseline-aligned, but multiline labels are "center"-aligned with them.
        """
        ...
    def get_multilinebaseline(self) -> bool:
        """
        Get multilinebaseline.
        """
        ...
    def set_transform(self, t: Transform) -> None:
        """
        set_transform is ignored.
        """
        ...
    def set_offset(self, xy: Sequence[float]) -> None:
        """
        Set the offset of the container.

        Parameters
        ----------
        xy : (float, float)
            The (x, y) coordinates of the offset in display units.
        """
        ...
    def get_offset(self) -> tuple[float, float]:
        """Return offset of the container."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AuxTransformBox(OffsetBox):
    """
    Offset Box with the aux_transform. Its children will be
    transformed with the aux_transform first then will be
    offsetted. The absolute coordinate of the aux_transform is meaning
    as it will be automatically adjust so that the left-lower corner
    of the bounding box of children will be set to (0, 0) before the
    offset transform.

    It is similar to drawing area, except that the extent of the box
    is not predetermined but calculated from the window extent of its
    children. Furthermore, the extent of the children will be
    calculated in the transformed coordinate.
    """

    def __init__(self, aux_transform) -> None: ...
    def add_artist(self, a: Artist):
        """Add an `.Artist` to the container box."""
        ...
    def get_transform(self) -> Transform:
        """
        Return the :class:`~Transform` applied
        to the children
        """
        ...
    def set_transform(self, t: Transform):
        """
        set_transform is ignored.
        """
        ...
    def set_offset(self, xy: Sequence[float]):
        """
        Set the offset of the container.

        Parameters
        ----------
        xy : (float, float)
            The (x, y) coordinates of the offset in display units.
        """
        ...
    def get_offset(self) -> tuple[float, float]:
        """Return offset of the container."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AnchoredOffsetbox(OffsetBox):
    """
    An offset box placed according to location *loc*.

    AnchoredOffsetbox has a single child.  When multiple children are needed,
    use an extra OffsetBox to enclose them.  By default, the offset box is
    anchored against its parent axes. You may explicitly specify the
    *bbox_to_anchor*.
    """

    zorder = ...
    codes = ...

    def __init__(
        self,
        loc: str,
        pad: float = ...,
        borderpad: float = ...,
        child: OffsetBox = ...,
        prop: FontProperties = ...,
        frameon: bool = ...,
        bbox_to_anchor: BboxBase | Sequence[float] = ...,
        bbox_transform: Transform | None = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        loc : str
            The box location.  Valid locations are
            'upper left', 'upper center', 'upper right',
            'center left', 'center', 'center right',
            'lower left', 'lower center, 'lower right'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        pad : float, default: 0.4
            Padding around the child as fraction of the fontsize.
        borderpad : float, default: 0.5
            Padding between the offsetbox frame and the *bbox_to_anchor*.
        child : `.OffsetBox`
            The box that will be anchored.
        prop : `.FontProperties`
            This is only used as a reference for paddings. If not given,
            :rc:`legend.fontsize` is used.
        frameon : bool
            Whether to draw a frame around the box.
        bbox_to_anchor : `.BboxBase`, 2-tuple, or 4-tuple of floats
            Box that is used to position the legend in conjunction with *loc*.
        bbox_transform : None or :class:`Transform`
            The transform for the bounding box (*bbox_to_anchor*).
        **kwargs
            All other parameters are passed on to `.OffsetBox`.

        Notes
        -----
        See `.Legend` for a detailed description of the anchoring mechanism.
        """
        ...
    def set_child(self, child):
        """Set the child to be anchored."""
        ...
    def get_child(self):
        """Return the child."""
        ...
    def get_children(self) -> list:
        """Return the list of children."""
        ...
    def get_extent(self, renderer: RendererBase):
        """
        Return the extent of the box as (width, height, x, y).

        This is the extent of the child plus the padding.
        """
        ...
    def get_bbox_to_anchor(self) -> Bbox:
        """Return the bbox that the box is anchored to."""
        ...
    def set_bbox_to_anchor(self, bbox: Bbox, transform: Transform = ...):
        """
        Set the bbox that the box is anchored to.

        *bbox* can be a Bbox instance, a list of [left, bottom, width,
        height], or a list of [left, bottom] where the width and
        height will be assumed to be zero. The bbox will be
        transformed to display coordinate by the given transform.
        """
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def update_frame(self, bbox: Bbox, fontsize: float = ...): ...
    def draw(self, renderer: RendererBase): ...

class AnchoredText(AnchoredOffsetbox):
    """
    AnchoredOffsetbox with Text.
    """

    patch: FancyBboxPatch

    def __init__(
        self,
        s: str,
        loc: str,
        pad: float = ...,
        borderpad: float = ...,
        prop: dict = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        s : str
            Text.

        loc : str
            Location code. See `AnchoredOffsetbox`.

        pad : float, default: 0.4
            Padding around the text as fraction of the fontsize.

        borderpad : float, default: 0.5
            Spacing between the offsetbox frame and the *bbox_to_anchor*.

        prop : dict, optional
            Dictionary of keyword parameters to be passed to the
            `~Text` instance contained inside AnchoredText.

        **kwargs
            All other parameters are passed to `AnchoredOffsetbox`.
        """
        ...

class OffsetImage(OffsetBox):
    def __init__(
        self,
        arr,
        zoom: float = ...,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        dpi_cor=...,
        **kwargs
    ) -> None: ...
    def set_data(self, arr: ArrayLike): ...
    def get_data(self): ...
    def set_zoom(self, zoom: float): ...
    def get_zoom(self) -> float: ...
    def get_offset(self):
        """Return offset of the container."""
        ...
    def get_children(self): ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AnnotationBbox(Artist, _AnnotationBase):
    """
    Container for an `OffsetBox` referring to a specific position *xy*.

    Optionally an arrow pointing from the offsetbox to *xy* can be drawn.

    This is like `.Annotation`, but with `OffsetBox` instead of `.Text`.
    """

    zorder = ...
    def __str__(self) -> str: ...
    def __init__(
        self,
        offsetbox,
        xy: Sequence[float],
        xybox: Sequence[float] = ...,
        xycoords: str | Artist | Transform | Callable | Sequence[float] = "data",
        boxcoords: str | Artist | Transform | Callable | Sequence[float] = ...,
        frameon: bool = True,
        pad: float = 0.4,
        annotation_clip=...,
        box_alignment: Sequence[float] = ...,
        bboxprops=...,
        arrowprops=...,
        fontsize: float = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        offsetbox : `OffsetBox`

        xy : (float, float)
            The point *(x, y)* to annotate. The coordinate system is determined
            by *xycoords*.

        xybox : (float, float), default: *xy*
            The position *(x, y)* to place the text at. The coordinate system
            is determined by *boxcoords*.

        xycoords : str or `.Artist` or `.Transform` or callable or \
(float, float), default: 'data'
            The coordinate system that *xy* is given in. See the parameter
            *xycoords* in `.Annotation` for a detailed description.

        boxcoords : str or `.Artist` or `.Transform` or callable or \
(float, float), default: value of *xycoords*
            The coordinate system that *xybox* is given in. See the parameter
            *textcoords* in `.Annotation` for a detailed description.

        frameon : bool, default: True
            By default, the text is surrounded by a white `.FancyBboxPatch`
            (accessible as the ``patch`` attribute of the `.AnnotationBbox`).
            If *frameon* is set to False, this patch is made invisible.

        pad : float, default: 0.4
            Padding around the offsetbox.

        box_alignment : (float, float)
            A tuple of two floats for a vertical and horizontal alignment of
            the offset box w.r.t. the *boxcoords*.
            The lower-left corner is (0, 0) and upper-right corner is (1, 1).

        **kwargs
            Other parameters are identical to `.Annotation`.
        """
        ...
    @property
    def xyann(self): ...
    @xyann.setter
    def xyann(self, xyann): ...
    @property
    def anncoords(self): ...
    @anncoords.setter
    def anncoords(self, coords): ...
    def contains(self, mouseevent: MouseEvent): ...
    def get_children(self) -> list: ...
    def set_figure(self, fig: Figure): ...
    def set_fontsize(self, s: float = ...):
        """
        Set the fontsize in points.

        If *s* is not given, reset to :rc:`legend.fontsize`.
        """
        ...
    def get_fontsize(self) -> float:
        """Return the fontsize in points."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
    def update_positions(self, renderee: RendererBase):
        """
        Update pixel positions for the annotated point, the text and the arrow.
        """
        ...
    def draw(self, renderer: RendererBase): ...

class DraggableBase:
    """
    Helper base class for a draggable artist (legend, offsetbox).

    Derived classes must override the following methods::

        def save_offset(self):
            '''
            Called when the object is picked for dragging; should save the
            reference position of the artist.
            '''

        def update_offset(self, dx, dy):
            '''
            Called during the dragging; (*dx*, *dy*) is the pixel offset from
            the point where the mouse drag started.
            '''

    Optionally, you may override the following method::

        def finalize_offset(self):
            '''Called when the mouse is released.'''

    In the current implementation of `.DraggableLegend` and
    `DraggableAnnotation`, `update_offset` places the artists in display
    coordinates, and `finalize_offset` recalculates their position in axes
    coordinate and set a relevant attribute.
    """

    def __init__(self, ref_artist, use_blit: bool = ...) -> None: ...
    def on_motion(self, evt: Event): ...
    def on_pick(self, evt: Event): ...
    def on_release(self, event: Event): ...
    def disconnect(self):
        """Disconnect the callbacks."""
        ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
    def finalize_offset(self): ...

class DraggableOffsetBox(DraggableBase):
    def __init__(self, ref_artist, offsetbox, use_blit: bool = ...) -> None: ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
    def get_loc_in_canvas(self): ...

class DraggableAnnotation(DraggableBase):
    def __init__(self, annotation, use_blit: bool = ...) -> None: ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
