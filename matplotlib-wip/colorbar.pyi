from typing import Literal, Sequence
from matplotlib.text import Text
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection
from matplotlib.ticker import Formatter, Locator
from matplotlib.colors import Colormap
from matplotlib.axes import Axes
from matplotlib.axis import Tick
from matplotlib.spines import Spine

class _ColorbarSpine(Spine):
    def __init__(self, axes) -> None: ...
    def get_window_extent(self, renderer=...): ...
    def set_xy(self, xy): ...
    def draw(self, renderer): ...

class _ColorbarAxesLocator:
    """
    Shrink the axes if there are triangular or rectangular extends.
    """

    def __init__(self, cbar) -> None: ...
    def __call__(self, ax, renderer): ...
    def get_subplotspec(self): ...

class Colorbar:
    ax: Axes
    lines: list[LineCollection]
    dividers: LineCollection
    r"""
    Draw a colorbar in an existing axes.

    Typically, colorbars are created using `.Figure.colorbar` or
    `.pyplot.colorbar` and associated with `.ScalarMappable`\s (such as an
    `.AxesImage` generated via `~.axes.Axes.imshow`).

    In order to draw a colorbar not associated with other elements in the
    figure, e.g. when showing a colormap by itself, one can create an empty
    `.ScalarMappable`, or directly pass *cmap* and *norm* instead of *mappable*
    to `Colorbar`.

    Useful public methods are :meth:`set_label` and :meth:`add_lines`.

    Attributes
    ----------
    ax : `~Axes`
        The `~.axes.Axes` instance in which the colorbar is drawn.
    lines : list
        A list of `.LineCollection` (empty if no lines were drawn).
    dividers : `.LineCollection`
        A LineCollection (empty if *drawedges* is ``False``).

    Parameters
    ----------
    ax : `~Axes`
        The `~.axes.Axes` instance in which the colorbar is drawn.

    mappable : `.ScalarMappable`
        The mappable whose colormap and norm will be used.

        To show the under- and over- value colors, the mappable's norm should
        be specified as ::

            norm = colors.Normalize(clip=False)

        To show the colors versus index instead of on a 0-1 scale, use::

            norm=colors.NoNorm()

    cmap : `~Colormap`, default: :rc:`image.cmap`
        The colormap to use.  This parameter is ignored, unless *mappable* is
        None.

    norm : `~Normalize`
        The normalization to use.  This parameter is ignored, unless *mappable*
        is None.

    alpha : float
        The colorbar transparency between 0 (transparent) and 1 (opaque).

    orientation : {'vertical', 'horizontal'}

    ticklocation : {'auto', 'left', 'right', 'top', 'bottom'}

    drawedges : bool

    filled : bool
    %s
    """
    n_rasterize = ...

    def __init__(
        self,
        ax: Axes,
        mappable: ScalarMappable = ...,
        *,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        alpha: float = ...,
        values: None = ...,
        boundaries: None = ...,
        orientation: Literal["vertical", "horizontal"] = ...,
        ticklocation: Literal["auto", "left", "right", "top", "bottom"] = ...,
        extend: Literal["neither", "both", "min", "max"] = ...,
        spacing: Literal["uniform", "proportional"] = ...,
        ticks: None | Sequence[Tick] | Locator = ...,
        format: None | str | Formatter = ...,
        drawedges: bool = ...,
        filled: bool = ...,
        extendfrac=...,
        extendrect: bool = ...,
        label: str = ...
    ) -> None: ...
    @property
    def locator(self):
        """Major tick `.Locator` for the colorbar."""
        ...
    @locator.setter
    def locator(self, loc): ...
    @property
    def minorlocator(self):
        """Minor tick `.Locator` for the colorbar."""
        ...
    @minorlocator.setter
    def minorlocator(self, loc): ...
    @property
    def formatter(self):
        """Major tick label `.Formatter` for the colorbar."""
        ...
    @formatter.setter
    def formatter(self, fmt): ...
    @property
    def minorformatter(self):
        """Minor tick `.Formatter` for the colorbar."""
        ...
    @minorformatter.setter
    def minorformatter(self, fmt): ...

    patch = ...
    filled = ...
    def update_normal(self, mappable):
        """
        Update solid patches, lines, etc.

        This is meant to be called when the norm of the image or contour plot
        to which this colorbar belongs changes.

        If the norm on the mappable is different than before, this resets the
        locator and formatter for the axis, so if these have been customized,
        they will need to be customized again.  However, if the norm only
        changes values of *vmin*, *vmax* or *cmap* then the old formatter
        and locator will be preserved.
        """
        ...
    def draw_all(self):
        """
        Calculate any free parameters based on the current cmap and norm,
        and do all the drawing.
        """
        ...
    def add_lines(self, *args, **kwargs):
        """
        Draw lines on the colorbar.

        The lines are appended to the list :attr:`lines`.

        Parameters
        ----------
        levels : array-like
            The positions of the lines.
        colors : color or list of colors
            Either a single color applying to all lines or one color value for
            each line.
        linewidths : float or array-like
            Either a single linewidth applying to all lines or one linewidth
            for each line.
        erase : bool, default: True
            Whether to remove any previously added lines.

        Notes
        -----
        Alternatively, this method can also be called with the signature
        ``colorbar.add_lines(contour_set, erase=True)``, in which case
        *levels*, *colors*, and *linewidths* are taken from *contour_set*.
        """
        ...
    def update_ticks(self):
        """
        Setup the ticks and ticklabels. This should not be needed by users.
        """
        ...
    def set_ticks(
        self,
        ticks: list[float],
        update_ticks=...,
        labels: list[str] = ...,
        *,
        minor: bool = ...,
        **kwargs
    ):
        """
        Set tick locations.

        Parameters
        ----------
        ticks : list of floats
            List of tick locations.
        labels : list of str, optional
            List of tick labels. If not set, the labels show the data value.
        minor : bool, default: False
            If ``False``, set the major ticks; if ``True``, the minor ticks.
        **kwargs
            `.Text` properties for the labels. These take effect only if you
            pass *labels*. In other cases, please use `~.Axes.tick_params`.
        """
        ...
    def get_ticks(self, minor: bool = ...):
        """
        Return the ticks as a list of locations.

        Parameters
        ----------
        minor : boolean, default: False
            if True return the minor ticks.
        """
        ...
    def set_ticklabels(
        self, ticklabels: Text, update_ticks: bool = ..., *, minor=..., **kwargs
    ):
        """
        Set tick labels.

        .. admonition:: Discouraged

            The use of this method is discouraged, because of the dependency
            on tick positions. In most cases, you'll want to use
            ``set_ticks(positions, labels=labels)`` instead.

            If you are using this method, you should always fix the tick
            positions before, e.g. by using `.Colorbar.set_ticks` or by
            explicitly setting a `~.ticker.FixedLocator` on the long axis
            of the colorbar. Otherwise, ticks are free to move and the
            labels may end up in unexpected positions.

        Parameters
        ----------
        ticklabels : sequence of str or of `.Text`
            Texts for labeling each tick location in the sequence set by
            `.Colorbar.set_ticks`; the number of labels must match the number
            of locations.

        update_ticks : bool, default: True
            This keyword argument is ignored and will be be removed.
            Deprecated

         minor : bool
            If True, set minor ticks instead of major ticks.

        **kwargs
            `.Text` properties for the labels.
        """
        ...
    def minorticks_on(self):
        """
        Turn on colorbar minor ticks.
        """
        ...
    def minorticks_off(self):
        """Turn the minor ticks of the colorbar off."""
        ...
    def set_label(self, label: str, *, loc: str = ..., **kwargs):
        """
        Add a label to the long axis of the colorbar.

        Parameters
        ----------
        label : str
            The label text.
        loc : str, optional
            The location of the label.

            - For horizontal orientation one of {'left', 'center', 'right'}
            - For vertical orientation one of {'bottom', 'center', 'top'}

            Defaults to :rc:`xaxis.labellocation` or :rc:`yaxis.labellocation`
            depending on the orientation.
        **kwargs
            Keyword arguments are passed to `~.Axes.set_xlabel` /
            `~.Axes.set_ylabel`.
            Supported keywords are *labelpad* and `.Text` properties.
        """
        ...
    def set_alpha(self, alpha):
        """
        Set the transparency between 0 (transparent) and 1 (opaque).

        If an array is provided, *alpha* will be set to None to use the
        transparency values associated with the colormap.
        """
        ...
    def remove(self):
        """
        Remove this colorbar from the figure.

        If the colorbar was created with ``use_gridspec=True`` the previous
        gridspec is restored.
        """
        ...
    def drag_pan(self, button, key, x, y): ...

