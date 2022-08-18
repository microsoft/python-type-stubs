import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.transforms import Transform
from matplotlib.text import Text
from matplotlib.backend_bases import RendererBase
from matplotlib.path import Path
from matplotlib.patches import Patch
from matplotlib.backend_bases import MouseEvent
from matplotlib.font_manager import FontProperties
from matplotlib.figure import Figure
from matplotlib.backend_bases import Event
from matplotlib.transforms import BboxBase
from matplotlib.transforms import Bbox
from matplotlib.artist import Artist

"""
This type stub file was generated by pyright.
"""
from datetime import datetime
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.backends.backend_pgf import RendererPgf
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.offsetbox import DraggableAnnotation
from matplotlib.patches import FancyBboxPatch, Rectangle, Wedge
from pathlib import PosixPath
from typing import Any, Dict, List, Optional, Tuple, Union

from . import _api, _docstring, artist
from .artist import Artist

"""
This type stub file was generated by pyright.
"""

def get_rotation(rotation: float | Literal[None, "horizontal", "vertical"]) -> float:
    """
    Return *rotation* normalized to an angle between 0 and 360 degrees.

    Parameters
    ----------
    rotation : float or {None, 'horizontal', 'vertical'}
        Rotation angle in degrees. *None* and 'horizontal' equal 0,
        'vertical' equals 90.

    Returns
    -------
    float
    """
    ...

