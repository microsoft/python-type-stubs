from ast import Str
from tkinter import Image
import numpy as np
from typing import Callable, Literal, Sequence
from ._typing import *
from .text import Text
from .patches import Circle
from .backend_bases import (
    DrawEvent,
    Event,
    FigureCanvasBase,
    KeyEvent,
    MouseButton,
    MouseEvent,
)
from .lines import Line2D
from .figure import Figure
from .axes import Axes
from .artist import Artist

class LockDraw:
    """
    Some widgets, like the cursor, draw onto the canvas, and this is not
    desirable under all circumstances, like when the toolbar is in zoom-to-rect
    mode and drawing a rectangle.  To avoid this, a widget can acquire a
    canvas' lock with ``canvas.widgetlock(widget)`` before drawing on the
    canvas; this will prevent other widgets from doing so at the same time (if
    they also try to acquire the lock first).
    """

    def __init__(self) -> None: ...
    def __call__(self, o: "Lasso") -> None:
        """Reserve the lock for *o*."""
        ...
    def release(self, o: "Lasso") -> None:
        """Release the lock from *o*."""
        ...
    def available(self, o: "Lasso") -> bool:
        """Return whether drawing is available to *o*."""
        ...
    def isowner(self, o: "Lasso") -> bool:
        """Return whether *o* owns this lock."""
        ...
    def locked(self) -> bool:
        """Return whether the lock is currently held by an owner."""
        ...

class Widget:
    """
    Abstract base class for GUI neutral widgets.
    """

    drawon = ...
    eventson = ...

    def set_active(self, active: Widget):
        """Set whether the widget is active."""
        ...
    def get_active(self) -> bool:
        """Get whether the widget is active."""
        ...
    active = ...
    def ignore(self, event: Event) -> bool:
        """
        Return whether *event* should be ignored.

        This method should be called at the beginning of any event callback.
        """
        ...

class AxesWidget(Widget):
    """
    Widget connected to a single `~Axes`.

    To guarantee that the widget remains responsive and not garbage-collected,
    a reference to the object should be maintained by the user.

    This is necessary because the callback registry
    maintains only weak-refs to the functions, which are member
    functions of the widget.  If there are no references to the widget
    object it may be garbage collected which will disconnect the callbacks.

    Attributes
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    canvas : `~FigureCanvasBase`
        The parent figure canvas for the widget.
    active : bool
        If False, the widget does not respond to events.
    """

    def __init__(self, ax: Axes) -> None: ...
    def connect_event(self, event: str, callback: Callable) -> None:
        """
        Connect a callback function with an event.

        This should be used in lieu of ``figure.canvas.mpl_connect`` since this
        function stores callback ids for later clean up.
        """
        ...
    def disconnect_events(self) -> None:
        """Disconnect all events created by this widget."""
        ...

class Button(AxesWidget):
    """
    A GUI neutral button.

    For the button to remain responsive you must keep a reference to it.
    Call `.on_clicked` to connect to the button.

    Attributes
    ----------
    ax
        The `Axes` the button renders into.
    label
        A `Text` instance.
    color
        The color of the button when not hovering.
    hovercolor
        The color of the button when hovering.
    """

    def __init__(
        self,
        ax: Axes,
        label: Str,
        image: Image | ArrayLike = ...,
        color: Color = ...,
        hovercolor: Color = ...,
    ) -> None:
        """
        Parameters
        ----------
        ax : `~Axes`
            The `~.axes.Axes` instance the button will be placed into.
        label : str
            The button text.
        image : array-like or PIL Image
            The image to place in the button, if not *None*.  The parameter is
            directly forwarded to `~Axes.imshow`.
        color : color
            The color of the button when not activated.
        hovercolor : color
            The color of the button when the mouse is over it.
        """
        ...
    def on_clicked(self, func: Callable) -> int:
        """
        Connect the callback function *func* to button click events.

        Returns a connection id, which can be used to disconnect the callback.
        """
        ...
    def disconnect(self, cid):
        """Remove the callback function with connection id *cid*."""
        ...

class SliderBase(AxesWidget):
    """
    The base class for constructing Slider widgets. Not intended for direct
    usage.

    For the slider to remain responsive you must maintain a reference to it.
    """

    def __init__(
        self,
        ax: Axes,
        orientation: Literal["horizontal", "vertical"],
        closedmin: bool,
        closedmax: bool,
        valmin: float,
        valmax: float,
        valfmt: str | None,
        dragging: bool,
        valstep: float | ArrayLike | None,
    ) -> None: ...
    def disconnect(self, cid: int):
        """
        Remove the observer with connection id *cid*.

        Parameters
        ----------
        cid : int
            Connection id of the observer to be removed.
        """
        ...
    def reset(self):
        """Reset the slider to the initial value."""
        ...

