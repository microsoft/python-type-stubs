from .backend_managers import ToolManager
from .texmanager import TexManager
from .widgets import Cursor, LockDraw
from typing import Any, Callable, Literal
from ._typing import *
from .transforms import Affine2DBase, Bbox, Transform, TransformedPath
from .text import Text
from .path import Path
from ._enums import CapStyle, JoinStyle
from .backend_tools import Cursors
from .font_manager import FontProperties
from .figure import Figure
from .axes import Axes
from .artist import Artist

from enum import Enum, IntEnum
from . import backend_tools as tools

def register_backend(format: str, backend, description: str = ...):
    """
    Register a backend for saving to a given file format.

    Parameters
    ----------
    format : str
        File extension
    backend : module string or canvas class
        Backend for handling file output
    description : str, default: ""
        Description of the file type.
    """
    ...

def get_registered_canvas_class(format):
    """
    Return the registered default canvas for given file format.
    Handles deferred import of required backend.
    """
    ...

class RendererBase:
    """
    An abstract base class to handle drawing/rendering operations.

    The following methods must be implemented in the backend for full
    functionality (though just implementing `draw_path` alone would give a
    highly capable backend):

    * `draw_path`
    * `draw_image`
    * `draw_gouraud_triangle`

    The following methods *should* be implemented in the backend for
    optimization reasons:

    * `draw_text`
    * `draw_markers`
    * `draw_path_collection`
    * `draw_quad_mesh`
    """

    def __init__(self) -> None: ...
    def open_group(self, s, gid=...):
        """
        Open a grouping element with label *s* and *gid* (if set) as id.

        Only used by the SVG renderer.
        """
        ...
    def close_group(self, s):
        """
        Close a grouping element with label *s*.

        Only used by the SVG renderer.
        """
        ...
    def draw_path(self, gc, path: Path, transform: Transform, rgbFace=...):
        """Draw a `~.path.Path` instance using the given affine transform."""
        ...
    def draw_markers(
        self,
        gc: GraphicsContextBase,
        marker_path: Path,
        marker_trans: Transform,
        path: Path,
        trans: Transform,
        rgbFace=...,
    ):
        """
        Draw a marker at each of *path*'s vertices (excluding control points).

        The base (fallback) implementation makes multiple calls to `draw_path`.
        Backends may want to override this method in order to draw the marker
        only once and reuse it multiple times.

        Parameters
        ----------
        gc : `.GraphicsContextBase`
            The graphics context.
        marker_trans : `Transform`
            An affine transform applied to the marker.
        trans : `Transform`
            An affine transform applied to the path.
        """
        ...
    def draw_path_collection(
        self,
        gc: GraphicsContextBase,
        master_transform: Transform,
        paths,
        all_transforms,
        offsets,
        offsetTrans,
        facecolors,
        edgecolors,
        linewidths,
        linestyles,
        antialiaseds,
        urls,
        offset_position,
    ):
        """
        Draw a collection of *paths*.

        Each path is first transformed by the corresponding entry
        in *all_transforms* (a list of (3, 3) matrices) and then by
        *master_transform*.  They are then translated by the corresponding
        entry in *offsets*, which has been first transformed by *offsetTrans*.

        *facecolors*, *edgecolors*, *linewidths*, *linestyles*, and
        *antialiased* are lists that set the corresponding properties.

        *offset_position* is unused now, but the argument is kept for
        backwards compatibility.

        The base (fallback) implementation makes multiple calls to `draw_path`.
        Backends may want to override this in order to render each set of
        path data only once, and then reference that path multiple times with
        the different offsets, colors, styles etc.  The generator methods
        `_iter_collection_raw_paths` and `_iter_collection` are provided to
        help with (and standardize) the implementation across backends.  It
        is highly recommended to use those generators, so that changes to the
        behavior of `draw_path_collection` can be made globally.
        """
        ...
    def draw_quad_mesh(
        self,
        gc: GraphicsContextBase,
        master_transform: Transform,
        meshWidth,
        meshHeight,
        coordinates,
        offsets,
        offsetTrans,
        facecolors,
        antialiased,
        edgecolors,
    ):
        """
        Draw a quadmesh.

        The base (fallback) implementation converts the quadmesh to paths and
        then calls `draw_path_collection`.
        """
        ...
    def draw_gouraud_triangle(
        self,
        gc: GraphicsContextBase,
        points: ArrayLike,
        colors: ArrayLike,
        transform: Transform,
    ):
        """
        Draw a Gouraud-shaded triangle.

        Parameters
        ----------
        gc : `.GraphicsContextBase`
            The graphics context.
        points : (3, 2) array-like
            Array of (x, y) points for the triangle.
        colors : (3, 4) array-like
            RGBA colors for each point of the triangle.
        transform : `Transform`
            An affine transform to apply to the points.
        """
        ...
    def draw_gouraud_triangles(
        self,
        gc: GraphicsContextBase,
        triangles_array: ArrayLike,
        colors_array: ArrayLike,
        transform: Transform,
    ):
        """
        Draw a series of Gouraud triangles.

        Parameters
        ----------
        points : (N, 3, 2) array-like
            Array of *N* (x, y) points for the triangles.
        colors : (N, 3, 4) array-like
            Array of *N* RGBA colors for each point of the triangles.
        transform : `Transform`
            An affine transform to apply to the points.
        """
        ...
    def get_image_magnification(self):
        """
        Get the factor by which to magnify images passed to `draw_image`.
        Allows a backend to have images at a different resolution to other
        artists.
        """
        ...
    def draw_image(
        self,
        gc: GraphicsContextBase,
        x: Scalar,
        y: Scalar,
        im: ArrayLike,
        transform: Affine2DBase = ...,
    ):
        """
        Draw an RGBA image.

        Parameters
        ----------
        gc : `.GraphicsContextBase`
            A graphics context with clipping information.

        x : scalar
            The distance in physical units (i.e., dots or pixels) from the left
            hand side of the canvas.

        y : scalar
            The distance in physical units (i.e., dots or pixels) from the
            bottom side of the canvas.

        im : (N, M, 4) array-like of np.uint8
            An array of RGBA pixels.

        transform : `Affine2DBase`
            If and only if the concrete backend is written such that
            `option_scale_image` returns ``True``, an affine transformation
            (i.e., an `.Affine2DBase`) *may* be passed to `draw_image`.  The
            translation vector of the transformation is given in physical units
            (i.e., dots or pixels). Note that the transformation does not
            override *x* and *y*, and has to be applied *before* translating
            the result by *x* and *y* (this can be accomplished by adding *x*
            and *y* to the translation vector defined by *transform*).
        """
        ...
    def option_image_nocomposite(self) -> bool:
        """
        Return whether image composition by Matplotlib should be skipped.

        Raster backends should usually return False (letting the C-level
        rasterizer take care of image composition); vector backends should
        usually return ``not rcParams["image.composite_image"]``.
        """
        ...
    def option_scale_image(self) -> bool:
        """
        Return whether arbitrary affine transformations in `draw_image` are
        supported (True for most vector backends).
        """
        ...
    def draw_tex(self, gc: GraphicsContextBase, x, y, s, prop, angle, *, mtext=...):
        """ """
        ...
    def draw_text(
        self,
        gc: GraphicsContextBase,
        x: float,
        y: float,
        s: str,
        prop: FontProperties,
        angle: float,
        ismath: bool = ...,
        mtext: Text = ...,
    ):
        """
        Draw a text instance.

        Parameters
        ----------
        gc : `.GraphicsContextBase`
            The graphics context.
        x : float
            The x location of the text in display coords.
        y : float
            The y location of the text baseline in display coords.
        s : str
            The text string.
        prop : `FontProperties`
            The font properties.
        angle : float
            The rotation angle in degrees anti-clockwise.
        mtext : `Text`
            The original text object to be rendered.

        Notes
        -----
        **Note for backend implementers:**

        When you are trying to determine if you have gotten your bounding box
        right (which is what enables the text layout/alignment to work
        properly), it helps to change the line in text.py::

            if 0: bbox_artist(self, renderer)

        to if 1, and then the actual bounding box will be plotted along with
        your text.
        """
        ...
    def get_text_width_height_descent(self, s: str, prop: FontProperties, ismath: bool):
        """
        Get the width, height, and descent (offset from the bottom
        to the baseline), in display coords, of the string *s* with
        `.FontProperties` *prop*.
        """
        ...
    def flipy(self) -> bool:
        """
        Return whether y values increase from top to bottom.

        Note that this only affects drawing of texts.
        """
        ...
    def get_canvas_width_height(self) -> tuple:
        """Return the canvas width and height in display coords."""
        ...
    def get_texmanager(self) -> TexManager:
        """Return the `.TexManager` instance."""
        ...
    def new_gc(self) -> GraphicsContextBase:
        """Return an instance of a `.GraphicsContextBase`."""
        ...
    def points_to_pixels(self, points: float | ArrayLike):
        """
        Convert points to display units.

        You need to override this function (unless your backend
        doesn't have a dpi, e.g., postscript or svg).  Some imaging
        systems assume some value for pixels per inch::

            points to pixels = points * pixels_per_inch/72 * dpi/72

        Parameters
        ----------
        points : float or array-like
            a float or a numpy array of float

        Returns
        -------
        Points converted to pixels
        """
        ...
    def start_rasterizing(self) -> None:
        """
        Switch to the raster renderer.

        Used by `.MixedModeRenderer`.
        """
        ...
    def stop_rasterizing(self) -> None:
        """
        Switch back to the vector renderer and draw the contents of the raster
        renderer as an image on the vector renderer.

        Used by `.MixedModeRenderer`.
        """
        ...
    def start_filter(self) -> bool:
        """
        Switch to a temporary renderer for image filtering effects.

        Currently only supported by the agg renderer.
        """
        ...
    def stop_filter(self, filter_func):
        """
        Switch back to the original renderer.  The contents of the temporary
        renderer is processed with the *filter_func* and is drawn on the
        original renderer as an image.

        Currently only supported by the agg renderer.
        """
        ...

