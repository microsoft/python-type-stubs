import datetime
from matplotlib.contour import QuadContourSet
import numpy as np
from typing import Callable, Literal, Sequence, overload
from matplotlib import rcParams as rcParams
from ._typing import *
from .tri.tricontour import TriContourSet
from .transforms import Bbox, Transform
from .text import Text, Annotation
from .container import BarContainer, ErrorbarContainer, StemContainer
from .patches import Polygon, FancyArrow
from .quiver import Quiver
from .colors import Colormap, Normalize
from .backend_bases import FigureCanvasBase, MouseButton, FigureManagerBase
from .collections import (
    LineCollection,
    Collection,
    QuadMesh,
    PathCollection,
    PolyCollection,
    BrokenBarHCollection,
)
from .lines import Line2D
from .legend import Legend
from .image import AxesImage, FigureImage
from .figure import Figure, SubFigure
from .scale import ScaleBase
from .backend_bases import _Backend
from .axes import Axes
from .artist import Artist
from .table import Table
from .widgets import SubplotTool
from .markers import MarkerStyle
from .streamplot import StreamplotSet

from array import array
import matplotlib
import matplotlib.image
from . import rcParams
from .rcsetup import interactive_bk as _interactive_bk

def install_repl_displayhook():
    """
    Connect to the display hook of the current shell.

    The display hook gets called when the read-evaluate-print-loop (REPL) of
    the shell has finished the execution of a command. We use this callback
    to be able to automatically update a figure in interactive mode.

    This works both with IPython and with vanilla python shells.
    """
    ...

def uninstall_repl_displayhook():
    """Disconnect from the display hook of the current shell."""
    ...

draw_all = ...

def set_loglevel(*args, **kwargs): ...
def findobj(o=..., match=..., include_self: bool = ...) -> list: ...
def switch_backend(newbackend: str):
    """
    Close all open figures and set the Matplotlib backend.

    The argument is case-insensitive.  Switching to an interactive backend is
    possible only if no event loop for another interactive backend has started.
    Switching to and from non-interactive backends is always possible.

    Parameters
    ----------
    newbackend : str
        The name of the backend to use.
    """

    class backend_mod(_Backend): ...

def new_figure_manager(*args, **kwargs):
    """Create a new figure manager instance."""
    ...

def draw_if_interactive(*args, **kwargs):
    """
    Redraw the current figure if in interactive mode.

    .. warning::

        End users will typically not have to call this function because the
        the interactive mode takes care of this.
    """
    ...

def show(*args, **kwargs):
    """
    Display all open figures.

    Parameters
    ----------
    block : bool, optional
        Whether to wait for all figures to be closed before returning.

        If `True` block and run the GUI main loop until all figure windows
        are closed.

        If `False` ensure that all figure windows are displayed and return
        immediately.  In this case, you are responsible for ensuring
        that the event loop is running to have responsive figures.

        Defaults to True in non-interactive mode and to False in interactive
        mode (see `.pyplot.isinteractive`).

    See Also
    --------
    ion : Enable interactive mode, which shows / updates the figure after
          every plotting command, so that calling ``show()`` is not necessary.
    ioff : Disable interactive mode.
    savefig : Save the figure to an image file instead of showing it on screen.

    Notes
    -----
    **Saving figures to file and showing a window at the same time**

    If you want an image file as well as a user interface window, use
    `.pyplot.savefig` before `.pyplot.show`. At the end of (a blocking)
    ``show()`` the figure is closed and thus unregistered from pyplot. Calling
    `.pyplot.savefig` afterwards would save a new and thus empty figure. This
    limitation of command order does not apply if the show is non-blocking or
    if you keep a reference to the figure and use `.Figure.savefig`.

    **Auto-show in jupyter notebooks**

    The jupyter backends (activated via ``%matplotlib inline``,
    ``%matplotlib notebook``, or ``%matplotlib widget``), call ``show()`` at
    the end of every cell by default. Thus, you usually don't have to call it
    explicitly there.
    """
    ...

def isinteractive() -> bool:
    """
    Return whether plots are updated after every plotting command.

    The interactive mode is mainly useful if you build plots from the command
    line and want to see the effect of each command while you are building the
    figure.

    In interactive mode:

    - newly created figures will be shown immediately;
    - figures will automatically redraw on change;
    - `.pyplot.show` will not block by default.

    In non-interactive mode:

    - newly created figures and changes to figures will not be reflected until
      explicitly asked to be;
    - `.pyplot.show` will block by default.

    See Also
    --------
    ion : Enable interactive mode.
    ioff : Disable interactive mode.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.
    """
    ...

class _IoffContext:
    """
    Context manager for `.ioff`.

    The state is changed in ``__init__()`` instead of ``__enter__()``. The
    latter is a no-op. This allows using `.ioff` both as a function and
    as a context.
    """

    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

class _IonContext:
    """
    Context manager for `.ion`.

    The state is changed in ``__init__()`` instead of ``__enter__()``. The
    latter is a no-op. This allows using `.ion` both as a function and
    as a context.
    """

    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

def ioff():
    """
    Disable interactive mode.

    See `.pyplot.isinteractive` for more details.

    See Also
    --------
    ion : Enable interactive mode.
    isinteractive : Whether interactive mode is enabled.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.

    Notes
    -----
    For a temporary change, this can be used as a context manager::

        # if interactive mode is on
        # then figures will be shown on creation
        plt.ion()
        # This figure will be shown immediately
        fig = plt.figure()

        with plt.ioff():
            # interactive mode will be off
            # figures will not automatically be shown
            fig2 = plt.figure()
            # ...

    To enable usage as a context manager, this function returns an
    ``_IoffContext`` object. The return value is not intended to be stored
    or accessed by the user.
    """
    ...

def ion():
    """
    Enable interactive mode.

    See `.pyplot.isinteractive` for more details.

    See Also
    --------
    ioff : Disable interactive mode.
    isinteractive : Whether interactive mode is enabled.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.

    Notes
    -----
    For a temporary change, this can be used as a context manager::

        # if interactive mode is off
        # then figures will not be shown on creation
        plt.ioff()
        # This figure will not be shown immediately
        fig = plt.figure()

        with plt.ion():
            # interactive mode will be on
            # figures will automatically be shown
            fig2 = plt.figure()
            # ...

    To enable usage as a context manager, this function returns an
    ``_IonContext`` object. The return value is not intended to be stored
    or accessed by the user.
    """
    ...

def pause(interval):
    """
    Run the GUI event loop for *interval* seconds.

    If there is an active figure, it will be updated and displayed before the
    pause, and the GUI event loop (if any) will run during the pause.

    This can be used for crude animation.  For more complex animation use
    :mod:`matplotlib.animation`.

    If there is no active figure, sleep for *interval* seconds instead.

    See Also
    --------
    matplotlib.animation : Proper animations
    show : Show all figures and optional block until all figures are closed.
    """
    ...