ColorbarBase = Colorbar

def make_axes(
    parents: Axes | list[Axes],
    location: None | Literal["left", "right", "top", "bottom"] = ...,
    orientation: None | Literal["vertical", "horizontal"] = ...,
    fraction: float = ...,
    shrink: float = ...,
    aspect: float = ...,
    **kwargs
):
    """
    Create an `~.axes.Axes` suitable for a colorbar.

    The axes is placed in the figure of the *parents* axes, by resizing and
    repositioning *parents*.

    Parameters
    ----------
    parents : `~.axes.Axes` or list of `~.axes.Axes`
        The Axes to use as parents for placing the colorbar.
    %s

    Returns
    -------
    cax : `~.axes.Axes`
        The child axes.
    kwargs : dict
        The reduced keyword dictionary to be passed when creating the colorbar
        instance.
    """
    ...

def make_axes_gridspec(
    parent: Axes,
    *,
    location: None | Literal["left", "right", "top", "bottom"] = ...,
    orientation: None | Literal["vertical", "horizontal"] = ...,
    fraction: float = ...,
    shrink: float = ...,
    aspect: float = ...,
    **kwargs
):
    """
    Create a `.SubplotBase` suitable for a colorbar.

    The axes is placed in the figure of the *parent* axes, by resizing and
    repositioning *parent*.

    This function is similar to `.make_axes`. Primary differences are

    - `.make_axes_gridspec` should only be used with a `.SubplotBase` parent.

    - `.make_axes` creates an `~.axes.Axes`; `.make_axes_gridspec` creates a
      `.SubplotBase`.

    - `.make_axes` updates the position of the parent.  `.make_axes_gridspec`
      replaces the ``grid_spec`` attribute of the parent with a new one.

    While this function is meant to be compatible with `.make_axes`,
    there could be some minor differences.

    Parameters
    ----------
    parent : `~.axes.Axes`
        The Axes to use as parent for placing the colorbar.
    %s

    Returns
    -------
    cax : `~.axes.SubplotBase`
        The child axes.
    kwargs : dict
        The reduced keyword dictionary to be passed when creating the colorbar
        instance.
    """
    ...