class GraphicsContextBase:
    """An abstract base class that provides color, line styles, etc."""

    def __init__(self) -> None: ...
    def copy_properties(self, gc: GraphicsContextBase):
        """Copy properties from *gc* to self."""
        ...
    def restore(self) -> None:
        """
        Restore the graphics context from the stack - needed only
        for backends that save graphics contexts on a stack.
        """
        ...
    def get_alpha(self) -> float:
        """
        Return the alpha value used for blending - not supported on all
        backends.
        """
        ...
    def get_antialiased(self) -> bool:
        """Return whether the object should try to do antialiased rendering."""
        ...
    def get_capstyle(self) -> CapStyle:
        """Return the `.CapStyle`."""
        ...
    def get_clip_rectangle(self) -> Bbox:
        """
        Return the clip rectangle as a `~Bbox` instance.
        """
        ...
    def get_clip_path(self) -> tuple[Path, Transform]:
        """
        Return the clip path in the form (path, transform), where path
        is a `~.path.Path` instance, and transform is
        an affine transform to apply to the path before clipping.
        """
        ...
    def get_dashes(self) -> tuple:
        """
        Return the dash style as an (offset, dash-list) pair.

        See `.set_dashes` for details.

        Default value is (None, None).
        """
        ...
    def get_forced_alpha(self) -> bool:
        """
        Return whether the value given by get_alpha() should be used to
        override any other alpha-channel values.
        """
        ...
    def get_joinstyle(self) -> JoinStyle:
        """Return the `.JoinStyle`."""
        ...
    def get_linewidth(self) -> float:
        """Return the line width in points."""
        ...
    def get_rgb(self) -> tuple[float, ...]:
        """Return a tuple of three or four floats from 0-1."""
        ...
    def get_url(self) -> str | None:
        """Return a url if one is set, None otherwise."""
        ...
    def get_gid(self):
        """Return the object identifier if one is set, None otherwise."""
        ...
    def get_snap(self) -> bool | None:
        """
        Return the snap setting, which can be:

        * True: snap vertices to the nearest pixel center
        * False: leave vertices as-is
        * None: (auto) If the path contains only rectilinear line segments,
          round to the nearest pixel center
        """
        ...
    def set_alpha(self, alpha: float):
        """
        Set the alpha value used for blending - not supported on all backends.

        If ``alpha=None`` (the default), the alpha components of the
        foreground and fill colors will be used to set their respective
        transparencies (where applicable); otherwise, ``alpha`` will override
        them.
        """
        ...
    def set_antialiased(self, b: bool):
        """Set whether object should be drawn with antialiased rendering."""
        ...
    def set_capstyle(self, cs: CapStyle | Literal["butt", "projecting", "round"]):
        """
        Set how to draw endpoints of lines.

        Parameters
        ----------
        cs : `.CapStyle` or %(CapStyle)s
        """
        ...
    def set_clip_rectangle(self, rectangle: Bbox):
        """Set the clip rectangle to a `.Bbox` or None."""
        ...
    def set_clip_path(self, path: TransformedPath | None):
        """Set the clip path to a `.TransformedPath` or None."""
        ...
    def set_dashes(self, dash_offset: float, dash_list: ArrayLike | None):
        """
        Set the dash style for the gc.

        Parameters
        ----------
        dash_offset : float
            Distance, in points, into the dash pattern at which to
            start the pattern. It is usually set to 0.
        dash_list : array-like or None
            The on-off sequence as points.  None specifies a solid line. All
            values must otherwise be non-negative (:math:`\\ge 0`).

        Notes
        -----
        See p. 666 of the PostScript
        `Language Reference
        <https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf>`_
        for more info.
        """
        ...
    def set_foreground(self, fg: Color, isRGBA: bool = ...) -> None:
        """
        Set the foreground color.

        Parameters
        ----------
        fg : color
        isRGBA : bool
            If *fg* is known to be an ``(r, g, b, a)`` tuple, *isRGBA* can be
            set to True to improve performance.
        """
        ...
    def set_joinstyle(self, js: JoinStyle | Literal["miter", "round", "bevel"]) -> None:
        """
        Set how to draw connections between line segments.

        Parameters
        ----------
        js : `.JoinStyle` or %(JoinStyle)s
        """
        ...
    def set_linewidth(self, w) -> None:
        """Set the linewidth in points."""
        ...
    def set_url(self, url: str) -> None:
        """Set the url for links in compatible backends."""
        ...
    def set_gid(self, id) -> None:
        """Set the id."""
        ...
    def set_snap(self, snap: bool | None) -> None:
        """
        Set the snap setting which may be:

        * True: snap vertices to the nearest pixel center
        * False: leave vertices as-is
        * None: (auto) If the path contains only rectilinear line segments,
          round to the nearest pixel center
        """
        ...
    def set_hatch(self, hatch) -> None:
        """Set the hatch style (for fills)."""
        ...
    def get_hatch(self):
        """Get the current hatch style."""
        ...
    def get_hatch_path(self, density=...) -> Path:
        """Return a `.Path` for the current hatch."""
        ...
    def get_hatch_color(self):
        """Get the hatch color."""
        ...
    def set_hatch_color(self, hatch_color):
        """Set the hatch color."""
        ...
    def get_hatch_linewidth(self):
        """Get the hatch linewidth."""
        ...
    def get_sketch_params(self) -> tuple[float, float, float] | None:
        """
        Return the sketch parameters for the artist.

        Returns
        -------
        tuple or `None`

            A 3-tuple with the following elements:

            * ``scale``: The amplitude of the wiggle perpendicular to the
              source line.
            * ``length``: The length of the wiggle along the line.
            * ``randomness``: The scale factor by which the length is
              shrunken or expanded.

            May return `None` if no sketch parameters were set.
        """
        ...
    def set_sketch_params(
        self, scale: float = ..., length: float = ..., randomness: float = ...
    ) -> None:
        """
        Set the sketch parameters.

        Parameters
        ----------
        scale : float, optional
            The amplitude of the wiggle perpendicular to the source line, in
            pixels.  If scale is `None`, or not provided, no sketch filter will
            be provided.
        length : float, default: 128
            The length of the wiggle along the line, in pixels.
        randomness : float, default: 16
            The scale factor by which the length is shrunken or expanded.
        """
        ...