class Text(Artist):
    """Handle storing and drawing of text in window or data coordinates."""

    zorder = ...
    def __repr__(self): ...
    def __init__(
        self,
        x: Union[int, float] = ...,
        y: Union[int, float] = ...,
        text: str = ...,
        color: Optional[
            Union[list[Union[int, float]], Tuple[float, float, float], str]
        ] = ...,
        verticalalignment: str = ...,
        horizontalalignment: str = ...,
        multialignment: Optional[str] = ...,
        fontproperties: Optional[FontProperties] = ...,
        rotation: Optional[Union[int, float, str]] = ...,
        linespacing: None = ...,
        rotation_mode: Optional[str] = ...,
        usetex: Optional[bool] = ...,
        wrap: bool = ...,
        transform_rotates_text: bool = ...,
        *,
        parse_math=...,
        **kwargs
    ) -> None:
        """
        Create a `.Text` instance at *x*, *y* with string *text*.

        The text is aligned relative to the anchor point (*x*, *y*) according
        to ``horizontalalignment`` (default: 'left') and ``verticalalignment``
        (default: 'bottom'). See also
        :doc:`/gallery/text_labels_and_annotations/text_alignment`.

        While Text accepts the 'label' keyword argument, by default it is not
        added to the handles of a legend.

        Valid keyword arguments are:

        %(Text:kwdoc)s
        """
        ...
    def update(self, kwargs: Dict[str, Any]) -> None: ...
    def __getstate__(self): ...
    def contains(
        self, mouseevent: MouseEvent
    ) -> Union[Tuple[bool, Dict[str, Dict[Any, Any]]], Tuple[bool, Dict[Any, Any]]]:
        """
        Return whether the mouse event occurred inside the axis-aligned
        bounding-box of the text.
        """
        ...
    def get_rotation(self) -> float:
        """Return the text angle in degrees between 0 and 360."""
        ...
    def get_transform_rotates_text(self) -> bool:
        """
        Return whether rotations of the transform affect the text direction.
        """
        ...
    def set_rotation_mode(self, m: Optional[str]) -> None:
        """
        Set text rotation mode.

        Parameters
        ----------
        m : {None, 'default', 'anchor'}
            If ``None`` or ``"default"``, the text will be first rotated, then
            aligned according to their horizontal and vertical alignments.  If
            ``"anchor"``, then alignment occurs before rotation.
        """
        ...
    def get_rotation_mode(self) -> Optional[str]:
        """Return the text rotation mode."""
        ...
    def update_from(self, other: "Text") -> None: ...
    def set_bbox(self, rectprops: Dict[str, Any]) -> None:
        """
        Draw a bounding box around self.

        Parameters
        ----------
        rectprops : dict with properties for `.patches.FancyBboxPatch`
             The default boxstyle is 'square'. The mutation
             scale of the `.patches.FancyBboxPatch` is set to the fontsize.

        Examples
        --------
        ::

            t.set_bbox(dict(facecolor='red', alpha=0.5))
        """
        ...
    def get_bbox_patch(self) -> Optional[FancyBboxPatch]:
        """
        Return the bbox Patch, or None if the `.patches.FancyBboxPatch`
        is not made.
        """
        ...
    def update_bbox_position_size(
        self, renderer: Union[MixedModeRenderer, RendererAgg]
    ) -> None:
        """
        Update the location and the size of the bbox.

        This method should be used when the position and size of the bbox needs
        to be updated before actually drawing the bbox.
        """
        ...
    def set_clip_box(self, clipbox: None) -> None: ...
    def set_clip_path(
        self, path: Union[Wedge, Rectangle], transform: None = ...
    ) -> None: ...
    def set_clip_on(self, b: bool) -> None: ...
    def get_wrap(self) -> bool:
        """Return whether the text can be wrapped."""
        ...
    def set_wrap(self, wrap: bool) -> None:
        """
        Set whether the text can be wrapped.

        Parameters
        ----------
        wrap : bool

        Notes
        -----
        Wrapping does not work together with
        ``savefig(..., bbox_inches='tight')`` (which is also used internally
        by ``%matplotlib inline`` in IPython/Jupyter). The 'tight' setting
        rescales the canvas to accommodate all content and happens before
        wrapping.
        """
        ...
    @artist.allow_rasterization
    def draw(self, renderer): ...
    def get_color(
        self,
    ) -> Union[
        Tuple[float, float, int],
        Tuple[int, float, float],
        Tuple[float, float, float],
        str,
    ]:
        """Return the color of the text."""
        ...
    def get_fontproperties(self) -> FontProperties:
        """Return the `.font_manager.FontProperties`."""
        ...
    def get_fontfamily(self) -> list[str]:
        """
        Return the list of font families used for font lookup.

        See Also
        --------
        .font_manager.FontProperties.get_family
        """
        ...
    def get_fontname(self) -> str:
        """
        Return the font name as a string.

        See Also
        --------
        .font_manager.FontProperties.get_name
        """
        ...
    def get_fontstyle(self) -> str:
        """
        Return the font style as a string.

        See Also
        --------
        .font_manager.FontProperties.get_style
        """
        ...
    def get_fontsize(self) -> float:
        """
        Return the font size as an integer.

        See Also
        --------
        .font_manager.FontProperties.get_size_in_points
        """
        ...
    def get_fontvariant(self) -> str:
        """
        Return the font variant as a string.

        See Also
        --------
        .font_manager.FontProperties.get_variant
        """
        ...
    def get_fontweight(self) -> str:
        """
        Return the font weight as a string or a number.

        See Also
        --------
        .font_manager.FontProperties.get_weight
        """
        ...
    def get_stretch(self) -> str:
        """
        Return the font stretch as a string or a number.

        See Also
        --------
        .font_manager.FontProperties.get_stretch
        """
        ...
    def get_horizontalalignment(self) -> str:
        """
        Return the horizontal alignment as a string.  Will be one of
        'left', 'center' or 'right'.
        """
        ...
    def get_unitless_position(self) -> Tuple[float, float]:
        """Return the (x, y) unitless position of the text."""
        ...
    def get_position(
        self,
    ) -> Union[
        Tuple[int, float], Tuple[int, int], Tuple[float, float], Tuple[float, int]
    ]:
        """Return the (x, y) position of the text."""
        ...
    def get_prop_tup(self, renderer: None = ...):
        """
        Return a hashable tuple of properties.

        Not intended to be human readable, but useful for backends who
        want to cache derived information about text (e.g., layouts) and
        need to know if the text has changed.
        """
        ...
    def get_text(self) -> str:
        """Return the text string."""
        ...
    def get_verticalalignment(self) -> str:
        """
        Return the vertical alignment as a string.  Will be one of
        'top', 'center', 'bottom', 'baseline' or 'center_baseline'.
        """
        ...
    def get_window_extent(
        self,
        renderer: Optional[Union[RendererPgf, MixedModeRenderer, RendererAgg]] = ...,
        dpi: None = ...,
    ):
        """
        Return the `.Bbox` bounding the text, in display units.

        In addition to being used internally, this is useful for specifying
        clickable regions in a png file on a web page.

        Parameters
        ----------
        renderer : Renderer, optional
            A renderer is needed to compute the bounding box.  If the artist
            has already been drawn, the renderer is cached; thus, it is only
            necessary to pass this argument when calling `get_window_extent`
            before the first draw.  In practice, it is usually easier to
            trigger a draw first, e.g. by calling
            `~.Figure.draw_without_rendering` or ``plt.show()``.

        dpi : float, optional
            The dpi value for computing the bbox, defaults to
            ``self.figure.dpi`` (*not* the renderer dpi); should be set e.g. if
            to match regions with a figure saved with a custom dpi value.
        """
        ...
    def set_backgroundcolor(self, color: str) -> None:
        """
        Set the background color of the text by updating the bbox.

        Parameters
        ----------
        color : color

        See Also
        --------
        .set_bbox : To change the position of the bounding box
        """
        ...
    def set_color(
        self, color: Union[list[Union[int, float]], Tuple[float, float, float], str]
    ) -> None:
        """
        Set the foreground color of the text

        Parameters
        ----------
        color : color
        """
        ...
    def set_horizontalalignment(self, align: str) -> None:
        """
        Set the horizontal alignment relative to the anchor point.

        See also :doc:`/gallery/text_labels_and_annotations/text_alignment`.

        Parameters
        ----------
        align : {'left', 'center', 'right'}
        """
        ...
    def set_multialignment(self, align: str) -> None:
        """
        Set the text alignment for multiline texts.

        The layout of the bounding box of all the lines is determined by the
        horizontalalignment and verticalalignment properties. This property
        controls the alignment of the text lines within that box.

        Parameters
        ----------
        align : {'left', 'right', 'center'}
        """
        ...
    def set_linespacing(self, spacing):
        """
        Set the line spacing as a multiple of the font size.

        The default line spacing is 1.2.

        Parameters
        ----------
        spacing : float (multiple of font size)
        """
        ...
    def set_fontfamily(self, fontname: str) -> None:
        """
        Set the font family.  May be either a single string, or a list of
        strings in decreasing priority.  Each string may be either a real font
        name or a generic font class name.  If the latter, the specific font
        names will be looked up in the corresponding rcParams.

        If a `Text` instance is constructed with ``fontfamily=None``, then the
        font is set to :rc:`font.family`, and the
        same is done when `set_fontfamily()` is called on an existing
        `Text` instance.

        Parameters
        ----------
        fontname : {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', \
'monospace'}

        See Also
        --------
        .font_manager.FontProperties.set_family
        """
        ...
    def set_fontvariant(self, variant: str) -> None:
        """
        Set the font variant.

        Parameters
        ----------
        variant : {'normal', 'small-caps'}

        See Also
        --------
        .font_manager.FontProperties.set_variant
        """
        ...
    def set_fontstyle(self, fontstyle: str) -> None:
        """
        Set the font style.

        Parameters
        ----------
        fontstyle : {'normal', 'italic', 'oblique'}

        See Also
        --------
        .font_manager.FontProperties.set_style
        """
        ...
    def set_fontsize(self, fontsize: Union[int, float, str]) -> None:
        """
        Set the font size.

        Parameters
        ----------
        fontsize : float or {'xx-small', 'x-small', 'small', 'medium', \
'large', 'x-large', 'xx-large'}
            If float, the fontsize in points. The string values denote sizes
            relative to the default font size.

        See Also
        --------
        .font_manager.FontProperties.set_size
        """
        ...
    def get_math_fontfamily(self) -> str:
        """
        Return the font family name for math text rendered by Matplotlib.

        The default value is :rc:`mathtext.fontset`.

        See Also
        --------
        set_math_fontfamily
        """
        ...
    def set_math_fontfamily(self, fontfamily: str) -> None:
        """
        Set the font family for math text rendered by Matplotlib.

        This does only affect Matplotlib's own math renderer. It has no effect
        when rendering with TeX (``usetex=True``).

        Parameters
        ----------
        fontfamily : str
            The name of the font family.

            Available font families are defined in the
            :ref:`matplotlibrc.template file
            <customizing-with-matplotlibrc-files>`.

        See Also
        --------
        get_math_fontfamily
        """
        ...
    def set_fontweight(self, weight: str) -> None:
        """
        Set the font weight.

        Parameters
        ----------
        weight : {a numeric value in range 0-1000, 'ultralight', 'light', \
'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', \
'demi', 'bold', 'heavy', 'extra bold', 'black'}

        See Also
        --------
        .font_manager.FontProperties.set_weight
        """
        ...
    def set_fontstretch(self, stretch):
        """
        Set the font stretch (horizontal condensation or expansion).

        Parameters
        ----------
        stretch : {a numeric value in range 0-1000, 'ultra-condensed', \
'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', \
'expanded', 'extra-expanded', 'ultra-expanded'}

        See Also
        --------
        .font_manager.FontProperties.set_stretch
        """
        ...
    def set_position(self, xy: Union[Tuple[int, float], Tuple[float, float]]) -> None:
        """
        Set the (*x*, *y*) position of the text.

        Parameters
        ----------
        xy : (float, float)
        """
        ...
    def set_x(self, x: Optional[Union[int, float]]) -> None:
        """
        Set the *x* position of the text.

        Parameters
        ----------
        x : float
        """
        ...
    def set_y(self, y: Union[int, float]) -> None:
        """
        Set the *y* position of the text.

        Parameters
        ----------
        y : float
        """
        ...
    def set_rotation(self, s: Optional[Union[int, float, str]]) -> None:
        """
        Set the rotation of the text.

        Parameters
        ----------
        s : float or {'vertical', 'horizontal'}
            The rotation angle in degrees in mathematically positive direction
            (counterclockwise). 'horizontal' equals 0, 'vertical' equals 90.
        """
        ...
    def set_transform_rotates_text(self, t: bool):
        """
        Whether rotations of the transform affect the text direction.

        Parameters
        ----------
        t : bool
        """
        ...
    def set_verticalalignment(self, align: str) -> None:
        """
        Set the vertical alignment relative to the anchor point.

        See also :doc:`/gallery/text_labels_and_annotations/text_alignment`.

        Parameters
        ----------
        align : {'bottom', 'baseline', 'center', 'center_baseline', 'top'}
        """
        ...
    def set_text(self, s: Optional[Union[datetime, str]]) -> None:
        r"""
        Set the text string *s*.

        It may contain newlines (``\n``) or math in LaTeX syntax.

        Parameters
        ----------
        s : object
            Any object gets converted to its `str` representation, except for
            ``None`` which is converted to an empty string.
        """
        ...
    def set_fontproperties(
        self, fp: Optional[Union[PosixPath, FontProperties]]
    ) -> None:
        """
        Set the font properties that control the text.

        Parameters
        ----------
        fp : `.font_manager.FontProperties` or `str` or `pathlib.Path`
            If a `str`, it is interpreted as a fontconfig pattern parsed by
            `.FontProperties`.  If a `pathlib.Path`, it is interpreted as the
            absolute path to a font file.
        """
        ...
    def set_usetex(self, usetex: Optional[bool]) -> None:
        """
        Parameters
        ----------
        usetex : bool or None
            Whether to render using TeX, ``None`` means to use
            :rc:`text.usetex`.
        """
        ...
    def get_usetex(self) -> bool:
        """Return whether this `Text` object uses TeX for rendering."""
        ...
    def set_parse_math(self, parse_math: bool) -> None:
        """
        Override switch to disable any mathtext parsing for this `Text`.

        Parameters
        ----------
        parse_math : bool
            If False, this `Text` will never use mathtext.  If True, mathtext
            will be used if there is an even number of unescaped dollar signs.
        """
        ...
    def get_parse_math(self) -> bool:
        """Return whether mathtext parsing is considered for this `Text`."""
        ...
    def set_fontname(self, fontname: str) -> None:
        """
        Alias for `set_family`.

        One-way alias only: the getter differs.

        Parameters
        ----------
        fontname : {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', \
'monospace'}

        See Also
        --------
        .font_manager.FontProperties.set_family

        """
        ...

