from matplotlib.widgets import LockDraw
from typing import Callable
from .backend_tools import ToolBase
from .figure import Figure
from .backend_bases import Event, FigureCanvasBase

class ToolEvent:
    def __init__(self, name: str, sender, tool, data=...) -> None: ...

class ToolTriggerEvent(ToolEvent):
    def __init__(self, name: str, sender, tool, canvasevent=..., data=...) -> None: ...

class ToolManagerMessageEvent:
    """
    Event carrying messages from toolmanager.

    Messages usually get displayed to the user by the toolbar.
    """

    def __init__(self, name: str, sender, message) -> None: ...

class ToolManager:
    """
    Manager for actions triggered by user interactions (key press, toolbar
    clicks, ...) on a Figure.

    Attributes
    ----------
    figure : `.Figure`
    keypresslock : `~matplotlib.widgets.LockDraw`
        `.LockDraw` object to know if the `canvas` key_press_event is locked.
    messagelock : `~matplotlib.widgets.LockDraw`
        `.LockDraw` object to know if the message is available to write.
    """

    keypresslock: LockDraw
    messagelock: LockDraw

    def __init__(self, figure=...) -> None: ...
    @property
    def canvas(self) -> FigureCanvasBase:
        """Canvas managed by FigureManager."""
        ...
    @property
    def figure(self) -> Figure:
        """Figure that holds the canvas."""
        ...
    @figure.setter
    def figure(self, figure): ...
    def set_figure(self, figure: Figure, update_tools: bool = ...):
        """
        Bind the given figure to the tools.

        Parameters
        ----------
        figure : `.Figure`
        update_tools : bool, default: True
            Force tools to update figure.
        """
        ...
    def toolmanager_connect(self, s: str, func: Callable) -> int:
        """
        Connect event with string *s* to *func*.

        Parameters
        ----------
        s : str
            The name of the event. The following events are recognized:

            - 'tool_message_event'
            - 'tool_removed_event'
            - 'tool_added_event'

            For every tool added a new event is created

            - 'tool_trigger_TOOLNAME', where TOOLNAME is the id of the tool.

        func : callable
            Callback function for the toolmanager event with signature::

                def func(event: ToolEvent) -> Any

        Returns
        -------
        cid
            The callback id for the connection. This can be used in
            `.toolmanager_disconnect`.
        """
        ...
    def toolmanager_disconnect(self, cid):
        """
        Disconnect callback id *cid*.

        Example usage::

            cid = toolmanager.toolmanager_connect('tool_trigger_zoom', onpress)
            #...later
            toolmanager.toolmanager_disconnect(cid)
        """
        ...
    def message_event(self, message, sender=...):
        """Emit a `ToolManagerMessageEvent`."""
        ...
    @property
    def active_toggle(self):
        """Currently toggled tools."""
        ...
    def get_tool_keymap(self, name: str) -> list[str]:
        """
        Return the keymap associated with the specified tool.

        Parameters
        ----------
        name : str
            Name of the Tool.

        Returns
        -------
        list of str
            List of keys associated with the tool.
        """
        ...
    def update_keymap(self, name: str, key: list[str] | str) -> None:
        """
        Set the keymap to associate with the specified tool.

        Parameters
        ----------
        name : str
            Name of the Tool.
        key : str or list of str
            Keys to associate with the tool.
        """
        ...
    def remove_tool(self, name: str) -> None:
        """
        Remove tool named *name*.

        Parameters
        ----------
        name : str
            Name of the tool.
        """
        ...
    def add_tool(self, name: str, tool: type, *args, **kwargs):
        """
        Add *tool* to `ToolManager`.

        If successful, adds a new event ``tool_trigger_{name}`` where
        ``{name}`` is the *name* of the tool; the event is fired every time the
        tool is triggered.

        Parameters
        ----------
        name : str
            Name of the tool, treated as the ID, has to be unique.
        tool : type
            Class of the tool to be added.  A subclass will be used
            instead if one was registered for the current canvas class.

        Notes
        -----
        args and kwargs get passed directly to the tools constructor.

        See Also
        --------
        ToolBase : The base class for tools.
        """
        ...
    def trigger_tool(
        self,
        name: str,
        sender: object = ...,
        canvasevent: Event = ...,
        data: object = ...,
    ):
        """
        Trigger a tool and emit the ``tool_trigger_{name}`` event.

        Parameters
        ----------
        name : str
            Name of the tool.
        sender : object
            Object that wishes to trigger the tool.
        canvasevent : Event
            Original Canvas event or None.
        data : object
            Extra data to pass to the tool when triggering.
        """
        ...
    @property
    def tools(self):
        """A dict mapping tool name -> controlled tool."""
        ...
    def get_tool(self, name: str | ToolBase, warn: bool = ...) -> tuple[ToolBase, None]:
        """
        Return the tool object with the given name.

        For convenience, this passes tool objects through.

        Parameters
        ----------
        name : str or `.ToolBase`
            Name of the tool, or the tool itself.
        warn : bool, default: True
            Whether a warning should be emitted it no tool with the given name
            exists.

        Returns
        -------
        `.ToolBase` or None
            The tool or None if no tool with the given name exists.
        """
        ...