class TimerBase:
    """
    A base class for providing timer events, useful for things animations.
    Backends need to implement a few specific methods in order to use their
    own timing mechanisms so that the timer events are integrated into their
    event loops.

    Subclasses must override the following methods:

    - ``_timer_start``: Backend-specific code for starting the timer.
    - ``_timer_stop``: Backend-specific code for stopping the timer.

    Subclasses may additionally override the following methods:

    - ``_timer_set_single_shot``: Code for setting the timer to single shot
      operating mode, if supported by the timer object.  If not, the `Timer`
      class itself will store the flag and the ``_on_timer`` method should be
      overridden to support such behavior.

    - ``_timer_set_interval``: Code for setting the interval on the timer, if
      there is a method for doing so on the timer object.

    - ``_on_timer``: The internal function that any timer object should call,
      which will handle the task of running all callbacks that have been set.
    """

    def __init__(
        self, interval: int = 1000, callbacks: list[tuple[Callable, tuple, dict]] = ...
    ) -> None:
        """
        Parameters
        ----------
        interval : int, default: 1000ms
            The time between timer events in milliseconds.  Will be stored as
            ``timer.interval``.
        callbacks : list[tuple[callable, tuple, dict]]
            List of (func, args, kwargs) tuples that will be called upon
            timer events.  This list is accessible as ``timer.callbacks`` and
            can be manipulated directly, or the functions `add_callback` and
            `remove_callback` can be used.
        """
        ...
    def __del__(self) -> None:
        """Need to stop timer and possibly disconnect timer."""
        ...
    def start(self, interval: int = ...) -> None:
        """
        Start the timer object.

        Parameters
        ----------
        interval : int, optional
            Timer interval in milliseconds; overrides a previously set interval
            if provided.
        """
        ...
    def stop(self) -> None:
        """Stop the timer."""
        ...
    @property
    def interval(self) -> int:
        """The time between timer events, in milliseconds."""
        ...
    @interval.setter
    def interval(self, interval): ...
    @property
    def single_shot(self) -> bool:
        """Whether this timer should stop after a single run."""
        ...
    @single_shot.setter
    def single_shot(self, ss): ...
    def add_callback(self, func: Callable, *args, **kwargs) -> None:
        """
        Register *func* to be called by timer when the event fires. Any
        additional arguments provided will be passed to *func*.

        This function returns *func*, which makes it possible to use it as a
        decorator.
        """
        ...
    def remove_callback(self, func: Callable, *args, **kwargs) -> None:
        """
        Remove *func* from list of callbacks.

        *args* and *kwargs* are optional and used to distinguish between copies
        of the same function registered to be called with different arguments.
        This behavior is deprecated.  In the future, ``*args, **kwargs`` won't
        be considered anymore; to keep a specific callback removable by itself,
        pass it to `add_callback` as a `functools.partial` object.
        """
        ...