class OffsetFrom:
    """Callable helper class for working with `Annotation`."""

    def __init__(
        self, artist: "Annotation", ref_coord: Tuple[float, int], unit: str = ...
    ) -> None:
        """
        Parameters
        ----------
        artist : `.Artist` or `.BboxBase` or `.Transform`
            The object to compute the offset from.

        ref_coord : (float, float)
            If *artist* is an `.Artist` or `.BboxBase`, this values is
            the location to of the offset origin in fractions of the
            *artist* bounding box.

            If *artist* is a transform, the offset origin is the
            transform applied to this value.

        unit : {'points, 'pixels'}, default: 'points'
            The screen units to use (pixels or points) for the offset input.
        """
        ...
    def set_unit(self, unit: str) -> None:
        """
        Set the unit for input to the transform used by ``__call__``.

        Parameters
        ----------
        unit : {'points', 'pixels'}
        """
        ...
    def get_unit(self) -> str:
        """Return the unit for input to the transform used by ``__call__``."""
        ...
    def __call__(self, renderer: RendererBase) -> Transform:
        """
        Return the offset transform.

        Parameters
        ----------
        renderer : `RendererBase`
            The renderer to use to compute the offset

        Returns
        -------
        `Transform`
            Maps (x, y) in pixel or point units to screen units
            relative to the given artist.
        """
        ...