def rc(group, **kwargs): ...
def rc_context(rc: dict = ..., fname: str | PathLike = ...): ...
def rcdefaults(): ...
def getp(obj: Artist, *args, **kwargs): ...
def get(obj: Artist, *args, **kwargs): ...
def setp(obj: Artist | list, *args, **kwargs): ...
def xkcd(scale: float = ..., length: float = ..., randomness: float = ...):
    """
    Turn on `xkcd <https://xkcd.com/>`_ sketch-style drawing mode.  This will
    only have effect on things drawn after this function is called.

    For best results, the "Humor Sans" font should be installed: it is
    not included with Matplotlib.

    Parameters
    ----------
    scale : float, optional
        The amplitude of the wiggle perpendicular to the source line.
    length : float, optional
        The length of the wiggle along the line.
    randomness : float, optional
        The scale factor by which the length is shrunken or expanded.

    Notes
    -----
    This function works by a number of rcParams, so it will probably
    override others you have set before.

    If you want the effects of this function to be temporary, it can
    be used as a context manager, for example::

        with plt.xkcd():
            # This figure will be in XKCD-style
            fig1 = plt.figure()
            # ...

        # This figure will be in regular style
        fig2 = plt.figure()
    """
    ...

class _xkcd:
    def __init__(self, scale: float, length: float, randomness: float) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

def figure(
    num: int | str | Figure | SubFigure = ...,
    figsize: Sequence[float] = ...,
    dpi: float = ...,
    facecolor: Color = ...,
    edgecolor: Color = ...,
    frameon: bool = ...,
    FigureClass=...,
    clear: bool = ...,
    **kwargs
) -> Figure:
    """
    Create a new figure, or activate an existing figure.

    Parameters
    ----------
    num : int or str or `.Figure` or `.SubFigure`, optional
        A unique identifier for the figure.

        If a figure with that identifier already exists, this figure is made
        active and returned. An integer refers to the ``Figure.number``
        attribute, a string refers to the figure label.

        If there is no figure with the identifier or *num* is not given, a new
        figure is created, made active and returned.  If *num* is an int, it
        will be used for the ``Figure.number`` attribute, otherwise, an
        auto-generated integer value is used (starting at 1 and incremented
        for each new figure). If *num* is a string, the figure label and the
        window title is set to this value.  If num is a ``SubFigure``, its
        parent ``Figure`` is activated.

    figsize : (float, float), default: :rc:`figure.figsize`
        Width, height in inches.

    dpi : float, default: :rc:`figure.dpi`
        The resolution of the figure in dots-per-inch.

    facecolor : color, default: :rc:`figure.facecolor`
        The background color.

    edgecolor : color, default: :rc:`figure.edgecolor`
        The border color.

    frameon : bool, default: True
        If False, suppress drawing the figure frame.

    FigureClass : subclass of `~Figure`
        If set, an instance of this subclass will be created, rather than a
        plain `.Figure`.

    clear : bool, default: False
        If True and the figure already exists, then it is cleared.

    layout : {'constrained', 'tight', `.LayoutEngine`, None}, default: None
        The layout mechanism for positioning of plot elements to avoid
        overlapping Axes decorations (labels, ticks, etc). Note that layout
        managers can measurably slow down figure display. Defaults to *None*
        (but see the documentation of the `.Figure` constructor regarding the
        interaction with rcParams).

    **kwargs
        Additional keyword arguments are passed to the `.Figure` constructor.

    Returns
    -------
    `~Figure`

    Notes
    -----
    Newly created figures will be passed to the
    `~.backend_template.new_figure_manager` function provided by the current
    backend, which will install a canvas and a manager on the figure.

    If you are creating many figures, make sure you explicitly call
    `.pyplot.close` on the figures you are not using, because this will
    enable pyplot to properly clean up the memory.

    `~matplotlib.rcParams` defines the default values, which can be modified
    in the matplotlibrc file.
    """
    ...

def gcf() -> Figure:
    """
    Get the current figure.

    If there is currently no figure on the pyplot figure stack, a new one is
    created using `~.pyplot.figure()`.  (To test whether there is currently a
    figure on the pyplot figure stack, check whether `~.pyplot.get_fignums()`
    is empty.)
    """
    ...

def fignum_exists(num) -> bool:
    """Return whether the figure with the given id exists."""
    ...

def get_fignums() -> list[int]:
    """Return a list of existing figure numbers."""
    ...

def get_figlabels():
    """Return a list of existing figure labels."""
    ...

def get_current_fig_manager() -> FigureManagerBase:
    """
    Return the figure manager of the current figure.

    The figure manager is a container for the actual backend-depended window
    that displays the figure on screen.

    If no current figure exists, a new one is created, and its figure
    manager is returned.

    Returns
    -------
    `.FigureManagerBase` or backend-dependent subclass thereof
    """
    ...

def connect(s: str, func: Callable): ...
def disconnect(cid): ...
def close(fig: None | int | str | Figure = ...):
    """
    Close a figure window.

    Parameters
    ----------
    fig : None or int or str or `.Figure`
        The figure to close. There are a number of ways to specify this:

        - *None*: the current figure
        - `.Figure`: the given `.Figure` instance
        - ``int``: a figure number
        - ``str``: a figure name
        - 'all': all figures

    """
    ...

def clf() -> None:
    """Clear the current figure."""
    ...

def draw() -> None:
    """
    Redraw the current figure.

    This is used to update a figure that has been altered, but not
    automatically re-drawn.  If interactive mode is on (via `.ion()`), this
    should be only rarely needed, but there may be ways to modify the state of
    a figure without marking it as "stale".  Please report these cases as bugs.

    This is equivalent to calling ``fig.canvas.draw_idle()``, where ``fig`` is
    the current figure.
    """
    ...

def savefig(*args, **kwargs) -> None: ...
def figlegend(*args, **kwargs) -> Legend: ...
def axes(arg: None | tuple = ..., **kwargs) -> Axes:
    """
    Add an Axes to the current figure and make it the current Axes.

    Call signatures::

        plt.axes()
        plt.axes(rect, projection=None, polar=False, **kwargs)
        plt.axes(ax)

    Parameters
    ----------
    arg : None or 4-tuple
        The exact behavior of this function depends on the type:

        - *None*: A new full window Axes is added using
          ``subplot(**kwargs)``.
        - 4-tuple of floats *rect* = ``[left, bottom, width, height]``.
          A new Axes is added with dimensions *rect* in normalized
          (0, 1) units using `~.Figure.add_axes` on the current figure.

    projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', \
'polar', 'rectilinear', str}, optional
        The projection type of the `~.axes.Axes`. *str* is the name of
        a custom projection, see `~matplotlib.projections`. The default
        None results in a 'rectilinear' projection.

    polar : bool, default: False
        If True, equivalent to projection='polar'.

    sharex, sharey : `~.axes.Axes`, optional
        Share the x or y `~matplotlib.axis` with sharex and/or sharey.
        The axis will have the same limits, ticks, and scale as the axis
        of the shared Axes.

    label : str
        A label for the returned Axes.

    Returns
    -------
    `~.axes.Axes`, or a subclass of `~.axes.Axes`
        The returned axes class depends on the projection used. It is
        `~.axes.Axes` if rectilinear projection is used and
        `.projections.polar.PolarAxes` if polar projection is used.

    Other Parameters
    ----------------
    **kwargs
        This method also takes the keyword arguments for
        the returned Axes class. The keyword arguments for the
        rectilinear Axes class `~.axes.Axes` can be found in
        the following table but there might also be other keyword
        arguments if another projection is used, see the actual Axes
        class.

        %(Axes:kwdoc)s

    Notes
    -----
    If the figure already has an Axes with key (*args*,
    *kwargs*) then it will simply make that axes current and
    return it.  This behavior is deprecated. Meanwhile, if you do
    not want this behavior (i.e., you want to force the creation of a
    new axes), you must use a unique set of args and kwargs.  The Axes
    *label* attribute has been exposed for this purpose: if you want
    two Axes that are otherwise identical to be added to the figure,
    make sure you give them unique labels.

    See Also
    --------
    .Figure.add_axes
    .pyplot.subplot
    .Figure.add_subplot
    .Figure.subplots
    .pyplot.subplots

    Examples
    --------
    ::

        # Creating a new full window Axes
        plt.axes()

        # Creating a new Axes with specified dimensions and a grey background
        plt.axes((left, bottom, width, height), facecolor='grey')
    """
    ...