class Event:

    name: str
    canvas: FigureCanvasBase
    guiEvent: Any

    def __init__(self, name: str, canvas: FigureCanvasBase, guiEvent=...) -> None: ...

class DrawEvent(Event):

    renderer: RendererBase
    def __init__(
        self, name: str, canvas: FigureCanvasBase, renderer: RendererBase
    ) -> None: ...

class ResizeEvent(Event):

    width: int
    height: int

    def __init__(self, name: str, canvas: FigureCanvasBase) -> None: ...

class CloseEvent(Event):
    """An event triggered by a figure being closed."""

    ...

class LocationEvent(Event):

    x: int | None
    y: int | None
    inaxes: Axes | None
    xdata: float | None
    ydata: float | None

    lastevent = ...
    def __init__(
        self, name: str, canvas: FigureCanvasBase, x: int, y: int, guiEvent=...
    ) -> None: ...

class MouseButton(IntEnum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    BACK = 8
    FORWARD = 9

class MouseEvent(LocationEvent):
    button: None | MouseButton | Literal["up", "down"]
    key: None | str
    step: float
    dblclick: bool
    """
    A mouse event ('button_press_event', 'button_release_event', \
'scroll_event', 'motion_notify_event').

    A MouseEvent has a number of special attributes in addition to those
    defined by the parent `Event` and `LocationEvent` classes.

    Attributes
    ----------
    button : None or `MouseButton` or {'up', 'down'}
        The button pressed. 'up' and 'down' are used for scroll events.
        Note that LEFT and RIGHT actually refer to the "primary" and
        "secondary" buttons, i.e. if the user inverts their left and right
        buttons ("left-handed setting") then the LEFT button will be the one
        physically on the right.

    key : None or str
        The key pressed when the mouse event triggered, e.g. 'shift'.
        See `KeyEvent`.

        .. warning::
           This key is currently obtained from the last 'key_press_event' or
           'key_release_event' that occurred within the canvas.  Thus, if the
           last change of keyboard state occurred while the canvas did not have
           focus, this attribute will be wrong.

    step : float
        The number of scroll steps (positive for 'up', negative for 'down').
        This applies only to 'scroll_event' and defaults to 0 otherwise.

    dblclick : bool
        Whether the event is a double-click. This applies only to
        'button_press_event' and is False otherwise. In particular, it's
        not used in 'button_release_event'.

    Examples
    --------
    ::

        def on_press(event):
            print('you pressed', event.button, event.xdata, event.ydata)

        cid = fig.canvas.mpl_connect('button_press_event', on_press)
    """

    def __init__(
        self,
        name: str,
        canvas: FigureCanvasBase,
        x: int,
        y: int,
        button: None | MouseButton | Literal["up", "down"] = ...,
        key: str | None = ...,
        step=...,
        dblclick: bool = ...,
        guiEvent=...,
    ) -> None: ...
    def __str__(self) -> str: ...

class PickEvent(Event):
    mouseevent: MouseEvent
    artist: Artist
    """
    A pick event.

    This event is fired when the user picks a location on the canvas
    sufficiently close to an artist that has been made pickable with
    `.Artist.set_picker`.

    A PickEvent has a number of special attributes in addition to those defined
    by the parent `Event` class.

    Attributes
    ----------
    mouseevent : `MouseEvent`
        The mouse event that generated the pick.
    artist : `Artist`
        The picked artist.  Note that artists are not pickable by default
        (see `.Artist.set_picker`).
    other
        Additional attributes may be present depending on the type of the
        picked object; e.g., a `.Line2D` pick may define different extra
        attributes than a `.PatchCollection` pick.

    Examples
    --------
    Bind a function ``on_pick()`` to pick events, that prints the coordinates
    of the picked data point::

        ax.plot(np.rand(100), 'o', picker=5)  # 5 points tolerance

        def on_pick(event):
            line = event.artist
            xdata, ydata = line.get_data()
            ind = event.ind
            print('on pick line:', np.array([xdata[ind], ydata[ind]]).T)

        cid = fig.canvas.mpl_connect('pick_event', on_pick)
    """

    def __init__(
        self,
        name: str,
        canvas: FigureCanvasBase,
        mouseevent: MouseEvent,
        artist: Artist,
        guiEvent=...,
        **kwargs
    ) -> None: ...

class KeyEvent(LocationEvent):
    key: None | str
    """
    A key event (key press, key release).

    A KeyEvent has a number of special attributes in addition to those defined
    by the parent `Event` and `LocationEvent` classes.

    Attributes
    ----------
    key : None or str
        The key(s) pressed. Could be *None*, a single case sensitive Unicode
        character ("g", "G", "#", etc.), a special key ("control", "shift",
        "f1", "up", etc.) or a combination of the above (e.g., "ctrl+alt+g",
        "ctrl+alt+G").

    Notes
    -----
    Modifier keys will be prefixed to the pressed key and will be in the order
    "ctrl", "alt", "super". The exception to this rule is when the pressed key
    is itself a modifier key, therefore "ctrl+alt" and "alt+control" can both
    be valid key values.

    Examples
    --------
    ::

        def on_key(event):
            print('you pressed', event.key, event.xdata, event.ydata)

        cid = fig.canvas.mpl_connect('key_press_event', on_key)
    """

    def __init__(
        self,
        name: str,
        canvas: FigureCanvasBase,
        key: None | str,
        x: int = ...,
        y: int = ...,
        guiEvent=...,
    ) -> None: ...

class FigureCanvasBase:
    """
    The canvas the figure renders into.

    Attributes
    ----------
    figure : `Figure`
        A high-level figure instance.
    """

    required_interactive_framework = ...
    manager_class = ...
    events = ...
    fixed_dpi = ...
    filetypes = ...
    widgetlock: LockDraw = ...

    @classmethod
    def supports_blit(cls):
        """If this Canvas sub-class supports blitting."""
        ...
    def __init__(self, figure: Figure = ...) -> None: ...

    callbacks = ...
    button_pick_id = ...
    scroll_pick_id = ...
    @classmethod
    def new_manager(cls, figure: Figure, num):
        """
        Create a new figure manager for *figure*, using this canvas class.

        Notes
        -----
        This method should not be reimplemented in subclasses.  If
        custom manager creation logic is needed, please reimplement
        ``FigureManager.create_with_canvas``.
        """
        ...
    def is_saving(self) -> bool:
        """
        Return whether the renderer is in the process of saving
        to a file, rather than rendering for an on-screen buffer.
        """
        ...
    def pick(self, mouseevent: MouseEvent): ...
    def blit(self, bbox=...) -> None:
        """Blit the canvas in bbox (default entire canvas)."""
        ...
    def resize(self, w: int, h: int) -> None:
        """
        UNUSED: Set the canvas size in pixels.

        Certain backends may implement a similar method internally, but this is
        not a requirement of, nor is it used by, Matplotlib itself.
        """
        ...
    def draw_event(self, renderer: RendererBase) -> None:
        """Pass a `DrawEvent` to all functions connected to ``draw_event``."""
        ...
    def resize_event(self) -> None:
        """
        Pass a `ResizeEvent` to all functions connected to ``resize_event``.
        """
        ...
    def close_event(self, guiEvent=...) -> None:
        """
        Pass a `CloseEvent` to all functions connected to ``close_event``.
        """
        ...
    def key_press_event(self, key: str | None, guiEvent=...) -> None:
        """
        Pass a `KeyEvent` to all functions connected to ``key_press_event``.
        """
        ...
    def key_release_event(self, key: str | None, guiEvent=...) -> None:
        """
        Pass a `KeyEvent` to all functions connected to ``key_release_event``.
        """
        ...
    def pick_event(self, mouseevent: MouseEvent, artist: Artist, **kwargs) -> None:
        """
        Callback processing for pick events.

        This method will be called by artists who are picked and will
        fire off `PickEvent` callbacks registered listeners.

        Note that artists are not pickable by default (see
        `.Artist.set_picker`).
        """
        ...
    def scroll_event(self, x: float, y: float, step, guiEvent=...) -> None:
        """
        Callback processing for scroll events.

        Backend derived classes should call this function on any
        scroll wheel event.  (*x*, *y*) are the canvas coords ((0, 0) is lower
        left).  button and key are as defined in `MouseEvent`.

        This method will call all functions connected to the 'scroll_event'
        with a `MouseEvent` instance.
        """
        ...
    def button_press_event(
        self, x: float, y: float, button, dblclick: bool = ..., guiEvent=...
    ) -> None:
        """
        Callback processing for mouse button press events.

        Backend derived classes should call this function on any mouse
        button press.  (*x*, *y*) are the canvas coords ((0, 0) is lower left).
        button and key are as defined in `MouseEvent`.

        This method will call all functions connected to the
        'button_press_event' with a `MouseEvent` instance.
        """
        ...
    def button_release_event(self, x: float, y: float, button, guiEvent=...) -> None:
        """
        Callback processing for mouse button release events.

        Backend derived classes should call this function on any mouse
        button release.

        This method will call all functions connected to the
        'button_release_event' with a `MouseEvent` instance.

        Parameters
        ----------
        x : float
            The canvas coordinates where 0=left.
        y : float
            The canvas coordinates where 0=bottom.
        guiEvent
            The native UI event that generated the Matplotlib event.
        """
        ...
    def motion_notify_event(self, x: float, y: float, guiEvent=...):
        """
        Callback processing for mouse movement events.

        Backend derived classes should call this function on any
        motion-notify-event.

        This method will call all functions connected to the
        'motion_notify_event' with a `MouseEvent` instance.

        Parameters
        ----------
        x : float
            The canvas coordinates where 0=left.
        y : float
            The canvas coordinates where 0=bottom.
        guiEvent
            The native UI event that generated the Matplotlib event.
        """
        ...
    def leave_notify_event(self, guiEvent=...) -> None:
        """
        Callback processing for the mouse cursor leaving the canvas.

        Backend derived classes should call this function when leaving
        canvas.

        Parameters
        ----------
        guiEvent
            The native UI event that generated the Matplotlib event.
        """
        ...
    def enter_notify_event(self, guiEvent=..., xy: tuple[float, float] = ...) -> None:
        """
        Callback processing for the mouse cursor entering the canvas.

        Backend derived classes should call this function when entering
        canvas.

        Parameters
        ----------
        guiEvent
            The native UI event that generated the Matplotlib event.
        xy : (float, float)
            The coordinate location of the pointer when the canvas is entered.
        """
        ...
    def inaxes(self, xy: tuple[float, float]) -> Axes | None:
        """
        Return the topmost visible `~.axes.Axes` containing the point *xy*.

        Parameters
        ----------
        xy : (float, float)
            (x, y) pixel positions from left/bottom of the canvas.

        Returns
        -------
        `~Axes` or None
            The topmost visible Axes containing the point, or None if there
            is no Axes at the point.
        """
        ...
    def grab_mouse(self, ax: Axes) -> None:
        """
        Set the child `~.axes.Axes` which is grabbing the mouse events.

        Usually called by the widgets themselves. It is an error to call this
        if the mouse is already grabbed by another Axes.
        """
        ...
    def release_mouse(self, ax: Axes) -> None:
        """
        Release the mouse grab held by the `~.axes.Axes` *ax*.

        Usually called by the widgets. It is ok to call this even if *ax*
        doesn't have the mouse grab currently.
        """
        ...
    def set_cursor(self, cursor: Cursors) -> None:
        """
        Set the current cursor.

        This may have no effect if the backend does not display anything.

        If required by the backend, this method should trigger an update in
        the backend event loop after the cursor is set, as this method may be
        called e.g. before a long-running task during which the GUI is not
        updated.

        Parameters
        ----------
        cursor : `.Cursors`
            The cursor to display over the canvas. Note: some backends may
            change the cursor for the entire window.
        """
        ...
    def draw(self, *args, **kwargs) -> None:
        """
        Render the `.Figure`.

        This method must walk the artist tree, even if no output is produced,
        because it triggers deferred work that users may want to access
        before saving output to disk. For example computing limits,
        auto-limits, and tick values.
        """
        ...
    def draw_idle(self, *args, **kwargs) -> None:
        """
        Request a widget redraw once control returns to the GUI event loop.

        Even if multiple calls to `draw_idle` occur before control returns
        to the GUI event loop, the figure will only be rendered once.

        Notes
        -----
        Backends may choose to override the method and implement their own
        strategy to prevent multiple renderings.

        """
        ...
    @property
    def device_pixel_ratio(self) -> float:
        """
        The ratio of physical to logical pixels used for the canvas on screen.

        By default, this is 1, meaning physical and logical pixels are the same
        size. Subclasses that support High DPI screens may set this property to
        indicate that said ratio is different. All Matplotlib interaction,
        unless working directly with the canvas, remains in logical pixels.

        """
        ...
    def get_width_height(self, *, physical: bool = ...) -> tuple[int, int]:
        """
        Return the figure width and height in integral points or pixels.

        When the figure is used on High DPI screens (and the backend supports
        it), the truncation to integers occurs after scaling by the device
        pixel ratio.

        Parameters
        ----------
        physical : bool, default: False
            Whether to return true physical pixels or logical pixels. Physical
            pixels may be used by backends that support HiDPI, but still
            configure the canvas using its actual size.

        Returns
        -------
        width, height : int
            The size of the figure, in points or pixels, depending on the
            backend.
        """
        ...
    @classmethod
    def get_supported_filetypes(cls) -> dict:
        """Return dict of savefig file formats supported by this backend."""
        ...
    @classmethod
    def get_supported_filetypes_grouped(cls) -> dict[str, list[str]]:
        """
        Return a dict of savefig file formats supported by this backend,
        where the keys are a file type name, such as 'Joint Photographic
        Experts Group', and the values are a list of filename extensions used
        for that filetype, such as ['jpg', 'jpeg'].
        """
        ...
    def print_figure(
        self,
        filename: str | PathLike | FileLike,
        dpi: float = ...,
        facecolor: Color | Literal["auto"] = ...,
        edgecolor: Color | Literal["auto"] = ...,
        orientation: Literal["landscape", "portrait"] = ...,
        format: str = ...,
        *,
        bbox_inches: Literal["tight"] | Bbox = ...,
        pad_inches: float = ...,
        bbox_extra_artists: list[Artist] = ...,
        backend: str = ...,
        **kwargs
    ) -> None:
        """
        Render the figure to hardcopy. Set the figure patch face and edge
        colors.  This is useful because some of the GUIs have a gray figure
        face color background and you'll probably want to override this on
        hardcopy.

        Parameters
        ----------
        filename : str or path-like or file-like
            The file where the figure is saved.

        dpi : float, default: :rc:`savefig.dpi`
            The dots per inch to save the figure in.

        facecolor : color or 'auto', default: :rc:`savefig.facecolor`
            The facecolor of the figure.  If 'auto', use the current figure
            facecolor.

        edgecolor : color or 'auto', default: :rc:`savefig.edgecolor`
            The edgecolor of the figure.  If 'auto', use the current figure
            edgecolor.

        orientation : {'landscape', 'portrait'}, default: 'portrait'
            Only currently applies to PostScript printing.

        format : str, optional
            Force a specific file format. If not given, the format is inferred
            from the *filename* extension, and if that fails from
            :rc:`savefig.format`.

        bbox_inches : 'tight' or `.Bbox`, default: :rc:`savefig.bbox`
            Bounding box in inches: only the given portion of the figure is
            saved.  If 'tight', try to figure out the tight bbox of the figure.

        pad_inches : float, default: :rc:`savefig.pad_inches`
            Amount of padding around the figure when *bbox_inches* is 'tight'.

        bbox_extra_artists : list of `~Artist`, optional
            A list of extra artists that will be considered when the
            tight bbox is calculated.

        backend : str, optional
            Use a non-default backend to render the file, e.g. to render a
            png file with the "cairo" backend rather than the default "agg",
            or a pdf file with the "pgf" backend rather than the default
            "pdf".  Note that the default backend is normally sufficient.  See
            :ref:`the-builtin-backends` for a list of valid backends for each
            file format.  Custom backends can be referenced as "module://...".
        """
        ...
    @classmethod
    def get_default_filetype(cls) -> str:
        """
        Return the default savefig file format as specified in
        :rc:`savefig.format`.

        The returned string does not include a period. This method is
        overridden in backends that only support a single file type.
        """
        ...
    def get_default_filename(self) -> str:
        """
        Return a string, which includes extension, suitable for use as
        a default filename.
        """
        ...
    def switch_backends(self, FigureCanvasClass) -> None:
        """
        Instantiate an instance of FigureCanvasClass

        This is used for backend switching, e.g., to instantiate a
        FigureCanvasPS from a FigureCanvasGTK.  Note, deep copying is
        not done, so any changes to one of the instances (e.g., setting
        figure size or line props), will be reflected in the other
        """
        ...
    def mpl_connect(self, s: str, func: Callable):
        """
        Bind function *func* to event *s*.

        Parameters
        ----------
        s : str
            One of the following events ids:

            - 'button_press_event'
            - 'button_release_event'
            - 'draw_event'
            - 'key_press_event'
            - 'key_release_event'
            - 'motion_notify_event'
            - 'pick_event'
            - 'resize_event'
            - 'scroll_event'
            - 'figure_enter_event',
            - 'figure_leave_event',
            - 'axes_enter_event',
            - 'axes_leave_event'
            - 'close_event'.

        func : callable
            The callback function to be executed, which must have the
            signature::

                def func(event: Event) -> Any

            For the location events (button and key press/release), if the
            mouse is over the Axes, the ``inaxes`` attribute of the event will
            be set to the `~Axes` the event occurs is over, and
            additionally, the variables ``xdata`` and ``ydata`` attributes will
            be set to the mouse location in data coordinates.  See `.KeyEvent`
            and `.MouseEvent` for more info.

        Returns
        -------
        cid
            A connection id that can be used with
            `.FigureCanvasBase.mpl_disconnect`.

        Examples
        --------
        ::

            def on_press(event):
                print('you pressed', event.button, event.xdata, event.ydata)

            cid = canvas.mpl_connect('button_press_event', on_press)
        """
        ...
    def mpl_disconnect(self, cid):
        """
        Disconnect the callback with id *cid*.

        Examples
        --------
        ::

            cid = canvas.mpl_connect('button_press_event', on_press)
            # ... later
            canvas.mpl_disconnect(cid)
        """
        ...
    _timer_cls = TimerBase
    def new_timer(
        self, interval: int = ..., callbacks: list[tuple[Callable, tuple, dict]] = ...
    ):
        """
        Create a new backend-specific subclass of `.Timer`.

        This is useful for getting periodic events through the backend's native
        event loop.  Implemented only for backends with GUIs.

        Parameters
        ----------
        interval : int
            Timer interval in milliseconds.

        callbacks : list[tuple[callable, tuple, dict]]
            Sequence of (func, args, kwargs) where ``func(*args, **kwargs)``
            will be executed by the timer every *interval*.

            Callbacks which return ``False`` or ``0`` will be removed from the
            timer.

        Examples
        --------
        >>> timer = fig.canvas.new_timer(callbacks=[(f1, (1,), {'a': 3})])
        """
        ...
    def flush_events(self) -> None:
        """
        Flush the GUI events for the figure.

        Interactive backends need to reimplement this method.
        """
        ...
    def start_event_loop(self, timeout: int = ...) -> None:
        """
        Start a blocking event loop.

        Such an event loop is used by interactive functions, such as
        `~.Figure.ginput` and `~.Figure.waitforbuttonpress`, to wait for
        events.

        The event loop blocks until a callback function triggers
        `stop_event_loop`, or *timeout* is reached.

        If *timeout* is 0 or negative, never timeout.

        Only interactive backends need to reimplement this method and it relies
        on `flush_events` being properly implemented.

        Interactive backends should implement this in a more native way.
        """
        ...
    def stop_event_loop(self) -> None:
        """
        Stop the current blocking event loop.

        Interactive backends need to reimplement this to match
        `start_event_loop`
        """
        ...

def key_press_handler(
    event: KeyEvent, canvas: FigureCanvasBase = ..., toolbar: NavigationToolbar2 = ...
) -> None:
    """
    Implement the default Matplotlib key bindings for the canvas and toolbar
    described at :ref:`key-event-handling`.

    Parameters
    ----------
    event : `KeyEvent`
        A key press/release event.
    canvas : `FigureCanvasBase`, default: ``event.canvas``
        The backend-specific canvas instance.  This parameter is kept for
        back-compatibility, but, if set, should always be equal to
        ``event.canvas``.
    toolbar : `NavigationToolbar2`, default: ``event.canvas.toolbar``
        The navigation cursor toolbar.  This parameter is kept for
        back-compatibility, but, if set, should always be equal to
        ``event.canvas.toolbar``.
    """
    ...

def button_press_handler(event, canvas: FigureCanvasBase = ..., toolbar=...) -> None:
    """
    The default Matplotlib button actions for extra mouse buttons.

    Parameters are as for `key_press_handler`, except that *event* is a
    `MouseEvent`.
    """
    ...

class NonGuiException(Exception):
    """Raised when trying show a figure in a non-GUI backend."""

    ...

class FigureManagerBase:
    """
    A backend-independent abstraction of a figure container and controller.

    The figure manager is used by pyplot to interact with the window in a
    backend-independent way. It's an adapter for the real (GUI) framework that
    represents the visual figure on screen.

    GUI backends define from this class to translate common operations such
    as *show* or *resize* to the GUI-specific code. Non-GUI backends do not
    support these operations an can just use the base class.

    This following basic operations are accessible:

    **Window operations**

    - `~.FigureManagerBase.show`
    - `~.FigureManagerBase.destroy`
    - `~.FigureManagerBase.full_screen_toggle`
    - `~.FigureManagerBase.resize`
    - `~.FigureManagerBase.get_window_title`
    - `~.FigureManagerBase.set_window_title`

    **Key and mouse button press handling**

    The figure manager sets up default key and mouse button press handling by
    hooking up the `.key_press_handler` to the matplotlib event system. This
    ensures the same shortcuts and mouse actions across backends.

    **Other operations**

    Subclasses will have additional attributes and functions to access
    additional functionality. This is of course backend-specific. For example,
    most GUI backends have ``window`` and ``toolbar`` attributes that give
    access to the native GUI widgets of the respective framework.

    Attributes
    ----------
    canvas : `FigureCanvasBase`
        The backend-specific canvas instance.

    num : int or str
        The figure number.

    key_press_handler_id : int
        The default key handler cid, when using the toolmanager.
        To disable the default key press handling use::

            figure.canvas.mpl_disconnect(
                figure.canvas.manager.key_press_handler_id)

    button_press_handler_id : int
        The default mouse button handler cid, when using the toolmanager.
        To disable the default button press handling use::

            figure.canvas.mpl_disconnect(
                figure.canvas.manager.button_press_handler_id)
    """

    canvas: FigureCanvasBase
    num: int | str
    key_press_handler_id: int
    button_press_handler_id: int

    def __init__(self, canvas: FigureCanvasBase, num: int | str) -> None: ...
    @classmethod
    def create_with_canvas(cls, canvas_class, figure: Figure, num: int | str):
        """
        Create a manager for a given *figure* using a specific *canvas_class*.

        Backends should override this method if they have specific needs for
        setting up the canvas or the manager.
        """
        ...
    def show(self) -> None:
        """
        For GUI backends, show the figure window and redraw.
        For non-GUI backends, raise an exception, unless running headless (i.e.
        on Linux with an unset DISPLAY); this exception is converted to a
        warning in `.Figure.show`.
        """
        ...
    def destroy(self) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def resize(self, w: int, h: int) -> None:
        """For GUI backends, resize the window (in physical pixels)."""
        ...
    def get_window_title(self) -> None:
        """
        Return the title text of the window containing the figure, or None
        if there is no window (e.g., a PS backend).
        """
        ...
    def set_window_title(self, title: str) -> None:
        """
        Set the title text of the window containing the figure.

        This has no effect for non-GUI (e.g., PS) backends.
        """
        ...

cursors = tools.cursors

class _Mode(str, Enum):
    NONE = ...
    PAN = ...
    ZOOM = ...
    def __str__(self) -> str: ...

class NavigationToolbar2:
    """
    Base class for the navigation cursor, version 2.

    Backends must implement a canvas that handles connections for
    'button_press_event' and 'button_release_event'.  See
    :meth:`FigureCanvasBase.mpl_connect` for more information.

    They must also define

      :meth:`save_figure`
         save the current figure

      :meth:`draw_rubberband` (optional)
         draw the zoom to rect "rubberband" rectangle

      :meth:`set_message` (optional)
         display message

      :meth:`set_history_buttons` (optional)
         you can change the history back / forward buttons to
         indicate disabled / enabled state.

    and override ``__init__`` to set up the toolbar -- without forgetting to
    call the base-class init.  Typically, ``__init__`` needs to set up toolbar
    buttons connected to the `home`, `back`, `forward`, `pan`, `zoom`, and
    `save_figure` methods and using standard icons in the "images" subdirectory
    of the data path.

    That's it, we'll do the rest!
    """

    toolitems = ...
    def __init__(self, canvas: FigureCanvasBase) -> None: ...
    def set_message(self, s: str):
        """Display a message on toolbar or in status bar."""
        ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None:
        """
        Draw a rectangle rubberband to indicate zoom limits.

        Note that it is not guaranteed that ``x0 <= x1`` and ``y0 <= y1``.
        """
        ...
    def remove_rubberband(self) -> None:
        """Remove the rubberband."""
        ...
    def home(self, *args) -> None:
        """
        Restore the original view.

        For convenience of being directly connected as a GUI callback, which
        often get passed additional parameters, this method accepts arbitrary
        parameters, but does not use them.
        """
        ...
    def back(self, *args) -> None:
        """
        Move back up the view lim stack.

        For convenience of being directly connected as a GUI callback, which
        often get passed additional parameters, this method accepts arbitrary
        parameters, but does not use them.
        """
        ...
    def forward(self, *args) -> None:
        """
        Move forward in the view lim stack.

        For convenience of being directly connected as a GUI callback, which
        often get passed additional parameters, this method accepts arbitrary
        parameters, but does not use them.
        """
        ...
    def mouse_move(self, event: MouseEvent) -> None: ...
    def pan(self, *args) -> None:
        """
        Toggle the pan/zoom tool.

        Pan with left button, zoom with right.
        """
        ...
    def press_pan(self, event: MouseEvent) -> None:
        """Callback for mouse button press in pan/zoom mode."""
        ...
    def drag_pan(self, event: MouseEvent) -> None:
        """Callback for dragging in pan/zoom mode."""
        ...
    def release_pan(self, event: MouseEvent) -> None:
        """Callback for mouse button release in pan/zoom mode."""
        ...
    def zoom(self, *args):
        """Toggle zoom to rect mode."""
        ...
    def press_zoom(self, event: MouseEvent) -> None:
        """Callback for mouse button press in zoom to rect mode."""
        ...
    def drag_zoom(self, event: MouseEvent) -> None:
        """Callback for dragging in zoom mode."""
        ...
    def release_zoom(self, event: MouseEvent) -> None:
        """Callback for mouse button release in zoom to rect mode."""
        ...
    def push_current(self) -> None:
        """Push the current view limits and position onto the stack."""
        ...
    def configure_subplots(self, *args) -> None: ...
    def save_figure(self, *args) -> None:
        """Save the current figure."""
        ...
    def set_cursor(self, cursor: Cursor) -> None:
        """
        Set the current cursor to one of the :class:`Cursors` enums values.

        If required by the backend, this method should trigger an update in
        the backend event loop after the cursor is set, as this method may be
        called e.g. before a long-running task during which the GUI is not
        updated.
        """
        ...
    def update(self) -> None:
        """Reset the Axes stack."""
        ...
    def set_history_buttons(self) -> None:
        """Enable or disable the back/forward button."""
        ...

class ToolContainerBase:
    """
    Base class for all tool containers, e.g. toolbars.

    Attributes
    ----------
    toolmanager : `.ToolManager`
        The tools with which this `ToolContainer` wants to communicate.
    """

    toolmanager: ToolManager

    def __init__(self, toolmanager: ToolManager) -> None: ...
    def add_tool(self, tool: ToolManager, group: str, position: int = ...) -> None:
        """
        Add a tool to this container.

        Parameters
        ----------
        tool : tool_like
            The tool to add, see `.ToolManager.get_tool`.
        group : str
            The name of the group to add this tool to.
        position : int, default: -1
            The position within the group to place this tool.
        """
        ...
    def trigger_tool(self, name: str) -> None:
        """
        Trigger the tool.

        Parameters
        ----------
        name : str
            Name (id) of the tool triggered from within the container.
        """
        ...
    def add_toolitem(
        self,
        name: str,
        group: str,
        position: int,
        image: str,
        description: str,
        toggle: bool,
    ) -> None:
        """
        Add a toolitem to the container.

        This method must be implemented per backend.

        The callback associated with the button click event,
        must be *exactly* ``self.trigger_tool(name)``.

        Parameters
        ----------
        name : str
            Name of the tool to add, this gets used as the tool's ID and as the
            default label of the buttons.
        group : str
            Name of the group that this tool belongs to.
        position : int
            Position of the tool within its group, if -1 it goes at the end.
        image : str
            Filename of the image for the button or `None`.
        description : str
            Description of the tool, used for the tooltips.
        toggle : bool
            * `True` : The button is a toggle (change the pressed/unpressed
              state between consecutive clicks).
            * `False` : The button is a normal button (returns to unpressed
              state after release).
        """
        ...
    def toggle_toolitem(self, name: str, toggled: bool) -> None:
        """
        Toggle the toolitem without firing event.

        Parameters
        ----------
        name : str
            Id of the tool to toggle.
        toggled : bool
            Whether to set this tool as toggled or not.
        """
        ...
    def remove_toolitem(self, name: str) -> None:
        """
        Remove a toolitem from the `ToolContainer`.

        This method must get implemented per backend.

        Called when `.ToolManager` emits a `tool_removed_event`.

        Parameters
        ----------
        name : str
            Name of the tool to remove.
        """
        ...
    def set_message(self, s: str) -> None:
        """
        Display a message on the toolbar.

        Parameters
        ----------
        s : str
            Message text.
        """
        ...

class _Backend:
    backend_version = ...
    FigureCanvas = FigureCanvasBase
    FigureManager = FigureManagerBase
    mainloop = ...
    @classmethod
    def new_figure_manager(cls, num, *args, **kwargs) -> FigureManagerBase:
        """Create a new figure manager instance."""
        ...
    @classmethod
    def new_figure_manager_given_figure(cls, num, figure) -> FigureManagerBase:
        """Create a new figure manager instance for the given figure."""
        ...
    @classmethod
    def draw_if_interactive(cls) -> None: ...
    @classmethod
    def show(cls, *, block: bool | None = ...) -> None:
        """
        Show all figures.

        `show` blocks by calling `mainloop` if *block* is ``True``, or if it
        is ``None`` and we are neither in IPython's ``%pylab`` mode, nor in
        `interactive` mode.
        """
        ...
    @classmethod
    def export(cls) -> None: ...

class ShowBase(_Backend):
    """
    Simple base class to generate a ``show()`` function in backends.

    Subclass must override ``mainloop()`` method.
    """

    def __call__(self, block: bool | None = ...) -> None: ...