class _AnnotationBase:
    def __init__(
        self,
        xy: Union[
            Tuple[int, int],
            Tuple[float, int],
            list[float],
            Tuple[int, float],
            Tuple[float, float],
        ],
        xycoords: Union[Annotation, Tuple[str, str], str] = ...,
        annotation_clip: None = ...,
    ) -> None: ...
    def set_annotation_clip(self, b: Optional[bool]) -> None:
        """
        Set the annotation's clipping behavior.

        Parameters
        ----------
        b : bool or None
            - True: The annotation will be clipped when ``self.xy`` is
              outside the axes.
            - False: The annotation will always be drawn.
            - None: The annotation will be clipped when ``self.xy`` is
              outside the axes and ``self.xycoords == "data"``.
        """
        ...
    def get_annotation_clip(self) -> Optional[bool]:
        """
        Return the annotation's clipping behavior.

        See `set_annotation_clip` for the meaning of return values.
        """
        ...
    def draggable(self, state: None = ..., use_blit: bool = ...) -> DraggableAnnotation:
        """
        Set whether the annotation is draggable with the mouse.

        Parameters
        ----------
        state : bool or None
            - True or False: set the draggability.
            - None: toggle the draggability.

        Returns
        -------
        DraggableAnnotation or None
            If the annotation is draggable, the corresponding
            `.DraggableAnnotation` helper is returned.
        """
        ...