def delaxes(ax: Axes = ...) -> None:
    """
    Remove an `~.axes.Axes` (defaulting to the current axes) from its figure.
    """
    ...

def sca(ax: Axes) -> None:
    """
    Set the current Axes to *ax* and the current Figure to the parent of *ax*.
    """
    ...

def cla() -> None:
    """Clear the current axes."""
    ...

def subplot(*args, **kwargs) -> Axes:
    """
    Add an Axes to the current figure or retrieve an existing Axes.

    This is a wrapper of `.Figure.add_subplot` which provides additional
    behavior when working with the implicit API (see the notes section).

    Call signatures::

       subplot(nrows, ncols, index, **kwargs)
       subplot(pos, **kwargs)
       subplot(**kwargs)
       subplot(ax)

    Parameters
    ----------
    *args : int, (int, int, *index*), or `.SubplotSpec`, default: (1, 1, 1)
        The position of the subplot described by one of

        - Three integers (*nrows*, *ncols*, *index*). The subplot will take the
          *index* position on a grid with *nrows* rows and *ncols* columns.
          *index* starts at 1 in the upper left corner and increases to the
          right. *index* can also be a two-tuple specifying the (*first*,
          *last*) indices (1-based, and including *last*) of the subplot, e.g.,
          ``fig.add_subplot(3, 1, (1, 2))`` makes a subplot that spans the
          upper 2/3 of the figure.
        - A 3-digit integer. The digits are interpreted as if given separately
          as three single-digit integers, i.e. ``fig.add_subplot(235)`` is the
          same as ``fig.add_subplot(2, 3, 5)``. Note that this can only be used
          if there are no more than 9 subplots.
        - A `.SubplotSpec`.

    projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', \
'polar', 'rectilinear', str}, optional
        The projection type of the subplot (`~.axes.Axes`). *str* is the name
        of a custom projection, see `~matplotlib.projections`. The default
        None results in a 'rectilinear' projection.

    polar : bool, default: False
        If True, equivalent to projection='polar'.

    sharex, sharey : `~.axes.Axes`, optional
        Share the x or y `~matplotlib.axis` with sharex and/or sharey. The
        axis will have the same limits, ticks, and scale as the axis of the
        shared axes.

    label : str
        A label for the returned axes.

    Returns
    -------
    `.axes.SubplotBase`, or another subclass of `~.axes.Axes`

        The axes of the subplot. The returned axes base class depends on
        the projection used. It is `~.axes.Axes` if rectilinear projection
        is used and `.projections.polar.PolarAxes` if polar projection
        is used. The returned axes is then a subplot subclass of the
        base class.

    Other Parameters
    ----------------
    **kwargs
        This method also takes the keyword arguments for the returned axes
        base class; except for the *figure* argument. The keyword arguments
        for the rectilinear base class `~.axes.Axes` can be found in
        the following table but there might also be other keyword
        arguments if another projection is used.

        %(Axes:kwdoc)s

    Notes
    -----
    Creating a new Axes will delete any preexisting Axes that
    overlaps with it beyond sharing a boundary::

        import matplotlib.pyplot as plt
        # plot a line, implicitly creating a subplot(111)
        plt.plot([1, 2, 3])
        # now create a subplot which represents the top plot of a grid
        # with 2 rows and 1 column. Since this subplot will overlap the
        # first, the plot (and its axes) previously created, will be removed
        plt.subplot(211)

    If you do not want this behavior, use the `.Figure.add_subplot` method
    or the `.pyplot.axes` function instead.

    If no *kwargs* are passed and there exists an Axes in the location
    specified by *args* then that Axes will be returned rather than a new
    Axes being created.

    If *kwargs* are passed and there exists an Axes in the location
    specified by *args*, the projection type is the same, and the
    *kwargs* match with the existing Axes, then the existing Axes is
    returned.  Otherwise a new Axes is created with the specified
    parameters.  We save a reference to the *kwargs* which we use
    for this comparison.  If any of the values in *kwargs* are
    mutable we will not detect the case where they are mutated.
    In these cases we suggest using `.Figure.add_subplot` and the
    explicit Axes API rather than the implicit pyplot API.

    See Also
    --------
    .Figure.add_subplot
    .pyplot.subplots
    .pyplot.axes
    .Figure.subplots

    Examples
    --------
    ::

        plt.subplot(221)

        # equivalent but more general
        ax1 = plt.subplot(2, 2, 1)

        # add a subplot with no frame
        ax2 = plt.subplot(222, frameon=False)

        # add a polar subplot
        plt.subplot(223, projection='polar')

        # add a red subplot that shares the x-axis with ax1
        plt.subplot(224, sharex=ax1, facecolor='red')

        # delete ax2 from the figure
        plt.delaxes(ax2)

        # add ax2 to the figure again
        plt.subplot(ax2)

        # make the first axes "current" again
        plt.subplot(221)

    """
    ...

# Unsqueezed is always a 2D array.
# Not sure of as good way to do this. The real type is the axes collections
# are array. But that is not a generic in typing, so I am using list. That
# works okay but not for the 2D case
@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    squeeze: Literal[False],
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]: ...
@overload
def subplots(
    nrows: Literal[1],
    ncols: Literal[1],
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, Axes]: ...

# Squeezed 1xN or Mx1 where N, M >1 is a list of Axes
@overload
def subplots(
    nrows: Literal[1],
    ncols: int,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    nrows: int,
    ncols: Literal[1],
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    *,
    nrows: int,
    ncols: int,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]: ...