class Slider(SliderBase):
    """
    A slider representing a floating point range.

    Create a slider from *valmin* to *valmax* in Axes *ax*. For the slider to
    remain responsive you must maintain a reference to it. Call
    :meth:`on_changed` to connect to the slider event.

    Attributes
    ----------
    val : float
        Slider value.
    """

    val: float

    def __init__(
        self,
        ax: Axes,
        label: str,
        valmin: float,
        valmax: float,
        valinit: float = ...,
        valfmt: str | None = ...,
        closedmin: bool = True,
        closedmax: bool = True,
        slidermin: Slider | None = None,
        slidermax: Slider | None = None,
        dragging: bool = True,
        valstep: float | ArrayLike | None = None,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        *,
        initcolo: Color = "r",
        track_color: Color = "lightgrey",
        handle_style: dict = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        ax : Axes
            The Axes to put the slider in.

        label : str
            Slider label.

        valmin : float
            The minimum value of the slider.

        valmax : float
            The maximum value of the slider.

        valinit : float, default: 0.5
            The slider initial position.

        valfmt : str, default: None
            %-format string used to format the slider value.  If None, a
            `.ScalarFormatter` is used instead.

        closedmin : bool, default: True
            Whether the slider interval is closed on the bottom.

        closedmax : bool, default: True
            Whether the slider interval is closed on the top.

        slidermin : Slider, default: None
            Do not allow the current slider to have a value less than
            the value of the Slider *slidermin*.

        slidermax : Slider, default: None
            Do not allow the current slider to have a value greater than
            the value of the Slider *slidermax*.

        dragging : bool, default: True
            If True the slider can be dragged by the mouse.

        valstep : float or array-like, default: None
            If a float, the slider will snap to multiples of *valstep*.
            If an array the slider will snap to the values in the array.

        orientation : {'horizontal', 'vertical'}, default: 'horizontal'
            The orientation of the slider.

        initcolor : color, default: 'r'
            The color of the line at the *valinit* position. Set to ``'none'``
            for no line.

        track_color : color, default: 'lightgrey'
            The color of the background track. The track is accessible for
            further styling via the *track* attribute.

        handle_style : dict
            Properties of the slider handle. Default values are

            ========= ===== ======= ========================================
            Key       Value Default Description
            ========= ===== ======= ========================================
            facecolor color 'white' The facecolor of the slider handle.
            edgecolor color '.75'   The edgecolor of the slider handle.
            size      int   10      The size of the slider handle in points.
            ========= ===== ======= ========================================

            Other values will be transformed as marker{foo} and passed to the
            `~.Line2D` constructor. e.g. ``handle_style = {'style'='x'}`` will
            result in ``markerstyle = 'x'``.

        Notes
        -----
        Additional kwargs are passed on to ``self.poly`` which is the
        `~Polygon` that draws the slider knob.  See the
        `.Polygon` documentation for valid property names (``facecolor``,
        ``edgecolor``, ``alpha``, etc.).
        """
        ...
    def set_val(self, val: float) -> None:
        """
        Set slider value to *val*.

        Parameters
        ----------
        val : float
        """
        ...
    def on_changed(self, func: Callable) -> int:
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed.
            The function must accept a single float as its arguments.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        ...

class RangeSlider(SliderBase):
    """
    A slider representing a range of floating point values. Defines the min and
    max of the range via the *val* attribute as a tuple of (min, max).

    Create a slider that defines a range contained within [*valmin*, *valmax*]
    in Axes *ax*. For the slider to remain responsive you must maintain a
    reference to it. Call :meth:`on_changed` to connect to the slider event.

    Attributes
    ----------
    val : tuple of float
        Slider value.
    """

    val: tuple[float, ...]

    def __init__(
        self,
        ax: Axes,
        label: str,
        valmin: float,
        valmax: float,
        valinit: Sequence[float] | None = None,
        valfmt: str | None = None,
        closedmin: bool = True,
        closedmax: bool = True,
        dragging: bool = True,
        valstep: float | None = None,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        track_color: Color = "lightgrey",
        handle_style: dict = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        ax : Axes
            The Axes to put the slider in.

        label : str
            Slider label.

        valmin : float
            The minimum value of the slider.

        valmax : float
            The maximum value of the slider.

        valinit : tuple of float or None, default: None
            The initial positions of the slider. If None the initial positions
            will be at the 25th and 75th percentiles of the range.

        valfmt : str, default: None
            %-format string used to format the slider values.  If None, a
            `.ScalarFormatter` is used instead.

        closedmin : bool, default: True
            Whether the slider interval is closed on the bottom.

        closedmax : bool, default: True
            Whether the slider interval is closed on the top.

        dragging : bool, default: True
            If True the slider can be dragged by the mouse.

        valstep : float, default: None
            If given, the slider will snap to multiples of *valstep*.

        orientation : {'horizontal', 'vertical'}, default: 'horizontal'
            The orientation of the slider.

        track_color : color, default: 'lightgrey'
            The color of the background track. The track is accessible for
            further styling via the *track* attribute.

        handle_style : dict
            Properties of the slider handles. Default values are

            ========= ===== ======= =========================================
            Key       Value Default Description
            ========= ===== ======= =========================================
            facecolor color 'white' The facecolor of the slider handles.
            edgecolor color '.75'   The edgecolor of the slider handles.
            size      int   10      The size of the slider handles in points.
            ========= ===== ======= =========================================

            Other values will be transformed as marker{foo} and passed to the
            `~.Line2D` constructor. e.g. ``handle_style = {'style'='x'}`` will
            result in ``markerstyle = 'x'``.

        Notes
        -----
        Additional kwargs are passed on to ``self.poly`` which is the
        `~Polygon` that draws the slider knob.  See the
        `.Polygon` documentation for valid property names (``facecolor``,
        ``edgecolor``, ``alpha``, etc.).
        """
        ...
    def set_min(self, min: float):
        """
        Set the lower value of the slider to *min*.

        Parameters
        ----------
        min : float
        """
        ...
    def set_max(self, max: float):
        """
        Set the lower value of the slider to *max*.

        Parameters
        ----------
        max : float
        """
        ...
    def set_val(self, val: Sequence[float]):
        """
        Set slider value to *val*.

        Parameters
        ----------
        val : tuple or array-like of float
        """
        ...
    def on_changed(self, func: Callable) -> int:
        """
        Connect *func* as callback function to changes of the slider value.

        Parameters
        ----------
        func : callable
            Function to call when slider is changed. The function
            must accept a numpy array with shape (2,) as its argument.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        ...

class CheckButtons(AxesWidget):
    r"""
    A GUI neutral set of check buttons.

    For the check buttons to remain responsive you must keep a
    reference to this object.

    Connect to the CheckButtons with the `.on_clicked` method.

    Attributes
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    labels : list of `.Text`

    rectangles : list of `.Rectangle`

    lines : list of (`.Line2D`, `.Line2D`) pairs
        List of lines for the x's in the check boxes.  These lines exist for
        each box, but have ``set_visible(False)`` when its box is not checked.
    """
    def __init__(
        self, ax: Axes, labels: Sequence[str], actives: Sequence[bool] = ...
    ) -> None:
        """
        Add check buttons to `Axes` instance *ax*.

        Parameters
        ----------
        ax : `~Axes`
            The parent Axes for the widget.

        labels : list of str
            The labels of the check buttons.

        actives : list of bool, optional
            The initial check states of the buttons. The list must have the
            same length as *labels*. If not given, all buttons are unchecked.
        """
        ...
    def set_active(self, index: int):
        """
        Toggle (activate or deactivate) a check button by index.

        Callbacks will be triggered if :attr:`eventson` is True.

        Parameters
        ----------
        index : int
            Index of the check button to toggle.

        Raises
        ------
        ValueError
            If *index* is invalid.
        """
        ...
    def get_status(self) -> tuple[bool, ...]:
        """
        Return a tuple of the status (True/False) of all of the check buttons.
        """
        ...
    def on_clicked(self, func: Callable) -> int:
        """
        Connect the callback function *func* to button click events.

        Returns a connection id, which can be used to disconnect the callback.
        """
        ...
    def disconnect(self, cid) -> None:
        """Remove the observer with connection id *cid*."""
        ...

class TextBox(AxesWidget):
    """
    A GUI neutral text input box.

    For the text box to remain responsive you must keep a reference to it.

    Call `.on_text_change` to be updated whenever the text changes.

    Call `.on_submit` to be updated whenever the user hits enter or
    leaves the text entry field.

    Attributes
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    label : `.Text`

    color : color
        The color of the text box when not hovering.
    hovercolor : color
        The color of the text box when hovering.
    """

    DIST_FROM_LEFT = ...
    def __init__(
        self,
        ax: Axes,
        label: str,
        initial: str = ...,
        color: Color = ...,
        hovercolor: Color = ...,
        label_pad: float = ...,
        textalignment: Literal["left", "center", "right"] = ...,
    ) -> None:
        """
        Parameters
        ----------
        ax : `~Axes`
            The `~.axes.Axes` instance the button will be placed into.
        label : str
            Label for this text box.
        initial : str
            Initial value in the text box.
        color : color
            The color of the box.
        hovercolor : color
            The color of the box when the mouse is over it.
        label_pad : float
            The distance between the label and the right side of the textbox.
        textalignment : {'left', 'center', 'right'}
            The horizontal location of the text.
        """
        ...
    @property
    def text(self) -> str: ...
    def set_val(self, val: str) -> None: ...
    def begin_typing(self, x): ...
    def stop_typing(self) -> None: ...
    def position_cursor(self, x: float): ...
    def on_text_change(self, func: Callable):
        """
        When the text changes, call this *func* with event.

        A connection id is returned which can be used to disconnect.
        """
        ...
    def on_submit(self, func: Callable) -> int:
        """
        When the user hits enter or leaves the submission box, call this
        *func* with event.

        A connection id is returned which can be used to disconnect.
        """
        ...
    def disconnect(self, cid):
        """Remove the observer with connection id *cid*."""
        ...

class RadioButtons(AxesWidget):
    """
    A GUI neutral radio button.

    For the buttons to remain responsive you must keep a reference to this
    object.

    Connect to the RadioButtons with the `.on_clicked` method.

    Attributes
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    activecolor : color
        The color of the selected button.
    labels : list of `.Text`
        The button labels.
    circles : list of `~.patches.Circle`
        The buttons.
    value_selected : str
        The label text of the currently selected button.
    """

    ax: Axes
    activecolor: Color
    labels: list[Text]
    circles: list[Circle]
    value_selected: str

    def __init__(
        self,
        ax: Axes,
        labels: Sequence[Text],
        active: int = ...,
        activecolor: Color = ...,
    ) -> None:
        """
        Add radio buttons to an `~.axes.Axes`.

        Parameters
        ----------
        ax : `~Axes`
            The Axes to add the buttons to.
        labels : list of str
            The button labels.
        active : int
            The index of the initially selected button.
        activecolor : color
            The color of the selected button.
        """
        ...
    def set_active(self, index: int):
        """
        Select button with number *index*.

        Callbacks will be triggered if :attr:`eventson` is True.
        """
        ...
    def on_clicked(self, func: Callable) -> int:
        """
        Connect the callback function *func* to button click events.

        Returns a connection id, which can be used to disconnect the callback.
        """
        ...
    def disconnect(self, cid):
        """Remove the observer with connection id *cid*."""
        ...

class SubplotTool(Widget):
    """
    A tool to adjust the subplot params of a `Figure`.
    """

    def __init__(self, targetfig: Figure, toolfig: Figure) -> None:
        """
        Parameters
        ----------
        targetfig : `.Figure`
            The figure instance to adjust.
        toolfig : `.Figure`
            The figure instance to embed the subplot tool into.
        """
        ...

class Cursor(AxesWidget):
    """
    A crosshair cursor that spans the Axes and moves with mouse cursor.

    For the cursor to remain responsive you must keep a reference to it.

    Parameters
    ----------
    ax : `Axes`
        The `~.axes.Axes` to attach the cursor to.
    horizOn : bool, default: True
        Whether to draw the horizontal line.
    vertOn : bool, default: True
        Whether to draw the vertical line.
    useblit : bool, default: False
        Use blitting for faster drawing if supported by the backend.
        See the tutorial :doc:`/tutorials/advanced/blitting` for details.

    Other Parameters
    ----------------
    **lineprops
        `.Line2D` properties that control the appearance of the lines.
        See also `~.Axes.axhline`.

    Examples
    --------
    See :doc:`/gallery/widgets/cursor`.
    """

    def __init__(
        self,
        ax: Axes,
        horizOn: bool = True,
        vertOn: bool = True,
        useblit: bool = False,
        **lineprops
    ) -> None: ...
    def clear(self, event: DrawEvent) -> None:
        """Internal event handler to clear the cursor."""
        ...
    def onmove(self, event: Event):
        """Internal event handler to draw the cursor when the mouse moves."""
        ...

class MultiCursor(Widget):
    """
    Provide a vertical (default) and/or horizontal line cursor shared between
    multiple Axes.

    For the cursor to remain responsive you must keep a reference to it.

    Parameters
    ----------
    canvas : `FigureCanvasBase`
        The FigureCanvas that contains all the Axes.

    axes : list of `Axes`
        The `~.axes.Axes` to attach the cursor to.

    useblit : bool, default: True
        Use blitting for faster drawing if supported by the backend.
        See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.

    horizOn : bool, default: False
        Whether to draw the horizontal line.

    vertOn : bool, default: True
        Whether to draw the vertical line.

    Other Parameters
    ----------------
    **lineprops
        `.Line2D` properties that control the appearance of the lines.
        See also `~.Axes.axhline`.

    Examples
    --------
    See :doc:`/gallery/widgets/multicursor`.
    """

    def __init__(
        self,
        canvas: FigureCanvasBase,
        axes: Sequence[Axes],
        useblit: bool = True,
        horizOn: bool = False,
        vertOn: bool = True,
        **lineprops
    ) -> None: ...
    def connect(self) -> None:
        """Connect events."""
        ...
    def disconnect(self):
        """Disconnect events."""
        ...
    def clear(self, event: DrawEvent) -> None:
        """Clear the cursor."""
        ...
    def onmove(self, event: Event): ...

class _SelectorWidget(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        useblit: bool = ...,
        button=...,
        state_modifier_keys=...,
        use_data_coordinates=...,
    ) -> None: ...

    eventpress = ...
    eventrelease = ...
    state = ...
    state_modifier_keys = ...
    def set_active(self, active): ...
    def update_background(self, event: DrawEvent) -> None:
        """Force an update of the background."""
        ...
    def connect_default_events(self) -> None:
        """Connect the major canvas events to methods."""
        ...
    def ignore(self, event: Event): ...
    def update(self) -> bool:
        """Draw using blit() or draw_idle(), depending on ``self.useblit``."""
        ...
    def press(self, event: Event):
        """Button press handler and validator."""
        ...
    def release(self, event: Event):
        """Button release event handler and validator."""
        ...
    def onmove(self, event: Event):
        """Cursor move event handler and validator."""
        ...
    def on_scroll(self, event: Event):
        """Mouse scroll event handler and validator."""
        ...
    def on_key_press(self, event: KeyEvent) -> None:
        """Key press event handler and validator for all selection widgets."""
        ...
    def on_key_release(self, event: Event):
        """Key release event handler and validator."""
        ...
    def set_visible(self, visible: bool) -> None:
        """Set the visibility of our artists."""
        ...
    def clear(self):
        """Clear the selection and set the selector ready to make a new one."""
        ...
    @property
    def artists(
        self,
    ) -> tuple[Artist, ...]:
        """Tuple of the artists of the selector."""
        ...
    def set_props(self, **props):
        """
        Set the properties of the selector artist. See the `props` argument
        in the selector docstring to know which properties are supported.
        """
        ...
    def set_handle_props(self, **handle_props):
        """
        Set the properties of the handles selector artist. See the
        `handle_props` argument in the selector docstring to know which
        properties are supported.
        """
        ...
    def add_state(self, state: str):
        """
        Add a state to define the widget's behavior. See the
        `state_modifier_keys` parameters for details.

        Parameters
        ----------
        state : str
            Must be a supported state of the selector. See the
            `state_modifier_keys` parameters for details.

        Raises
        ------
        ValueError
            When the state is not supported by the selector.

        """
        ...
    def remove_state(self, state: str):
        """
        Remove a state to define the widget's behavior. See the
        `state_modifier_keys` parameters for details.

        Parameters
        ----------
        value : str
            Must be a supported state of the selector. See the
            `state_modifier_keys` parameters for details.

        Raises
        ------
        ValueError
            When the state is not supported by the selector.

        """
        ...

class SpanSelector(_SelectorWidget):
    """
    Visually select a min/max range on a single axis and call a function with
    those values.

    To guarantee that the selector remains responsive, keep a reference to it.

    In order to turn off the SpanSelector, set ``span_selector.active`` to
    False.  To turn it back on, set it to True.

    Press and release events triggered at the same coordinates outside the
    selection will clear the selector, except when
    ``ignore_event_outside=True``.

    Parameters
    ----------
    ax : `Axes`

    onselect : callable
        A callback function that is called after a release event and the
        selection is created, changed or removed.
        It must have the signature::

            def on_select(min: float, max: float) -> Any

    direction : {"horizontal", "vertical"}
        The direction along which to draw the span selector.

    minspan : float, default: 0
        If selection is less than or equal to *minspan*, the selection is
        removed (when already existing) or cancelled.

    useblit : bool, default: False
        If True, use the backend-dependent blitting features for faster
        canvas updates. See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.

    props : dict, optional
        Dictionary of `Patch` properties.
        Default:

            ``dict(facecolor='red', alpha=0.5)``

    onmove_callback : func(min, max), min/max are floats, default: None
        Called on mouse move while the span is being selected.

    span_stays : bool, default: False
        If True, the span stays visible after the mouse is released.
        Deprecated, use *interactive* instead.

    interactive : bool, default: False
        Whether to draw a set of handles that allow interaction with the
        widget after it is drawn.

    button : `.MouseButton` or list of `.MouseButton`, default: all buttons
        The mouse buttons which activate the span selector.

    handle_props : dict, default: None
        Properties of the handle lines at the edges of the span. Only used
        when *interactive* is True. See `Line2D` for valid
        properties.

    grab_range : float, default: 10
        Distance in pixels within which the interactive tool handles can be
        activated.

    state_modifier_keys : dict, optional
        Keyboard modifiers which affect the widget's behavior.  Values
        amend the defaults, which are:

        - "clear": Clear the current shape, default: "escape".

    drag_from_anywhere : bool, default: False
        If `True`, the widget can be moved by clicking anywhere within
        its bounds.

    ignore_event_outside : bool, default: False
        If `True`, the event triggered outside the span selector will be
        ignored.

    snap_values : 1D array-like, optional
        Snap the selector edges to the given values.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import matplotlib.widgets as mwidgets
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [10, 50, 100])
    >>> def onselect(vmin, vmax):
    ...     print(vmin, vmax)
    >>> span = mwidgets.SpanSelector(ax, onselect, 'horizontal',
    ...                              props=dict(facecolor='blue', alpha=0.5))
    >>> fig.show()

    See also: :doc:`/gallery/widgets/span_selector`
    """

    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        direction: Literal["horizontal", "vertical"],
        minspan: float = 0,
        useblit: bool = False,
        props: dict = ...,
        onmove_callback: Callable = ...,
        interactive: bool = False,
        button: MouseButton | Sequence[MouseButton] = ...,
        handle_props: dict = ...,
        grab_range: float = 10,
        state_modifier_keys: dict = ...,
        drag_from_anywhere: bool = False,
        ignore_event_outside: bool = False,
        snap_values: ArrayLike = ...,
    ) -> None: ...

    rect = ...
    rectprops = ...
    active_handle = ...
    pressv = ...
    span_stays = ...
    prev = ...
    def new_axes(self, ax: Axes):
        """Set SpanSelector to operate on a new Axes."""
        ...
    def connect_default_events(self) -> None: ...
    @property
    def direction(self):
        """Direction of the span selector: 'vertical' or 'horizontal'."""
        ...
    @direction.setter
    def direction(self, direction):
        """Set the direction of the span selector."""
        ...
    @property
    def extents(self):
        """Return extents of the span selector."""
        ...
    @extents.setter
    def extents(self, extents): ...

class ToolLineHandles:
    """
    Control handles for canvas tools.

    Parameters
    ----------
    ax : `Axes`
        Matplotlib Axes where tool handles are displayed.
    positions : 1D array
        Positions of handles in data coordinates.
    direction : {"horizontal", "vertical"}
        Direction of handles, either 'vertical' or 'horizontal'
    line_props : dict, optional
        Additional line properties. See `Line2D`.
    useblit : bool, default: True
        Whether to use blitting for faster drawing (if supported by the
        backend). See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.
    """

    def __init__(
        self,
        ax: Axes,
        positions: ArrayLike,
        direction: Literal["horizontal", "vertical"],
        line_props: dict = ...,
        useblit: bool = True,
    ) -> None: ...
    @property
    def artists(self) -> tuple[Line2D, Line2D]: ...
    @property
    def positions(self):
        """Positions of the handle in data coordinates."""
        ...
    @property
    def direction(self) -> str:
        """Direction of the handle: 'vertical' or 'horizontal'."""
        ...
    def set_data(self, positions: tuple):
        """
        Set x or y positions of handles, depending if the lines are vertical
        of horizontal.

        Parameters
        ----------
        positions : tuple of length 2
            Set the positions of the handle in data coordinates
        """
        ...
    def set_visible(self, value):
        """Set the visibility state of the handles artist."""
        ...
    def set_animated(self, value):
        """Set the animated state of the handles artist."""
        ...
    def remove(self):
        """Remove the handles artist from the figure."""
        ...
    def closest(self, x: float, y: float) -> tuple[int, float]:
        """
        Return index and pixel distance to closest handle.

        Parameters
        ----------
        x, y : float
            x, y position from which the distance will be calculated to
            determinate the closest handle

        Returns
        -------
        index, distance : index of the handle and its distance from
            position x, y
        """
        ...

class ToolHandles:
    """
    Control handles for canvas tools.

    Parameters
    ----------
    ax : `Axes`
        Matplotlib Axes where tool handles are displayed.
    x, y : 1D arrays
        Coordinates of control handles.
    marker : str, default: 'o'
        Shape of marker used to display handle. See `matplotlib.pyplot.plot`.
    marker_props : dict, optional
        Additional marker properties. See `Line2D`.
    useblit : bool, default: True
        Whether to use blitting for faster drawing (if supported by the
        backend). See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.
    """

    def __init__(
        self,
        ax: Axes,
        x: ArrayLike,
        y: ArrayLike,
        marker: str = "o",
        marker_props: dict = ...,
        useblit: bool = True,
    ) -> None: ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def artists(self) -> tuple[Line2D, ...]: ...
    def set_data(self, pts: Sequence[float], y: Sequence[float] = ...) -> None:
        """Set x and y positions of handles."""
        ...
    def set_visible(self, val): ...
    def set_animated(self, val): ...
    def closest(self, x: float, y: float) -> tuple[int, float]:
        """Return index and pixel distance to closest index."""
        ...

class RectangleSelector(_SelectorWidget):
    """
    Select a rectangular region of an Axes.

    For the cursor to remain responsive you must keep a reference to it.

    Press and release events triggered at the same coordinates outside the
    selection will clear the selector, except when
    ``ignore_event_outside=True``.

    %s

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import matplotlib.widgets as mwidgets
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [10, 50, 100])
    >>> def onselect(eclick, erelease):
    ...     print(eclick.xdata, eclick.ydata)
    ...     print(erelease.xdata, erelease.ydata)
    >>> props = dict(facecolor='blue', alpha=0.5)
    >>> rect = mwidgets.RectangleSelector(ax, onselect, interactive=True,
                                          props=props)
    >>> fig.show()

    >>> selector.add_state('square')

    See also: :doc:`/gallery/widgets/rectangle_selector`
    """

    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        drawtype=...,
        minspanx=...,
        minspany=...,
        useblit=...,
        lineprops=...,
        props=...,
        spancoords=...,
        button=...,
        grab_range=...,
        handle_props=...,
        interactive=...,
        state_modifier_keys=...,
        drag_from_anywhere=...,
        ignore_event_outside=...,
        use_data_coordinates=...,
    ) -> None: ...

    to_draw = ...
    drawtype = ...
    active_handle = ...
    interactive = ...
    maxdist = ...
    @property
    def corners(self):
        """
        Corners of rectangle in data coordinates from lower left,
        moving clockwise.
        """
        ...
    @property
    def edge_centers(self):
        """
        Midpoint of rectangle edges in data coordinates from left,
        moving anti-clockwise.
        """
        ...
    @property
    def center(self) -> tuple[float, float]:
        """Center of rectangle in data coordinates."""
        ...
    @property
    def extents(self):
        """
        Return (xmin, xmax, ymin, ymax) in data coordinates as defined by the
        bounding box before rotation.
        """
        ...
    @extents.setter
    def extents(self, extents): ...
    @property
    def rotation(self) -> float:
        """
        Rotation in degree in interval [-45°, 45°]. The rotation is limited in
        range to keep the implementation simple.
        """
        ...
    @rotation.setter
    def rotation(self, value: float): ...

    draw_shape = ...
    @property
    def geometry(self) -> np.ndarray:
        """
        Return an array of shape (2, 5) containing the
        x (``RectangleSelector.geometry[1, :]``) and
        y (``RectangleSelector.geometry[0, :]``) data coordinates of the four
        corners of the rectangle starting and ending in the top left corner.
        """
        ...

class EllipseSelector(RectangleSelector):
    """
    Select an elliptical region of an Axes.

    For the cursor to remain responsive you must keep a reference to it.

    Press and release events triggered at the same coordinates outside the
    selection will clear the selector, except when
    ``ignore_event_outside=True``.

    %s

    Examples
    --------
    :doc:`/gallery/widgets/rectangle_selector`
    """

    draw_shape = ...

class LassoSelector(_SelectorWidget):
    """
    Selection curve of an arbitrary shape.

    For the selector to remain responsive you must keep a reference to it.

    The selected path can be used in conjunction with `~.Path.contains_point`
    to select data points from an image.

    In contrast to `Lasso`, `LassoSelector` is written with an interface
    similar to `RectangleSelector` and `SpanSelector`, and will continue to
    interact with the Axes until disconnected.

    Example usage::

        ax = plt.subplot()
        ax.plot(x, y)

        def onselect(verts):
            print(verts)
        lasso = LassoSelector(ax, onselect)

    Parameters
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    onselect : function
        Whenever the lasso is released, the *onselect* function is called and
        passed the vertices of the selected path.
    useblit : bool, default: True
        Whether to use blitting for faster drawing (if supported by the
        backend). See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.
    props : dict, optional
        Properties with which the line is drawn, see `Line2D`
        for valid properties. Default values are defined in ``mpl.rcParams``.
    button : `.MouseButton` or list of `.MouseButton`, optional
        The mouse buttons used for rectangle selection.  Default is ``None``,
        which corresponds to all buttons.
    """

    def __init__(
        self,
        ax: Axes,
        onselect: Callable = ...,
        useblit: bool = True,
        props: dict = ...,
        button: MouseButton | Sequence[MouseButton] = ...,
    ) -> None: ...
    def onpress(self, event): ...
    def onrelease(self, event): ...

class PolygonSelector(_SelectorWidget):
    """
    Select a polygon region of an Axes.

    Place vertices with each mouse click, and make the selection by completing
    the polygon (clicking on the first vertex). Once drawn individual vertices
    can be moved by clicking and dragging with the left mouse button, or
    removed by clicking the right mouse button.

    In addition, the following modifier keys can be used:

    - Hold *ctrl* and click and drag a vertex to reposition it before the
      polygon has been completed.
    - Hold the *shift* key and click and drag anywhere in the Axes to move
      all vertices.
    - Press the *esc* key to start a new polygon.

    For the selector to remain responsive you must keep a reference to it.

    Parameters
    ----------
    ax : `~Axes`
        The parent Axes for the widget.

    onselect : function
        When a polygon is completed or modified after completion,
        the *onselect* function is called and passed a list of the vertices as
        ``(xdata, ydata)`` tuples.

    useblit : bool, default: False
        Whether to use blitting for faster drawing (if supported by the
        backend). See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.

    props : dict, optional
        Properties with which the line is drawn, see `Line2D`
        for valid properties.
        Default:

            ``dict(color='k', linestyle='-', linewidth=2, alpha=0.5)``

    handle_props : dict, optional
        Artist properties for the markers drawn at the vertices of the polygon.
        See the marker arguments in `Line2D` for valid
        properties.  Default values are defined in ``mpl.rcParams`` except for
        the default value of ``markeredgecolor`` which will be the same as the
        ``color`` property in *props*.

    grab_range : float, default: 10
        A vertex is selected (to complete the polygon or to move a vertex) if
        the mouse click is within *grab_range* pixels of the vertex.

    draw_bounding_box : bool, optional
        If `True`, a bounding box will be drawn around the polygon selector
        once it is complete. This box can be used to move and resize the
        selector.

    box_handle_props : dict, optional
        Properties to set for the box handles. See the documentation for the
        *handle_props* argument to `RectangleSelector` for more info.

    box_props : dict, optional
        Properties to set for the box. See the documentation for the *props*
        argument to `RectangleSelector` for more info.

    Examples
    --------
    :doc:`/gallery/widgets/polygon_selector_simple`
    :doc:`/gallery/widgets/polygon_selector_demo`

    Notes
    -----
    If only one point remains after removing points, the selector reverts to an
    incomplete state and you can start drawing a new polygon from the existing
    point.
    """

    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        useblit: bool = True,
        props: dict = ...,
        handle_props: dict = ...,
        grab_range: float = 10,
        *,
        draw_bounding_box: bool = ...,
        box_handle_props: dict = ...,
        box_props: dict = ...
    ) -> None: ...

    line = ...
    vertex_select_radius = ...
    def onmove(self, event: Event):
        """Cursor move event handler and validator."""
        ...
    @property
    def verts(self):
        """The polygon vertices, as a list of ``(x, y)`` pairs."""
        ...
    @verts.setter
    def verts(self, xys):
        """
        Set the polygon vertices.

        This will remove any preexisting vertices, creating a complete polygon
        with the new vertices.
        """
        ...

class Lasso(AxesWidget):
    """
    Selection curve of an arbitrary shape.

    The selected path can be used in conjunction with
    `~Path.contains_point` to select data points from an image.

    Unlike `LassoSelector`, this must be initialized with a starting
    point *xy*, and the `Lasso` events are destroyed upon release.

    Parameters
    ----------
    ax : `~Axes`
        The parent Axes for the widget.
    xy : (float, float)
        Coordinates of the start of the lasso.
    useblit : bool, default: True
        Whether to use blitting for faster drawing (if supported by the
        backend). See the tutorial :doc:`/tutorials/advanced/blitting`
        for details.
    callback : callable
        Whenever the lasso is released, the *callback* function is called and
        passed the vertices of the selected path.
    """

    def __init__(
        self,
        ax: Axes,
        xy: Sequence[float],
        callback: Callable = ...,
        useblit: bool = True,
    ) -> None: ...
    def onrelease(self, event: MouseEvent) -> None: ...
    def onmove(self, event: MouseEvent) -> None: ...
