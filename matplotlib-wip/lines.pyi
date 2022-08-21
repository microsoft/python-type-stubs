from matplotlib.markers import MarkerStyle
import numpy as np
from typing import Any, Callable, Literal, Sequence
from ._typing import *
from .transforms import Bbox, Transform
from .path import Path
from .backend_bases import Event, MouseEvent, RendererBase
from ._enums import CapStyle, JoinStyle
from .artist import Artist, allow_rasterization
from .backends.backend_agg import RendererAgg

def segment_hits(cx, cy, x, y, radius):
    """
    Return the indices of the segments in the polyline with coordinates (*cx*,
    *cy*) that are within a distance *radius* of the point (*x*, *y*).
    """
    ...

class Line2D(Artist):
    """
    A line - the line can have both a solid linestyle connecting all
    the vertices, and a marker at each vertex.  Additionally, the
    drawing of the solid line is influenced by the drawstyle, e.g., one
    can create "stepped" lines in various styles.
    """

    lineStyles = ...

    drawStyles = ...
    drawStyleKeys = ...
    markers = ...
    filled_markers = ...
    fillStyles = ...
    zorder = ...
    def __str__(self) -> str: ...
    def __init__(
        self,
        xdata: Sequence[float],
        ydata: Sequence[float],
        linewidth: float = ...,
        linestyle=...,
        color: Color = ...,
        marker: str = ...,
        markersize: float = ...,
        markeredgewidth: float = ...,
        markeredgecolor: Color = ...,
        markerfacecolor: Color = ...,
        markerfacecoloralt: Color = ...,
        fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
        antialiased: bool = ...,
        dash_capstyle: CapStyle = ...,
        solid_capstyle: CapStyle = ...,
        dash_joinstyle: JoinStyle = ...,
        solid_joinstyle: JoinStyle = ...,
        pickradius: float = ...,
        drawstyle: Literal[
            "default", "steps", "steps-pre", "steps-mid", "steps-post"
        ] = "default",
        markevery=...,
        **kwargs
    ) -> None:
        """
        Create a `.Line2D` instance with *x* and *y* data in sequences of
        *xdata*, *ydata*.

        Additional keyword arguments are `.Line2D` properties:

        %(Line2D:kwdoc)s

        See :meth:`set_linestyle` for a description of the line styles,
        :meth:`set_marker` for a description of the markers, and
        :meth:`set_drawstyle` for a description of the draw styles.

        """
        ...
    def contains(self, mouseevent: MouseEvent):
        """
        Test whether *mouseevent* occurred on the line.

        An event is deemed to have occurred "on" the line if it is less
        than ``self.pickradius`` (default: 5 points) away from it.  Use
        `~.Line2D.get_pickradius` or `~.Line2D.set_pickradius` to get or set
        the pick radius.

        Parameters
        ----------
        mouseevent : `MouseEvent`

        Returns
        -------
        contains : bool
            Whether any values are within the radius.
        details : dict
            A dictionary ``{'ind': pointlist}``, where *pointlist* is a
            list of points of the line that are within the pickradius around
            the event position.

            TODO: sort returned indices by distance
        """
        ...
    def get_pickradius(self) -> float:
        """
        Return the pick radius used for containment tests.

        See `.contains` for more details.
        """
        ...
    def set_pickradius(self, d: float) -> None:
        """
        Set the pick radius used for containment tests.

        See `.contains` for more details.

        Parameters
        ----------
        d : float
            Pick radius, in points.
        """
        ...
    pickradius = ...
    def get_fillstyle(self) -> str:
        """
        Return the marker fill style.

        See also `~.Line2D.set_fillstyle`.
        """
        ...
    def set_fillstyle(
        self, fs: Literal["full", "left", "right", "bottom", "top", "none"]
    ):
        """
        Set the marker fill style.

        Parameters
        ----------
        fs : {'full', 'left', 'right', 'bottom', 'top', 'none'}
            Possible values:

            - 'full': Fill the whole marker with the *markerfacecolor*.
            - 'left', 'right', 'bottom', 'top': Fill the marker half at
              the given side with the *markerfacecolor*. The other
              half of the marker is filled with *markerfacecoloralt*.
            - 'none': No filling.

            For examples see :ref:`marker_fill_styles`.
        """
        ...
    def set_markevery(self, every) -> None:
        """
        Set the markevery property to subsample the plot when using markers.

        e.g., if ``every=5``, every 5-th marker will be plotted.

        Parameters
        ----------
        every : None or int or (int, int) or slice or list[int] or float or \
(float, float) or list[bool]
            Which markers to plot.

            - ``every=None``: every point will be plotted.
            - ``every=N``: every N-th marker will be plotted starting with
              marker 0.
            - ``every=(start, N)``: every N-th marker, starting at index
              *start*, will be plotted.
            - ``every=slice(start, end, N)``: every N-th marker, starting at
              index *start*, up to but not including index *end*, will be
              plotted.
            - ``every=[i, j, m, ...]``: only markers at the given indices
              will be plotted.
            - ``every=[True, False, True, ...]``: only positions that are True
              will be plotted. The list must have the same length as the data
              points.
            - ``every=0.1``, (i.e. a float): markers will be spaced at
              approximately equal visual distances along the line; the distance
              along the line between markers is determined by multiplying the
              display-coordinate distance of the axes bounding-box diagonal
              by the value of *every*.
            - ``every=(0.5, 0.1)`` (i.e. a length-2 tuple of float): similar
              to ``every=0.1`` but the first marker will be offset along the
              line by 0.5 multiplied by the
              display-coordinate-diagonal-distance along the line.

            For examples see
            :doc:`/gallery/lines_bars_and_markers/markevery_demo`.

        Notes
        -----
        Setting *markevery* will still only draw markers at actual data points.
        While the float argument form aims for uniform visual spacing, it has
        to coerce from the ideal spacing to the nearest available data point.
        Depending on the number and distribution of data points, the result
        may still not look evenly spaced.

        When using a start offset to specify the first marker, the offset will
        be from the first data point which may be different from the first
        the visible data point if the plot is zoomed in.

        If zooming in on a plot when using float arguments then the actual
        data points that have markers will change because the distance between
        markers is always determined from the display-coordinates
        axes-bounding-box-diagonal regardless of the actual axes data limits.

        """
        ...
    def get_markevery(self) -> Any:
        """
        Return the markevery setting for marker subsampling.

        See also `~.Line2D.set_markevery`.
        """
        ...
    def set_picker(self, p: Callable | float) -> None:
        """
        Set the event picker details for the line.

        Parameters
        ----------
        p : float or callable[[Artist, Event], tuple[bool, dict]]
            If a float, it is used as the pick radius in points.
        """
        ...
    def get_bbox(self) -> Bbox:
        """Get the bounding box of this line."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def set_data(self, *args) -> None:
        """
        Set the x and y data.

        Parameters
        ----------
        *args : (2, N) array or two 1D arrays
        """
        ...
    def recache_always(self) -> bool: ...
    def recache(self, always: bool = ...) -> None: ...
    def set_transform(self, t: Transform): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def get_antialiased(self) -> bool:
        """Return whether antialiased rendering is used."""
        ...
    def get_color(self) -> str:
        """
        Return the line color.

        See also `~.Line2D.set_color`.
        """
        ...
    def get_drawstyle(self) -> str:
        """
        Return the drawstyle.

        See also `~.Line2D.set_drawstyle`.
        """
        ...
    def get_linestyle(self) -> str:
        """
        Return the linestyle.

        See also `~.Line2D.set_linestyle`.
        """
        ...
    def get_linewidth(self) -> float:
        """
        Return the linewidth in points.

        See also `~.Line2D.set_linewidth`.
        """
        ...
    def get_marker(self) -> int | str:
        """
        Return the line marker.

        See also `~.Line2D.set_marker`.
        """
        ...
    def get_markeredgecolor(self) -> Color:
        """
        Return the marker edge color.

        See also `~.Line2D.set_markeredgecolor`.
        """
        ...
    def get_markeredgewidth(self) -> float:
        """
        Return the marker edge width in points.

        See also `~.Line2D.set_markeredgewidth`.
        """
        ...
    def get_markerfacecolor(self) -> Color:
        """
        Return the marker face color.

        See also `~.Line2D.set_markerfacecolor`.
        """
        ...
    def get_markerfacecoloralt(self) -> Color:
        """
        Return the alternate marker face color.

        See also `~.Line2D.set_markerfacecoloralt`.
        """
        ...
    def get_markersize(self) -> float:
        """
        Return the marker size in points.

        See also `~.Line2D.set_markersize`.
        """
        ...
    def get_data(self, orig: bool = False) -> tuple[Sequence[float], Sequence[float]]:
        """
        Return the line data as an ``(xdata, ydata)`` pair.

        If *orig* is *True*, return the original data.
        """
        ...
    def get_xdata(self, orig: bool = False) -> Sequence[float]:
        """
        Return the xdata.

        If *orig* is *True*, return the original data, else the
        processed data.
        """
        ...
    def get_ydata(self, orig: bool = False) -> Sequence[float]:
        """
        Return the ydata.

        If *orig* is *True*, return the original data, else the
        processed data.
        """
        ...
    def get_path(self) -> Path:
        """Return the `~Path` associated with this line."""
        ...
    def get_xydata(self) -> np.ndarray:
        """
        Return the *xy* data as a Nx2 numpy array.
        """
        ...
    def set_antialiased(self, b: bool) -> None:
        """
        Set whether to use antialiased rendering.

        Parameters
        ----------
        b : bool
        """
        ...
    def set_color(self, color: Color) -> None:
        """
        Set the color of the line.

        Parameters
        ----------
        color : color
        """
        ...
    def set_drawstyle(
        self,
        drawstyle: Literal[
            "default", "steps", "steps-pre", "steps-mid", "steps-post"
        ] = "default",
    ) -> None:
        """
        Set the drawstyle of the plot.

        The drawstyle determines how the points are connected.

        Parameters
        ----------
        drawstyle : {'default', 'steps', 'steps-pre', 'steps-mid', \
'steps-post'}, default: 'default'
            For 'default', the points are connected with straight lines.

            The steps variants connect the points with step-like lines,
            i.e. horizontal lines with vertical steps. They differ in the
            location of the step:

            - 'steps-pre': The step is at the beginning of the line segment,
              i.e. the line will be at the y-value of point to the right.
            - 'steps-mid': The step is halfway between the points.
            - 'steps-post: The step is at the end of the line segment,
              i.e. the line will be at the y-value of the point to the left.
            - 'steps' is equal to 'steps-pre' and is maintained for
              backward-compatibility.

            For examples see :doc:`/gallery/lines_bars_and_markers/step_demo`.
        """
        ...
    def set_linewidth(self, w: float) -> None:
        """
        Set the line width in points.

        Parameters
        ----------
        w : float
            Line width, in points.
        """
        ...
    def set_linestyle(self, ls: Any) -> None:
        """
        Set the linestyle of the line.

        Parameters
        ----------
        ls : {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
            Possible values:

            - A string:

              ==========================================  =================
              linestyle                                   description
              ==========================================  =================
              ``'-'`` or ``'solid'``                      solid line
              ``'--'`` or  ``'dashed'``                   dashed line
              ``'-.'`` or  ``'dashdot'``                  dash-dotted line
              ``':'`` or ``'dotted'``                     dotted line
              ``'none'``, ``'None'``, ``' '``, or ``''``  draw nothing
              ==========================================  =================

            - Alternatively a dash tuple of the following form can be
              provided::

                  (offset, onoffseq)

              where ``onoffseq`` is an even length tuple of on and off ink
              in points. See also :meth:`set_dashes`.

            For examples see :doc:`/gallery/lines_bars_and_markers/linestyles`.
        """
        ...
    def set_marker(self, marker: str | Path | MarkerStyle) -> None:
        """
        Set the line marker.

        Parameters
        ----------
        marker : marker style string, `~.path.Path` or `~.markers.MarkerStyle`
            See `~matplotlib.markers` for full description of possible
            arguments.
        """
        ...
    def set_markeredgecolor(self, ec: Color) -> None:
        """
        Set the marker edge color.

        Parameters
        ----------
        ec : color
        """
        ...
    def set_markerfacecolor(self, fc: Color) -> None:
        """
        Set the marker face color.

        Parameters
        ----------
        fc : color
        """
        ...
    def set_markerfacecoloralt(self, fc: Color) -> None:
        """
        Set the alternate marker face color.

        Parameters
        ----------
        fc : color
        """
        ...
    def set_markeredgewidth(self, ew: float) -> None:
        """
        Set the marker edge width in points.

        Parameters
        ----------
        ew : float
             Marker edge width, in points.
        """
        ...
    def set_markersize(self, sz: float) -> None:
        """
        Set the marker size in points.

        Parameters
        ----------
        sz : float
             Marker size, in points.
        """
        ...
    def set_xdata(self, x: ArrayLike) -> None:
        """
        Set the data array for x.

        Parameters
        ----------
        x : 1D array
        """
        ...
    def set_ydata(self, y: ArrayLike) -> None:
        """
        Set the data array for y.

        Parameters
        ----------
        y : 1D array
        """
        ...
    def set_dashes(self, seq: Sequence[int]) -> None:
        """
        Set the dash sequence.

        The dash sequence is a sequence of floats of even length describing
        the length of dashes and spaces in points.

        For example, (5, 2, 1, 2) describes a sequence of 5 point and 1 point
        dashes separated by 2 point spaces.

        Parameters
        ----------
        seq : sequence of floats (on/off ink in points) or (None, None)
            If *seq* is empty or ``(None, None)``, the linestyle will be set
            to solid.
        """
        ...
    def update_from(self, other: Line2D) -> None:
        """Copy properties from *other* to self."""
        ...
    def set_dash_joinstyle(self, s: JoinStyle) -> None:
        """
        How to join segments of the line if it `~Line2D.is_dashed`.

        The default joinstyle is :rc:`lines.dash_joinstyle`.

        Parameters
        ----------
        s : `.JoinStyle` or %(JoinStyle)s
        """
        ...
    def set_solid_joinstyle(self, s: JoinStyle | str) -> None:
        """
        How to join segments if the line is solid (not `~Line2D.is_dashed`).

        The default joinstyle is :rc:`lines.solid_joinstyle`.

        Parameters
        ----------
        s : `.JoinStyle` or %(JoinStyle)s
        """
        ...
    def get_dash_joinstyle(self) -> JoinStyle | str:
        """
        Return the `.JoinStyle` for dashed lines.

        See also `~.Line2D.set_dash_joinstyle`.
        """
        ...
    def get_solid_joinstyle(self) -> JoinStyle | str:
        """
        Return the `.JoinStyle` for solid lines.

        See also `~.Line2D.set_solid_joinstyle`.
        """
        ...
    def set_dash_capstyle(self, s: CapStyle | str) -> None:
        """
        How to draw the end caps if the line is `~Line2D.is_dashed`.

        The default capstyle is :rc:`lines.dash_capstyle`.

        Parameters
        ----------
        s : `.CapStyle` or %(CapStyle)s
        """
        ...
    def set_solid_capstyle(self, s: CapStyle | str) -> None:
        """
        How to draw the end caps if the line is solid (not `~Line2D.is_dashed`)

        The default capstyle is :rc:`lines.solid_capstyle`.

        Parameters
        ----------
        s : `.CapStyle` or %(CapStyle)s
        """
        ...
    def get_dash_capstyle(self) -> CapStyle | str:
        """
        Return the `.CapStyle` for dashed lines.

        See also `~.Line2D.set_dash_capstyle`.
        """
        ...
    def get_solid_capstyle(self) -> CapStyle | str:
        """
        Return the `.CapStyle` for solid lines.

        See also `~.Line2D.set_solid_capstyle`.
        """
        ...
    def is_dashed(self) -> bool:
        """
        Return whether line has a dashed linestyle.

        A custom linestyle is assumed to be dashed, we do not inspect the
        ``onoffseq`` directly.

        See also `~.Line2D.set_linestyle`.
        """
        ...

class _AxLine(Line2D):
    """
    A helper class that implements `~.Axes.axline`, by recomputing the artist
    transform at draw time.
    """

    def __init__(
        self, xy1: Sequence[float], xy2: Sequence[float], slope: float, **kwargs
    ) -> None: ...
    def get_transform(self): ...
    def draw(self, renderer: RendererAgg) -> None: ...

class VertexSelector:
    """
    Manage the callbacks to maintain a list of selected vertices for `.Line2D`.
    Derived classes should override the `process_selected` method to do
    something with the picks.

    Here is an example which highlights the selected verts with red
    circles::

        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.lines as lines

        class HighlightSelected(lines.VertexSelector):
            def __init__(self, line, fmt='ro', **kwargs):
                lines.VertexSelector.__init__(self, line)
                self.markers, = self.axes.plot([], [], fmt, **kwargs)

            def process_selected(self, ind, xs, ys):
                self.markers.set_data(xs, ys)
                self.canvas.draw()

        fig, ax = plt.subplots()
        x, y = np.random.rand(2, 30)
        line, = ax.plot(x, y, 'bs-', picker=5)

        selector = HighlightSelected(line)
        plt.show()

    """

    def __init__(self, line: Line2D) -> None:
        """
        Initialize the class with a `.Line2D`.  The line should already be
        added to an `~.axes.Axes` and should have the picker property set.
        """
        ...
    def process_selected(self, ind: Sequence[int], xs: ArrayLike, ys: ArrayLike):
        """
        Default "do nothing" implementation of the `process_selected` method.

        Parameters
        ----------
        ind : list of int
            The indices of the selected vertices.
        xs, ys : array-like
            The coordinates of the selected vertices.
        """
        ...
    def onpick(self, event: Event):
        """When the line is picked, update the set of selected indices."""
        ...

lineStyles = ...
lineMarkers = ...
drawStyles = ...
fillStyles = ...