@overload
def subplots(
    *,
    ncols: int,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...
@overload
def subplots(
    nrows: int,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[Axes]]: ...

# Squeezed 1x1 is just an Axes
@overload
def subplots(
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, Axes]: ...

# Squeezed NxM where N, M >1 is a list of lists of Axes
@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: bool = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    **fig_kw
) -> tuple[Figure, list[list[Axes]]]:
    """
    Create a figure and a set of subplots.

    This utility wrapper makes it convenient to create common layouts of
    subplots, including the enclosing figure object, in a single call.

    Parameters
    ----------
    nrows, ncols : int, default: 1
        Number of rows/columns of the subplot grid.

    sharex, sharey : bool or {'none', 'all', 'row', 'col'}, default: False
        Controls sharing of properties among x (*sharex*) or y (*sharey*)
        axes:

        - True or 'all': x- or y-axis will be shared among all subplots.
        - False or 'none': each subplot x- or y-axis will be independent.
        - 'row': each subplot row will share an x- or y-axis.
        - 'col': each subplot column will share an x- or y-axis.

        When subplots have a shared x-axis along a column, only the x tick
        labels of the bottom subplot are created. Similarly, when subplots
        have a shared y-axis along a row, only the y tick labels of the first
        column subplot are created. To later turn other subplots' ticklabels
        on, use `~Axes.tick_params`.

        When subplots have a shared axis that has units, calling
        `~Axis.set_units` will update each axis with the
        new units.

    squeeze : bool, default: True
        - If True, extra dimensions are squeezed out from the returned
          array of `~Axes`:

          - if only one subplot is constructed (nrows=ncols=1), the
            resulting single Axes object is returned as a scalar.
          - for Nx1 or 1xM subplots, the returned object is a 1D numpy
            object array of Axes objects.
          - for NxM, subplots with N>1 and M>1 are returned as a 2D array.

        - If False, no squeezing at all is done: the returned Axes object is
          always a 2D array containing Axes instances, even if it ends up
          being 1x1.

    subplot_kw : dict, optional
        Dict with keywords passed to the
        `~Figure.add_subplot` call used to create each
        subplot.

    gridspec_kw : dict, optional
        Dict with keywords passed to the `~matplotlib.gridspec.GridSpec`
        constructor used to create the grid the subplots are placed on.

    **fig_kw
        All additional keyword arguments are passed to the
        `.pyplot.figure` call.

    Returns
    -------
    fig : `.Figure`

    ax : `~.axes.Axes` or array of Axes
        *ax* can be either a single `~.axes.Axes` object, or an array of Axes
        objects if more than one subplot was created.  The dimensions of the
        resulting array can be controlled with the squeeze keyword, see above.

        Typical idioms for handling the return value are::

            # using the variable ax for single a Axes
            fig, ax = plt.subplots()

            # using the variable axs for multiple Axes
            fig, axs = plt.subplots(2, 2)

            # using tuple unpacking for multiple Axes
            fig, (ax1, ax2) = plt.subplots(1, 2)
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        The names ``ax`` and pluralized ``axs`` are preferred over ``axes``
        because for the latter it's not clear if it refers to a single
        `~.axes.Axes` instance or a collection of these.

    See Also
    --------
    .pyplot.figure
    .pyplot.subplot
    .pyplot.axes
    .Figure.subplots
    .Figure.add_subplot

    Examples
    --------
    ::

        # First create some toy data:
        x = np.linspace(0, 2*np.pi, 400)
        y = np.sin(x**2)

        # Create just a figure and only one subplot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Simple plot')

        # Create two subplots and unpack the output array immediately
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.plot(x, y)
        ax1.set_title('Sharing Y axis')
        ax2.scatter(x, y)

        # Create four polar axes and access them through the returned array
        fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
        axs[0, 0].plot(x, y)
        axs[1, 1].scatter(x, y)

        # Share a X axis with each column of subplots
        plt.subplots(2, 2, sharex='col')

        # Share a Y axis with each row of subplots
        plt.subplots(2, 2, sharey='row')

        # Share both X and Y axes with all subplots
        plt.subplots(2, 2, sharex='all', sharey='all')

        # Note that this is the same as
        plt.subplots(2, 2, sharex=True, sharey=True)

        # Create figure number 10 with a single subplot
        # and clears it if it already exists.
        fig, ax = plt.subplots(num=10, clear=True)

    """
    ...

def subplot_mosaic(
    mosaic: list | str,
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    subplot_kw: dict = ...,
    gridspec_kw: dict = ...,
    empty_sentinel: object = ...,
    **fig_kw
) -> dict[Text, Axes]:
    """
    Build a layout of Axes based on ASCII art or nested lists.

    This is a helper function to build complex GridSpec layouts visually.

    .. note::

       This API is provisional and may be revised in the future based on
       early user feedback.

    See :doc:`/tutorials/provisional/mosaic`
    for an example and full API documentation

    Parameters
    ----------
    mosaic : list of list of {hashable or nested} or str

        A visual layout of how you want your Axes to be arranged
        labeled as strings.  For example ::

           x = [['A panel', 'A panel', 'edge'],
                ['C panel', '.',       'edge']]

        produces 4 axes:

        - 'A panel' which is 1 row high and spans the first two columns
        - 'edge' which is 2 rows high and is on the right edge
        - 'C panel' which in 1 row and 1 column wide in the bottom left
        - a blank space 1 row and 1 column wide in the bottom center

        Any of the entries in the layout can be a list of lists
        of the same form to create nested layouts.

        If input is a str, then it must be of the form ::

          '''
          AAE
          C.E
          '''

        where each character is a column and each line is a row.
        This only allows only single character Axes labels and does
        not allow nesting but is very terse.

    sharex, sharey : bool, default: False
        If True, the x-axis (*sharex*) or y-axis (*sharey*) will be shared
        among all subplots.  In that case, tick label visibility and axis units
        behave as for `subplots`.  If False, each subplot's x- or y-axis will
        be independent.

    subplot_kw : dict, optional
        Dictionary with keywords passed to the `.Figure.add_subplot` call
        used to create each subplot.

    gridspec_kw : dict, optional
        Dictionary with keywords passed to the `.GridSpec` constructor used
        to create the grid the subplots are placed on.

    empty_sentinel : object, optional
        Entry in the layout to mean "leave this space empty".  Defaults
        to ``'.'``. Note, if *layout* is a string, it is processed via
        `inspect.cleandoc` to remove leading white space, which may
        interfere with using white-space as the empty sentinel.

    **fig_kw
        All additional keyword arguments are passed to the
        `.pyplot.figure` call.

    Returns
    -------
    fig : `.Figure`
       The new figure

    dict[label, Axes]
       A dictionary mapping the labels to the Axes objects.  The order of
       the axes is left-to-right and top-to-bottom of their position in the
       total layout.

    """
    ...

def subplot2grid(
    shape: Sequence[int],
    loc: Sequence[int],
    rowspan: int = ...,
    colspan: int = ...,
    fig: Figure = ...,
    **kwargs
) -> Axes:
    """
    Create a subplot at a specific location inside a regular grid.

    Parameters
    ----------
    shape : (int, int)
        Number of rows and of columns of the grid in which to place axis.
    loc : (int, int)
        Row number and column number of the axis location within the grid.
    rowspan : int, default: 1
        Number of rows for the axis to span downwards.
    colspan : int, default: 1
        Number of columns for the axis to span to the right.
    fig : `.Figure`, optional
        Figure to place the subplot in. Defaults to the current figure.
    **kwargs
        Additional keyword arguments are handed to `~.Figure.add_subplot`.

    Returns
    -------
    `.axes.SubplotBase`, or another subclass of `~.axes.Axes`

        The axes of the subplot.  The returned axes base class depends on the
        projection used.  It is `~.axes.Axes` if rectilinear projection is used
        and `.projections.polar.PolarAxes` if polar projection is used.  The
        returned axes is then a subplot subclass of the base class.

    Notes
    -----
    The following call ::

        ax = subplot2grid((nrows, ncols), (row, col), rowspan, colspan)

    is identical to ::

        fig = gcf()
        gs = fig.add_gridspec(nrows, ncols)
        ax = fig.add_subplot(gs[row:row+rowspan, col:col+colspan])
    """
    ...

def twinx(ax: Axes = ...) -> Axes:
    """
    Make and return a second axes that shares the *x*-axis.  The new axes will
    overlay *ax* (or the current axes if *ax* is *None*), and its ticks will be
    on the right.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`
    """
    ...

