from matplotlib.widgets import Cursor
from typing import Any
from .backend_bases import Event, MouseEvent, ToolContainerBase
from .figure import Figure
from .axes import Axes
from .backend_managers import ToolManager

import enum

class Cursors(enum.IntEnum):
    """Backend-independent cursor types."""

    POINTER = 1
    HAND = 2
    SELECT_REGION = 3
    MOVE = 4
    WAIT = 5
    RESIZE_HORIZONTAL = 6
    RESIZE_VERTICAL = 7

cursors = Cursors

class ToolBase:
    """
    Base tool class.

    A base tool, only implements `trigger` method or no method at all.
    The tool is instantiated by `matplotlib.backend_managers.ToolManager`.
    """

    default_keymap = ...
    description = ...
    image = ...
    def __init__(self, toolmanager: ToolManager, name: str) -> None: ...

    name = ...
    toolmanager = ...
    canvas = ...
    @property
    def figure(self):
        """The Figure affected by this tool, or None."""
        ...
    @figure.setter
    def figure(self, figure): ...

    set_figure = ...
    def trigger(self, sender: object, event: Event, data: object = ...):
        """
        Called when this tool gets used.

        This method is called by `.ToolManager.trigger_tool`.

        Parameters
        ----------
        event : `.Event`
            The canvas event that caused this tool to be called.
        sender : object
            Object that requested the tool to be triggered.
        data : object
            Extra data.
        """
        ...
    def destroy(self) -> None:
        """
        Destroy the tool.

        This method is called by `.ToolManager.remove_tool`.
        """
        ...

class ToolToggleBase(ToolBase):
    """
    Toggleable tool.

    Every time it is triggered, it switches between enable and disable.

    Parameters
    ----------
    ``*args``
        Variable length argument to be used by the Tool.
    ``**kwargs``
        `toggled` if present and True, sets the initial state of the Tool
        Arbitrary keyword arguments to be consumed by the Tool
    """

    radio_group = ...
    cursor = ...
    default_toggled = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def trigger(self, sender, event, data=...) -> None:
        """Calls `enable` or `disable` based on `toggled` value."""
        ...
    def enable(self, event=...) -> None:
        """
        Enable the toggle tool.

        `trigger` calls this method when `toggled` is False.
        """
        ...
    def disable(self, event=...) -> None:
        """
        Disable the toggle tool.

        `trigger` call this method when `toggled` is True.

        This can happen in different circumstances.

        * Click on the toolbar tool button.
        * Call to `matplotlib.backend_managers.ToolManager.trigger_tool`.
        * Another `ToolToggleBase` derived tool is triggered
          (from the same `.ToolManager`).
        """
        ...
    @property
    def toggled(self) -> bool:
        """State of the toggled tool."""
        ...
    def set_figure(self, figure): ...

class SetCursorBase(ToolBase):
    """
    Change to the current cursor while inaxes.

    This tool, keeps track of all `ToolToggleBase` derived tools, and calls
    `set_cursor` when a tool gets triggered.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure: Figure) -> None: ...
    def set_cursor(self, cursor: Cursor) -> None:
        """
        Set the cursor.
        """
        ...

ToolSetCursor = SetCursorBase

class ToolCursorPosition(ToolBase):
    """
    Send message with the current pointer position.

    This tool runs in the background reporting the position of the cursor.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure: Figure): ...
    def send_message(self, event: MouseEvent) -> None:
        """Call `matplotlib.backend_managers.ToolManager.message_event`."""
        ...

class RubberbandBase(ToolBase):
    """Draw and remove a rubberband."""

    def trigger(self, sender, event: Event, data):
        """Call `draw_rubberband` or `remove_rubberband` based on data."""
        ...
    def draw_rubberband(self, *data):
        """
        Draw rubberband.

        This method must get implemented per backend.
        """
        ...
    def remove_rubberband(self):
        """
        Remove rubberband.

        This method should get implemented per backend.
        """
        ...

class ToolQuit(ToolBase):
    """Tool to call the figure manager destroy method."""

    description = ...
    default_keymap = ...
    def trigger(self, sender: object, event: Event, data: object = ...): ...

class ToolQuitAll(ToolBase):
    """Tool to call the figure manager destroy method."""

    description = ...
    default_keymap = ...
    def trigger(self, sender: object, event: Event, data: object = ...) -> None: ...

class ToolGrid(ToolBase):
    """Tool to toggle the major grids of the figure."""

    description = ...
    default_keymap = ...
    def trigger(self, sender: object, event: Event, data: object = ...) -> None: ...

class ToolMinorGrid(ToolBase):
    """Tool to toggle the major and minor grids of the figure."""

    description = ...
    default_keymap = ...
    def trigger(self, sender: object, event: Event, data: object = ...) -> None: ...

class ToolFullScreen(ToolBase):
    """Tool to toggle full screen."""

    description = ...
    default_keymap = ...
    def trigger(self, sender: object, event: Event, data: object = ...) -> None: ...

class AxisScaleBase(ToolToggleBase):
    """Base Tool to toggle between linear and logarithmic."""

    def trigger(self, sender, event: Event, data=...) -> None: ...
    def enable(self, event: Event) -> None: ...
    def disable(self, event: Event) -> None: ...

class ToolYScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the Y axis."""

    description = ...
    default_keymap = ...
    def set_scale(self, ax, scale) -> None: ...

class ToolXScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the X axis."""

    description = ...
    default_keymap = ...
    def set_scale(self, ax: Axes, scale): ...

class ToolViewsPositions(ToolBase):
    """
    Auxiliary Tool to handle changes in views and positions.

    Runs in the background and should get used by all the tools that
    need to access the figure's history of views and positions, e.g.

    * `ToolZoom`
    * `ToolPan`
    * `ToolHome`
    * `ToolBack`
    * `ToolForward`
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def add_figure(self, figure: Figure) -> None:
        """Add the current figure to the stack of views and positions."""
        ...
    def clear(self, figure: Figure) -> None:
        """Reset the axes stack."""
        ...
    def update_view(self) -> None:
        """
        Update the view limits and position for each axes from the current
        stack position. If any axes are present in the figure that aren't in
        the current stack position, use the home view limits for those axes and
        don't update *any* positions.
        """
        ...
    def push_current(self, figure: Figure = ...) -> None:
        """
        Push the current view limits and position onto their respective stacks.
        """
        ...
    def update_home_views(self, figur: Figure = ...) -> None:
        """
        Make sure that ``self.home_views`` has an entry for all axes present
        in the figure.
        """
        ...
    def home(self) -> None:
        """Recall the first view and position from the stack."""
        ...
    def back(self) -> None:
        """Back one step in the stack of views and positions."""
        ...
    def forward(self) -> None:
        """Forward one step in the stack of views and positions."""
        ...

class ViewsPositionsBase(ToolBase):
    """Base class for `ToolHome`, `ToolBack` and `ToolForward`."""

    def trigger(self, sender: object, event: Event, data: object = ...): ...

class ToolHome(ViewsPositionsBase):
    """Restore the original view limits."""

    description = ...
    image = ...
    default_keymap = ...

class ToolBack(ViewsPositionsBase):
    """Move back up the view limits stack."""

    description = ...
    image = ...
    default_keymap = ...

class ToolForward(ViewsPositionsBase):
    """Move forward in the view lim stack."""

    description = ...
    image = ...
    default_keymap = ...

class ConfigureSubplotsBase(ToolBase):
    """Base tool for the configuration of subplots."""

    description = ...
    image = ...

class SaveFigureBase(ToolBase):
    """Base tool for figure saving."""

    description = ...
    image = ...
    default_keymap = ...

class ZoomPanBase(ToolToggleBase):
    """Base class for `ToolZoom` and `ToolPan`."""

    def __init__(self, *args) -> None: ...
    def enable(self, event: Event) -> None:
        """Connect press/release events and lock the canvas."""
        ...
    def disable(self, event: Event) -> None:
        """Release the canvas and disconnect press/release events."""
        ...
    def trigger(self, sender, event: Event, data=...) -> None: ...
    def scroll_zoom(self, event: Event) -> None: ...

class ToolZoom(ZoomPanBase):
    """A Tool for zooming using a rectangle selector."""

    description = ...
    image = ...
    default_keymap = ...
    cursor = ...
    radio_group = ...
    def __init__(self, *args) -> None: ...

class ToolPan(ZoomPanBase):
    """Pan axes with left mouse, zoom with right."""

    default_keymap = ...
    description = ...
    image = ...
    cursor = ...
    radio_group = ...
    def __init__(self, *args) -> None: ...

class ToolHelpBase(ToolBase):
    description = ...
    default_keymap = ...
    image = ...
    @staticmethod
    def format_shortcut(key_sequence) -> None:
        """
        Convert a shortcut string from the notation used in rc config to the
        standard notation for displaying shortcuts, e.g. 'ctrl+a' -> 'Ctrl+A'.
        """
        ...

class ToolCopyToClipboardBase(ToolBase):
    """Tool to copy the figure to the clipboard."""

    description = ...
    default_keymap = ...
    def trigger(self, *args, **kwargs) -> None: ...

default_tools = ...
default_toolbar_tools = ...

def add_tools_to_manager(toolmanager: ToolManager, tools: dict[str, Any] = ...) -> None:
    """
    Add multiple tools to a `.ToolManager`.

    Parameters
    ----------
    toolmanager : `.backend_managers.ToolManager`
        Manager to which the tools are added.
    tools : {str: class_like}, optional
        The tools to add in a {name: tool} dict, see
        `.backend_managers.ToolManager.add_tool` for more info.
    """
    ...

def add_tools_to_container(container: ToolContainerBase, tools: list = ...) -> None:
    """
    Add multiple tools to the container.

    Parameters
    ----------
    container : Container
        `.backend_bases.ToolContainerBase` object that will get the tools
        added.
    tools : list, optional
        List in the form ``[[group1, [tool1, tool2 ...]], [group2, [...]]]``
        where the tools ``[tool1, tool2, ...]`` will display in group1.
        See `.backend_bases.ToolContainerBase.add_tool` for details.
    """
    ...
