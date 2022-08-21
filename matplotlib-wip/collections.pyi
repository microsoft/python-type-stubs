import numpy as np
from typing import Callable, Literal
from matplotlib._typing import *
from matplotlib.transforms import Transform
from matplotlib.cm import ScalarMappable
from matplotlib.backend_bases import MouseEvent
from matplotlib._enums import CapStyle, JoinStyle
from matplotlib.artist import Artist, allow_rasterization

class Collection(Artist, ScalarMappable):
    r"""
    Base class for Collections. Must be subclassed to be usable.

    A Collection represents a sequence of `.Patch`\es that can be drawn
    more efficiently together than individually. For example, when a single
    path is being drawn repeatedly at different offsets, the renderer can
    typically execute a ``draw_marker()`` call much more efficiently than a
    series of repeated calls to ``draw_path()`` with the offsets put in
    one-by-one.

    Most properties of a collection can be configured per-element. Therefore,
    Collections have "plural" versions of many of the properties of a `.Patch`
    (e.g. `.Collection.get_paths` instead of `.Patch.get_path`). Exceptions are
    the *zorder*, *hatch*, *pickradius*, *capstyle* and *joinstyle* properties,
    which can only be set globally for the whole collection.

    Besides these exceptions, all properties can be specified as single values
    (applying to all elements) or sequences of values. The property of the
    ``i``\th element of the collection is::

      prop[i % len(prop)]

    Each Collection can optionally be used as its own `.ScalarMappable` by
    passing the *norm* and *cmap* parameters to its constructor. If the
    Collection's `.ScalarMappable` matrix ``_A`` has been set (via a call
    to `.Collection.set_array`), then at draw time this internal scalar
    mappable will be used to set the ``facecolors`` and ``edgecolors``,
    ignoring those that were manually passed in.
    """
    _transforms = np.empty((0, 3, 3))

    def __init__(
        self,
        edgecolors=...,
        facecolors=...,
        linewidths=...,
        linestyles=...,
        capstyle=...,
        joinstyle=...,
        antialiaseds=...,
        offsets=...,
        offset_transform=...,
        norm=...,
        cmap=...,
        pickradius=...,
        hatch=...,
        urls=...,
        *,
        zorder=...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        edgecolors : color or list of colors, default: :rc:`patch.edgecolor`
            Edge color for each patch making up the collection. The special
            value 'face' can be passed to make the edgecolor match the
            facecolor.
        facecolors : color or list of colors, default: :rc:`patch.facecolor`
            Face color for each patch making up the collection.
        linewidths : float or list of floats, default: :rc:`patch.linewidth`
            Line width for each patch making up the collection.
        linestyles : str or tuple or list thereof, default: 'solid'
            Valid strings are ['solid', 'dashed', 'dashdot', 'dotted', '-',
            '--', '-.', ':']. Dash tuples should be of the form::

                (offset, onoffseq),

            where *onoffseq* is an even length tuple of on and off ink lengths
            in points. For examples, see
            :doc:`/gallery/lines_bars_and_markers/linestyles`.
        capstyle : `.CapStyle`-like, default: :rc:`patch.capstyle`
            Style to use for capping lines for all paths in the collection.
            Allowed values are %(CapStyle)s.
        joinstyle : `.JoinStyle`-like, default: :rc:`patch.joinstyle`
            Style to use for joining lines for all paths in the collection.
            Allowed values are %(JoinStyle)s.
        antialiaseds : bool or list of bool, default: :rc:`patch.antialiased`
            Whether each patch in the collection should be drawn with
            antialiasing.
        offsets : (float, float) or list thereof, default: (0, 0)
            A vector by which to translate each patch after rendering (default
            is no translation). The translation is performed in screen (pixel)
            coordinates (i.e. after the Artist's transform is applied).
        offset_transform : `~.Transform`, default: `.IdentityTransform`
            A single transform which will be applied to each *offsets* vector
            before it is used.
        norm : `~.colors.Normalize`, optional
            Forwarded to `.ScalarMappable`. The default of
            ``None`` means that the first draw call will set ``vmin`` and
            ``vmax`` using the minimum and maximum values of the data.
        cmap : `~.colors.Colormap`, optional
            Forwarded to `.ScalarMappable`. The default of
            ``None`` will result in :rc:`image.cmap` being used.
        hatch : str, optional
            Hatching pattern to use in filled paths, if any. Valid strings are
            ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']. See
            :doc:`/gallery/shapes_and_collections/hatch_style_reference` for
            the meaning of each hatch type.
        pickradius : float, default: 5.0
            If ``pickradius <= 0``, then `.Collection.contains` will return
            ``True`` whenever the test point is inside of one of the polygons
            formed by the control points of a Path in the Collection. On the
            other hand, if it is greater than 0, then we instead check if the
            test point is contained in a stroke of width ``2*pickradius``
            following any of the Paths in the Collection.
        urls : list of str, default: None
            A URL for each patch to link to once drawn. Currently only works
            for the SVG backend. See :doc:`/gallery/misc/hyperlinks_sgskip` for
            examples.
        zorder : float, default: 1
            The drawing order, shared by all Patches in the Collection. See
            :doc:`/gallery/misc/zorder_demo` for all defaults and examples.
        """
        ...
    def get_paths(self): ...
    def set_paths(self): ...
    def get_transforms(self): ...
    def get_offset_transform(self):
        """Return the `.Transform` instance used by this artist offset."""
        ...
    def set_offset_transform(self, offset_transform: Transform):
        """
        Set the artist offset transform.

        Parameters
        ----------
        offset_transform : `.Transform`
        """
        ...
    def get_datalim(self, transData): ...
    def get_window_extent(self, renderer=...): ...
    @allow_rasterization
    def draw(self, renderer): ...
    def set_pickradius(self, pr: float):
        """
        Set the pick radius used for containment tests.

        Parameters
        ----------
        pr : float
            Pick radius, in points.
        """
        ...
    def get_pickradius(self): ...
    def contains(self, mouseevent):
        """
        Test whether the mouse event occurred in the collection.

        Returns ``bool, dict(ind=itemlist)``, where every item in itemlist
        contains the event.
        """
        ...
    def set_urls(self, urls: list[str] | None):
        """
        Parameters
        ----------
        urls : list of str or None

        Notes
        -----
        URLs are currently only implemented by the SVG backend. They are
        ignored by all other backends.
        """
        ...
    def get_urls(self):
        """
        Return a list of URLs, one for each element of the collection.

        The list contains *None* for elements without a URL. See
        :doc:`/gallery/misc/hyperlinks_sgskip` for an example.
        """
        ...
    def set_hatch(
        self, hatch: Literal["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]
    ):
        r"""
        Set the hatching pattern

        *hatch* can be one of::

          /   - diagonal hatching
          \   - back diagonal
          |   - vertical
          -   - horizontal
          +   - crossed
          x   - crossed diagonal
          o   - small circle
          O   - large circle
          .   - dots
          *   - stars

        Letters can be combined, in which case all the specified
        hatchings are done.  If same letter repeats, it increases the
        density of hatching of that pattern.

        Hatching is supported in the PostScript, PDF, SVG and Agg
        backends only.

        Unlike other properties such as linewidth and colors, hatching
        can only be specified for the collection as a whole, not separately
        for each member.

        Parameters
        ----------
        hatch : {'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
        """
        ...
    def get_hatch(self):
        """Return the current hatching pattern."""
        ...
    def set_offsets(self, offsets: ArrayLike):
        """
        Set the offsets for the collection.

        Parameters
        ----------
        offsets : (N, 2) or (2,) array-like
        """
        ...
    def get_offsets(self) -> ArrayLike:
        """Return the offsets for the collection."""
        ...
    def set_linewidth(self, lw: float | list[float]):
        """
        Set the linewidth(s) for the collection.  *lw* can be a scalar
        or a sequence; if it is a sequence the patches will cycle
        through the sequence

        Parameters
        ----------
        lw : float or list of floats
        """
        ...
    def set_linestyle(self, ls: str | tuple):
        """
        Set the linestyle(s) for the collection.

        ===========================   =================
        linestyle                     description
        ===========================   =================
        ``'-'`` or ``'solid'``        solid line
        ``'--'`` or  ``'dashed'``     dashed line
        ``'-.'`` or  ``'dashdot'``    dash-dotted line
        ``':'`` or ``'dotted'``       dotted line
        ===========================   =================

        Alternatively a dash tuple of the following form can be provided::

            (offset, onoffseq),

        where ``onoffseq`` is an even length tuple of on and off ink in points.

        Parameters
        ----------
        ls : str or tuple or list thereof
            Valid values for individual linestyles include {'-', '--', '-.',
            ':', '', (offset, on-off-seq)}. See `.Line2D.set_linestyle` for a
            complete description.
        """
        ...
    def set_capstyle(self, cs: CapStyle | Literal["butt", "projecting", "round"]):
        """
        Set the `.CapStyle` for the collection (for all its elements).

        Parameters
        ----------
        cs : `.CapStyle` or %(CapStyle)s
        """
        ...
    def get_capstyle(self): ...
    def set_joinstyle(self, js: JoinStyle | Literal["miter", "round", "bevel"]):
        """
        Set the `.JoinStyle` for the collection (for all its elements).

        Parameters
        ----------
        js : `.JoinStyle` or %(JoinStyle)s
        """
        ...
    def get_joinstyle(self): ...
    def set_antialiased(self, aa: bool | list[bool]):
        """
        Set the antialiasing state for rendering.

        Parameters
        ----------
        aa : bool or list of bools
        """
        ...
    def set_color(self, c: Color | list):
        """
        Set both the edgecolor and the facecolor.

        Parameters
        ----------
        c : color or list of rgba tuples

        See Also
        --------
        Collection.set_facecolor, Collection.set_edgecolor
            For setting the edge or face color individually.
        """
        ...
    def set_facecolor(self, c: Color | list[Color]):
        """
        Set the facecolor(s) of the collection. *c* can be a color (all patches
        have same color), or a sequence of colors; if it is a sequence the
        patches will cycle through the sequence.

        If *c* is 'none', the patch will not be filled.

        Parameters
        ----------
        c : color or list of colors
        """
        ...
    def set_facecolors(self, c: Color | list[Color]): ...
    def get_facecolor(self) -> Color | list[Color]: ...
    def get_edgecolor(self) -> Color | list[Color]: ...
    def get_facecolors(self) -> Color | list[Color]: ...
    def get_edgecolors(self) -> Color | list[Color]: ...
    def set_edgecolor(self, c: Color | list[Color] | Literal["face"]):
        """
        Set the edgecolor(s) of the collection.

        Parameters
        ----------
        c : color or list of colors or 'face'
            The collection edgecolor(s).  If a sequence, the patches cycle
            through it.  If 'face', match the facecolor.
        """
        ...
    def set_edgecolors(self, c: Color | list[Color] | Literal["face"]): ...
    def set_alpha(self, alpha: ArrayLike | Scalar | None):
        """
        Set the transparency of the collection.

        Parameters
        ----------
        alpha : float or array of float or None
            If not None, *alpha* values must be between 0 and 1, inclusive.
            If an array is provided, its length must match the number of
            elements in the collection.  Masked values and nans are not
            supported.
        """
        ...
    def get_linewidth(self): ...
    def get_linestyle(self): ...
    def update_scalarmappable(self):
        """
        Update colors from the scalar mappable array, if any.

        Assign colors to edges and faces based on the array and/or
        colors that were directly set, as appropriate.
        """
        ...
    def get_fill(self):
        """Return whether face is colored."""
        ...
    def update_from(self, other):
        """Copy properties from other to self."""
        ...

class _CollectionWithSizes(Collection):
    """
    Base class for collections that have an array of sizes.
    """

    def get_sizes(self) -> list:
        """
        Return the sizes ('areas') of the elements in the collection.

        Returns
        -------
        array
            The 'area' of each element.
        """
        ...
    def set_sizes(self, sizes: np.ndarray | None, dpi: float = ...):
        """
        Set the sizes of each member of the collection.

        Parameters
        ----------
        sizes : np.ndarray or None
            The size to set for each element of the collection.  The
            value is the 'area' of the element.
        dpi : float, default: 72
            The dpi of the canvas.
        """
        ...
    @allow_rasterization
    def draw(self, renderer): ...

class PathCollection(_CollectionWithSizes):
    r"""
    A collection of `~.path.Path`\s, as created by e.g. `~.Axes.scatter`.
    """
    def __init__(self, paths, sizes=..., **kwargs) -> None:
        """
        Parameters
        ----------
        paths : list of `.path.Path`
            The paths that will make up the `.Collection`.
        sizes : array-like
            The factor by which to scale each drawn `~.path.Path`. One unit
            squared in the Path's data space is scaled to be ``sizes**2``
            points when rendered.
        **kwargs
            Forwarded to `.Collection`.
        """
        ...
    def set_paths(self, paths): ...
    def get_paths(self): ...
    def legend_elements(
        self,
        prop: Literal["colors", "sizes"] = ...,
        num=...,
        fmt=...,
        func: Callable = ...,
        **kwargs
    ):
        """
        Create legend handles and labels for a PathCollection.

        Each legend handle is a `.Line2D` representing the Path that was drawn,
        and each label is a string what each Path represents.

        This is useful for obtaining a legend for a `~.Axes.scatter` plot;
        e.g.::

            scatter = plt.scatter([1, 2, 3],  [4, 5, 6],  c=[7, 2, 3])
            plt.legend(*scatter.legend_elements())

        creates three legend elements, one for each color with the numerical
        values passed to *c* as the labels.

        Also see the :ref:`automatedlegendcreation` example.

        Parameters
        ----------
        prop : {"colors", "sizes"}, default: "colors"
            If "colors", the legend handles will show the different colors of
            the collection. If "sizes", the legend will show the different
            sizes. To set both, use *kwargs* to directly edit the `.Line2D`
            properties.
        num : int, None, "auto" (default), array-like, or `~.ticker.Locator`
            Target number of elements to create.
            If None, use all unique elements of the mappable array. If an
            integer, target to use *num* elements in the normed range.
            If *"auto"*, try to determine which option better suits the nature
            of the data.
            The number of created elements may slightly deviate from *num* due
            to a `~.ticker.Locator` being used to find useful locations.
            If a list or array, use exactly those elements for the legend.
            Finally, a `~.ticker.Locator` can be provided.
        fmt : str, `~Formatter`, or None (default)
            The format or formatter to use for the labels. If a string must be
            a valid input for a `.StrMethodFormatter`. If None (the default),
            use a `.ScalarFormatter`.
        func : function, default: ``lambda x: x``
            Function to calculate the labels.  Often the size (or color)
            argument to `~.Axes.scatter` will have been pre-processed by the
            user using a function ``s = f(x)`` to make the markers visible;
            e.g. ``size = np.log10(x)``.  Providing the inverse of this
            function here allows that pre-processing to be inverted, so that
            the legend labels have the correct values; e.g. ``func = lambda
            x: 10**x``.
        **kwargs
            Allowed keyword arguments are *color* and *size*. E.g. it may be
            useful to set the color of the markers if *prop="sizes"* is used;
            similarly to set the size of the markers if *prop="colors"* is
            used. Any further parameters are passed onto the `.Line2D`
            instance. This may be useful to e.g. specify a different
            *markeredgecolor* or *alpha* for the legend handles.

        Returns
        -------
        handles : list of `.Line2D`
            Visual representation of each element of the legend.
        labels : list of str
            The string labels for elements of the legend.
        """
        ...

class PolyCollection(_CollectionWithSizes):
    def __init__(self, verts, sizes=..., closed=..., **kwargs) -> None:
        """
        Parameters
        ----------
        verts : list of array-like
            The sequence of polygons [*verts0*, *verts1*, ...] where each
            element *verts_i* defines the vertices of polygon *i* as a 2D
            array-like of shape (M, 2).
        sizes : array-like, default: None
            Squared scaling factors for the polygons. The coordinates of each
            polygon *verts_i* are multiplied by the square-root of the
            corresponding entry in *sizes* (i.e., *sizes* specify the scaling
            of areas). The scaling is applied before the Artist master
            transform.
        closed : bool, default: True
            Whether the polygon should be closed by adding a CLOSEPOLY
            connection at the end.
        **kwargs
            Forwarded to `.Collection`.
        """
        ...
    def set_verts(self, verts: list[ArrayLike], closed: bool = ...):
        """
        Set the vertices of the polygons.

        Parameters
        ----------
        verts : list of array-like
            The sequence of polygons [*verts0*, *verts1*, ...] where each
            element *verts_i* defines the vertices of polygon *i* as a 2D
            array-like of shape (M, 2).
        closed : bool, default: True
            Whether the polygon should be closed by adding a CLOSEPOLY
            connection at the end.
        """
        ...
    set_paths = ...
    def set_verts_and_codes(self, verts, codes):
        """Initialize vertices with path codes."""
        ...

class BrokenBarHCollection(PolyCollection):
    """
    A collection of horizontal bars spanning *yrange* with a sequence of
    *xranges*.
    """

    def __init__(self, xranges, yrange, **kwargs) -> None:
        """
        Parameters
        ----------
        xranges : list of (float, float)
            The sequence of (left-edge-position, width) pairs for each bar.
        yrange : (float, float)
            The (lower-edge, height) common to all bars.
        **kwargs
            Forwarded to `.Collection`.
        """
        ...
    @classmethod
    def span_where(cls, x, ymin, ymax, where, **kwargs):
        """
        Return a `.BrokenBarHCollection` that plots horizontal bars from
        over the regions in *x* where *where* is True.  The bars range
        on the y-axis from *ymin* to *ymax*

        *kwargs* are passed on to the collection.
        """
        ...

class RegularPolyCollection(_CollectionWithSizes):
    """A collection of n-sided regular polygons."""

    _factor = np.pi ** (-1 / 2)

    def __init__(self, numsides, rotation=..., sizes=..., **kwargs) -> None:
        """
        Parameters
        ----------
        numsides : int
            The number of sides of the polygon.
        rotation : float
            The rotation of the polygon in radians.
        sizes : tuple of float
            The area of the circle circumscribing the polygon in points^2.
        **kwargs
            Forwarded to `.Collection`.

        Examples
        --------
        See :doc:`/gallery/event_handling/lasso_demo` for a complete example::

            offsets = np.random.rand(20, 2)
            facecolors = [cm.jet(x) for x in np.random.rand(20)]

            collection = RegularPolyCollection(
                numsides=5, # a pentagon
                rotation=0, sizes=(50,),
                facecolors=facecolors,
                edgecolors=("black",),
                linewidths=(1,),
                offsets=offsets,
                offset_transform=ax.transData,
                )
        """
        ...
    def get_numsides(self): ...
    def get_rotation(self): ...
    @allow_rasterization
    def draw(self, renderer): ...

class StarPolygonCollection(RegularPolyCollection):
    """Draw a collection of regular stars with *numsides* points."""

class AsteriskPolygonCollection(RegularPolyCollection):
    """Draw a collection of regular asterisks with *numsides* points."""

class LineCollection(Collection):
    r"""
    Represents a sequence of `.Line2D`\s that should be drawn together.

    This class extends `.Collection` to represent a sequence of
    `.Line2D`\s instead of just a sequence of `.Patch`\s.
    Just as in `.Collection`, each property of a *LineCollection* may be either
    a single value or a list of values. This list is then used cyclically for
    each element of the LineCollection, so the property of the ``i``\th element
    of the collection is::

      prop[i % len(prop)]

    The properties of each member of a *LineCollection* default to their values
    in :rc:`lines.*` instead of :rc:`patch.*`, and the property *colors* is
    added in place of *edgecolors*.
    """

    def __init__(self, segments, *, zorder=..., **kwargs) -> None:
        """
        Parameters
        ----------
        segments : list of array-like
            A sequence of (*line0*, *line1*, *line2*), where::

                linen = (x0, y0), (x1, y1), ... (xm, ym)

            or the equivalent numpy array with two columns. Each line
            can have a different number of segments.
        linewidths : float or list of float, default: :rc:`lines.linewidth`
            The width of each line in points.
        colors : color or list of color, default: :rc:`lines.color`
            A sequence of RGBA tuples (e.g., arbitrary color strings, etc, not
            allowed).
        antialiaseds : bool or list of bool, default: :rc:`lines.antialiased`
            Whether to use antialiasing for each line.
        zorder : int, default: 2
            zorder of the lines once drawn.

        facecolors : color or list of color, default: 'none'
            When setting *facecolors*, each line is interpreted as a boundary
            for an area, implicitly closing the path from the last point to the
            first point. The enclosed area is filled with *facecolor*.
            In order to manually specify what should count as the "interior" of
            each line, please use `.PathCollection` instead, where the
            "interior" can be specified by appropriate usage of
            `~.path.Path.CLOSEPOLY`.

        **kwargs
            Forwarded to `.Collection`.
        """
        ...
    def set_segments(self, segments): ...

    set_verts = ...
    set_paths = ...
    def get_segments(self) -> list:
        """
        Returns
        -------
        list
            List of segments in the LineCollection. Each list item contains an
            array of vertices.
        """
        ...
    def set_color(self, c: Color | list[Color]):
        """
        Set the edgecolor(s) of the LineCollection.

        Parameters
        ----------
        c : color or list of colors
            Single color (all lines have same color), or a
            sequence of rgba tuples; if it is a sequence the lines will
            cycle through the sequence.
        """
        ...
    set_colors = ...
    def get_color(self): ...

    get_colors = ...

class EventCollection(LineCollection):
    """
    A collection of locations along a single axis at which an "event" occurred.

    The events are given by a 1-dimensional array. They do not have an
    amplitude and are displayed as parallel lines.
    """

    def __init__(
        self,
        positions,
        orientation=...,
        lineoffset=...,
        linelength=...,
        linewidth=...,
        color=...,
        linestyle=...,
        antialiased=...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        positions : 1D array-like
            Each value is an event.
        orientation : {'horizontal', 'vertical'}, default: 'horizontal'
            The sequence of events is plotted along this direction.
            The marker lines of the single events are along the orthogonal
            direction.
        lineoffset : float, default: 0
            The offset of the center of the markers from the origin, in the
            direction orthogonal to *orientation*.
        linelength : float, default: 1
            The total height of the marker (i.e. the marker stretches from
            ``lineoffset - linelength/2`` to ``lineoffset + linelength/2``).
        linewidth : float or list thereof, default: :rc:`lines.linewidth`
            The line width of the event lines, in points.
        color : color or list of colors, default: :rc:`lines.color`
            The color of the event lines.
        linestyle : str or tuple or list thereof, default: 'solid'
            Valid strings are ['solid', 'dashed', 'dashdot', 'dotted',
            '-', '--', '-.', ':']. Dash tuples should be of the form::

                (offset, onoffseq),

            where *onoffseq* is an even length tuple of on and off ink
            in points.
        antialiased : bool or list thereof, default: :rc:`lines.antialiased`
            Whether to use antialiasing for drawing the lines.
        **kwargs
            Forwarded to `.LineCollection`.

        Examples
        --------
        .. plot:: gallery/lines_bars_and_markers/eventcollection_demo.py
        """
        ...
    def get_positions(self):
        """
        Return an array containing the floating-point values of the positions.
        """
        ...
    def set_positions(self, positions):
        """Set the positions of the events."""
        ...
    def add_positions(self, position):
        """Add one or more events at the specified positions."""
        ...
    extend_positions = ...
    def is_horizontal(self):
        """True if the eventcollection is horizontal, False if vertical."""
        ...
    def get_orientation(self):
        """
        Return the orientation of the event line ('horizontal' or 'vertical').
        """
        ...
    def switch_orientation(self):
        """
        Switch the orientation of the event line, either from vertical to
        horizontal or vice versus.
        """
        ...
    def set_orientation(self, orientation: Literal["horizontal", "vertical"]):
        """
        Set the orientation of the event line.

        Parameters
        ----------
        orientation : {'horizontal', 'vertical'}
        """
        ...
    def get_linelength(self):
        """Return the length of the lines used to mark each event."""
        ...
    def set_linelength(self, linelength):
        """Set the length of the lines used to mark each event."""
        ...
    def get_lineoffset(self):
        """Return the offset of the lines used to mark each event."""
        ...
    def set_lineoffset(self, lineoffset):
        """Set the offset of the lines used to mark each event."""
        ...
    def get_linewidth(self):
        """Get the width of the lines used to mark each event."""
        ...
    def get_linewidths(self): ...
    def get_color(self):
        """Return the color of the lines used to mark each event."""
        ...

class CircleCollection(_CollectionWithSizes):
    """A collection of circles, drawn using splines."""

    _factor = np.pi ** (-1 / 2)
    def __init__(self, sizes, **kwargs) -> None:
        """
        Parameters
        ----------
        sizes : float or array-like
            The area of each circle in points^2.
        **kwargs
            Forwarded to `.Collection`.
        """
        ...

class EllipseCollection(Collection):
    """A collection of ellipses, drawn using splines."""

    def __init__(self, widths, heights, angles, units=..., **kwargs) -> None:
        """
        Parameters
        ----------
        widths : array-like
            The lengths of the first axes (e.g., major axis lengths).
        heights : array-like
            The lengths of second axes.
        angles : array-like
            The angles of the first axes, degrees CCW from the x-axis.
        units : {'points', 'inches', 'dots', 'width', 'height', 'x', 'y', 'xy'}
            The units in which majors and minors are given; 'width' and
            'height' refer to the dimensions of the axes, while 'x' and 'y'
            refer to the *offsets* data units. 'xy' differs from all others in
            that the angle as plotted varies with the aspect ratio, and equals
            the specified angle only when the aspect ratio is unity.  Hence
            it behaves the same as the `~.patches.Ellipse` with
            ``axes.transData`` as its transform.
        **kwargs
            Forwarded to `Collection`.
        """
        ...
    @allow_rasterization
    def draw(self, renderer): ...

class PatchCollection(Collection):
    """
    A generic collection of patches.

    PatchCollection draws faster than a large number of equivalent individual
    Patches. It also makes it easier to assign a colormap to a heterogeneous
    collection of patches.
    """

    def __init__(self, patches, match_original=..., **kwargs) -> None:
        """
        Parameters
        ----------
        patches : list of `.Patch`
            A sequence of Patch objects.  This list may include
            a heterogeneous assortment of different patch types.

        match_original : bool, default: False
            If True, use the colors and linewidths of the original
            patches.  If False, new colors may be assigned by
            providing the standard collection arguments, facecolor,
            edgecolor, linewidths, norm or cmap.

        **kwargs
            All other parameters are forwarded to `.Collection`.

            If any of *edgecolors*, *facecolors*, *linewidths*, *antialiaseds*
            are None, they default to their `.rcParams` patch setting, in
            sequence form.

        Notes
        -----
        The use of `~ScalarMappable` functionality is optional.
        If the `~ScalarMappable` matrix ``_A`` has been set (via
        a call to `~.ScalarMappable.set_array`), at draw time a call to scalar
        mappable will be made to set the face colors.
        """
        ...
    def set_paths(self, patches): ...

class TriMesh(Collection):
    """
    Class for the efficient drawing of a triangular mesh using Gouraud shading.

    A triangular mesh is a `~matplotlib.tri.Triangulation` object.
    """

    def __init__(self, triangulation, **kwargs) -> None: ...
    def get_paths(self): ...
    def set_paths(self): ...
    @staticmethod
    def convert_mesh_to_paths(tri):
        """
        Convert a given mesh into a sequence of `.Path` objects.

        This function is primarily of use to implementers of backends that do
        not directly support meshes.
        """
        ...
    @allow_rasterization
    def draw(self, renderer): ...

class QuadMesh(Collection):
    r"""
    Class for the efficient drawing of a quadrilateral mesh.

    A quadrilateral mesh is a grid of M by N adjacent quadrilaterals that are
    defined via a (M+1, N+1) grid of vertices. The quadrilateral (m, n) is
    defined by the vertices ::

               (m+1, n) ----------- (m+1, n+1)
                  /                   /
                 /                 /
                /               /
            (m, n) -------- (m, n+1)

    The mesh need not be regular and the polygons need not be convex.

    Parameters
    ----------
    coordinates : (M+1, N+1, 2) array-like
        The vertices. ``coordinates[m, n]`` specifies the (x, y) coordinates
        of vertex (m, n).

    antialiased : bool, default: True

    shading : {'flat', 'gouraud'}, default: 'flat'

    Notes
    -----
    Unlike other `.Collection`\s, the default *pickradius* of `.QuadMesh` is 0,
    i.e. `~.Artist.contains` checks whether the test point is within any of the
    mesh quadrilaterals.

    There exists a deprecated API version ``QuadMesh(M, N, coords)``, where
    the dimensions are given explicitly and ``coords`` is a (M*N, 2)
    array-like. This has been deprecated in Matplotlib 3.5. The following
    describes the semantics of this deprecated API.

    A quadrilateral mesh consists of a grid of vertices.
    The dimensions of this array are (*meshWidth* + 1, *meshHeight* + 1).
    Each vertex in the mesh has a different set of "mesh coordinates"
    representing its position in the topology of the mesh.
    For any values (*m*, *n*) such that 0 <= *m* <= *meshWidth*
    and 0 <= *n* <= *meshHeight*, the vertices at mesh coordinates
    (*m*, *n*), (*m*, *n* + 1), (*m* + 1, *n* + 1), and (*m* + 1, *n*)
    form one of the quadrilaterals in the mesh. There are thus
    (*meshWidth* * *meshHeight*) quadrilaterals in the mesh.  The mesh
    need not be regular and the polygons need not be convex.

    A quadrilateral mesh is represented by a (2 x ((*meshWidth* + 1) *
    (*meshHeight* + 1))) numpy array *coordinates*, where each row is
    the *x* and *y* coordinates of one of the vertices.  To define the
    function that maps from a data point to its corresponding color,
    use the :meth:`set_cmap` method.  Each of these arrays is indexed in
    row-major order by the mesh coordinates of the vertex (or the mesh
    coordinates of the lower left vertex, in the case of the colors).

    For example, the first entry in *coordinates* is the coordinates of the
    vertex at mesh coordinates (0, 0), then the one at (0, 1), then at (0, 2)
    .. (0, meshWidth), (1, 0), (1, 1), and so on.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def get_paths(self): ...
    def set_paths(self): ...
    def set_array(self, A):
        """
        Set the data values.

        Parameters
        ----------
        A : (M, N) array-like or M*N array-like
            If the values are provided as a 2D grid, the shape must match the
            coordinates grid. If the values are 1D, they are reshaped to 2D.
            M, N follow from the coordinates grid, where the coordinates grid
            shape is (M, N) for 'gouraud' *shading* and (M+1, N+1) for 'flat'
            shading.
        """
        ...
    def get_datalim(self, transData): ...
    def get_coordinates(self):
        """
        Return the vertices of the mesh as an (M+1, N+1, 2) array.

        M, N are the number of quadrilaterals in the rows / columns of the
        mesh, corresponding to (M+1, N+1) vertices.
        The last dimension specifies the components (x, y).
        """
        ...
    @staticmethod
    def convert_mesh_to_paths(meshWidth, meshHeight, coordinates): ...
    def convert_mesh_to_triangles(self, meshWidth, meshHeight, coordinates): ...
    @allow_rasterization
    def draw(self, renderer): ...
    def get_cursor_data(self, event: MouseEvent): ...