def twiny(ax: Axes = ...) -> Axes:
    """
    Make and return a second axes that shares the *y*-axis.  The new axes will
    overlay *ax* (or the current axes if *ax* is *None*), and its ticks will be
    on the top.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`
    """
    ...

def subplot_tool(targetfig: Figure = ...) -> SubplotTool:
    """
    Launch a subplot tool window for a figure.

    Returns
    -------
    `matplotlib.widgets.SubplotTool`
    """
    ...

def box(on: bool | None = ...):
    """
    Turn the axes box on or off on the current axes.

    Parameters
    ----------
    on : bool or None
        The new `~Axes` box state. If ``None``, toggle
        the state.

    See Also
    --------
    :meth:`Axes.set_frame_on`
    :meth:`Axes.get_frame_on`
    """
    ...

def xlim(*args, **kwargs) -> tuple[float, float]:
    """
    Get or set the x limits of the current axes.

    Call signatures::

        left, right = xlim()  # return the current xlim
        xlim((left, right))   # set the xlim to left, right
        xlim(left, right)     # set the xlim to left, right

    If you do not specify args, you can pass *left* or *right* as kwargs,
    i.e.::

        xlim(right=3)  # adjust the right leaving left unchanged
        xlim(left=1)  # adjust the left leaving right unchanged

    Setting limits turns autoscaling off for the x-axis.

    Returns
    -------
    left, right
        A tuple of the new x-axis limits.

    Notes
    -----
    Calling this function with no arguments (e.g. ``xlim()``) is the pyplot
    equivalent of calling `~.Axes.get_xlim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xlim` on the current axes. All arguments are passed though.
    """
    ...

def ylim(*args, **kwargs) -> tuple[float, float]:
    """
    Get or set the y-limits of the current axes.

    Call signatures::

        bottom, top = ylim()  # return the current ylim
        ylim((bottom, top))   # set the ylim to bottom, top
        ylim(bottom, top)     # set the ylim to bottom, top

    If you do not specify args, you can alternatively pass *bottom* or
    *top* as kwargs, i.e.::

        ylim(top=3)  # adjust the top leaving bottom unchanged
        ylim(bottom=1)  # adjust the bottom leaving top unchanged

    Setting limits turns autoscaling off for the y-axis.

    Returns
    -------
    bottom, top
        A tuple of the new y-axis limits.

    Notes
    -----
    Calling this function with no arguments (e.g. ``ylim()``) is the pyplot
    equivalent of calling `~.Axes.get_ylim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_ylim` on the current axes. All arguments are passed though.
    """
    ...

def xticks(
    ticks: ArrayLike = ..., labels: ArrayLike = ..., **kwargs
) -> tuple[list, list[Text]]:
    """
    Get or set the current tick locations and labels of the x-axis.

    Pass no arguments to return the current values without modifying them.

    Parameters
    ----------
    ticks : array-like, optional
        The list of xtick locations.  Passing an empty list removes all xticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.

    Returns
    -------
    locs
        The list of xtick locations.
    labels
        The list of xlabel `.Text` objects.

    Notes
    -----
    Calling this function with no arguments (e.g. ``xticks()``) is the pyplot
    equivalent of calling `~.Axes.get_xticks` and `~.Axes.get_xticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xticks` and `~.Axes.set_xticklabels` on the current axes.

    Examples
    --------
    >>> locs, labels = xticks()  # Get the current locations and labels.
    >>> xticks(np.arange(0, 1, step=0.2))  # Set label locations.
    >>> xticks(np.arange(3), ['Tom', 'Dick', 'Sue'])  # Set text labels.
    >>> xticks([0, 1, 2], ['January', 'February', 'March'],
    ...        rotation=20)  # Set text labels and properties.
    >>> xticks([])  # Disable xticks.
    """
    ...

def yticks(
    ticks: ArrayLike = ..., labels: ArrayLike = ..., **kwargs
) -> tuple[list, list[Text]]:
    """
    Get or set the current tick locations and labels of the y-axis.

    Pass no arguments to return the current values without modifying them.

    Parameters
    ----------
    ticks : array-like, optional
        The list of ytick locations.  Passing an empty list removes all yticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.

    Returns
    -------
    locs
        The list of ytick locations.
    labels
        The list of ylabel `.Text` objects.

    Notes
    -----
    Calling this function with no arguments (e.g. ``yticks()``) is the pyplot
    equivalent of calling `~.Axes.get_yticks` and `~.Axes.get_yticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_yticks` and `~.Axes.set_yticklabels` on the current axes.

    Examples
    --------
    >>> locs, labels = yticks()  # Get the current locations and labels.
    >>> yticks(np.arange(0, 1, step=0.2))  # Set label locations.
    >>> yticks(np.arange(3), ['Tom', 'Dick', 'Sue'])  # Set text labels.
    >>> yticks([0, 1, 2], ['January', 'February', 'March'],
    ...        rotation=45)  # Set text labels and properties.
    >>> yticks([])  # Disable yticks.
    """
    ...

def rgrids(
    radii: Sequence[float] = ...,
    labels: Sequence[str] | None = ...,
    angle: float = ...,
    fmt: str | None = ...,
    **kwargs
) -> tuple[list[Line2D], list[Text]]:
    """
    Get or set the radial gridlines on the current polar plot.

    Call signatures::

     lines, labels = rgrids()
     lines, labels = rgrids(radii, labels=None, angle=22.5, fmt=None, **kwargs)

    When called with no arguments, `.rgrids` simply returns the tuple
    (*lines*, *labels*). When called with arguments, the labels will
    appear at the specified radial distances and angle.

    Parameters
    ----------
    radii : tuple with floats
        The radii for the radial gridlines

    labels : tuple with strings or None
        The labels to use at each radial gridline. The
        `matplotlib.ticker.ScalarFormatter` will be used if None.

    angle : float
        The angular position of the radius labels in degrees.

    fmt : str or None
        Format string used in `matplotlib.ticker.FormatStrFormatter`.
        For example '%f'.

    Returns
    -------
    lines : list of `.lines.Line2D`
        The radial gridlines.

    labels : list of `.text.Text`
        The tick labels.

    Other Parameters
    ----------------
    **kwargs
        *kwargs* are optional `.Text` properties for the labels.

    See Also
    --------
    .pyplot.thetagrids
    .projections.polar.PolarAxes.set_rgrids
    .Axis.get_gridlines
    .Axis.get_ticklabels

    Examples
    --------
    ::

      # set the locations of the radial gridlines
      lines, labels = rgrids( (0.25, 0.5, 1.0) )

      # set the locations and labels of the radial gridlines
      lines, labels = rgrids( (0.25, 0.5, 1.0), ('Tom', 'Dick', 'Harry' ))
    """
    ...