class Annotation(Text, _AnnotationBase):
    """
    An `.Annotation` is a `.Text` that can refer to a specific position *xy*.
    Optionally an arrow pointing from the text to *xy* can be drawn.

    Attributes
    ----------
    xy
        The annotated position.
    xycoords
        The coordinate system for *xy*.
    arrow_patch
        A `.FancyArrowPatch` to point from *xytext* to *xy*.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        text: str,
        xy: Union[
            Tuple[int, float], Tuple[int, int], Tuple[float, float], Tuple[float, int]
        ],
        xytext: Optional[
            Union[
                Tuple[int, int],
                Tuple[float, int],
                Tuple[int, float],
                Tuple[float, float],
            ]
        ] = ...,
        xycoords: Union[Annotation, Tuple[str, str], str] = ...,
        textcoords: Optional[
            Union[Annotation, Tuple[Annotation, str], OffsetFrom, str]
        ] = ...,
        arrowprops: Any = ...,
        annotation_clip: None = ...,
        **kwargs
    ) -> None:
        """
        Annotate the point *xy* with text *text*.

        In the simplest form, the text is placed at *xy*.

        Optionally, the text can be displayed in another position *xytext*.
        An arrow pointing from the text to the annotated point *xy* can then
        be added by defining *arrowprops*.

        Parameters
        ----------
        text : str
            The text of the annotation.

        xy : (float, float)
            The point *(x, y)* to annotate. The coordinate system is determined
            by *xycoords*.

        xytext : (float, float), default: *xy*
            The position *(x, y)* to place the text at. The coordinate system
            is determined by *textcoords*.

        xycoords : str or `.Artist` or `.Transform` or callable or \
(float, float), default: 'data'

            The coordinate system that *xy* is given in. The following types
            of values are supported:

            - One of the following strings:

              ==================== ============================================
              Value                Description
              ==================== ============================================
              'figure points'      Points from the lower left of the figure
              'figure pixels'      Pixels from the lower left of the figure
              'figure fraction'    Fraction of figure from lower left
              'subfigure points'   Points from the lower left of the subfigure
              'subfigure pixels'   Pixels from the lower left of the subfigure
              'subfigure fraction' Fraction of subfigure from lower left
              'axes points'        Points from lower left corner of axes
              'axes pixels'        Pixels from lower left corner of axes
              'axes fraction'      Fraction of axes from lower left
              'data'               Use the coordinate system of the object
                                   being annotated (default)
              'polar'              *(theta, r)* if not native 'data'
                                   coordinates
              ==================== ============================================

              Note that 'subfigure pixels' and 'figure pixels' are the same
              for the parent figure, so users who want code that is usable in
              a subfigure can use 'subfigure pixels'.

            - An `.Artist`: *xy* is interpreted as a fraction of the artist's
              `~Bbox`. E.g. *(0, 0)* would be the lower
              left corner of the bounding box and *(0.5, 1)* would be the
              center top of the bounding box.

            - A `.Transform` to transform *xy* to screen coordinates.

            - A function with one of the following signatures::

                def transform(renderer) -> Bbox
                def transform(renderer) -> Transform

              where *renderer* is a `.RendererBase` subclass.

              The result of the function is interpreted like the `.Artist` and
              `.Transform` cases above.

            - A tuple *(xcoords, ycoords)* specifying separate coordinate
              systems for *x* and *y*. *xcoords* and *ycoords* must each be
              of one of the above described types.

            See :ref:`plotting-guide-annotation` for more details.

        textcoords : str or `.Artist` or `.Transform` or callable or \