def thetagrids(
    angles: Sequence[float] = ...,
    labels: Sequence[str] | None = ...,
    fmt: str | None = ...,
    **kwargs
) -> tuple[list[Line2D], list[Text]]:
    """
    Get or set the theta gridlines on the current polar plot.

    Call signatures::

     lines, labels = thetagrids()
     lines, labels = thetagrids(angles, labels=None, fmt=None, **kwargs)

    When called with no arguments, `.thetagrids` simply returns the tuple
    (*lines*, *labels*). When called with arguments, the labels will
    appear at the specified angles.

    Parameters
    ----------
    angles : tuple with floats, degrees
        The angles of the theta gridlines.

    labels : tuple with strings or None
        The labels to use at each radial gridline. The
        `.projections.polar.ThetaFormatter` will be used if None.

    fmt : str or None
        Format string used in `matplotlib.ticker.FormatStrFormatter`.
        For example '%f'. Note that the angle in radians will be used.

    Returns
    -------
    lines : list of `.lines.Line2D`
        The theta gridlines.

    labels : list of `.text.Text`
        The tick labels.

    Other Parameters
    ----------------
    **kwargs
        *kwargs* are optional `.Text` properties for the labels.

    See Also
    --------
    .pyplot.rgrids
    .projections.polar.PolarAxes.set_thetagrids
    .Axis.get_gridlines
    .Axis.get_ticklabels

    Examples
    --------
    ::

      # set the locations of the angular gridlines
      lines, labels = thetagrids(range(45, 360, 90))

      # set the locations and labels of the angular gridlines
      lines, labels = thetagrids(range(45, 360, 90), ('NE', 'NW', 'SW', 'SE'))
    """
    ...

def get_plot_commands() -> list:
    """
    Get a sorted list of all of the plotting commands.
    """
    ...

def colorbar(mappable=..., cax: Axes = ..., ax: Axes = ..., **kwargs): ...
def clim(vmin: float | None = ..., vmax: float | None = ...):
    """
    Set the color limits of the current image.

    If either *vmin* or *vmax* is None, the image min/max respectively
    will be used for color scaling.

    If you want to set the clim of multiple images, use
    `~.ScalarMappable.set_clim` on every image, for example::

      for im in gca().get_images():
          im.set_clim(0, 0.5)

    """
    ...

def set_cmap(cmap: Colormap | str):
    """
    Set the default colormap, and applies it to the current image if any.

    Parameters
    ----------
    cmap : `~Colormap` or str
        A colormap instance or the name of a registered colormap.

    See Also
    --------
    colormaps
    matplotlib.cm.register_cmap
    matplotlib.cm.get_cmap
    """
    ...

def imread(fname: str | FileLike, format: str = ...) -> np.ndarray: ...
def imsave(fname: str | PathLike | FileLike, arr: ArrayLike, **kwargs): ...
def matshow(
    A: ArrayLike, fignum: None | int | Literal[False] = ..., **kwargs
) -> AxesImage:
    """
    Display an array as a matrix in a new figure window.

    The origin is set at the upper left hand corner and rows (first
    dimension of the array) are displayed horizontally.  The aspect
    ratio of the figure window is that of the array, unless this would
    make an excessively short or narrow figure.

    Tick labels for the xaxis are placed on top.

    Parameters
    ----------
    A : 2D array-like
        The matrix to be displayed.

    fignum : None or int or False
        If *None*, create a new figure window with automatic numbering.

        If a nonzero integer, draw into the figure with the given number
        (create it if it does not exist).

        If 0, use the current axes (or create one if it does not exist).

        .. note::

           Because of how `.Axes.matshow` tries to set the figure aspect
           ratio to be the one of the array, strange things may happen if you
           reuse an existing figure.

    Returns
    -------
    `~matplotlib.image.AxesImage`

    Other Parameters
    ----------------
    **kwargs : `~Axes.imshow` arguments

    """
    ...

def polar(*args, **kwargs):
    """
    Make a polar plot.

    call signature::

      polar(theta, r, **kwargs)

    Multiple *theta*, *r* arguments are supported, with format strings, as in
    `plot`.
    """
    ...

def figimage(
    X: ArrayLike,
    xo: float = ...,
    yo: float = ...,
    alpha: None | float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    origin: Literal["upper", "lower"] = ...,
    resize: bool = ...,
    **kwargs
) -> FigureImage: ...
def figtext(
    x: float, y: float, s: str, fontdict: dict = ..., **kwargs
) -> text.Text: ...
def gca(): ...
def gci(): ...
def ginput(
    n: int = ...,
    timeout: float = ...,
    show_clicks: bool = ...,
    mouse_add: MouseButton | None = ...,
    mouse_pop: MouseButton | None = ...,
    mouse_stop: MouseButton | None = ...,
) -> list[tuple]: ...
def subplots_adjust(
    left: float = ...,
    bottom: float = ...,
    right: float = ...,
    top: float = ...,
    wspace: float = ...,
    hspace: float = ...,
): ...
def suptitle(t: str, **kwargs) -> Text: ...
def tight_layout(
    *,
    pad: float = ...,
    h_pad: float = ...,
    w_pad: float = ...,
    rect: Sequence[float] = ...
): ...
def waitforbuttonpress(timeout=...): ...
def acorr(x: ArrayLike, *, data=..., **kwargs): ...
def angle_spectrum(
    x: Sequence[float],
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    *,
    data=...,
    **kwargs
): ...
def annotate(
    text: str,
    xy: Sequence[float],
    xytext: Sequence[float] = ...,
    xycoords: str | Artist | Transform | Callable = ...,
    textcoords: str | Artist | Transform | Callable = ...,
    arrowprops: dict = ...,
    annotation_clip: bool | None = ...,
    **kwargs
) -> Annotation: ...
def arrow(x: float, y: float, dx: float, dy: float, **kwargs) -> FancyArrow: ...
def autoscale(
    enable: bool | None = ...,
    axis: Literal["both", "x", "y"] = ...,
    tight: bool | None = ...,
): ...
def axhline(
    y: float = ..., xmin: float = ..., xmax: float = ..., **kwargs
) -> Line2D: ...
def axhspan(
    ymin: float, ymax: float, xmin: float = ..., xmax: float = ..., **kwargs
) -> Polygon: ...
def axis(*args, emit: bool = ..., **kwargs): ...
def axline(
    xy1: Sequence[float], xy2: Sequence[float] = ..., *, slope: float = ..., **kwargs
) -> Line2D: ...
def axvline(
    x: float = ..., ymin: float = ..., ymax: float = ..., **kwargs
) -> Line2D: ...
def axvspan(
    xmin: float, xmax: float, ymin: float = ..., ymax: float = ..., **kwargs
) -> Polygon: ...
def bar(
    x: float | ArrayLike,
    height: float | ArrayLike,
    width: float | ArrayLike = ...,
    bottom: float | ArrayLike = ...,
    *,
    align: Literal["center", "edge"] = ...,
    data=...,
    **kwargs
) -> BarContainer: ...
def barbs(*args, data=..., **kwargs): ...
def barh(
    y: float | ArrayLike,
    width: float | ArrayLike,
    height: float | ArrayLike = ...,
    left: float | ArrayLike = ...,
    *,
    align: Literal["center", "edge"] = ...,
    **kwargs
) -> BarContainer: ...
def bar_label(
    container: BarContainer,
    labels: ArrayLike = ...,
    *,
    fmt: str = ...,
    label_type: Literal["edge", "center"] = ...,
    padding: float = ...,
    **kwargs
) -> list: ...
def boxplot(
    x: ArrayLike,
    notch: bool = ...,
    sym: str = ...,
    vert: bool = ...,
    whis: float = ...,
    positions: ArrayLike = ...,
    widths: float | ArrayLike = ...,
    patch_artist: bool = ...,
    bootstrap: int = ...,
    usermedians=...,
    conf_intervals: ArrayLike = ...,
    meanline: bool = ...,
    showmeans=...,
    showcaps=...,
    showbox=...,
    showfliers=...,
    boxprops=...,
    labels: Sequence = ...,
    flierprops=...,
    medianprops=...,
    meanprops=...,
    capprops=...,
    whiskerprops=...,
    manage_ticks: bool = ...,
    autorange: bool = ...,
    zorder: float = ...,
    capwidths=...,
    *,
    data=...
) -> dict: ...
def broken_barh(xranges, yrange, *, data=..., **kwargs) -> BrokenBarHCollection: ...
def clabel(CS, levels: ArrayLike = ..., **kwargs): ...
def cohere(
    x,
    y,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def contour(*args, data=..., **kwargs) -> QuadContourSet: ...
def contourf(*args, data=..., **kwargs) -> QuadContourSet: ...
def csd(
    x: Sequence[float],
    y: Sequence[float],
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    return_line: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def errorbar(
    x: float | ArrayLike,
    y: float | ArrayLike,
    yerr: float | ArrayLike = ...,
    xerr: float | ArrayLike = ...,
    fmt: str = ...,
    ecolor: Color = ...,
    elinewidth: float = ...,
    capsize: float = ...,
    barsabove: bool = ...,
    lolims: bool = ...,
    uplims: bool = ...,
    xlolims: bool = ...,
    xuplims: bool = ...,
    errorevery: int = ...,
    capthick: float = ...,
    *,
    data=...,
    **kwargs
) -> ErrorbarContainer: ...
def eventplot(
    positions: ArrayLike | Sequence[ArrayLike],
    orientation: Literal["horizontal", "vertical"] = ...,
    lineoffsets: float | ArrayLike = ...,
    linelengths: float | ArrayLike = ...,
    linewidths: float | ArrayLike = ...,
    colors: Color | list[Color] = ...,
    linestyles: str | tuple | list = ...,
    *,
    data=...,
    **kwargs
) -> list: ...
def fill(*args, data=..., **kwargs) -> list[Polygon]: ...
def fill_between(
    x,
    y1: Scalar,
    y2: Scalar = ...,
    where: ArrayLike = ...,
    interpolate: bool = ...,
    step: Literal["pre", "post", "mid"] = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def fill_betweenx(
    y,
    x1: Scalar,
    x2: Scalar = ...,
    where: ArrayLike = ...,
    step: Literal["pre", "post", "mid"] = ...,
    interpolate: bool = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def grid(
    visible: bool | None = ...,
    which: Literal["major", "minor", "both"] = ...,
    axis: Literal["both", "x", "y"] = ...,
    **kwargs
): ...
def hexbin(
    x: ArrayLike,
    y: ArrayLike,
    C: ArrayLike = ...,
    gridsize: int = ...,
    bins: Literal["log"] | int | Sequence = ...,
    xscale: Literal["linear", "log"] = ...,
    yscale: Literal["linear", "log"] = ...,
    extent=...,
    cmap=...,
    norm=...,
    vmin=...,
    vmax=...,
    alpha=...,
    linewidths=...,
    edgecolors=...,
    reduce_C_function=...,
    mincnt: int = ...,
    marginals: bool = ...,
    *,
    data=...,
    **kwargs
) -> PolyCollection: ...
def hist(
    x,
    bins: int | Sequence | str = ...,
    range: tuple | None = ...,
    density: bool = ...,
    weights=...,
    cumulative: bool | Literal[-1] = ...,
    bottom=...,
    histtype: Literal["bar", "barstacked", "step", "stepfilled"] = ...,
    align: Literal["left", "mid", "right"] = ...,
    orientation: Literal["vertical", "horizontal"] = ...,
    rwidth: float | None = ...,
    log: bool = ...,
    color: Color | None = ...,
    label: str | None = ...,
    stacked: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def stairs(
    values: ArrayLike,
    edges: ArrayLike = ...,
    *,
    orientation: Literal["vertical", "horizontal"] = ...,
    baseline: float | ArrayLike | None = ...,
    fill: bool = ...,
    data=...,
    **kwargs
): ...
def hist2d(
    x,
    y,
    bins: None | int | ArrayLike = ...,
    range=...,
    density: bool = ...,
    weights=...,
    cmin: float = ...,
    cmax: float = ...,
    *,
    data=...,
    **kwargs
): ...
def hlines(
    y: float | ArrayLike,
    xmin: float | ArrayLike,
    xmax: float | ArrayLike,
    colors: list[Color] = ...,
    linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
    label: str = ...,
    *,
    data=...,
    **kwargs
) -> LineCollection: ...
def imshow(
    X: ArrayLike,
    cmap: str | Colormap = ...,
    norm: Normalize = ...,
    aspect: Literal["equal", "auto"] | float = ...,
    interpolation: str = ...,
    alpha: float | ArrayLike = ...,
    vmin: float = ...,
    vmax: float = ...,
    origin: Literal["upper", "lower"] = ...,
    extent: Sequence[float] = ...,
    *,
    interpolation_stage: Literal["data", "rgba"] = ...,
    filternorm: bool = ...,
    filterrad: float = ...,
    resample: bool = ...,
    url: str = ...,
    data=...,
    **kwargs
) -> AxesImage: ...
def legend(*args, **kwargs) -> Legend: ...
def locator_params(
    axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
): ...
def loglog(*args, **kwargs) -> list: ...
def magnitude_spectrum(
    x: Sequence,
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale: Literal["default", "linear", "dB"] = ...,
    *,
    data=...,
    **kwargs
): ...
def margins(*margins, x: float = ..., y: float = ..., tight: bool | None = ...): ...
def minorticks_off(): ...
def minorticks_on(): ...
def pcolor(
    *args,
    shading: Literal["flat", "nearest", "auto"] = ...,
    alpha: float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    data=...,
    **kwargs
) -> Collection: ...
def pcolormesh(
    *args,
    alpha: float = ...,
    norm: Normalize = ...,
    cmap: str | Colormap = ...,
    vmin: float = ...,
    vmax: float = ...,
    shading: Literal["flat", "nearest", "gouraud", "auto"] = ...,
    antialiased=...,
    data=...,
    **kwargs
) -> QuadMesh: ...
def phase_spectrum(
    x: Sequence,
    Fs: float = ...,
    Fc: float = ...,
    window: Callable | np.ndarray = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    *,
    data=...,
    **kwargs
): ...
def pie(
    x,
    explode: ArrayLike = ...,
    labels: Sequence[str] = ...,
    colors: ArrayLike = ...,
    autopct: None | str | Callable = ...,
    pctdistance: float = ...,
    shadow: bool = ...,
    labeldistance: float | None = ...,
    startangle: float = ...,
    radius: float = ...,
    counterclock: bool = ...,
    wedgeprops: dict = ...,
    textprops: dict = ...,
    center: tuple[float, float] = ...,
    frame: bool = ...,
    rotatelabels: bool = ...,
    *,
    normalize: bool = ...,
    data=...
): ...
def plot(*args, scalex=..., scaley=..., data=..., **kwargs) -> list: ...
def plot_date(
    x: ArrayLike,
    y: ArrayLike,
    fmt: str = ...,
    tz: datetime.tzinfo = ...,
    xdate: bool = ...,
    ydate: bool = ...,
    *,
    data=...,
    **kwargs
) -> list: ...
def psd(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: float = ...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    return_line: bool = ...,
    *,
    data=...,
    **kwargs
): ...
def quiver(*args, data=..., **kwargs) -> Quiver: ...
def quiverkey(Q: Quiver, X: float, Y: float, U: float, label: str, **kwargs): ...
def scatter(
    x: float | ArrayLike,
    y: float | ArrayLike,
    s: float | ArrayLike = ...,
    c: ArrayLike | list[Color] | Color = ...,
    marker: MarkerStyle = ...,
    cmap: str | Colormap = ...,
    norm: Normalize = ...,
    vmin: float = ...,
    vmax: float = ...,
    alpha: float = ...,
    linewidths: float | ArrayLike = ...,
    *,
    edgecolors: Color = ...,
    plotnonfinite: bool = ...,
    data=...,
    **kwargs
) -> PathCollection: ...
def semilogx(*args, **kwargs) -> list: ...
def semilogy(*args, **kwargs) -> list: ...
def specgram(
    x: Sequence,
    NFFT: int = ...,
    Fs: float = ...,
    Fc: float = ...,
    detrend: Literal["none", "mean", "linear"] | Callable = ...,
    window: Callable | np.ndarray = ...,
    noverlap: int = ...,
    cmap: Colormap = ...,
    xextent=...,
    pad_to: float = ...,
    sides: Literal["default", "onesided", "twosided"] = ...,
    scale_by_freq: bool = ...,
    mode: Literal["default", "psd", "magnitude", "angle", "phase"] = ...,
    scale: Literal["default", "linear", "dB"] = ...,
    vmin=...,
    vmax=...,
    *,
    data=...,
    **kwargs
): ...
def spy(
    Z,
    precision: float | Literal["present"] = ...,
    marker=...,
    markersize=...,
    aspect: Literal["equal", "auto", None] | float = ...,
    origin: Literal["upper", "lower"] = ...,
    **kwargs
) -> tuple[AxesImage, Line2D]: ...
def stackplot(
    x,
    *args,
    labels: list[str] = ...,
    colors: list[Color] = ...,
    baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = ...,
    data=...,
    **kwargs
) -> list: ...
def stem(
    *args,
    linefmt: str = ...,
    markerfmt: str = ...,
    basefmt: str = ...,
    bottom: float = ...,
    label: str = ...,
    use_line_collection: bool = ...,
    orientation: str = ...,
    data=...
) -> StemContainer: ...
def step(
    x: ArrayLike,
    y: ArrayLike,
    *args,
    where: Literal["pre", "post", "mid"] = ...,
    data=...,
    **kwargs
) -> list: ...
def streamplot(
    x,
    y,
    u,
    v,
    density: float = ...,
    linewidth: float = ...,
    color: Color = ...,
    cmap: Colormap = ...,
    norm: Normalize = ...,
    arrowsize: float = ...,
    arrowstyle: str = ...,
    minlength: float = ...,
    transform=...,
    zorder: int = ...,
    start_points=...,
    maxlength: float = ...,
    integration_direction: Literal["forward", "backward", "both"] = ...,
    broken_streamlines: bool = ...,
    *,
    data=...
) -> StreamplotSet: ...
def table(
    cellText=...,
    cellColours=...,
    cellLoc: Literal["left", "center", "right"] = ...,
    colWidths: list[float] = ...,
    rowLabels: list[str] = ...,
    rowColours: list[Color] = ...,
    rowLoc: Literal["left", "center", "right"] = ...,
    colLabels: list[str] = ...,
    colColours: list[Color] = ...,
    colLoc: Literal["left", "center", "right"] = ...,
    loc: str = ...,
    bbox: Bbox = ...,
    edges: Literal["open", "closed", "horizontal", "vertical"] = ...,
    **kwargs
) -> Table: ...
def text(x: float, y: float, s: str, fontdict: dict = ..., **kwargs) -> Text: ...
def tick_params(axis: Literal["x", "y", "both"] = ..., **kwargs): ...
def ticklabel_format(
    *,
    axis: Literal["x", "y", "both"] = ...,
    style: Literal["sci", "scientific", "plain"] = ...,
    scilimits=...,
    useOffset: bool | float = ...,
    useLocale: bool = ...,
    useMathText: bool = ...
): ...
def tricontour(*args, **kwargs) -> TriContourSet: ...
def tricontourf(*args, **kwargs) -> TriContourSet: ...
def tripcolor(
    *args,
    alpha=...,
    norm=...,
    cmap=...,
    vmin: float = ...,
    vmax: float = ...,
    shading: Literal["flat", "gouraud"] = ...,
    facecolors: ArrayLike = ...,
    **kwargs
): ...
def triplot(*args, **kwargs): ...
def violinplot(
    dataset: ArrayLike,
    positions: ArrayLike = ...,
    vert: bool = ...,
    widths: ArrayLike = ...,
    showmeans: bool = ...,
    showextrema: bool = ...,
    showmedians: bool = ...,
    quantiles: ArrayLike = ...,
    points: int = ...,
    bw_method: str | Scalar | Callable = ...,
    *,
    data=...
) -> dict: ...
def vlines(
    x: float | ArrayLike,
    ymin: float | ArrayLike,
    ymax: float | ArrayLike,
    colors: list[Color] = ...,
    linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
    label: str = ...,
    *,
    data=...,
    **kwargs
) -> LineCollection: ...
def xcorr(
    x,
    y,
    normed: bool = ...,
    detrend: Callable = ...,
    usevlines: bool = ...,
    maxlags: int = ...,
    *,
    data=...,
    **kwargs
): ...
def sci(im): ...
def title(
    label: str,
    fontdict: dict = ...,
    loc: Literal["center", "left", "right"] = ...,
    pad: float = ...,
    *,
    y: float = ...,
    **kwargs
) -> Text: ...
def xlabel(
    xlabel: str,
    fontdict=...,
    labelpad: float = ...,
    *,
    loc: Literal["left", "center", "right"] = ...,
    **kwargs
): ...
def ylabel(
    ylabel: str,
    fontdict=...,
    labelpad: float = ...,
    *,
    loc: Literal["bottom", "center", "top"] = ...,
    **kwargs
): ...
def xscale(
    value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
): ...
def yscale(
    value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
): ...
def autumn():
    """
    Set the colormap to 'autumn'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def bone():
    """
    Set the colormap to 'bone'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def cool():
    """
    Set the colormap to 'cool'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def copper():
    """
    Set the colormap to 'copper'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def flag():
    """
    Set the colormap to 'flag'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def gray():
    """
    Set the colormap to 'gray'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def hot():
    """
    Set the colormap to 'hot'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def hsv():
    """
    Set the colormap to 'hsv'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def jet():
    """
    Set the colormap to 'jet'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def pink():
    """
    Set the colormap to 'pink'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def prism():
    """
    Set the colormap to 'prism'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def spring():
    """
    Set the colormap to 'spring'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def summer():
    """
    Set the colormap to 'summer'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def winter():
    """
    Set the colormap to 'winter'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def magma():
    """
    Set the colormap to 'magma'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def inferno():
    """
    Set the colormap to 'inferno'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def plasma():
    """
    Set the colormap to 'plasma'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def viridis():
    """
    Set the colormap to 'viridis'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...

def nipy_spectral():
    """
    Set the colormap to 'nipy_spectral'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
    ...