(float, float), default: value of *xycoords*
            The coordinate system that *xytext* is given in.

            All *xycoords* values are valid as well as the following
            strings:

            =================   =========================================
            Value               Description
            =================   =========================================
            'offset points'     Offset (in points) from the *xy* value
            'offset pixels'     Offset (in pixels) from the *xy* value
            =================   =========================================

        arrowprops : dict, optional
            The properties used to draw a `.FancyArrowPatch` arrow between the
            positions *xy* and *xytext*.  Defaults to None, i.e. no arrow is
            drawn.

            For historical reasons there are two different ways to specify
            arrows, "simple" and "fancy":

            **Simple arrow:**

            If *arrowprops* does not contain the key 'arrowstyle' the
            allowed keys are:

            ==========   ======================================================
            Key          Description
            ==========   ======================================================
            width        The width of the arrow in points
            headwidth    The width of the base of the arrow head in points
            headlength   The length of the arrow head in points
            shrink       Fraction of total length to shrink from both ends
            ?            Any key to :class:`matplotlib.patches.FancyArrowPatch`
            ==========   ======================================================

            The arrow is attached to the edge of the text box, the exact
            position (corners or centers) depending on where it's pointing to.

            **Fancy arrow:**

            This is used if 'arrowstyle' is provided in the *arrowprops*.

            Valid keys are the following `~matplotlib.patches.FancyArrowPatch`
            parameters:

            ===============  ==================================================
            Key              Description
            ===============  ==================================================
            arrowstyle       the arrow style
            connectionstyle  the connection style
            relpos           see below; default is (0.5, 0.5)
            patchA           default is bounding box of the text
            patchB           default is None
            shrinkA          default is 2 points
            shrinkB          default is 2 points
            mutation_scale   default is text size (in points)
            mutation_aspect  default is 1.
            ?                any key for :class:`matplotlib.patches.PathPatch`
            ===============  ==================================================

            The exact starting point position of the arrow is defined by
            *relpos*. It's a tuple of relative coordinates of the text box,
            where (0, 0) is the lower left corner and (1, 1) is the upper
            right corner. Values <0 and >1 are supported and specify points
            outside the text box. By default (0.5, 0.5) the starting point is
            centered in the text box.

        annotation_clip : bool or None, default: None
            Whether to clip (i.e. not draw) the annotation when the annotation
            point *xy* is outside the axes area.

            - If *True*, the annotation will be clipped when *xy* is outside
              the axes.
            - If *False*, the annotation will always be drawn.
            - If *None*, the annotation will be clipped when *xy* is outside
              the axes and *xycoords* is 'data'.

        **kwargs
            Additional kwargs are passed to `~Text`.

        Returns
        -------
        `.Annotation`

        See Also
        --------
        :ref:`plotting-guide-annotation`

        """
        ...
    def contains(self, event): ...
    @property
    def xycoords(self): ...
    @xycoords.setter
    def xycoords(self, xycoords): ...
    @property
    def xyann(self):
        """
        The text position.

        See also *xytext* in `.Annotation`.
        """
        ...
    @xyann.setter
    def xyann(self, xytext): ...
    def get_anncoords(
        self,
    ) -> Union[Tuple[Annotation, str], Annotation, OffsetFrom, str]:
        """
        Return the coordinate system to use for `.Annotation.xyann`.

        See also *xycoords* in `.Annotation`.
        """
        ...
    def set_anncoords(self, coords):
        """
        Set the coordinate system to use for `.Annotation.xyann`.

        See also *xycoords* in `.Annotation`.
        """
        ...
    anncoords = ...
    def set_figure(self, fig: Figure) -> None: ...
    def update_positions(self, renderer: Union[MixedModeRenderer, RendererAgg]) -> None:
        """
        Update the pixel positions of the annotation text and the arrow patch.
        """
        ...
    @artist.allow_rasterization
    def draw(self, renderer): ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
