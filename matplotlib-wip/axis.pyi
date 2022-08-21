import datetime
from .cbook import CallbackRegistry
from .transforms import Transform
import numpy as np
from typing import Any, Callable, Literal, Type
from .text import Text
from .backend_bases import MouseEvent
from .lines import Line2D
from .axes import Axes
from .artist import Artist, allow_rasterization

from units.basic_units import BasicUnit

from .backend_bases import RendererBase
from datetime import timezone
from .backends.backend_mixed import MixedModeRenderer
from .patches import Patch
from .ticker import (
    Formatter,
    Locator,
)

GRIDLINE_INTERPOLATION_STEPS = ...

class Tick(Artist):
    """
    Abstract base class for the axis ticks, grid lines and labels.

    Ticks mark a position on an Axis. They contain two lines as markers and
    two labels; one each for the bottom and top positions (in case of an
    `.XAxis`) or for the left and right positions (in case of a `.YAxis`).

    Attributes
    ----------
    tick1line : `.Line2D`
        The left/bottom tick marker.
    tick2line : `.Line2D`
        The right/top tick marker.
    gridline : `.Line2D`
        The grid line associated with the label position.
    label1 : `.Text`
        The left/bottom tick label.
    label2 : `.Text`
        The right/top tick label.

    """

    tick1line: Line2D
    tick2line: Line2D
    gridline: Line2D
    label1: Text
    label2: Text

    def __init__(
        self,
        axes,
        loc,
        *,
        size=...,
        width=...,
        color=...,
        tickdir=...,
        pad=...,
        labelsize=...,
        labelcolor=...,
        zorder=...,
        gridOn=...,
        tick1On=...,
        tick2On=...,
        label1On=...,
        label2On=...,
        major=...,
        labelrotation=...,
        grid_color=...,
        grid_linestyle=...,
        grid_linewidth=...,
        grid_alpha=...,
        **kwargs
    ) -> None:
        """
        bbox is the Bound2D bounding box in display coords of the Axes
        loc is the tick location in data coords
        size is the tick size in points
        """
        ...
    @property
    def label(self): ...
    def apply_tickdir(self, tickdir): ...
    def get_tickdir(self): ...
    def get_tick_padding(self) -> float:
        """Get the length of the tick outside of the Axes."""
        ...
    def get_children(self): ...
    def set_clip_path(
        self, clippath: Patch, transform: Transform | None = ...
    ) -> None: ...
    def get_pad_pixels(self): ...
    def contains(self, mouseevent) -> bool:
        """
        Test whether the mouse event occurred in the Tick marks.

        This function always returns false.  It is more useful to test if the
        axis as a whole contains the mouse rather than the set of tick marks.
        """
        ...
    def set_pad(self, val: float) -> None:
        """
        Set the tick label pad in points

        Parameters
        ----------
        val : float
        """
        ...
    def get_pad(self) -> float:
        """Get the value of the tick label pad in points."""
        ...
    def get_loc(self) -> int:
        """Return the tick location (data coords) as a scalar."""
        ...
    @allow_rasterization
    def draw(self, renderer) -> None: ...
    def set_label1(self, s: str) -> None:
        """
        Set the label1 text.

        Parameters
        ----------
        s : str
        """
        ...
    set_label = ...
    def set_label2(self, s: str) -> None:
        """
        Set the label2 text.

        Parameters
        ----------
        s : str
        """
        ...
    def set_url(self, url: str) -> None:
        """
        Set the url of label1 and label2.

        Parameters
        ----------
        url : str
        """
        ...
    def get_view_interval(self) -> tuple:
        """
        Return the view limits ``(min, max)`` of the axis the tick belongs to.
        """
        ...
    def update_position(self, loc) -> None:
        """Set the location of tick in data coords with scalar *loc*."""
        ...

class XTick(Tick):
    """
    Contains all the Artists needed to make an x tick - the tick line,
    the label text and the grid line
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc: int) -> None:
        """Set the location of tick in data coords with scalar *loc*."""
        ...
    def get_view_interval(self): ...

class YTick(Tick):
    """
    Contains all the Artists needed to make a Y tick - the tick line,
    the label text and the grid line
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc: int) -> None:
        """Set the location of tick in data coords with scalar *loc*."""
        ...
    def get_view_interval(self): ...

class Ticker:
    """
    A container for the objects defining tick position and format.

    Attributes
    ----------
    locator : `Locator` subclass
        Determines the positions of the ticks.
    formatter : `Formatter` subclass
        Determines the format of the tick labels.
    """

    def __init__(self) -> None: ...
    @property
    def locator(self): ...
    @locator.setter
    def locator(self, locator): ...
    @property
    def formatter(self): ...
    @formatter.setter
    def formatter(self, formatter): ...

class _LazyTickList:
    """
    A descriptor for lazy instantiation of tick lists.

    See comment above definition of the ``majorTicks`` and ``minorTicks``
    attributes.
    """

    def __init__(self, major: bool) -> None: ...
    def __get__(
        self, instance: XAxis | YAxis, cls: Type[XAxis] | Type[YAxis]
    ) -> list[XTick | YTick]: ...

class Axis(Artist):

    isDefault_label: bool
    axes: Axes
    major: Ticker
    minor: Ticker
    callbacks: CallbackRegistry
    label: Text
    labelpad: float = 4
    offsetText: Text
    pickradius: float
    majorTicks: list[Tick]
    minorTicks: list[Tick]

    OFFSETTEXTPAD = ...

    def __str__(self) -> str: ...
    def __init__(self, axes: Axes, pickradius: float = ...) -> None:
        """
        Parameters
        ----------
        axes : `Axes`
            The `~.axes.Axes` to which the created Axis belongs.
        pickradius : float
            The acceptance radius for containment tests. See also
            `.Axis.contains`.
        """
        ...
    @property
    def isDefault_majloc(self): ...
    @isDefault_majloc.setter
    def isDefault_majloc(self, value): ...
    @property
    def isDefault_majfmt(self): ...
    @isDefault_majfmt.setter
    def isDefault_majfmt(self, value): ...
    @property
    def isDefault_minloc(self): ...
    @isDefault_minloc.setter
    def isDefault_minloc(self, value): ...
    @property
    def isDefault_minfmt(self): ...
    @isDefault_minfmt.setter
    def isDefault_minfmt(self, value): ...

    majorTicks = ...
    minorTicks = ...
    def get_remove_overlapping_locs(self) -> bool: ...
    def set_remove_overlapping_locs(self, val): ...

    remove_overlapping_locs = ...
    def set_label_coords(self, x: float, y: float, transform: None = ...) -> None:
        """
        Set the coordinates of the label.

        By default, the x coordinate of the y label and the y coordinate of the
        x label are determined by the tick label bounding boxes, but this can
        lead to poor alignment of multiple labels if there are multiple axes.

        You can also specify the coordinate system of the label with the
        transform.  If None, the default coordinate system will be the axes
        coordinate system: (0, 0) is bottom left, (0.5, 0.5) is center, etc.
        """
        ...
    def get_transform(self): ...
    def get_scale(self) -> str:
        """Return this Axis' scale (as a str)."""
        ...
    def limit_range_for_scale(
        self, vmin: float, vmax: float
    ) -> tuple[float, float]: ...
    def get_children(self): ...
    def clear(self) -> None:
        """
        Clear the axis.

        This resets axis properties to their default values:

        - the label
        - the scale
        - locators, formatters and ticks
        - major and minor grid
        - units
        - registered callbacks

        This does not reset tick and tick label visibility.
        """
        ...
    def reset_ticks(self) -> None:
        """
        Re-initialize the major and minor Tick lists.

        Each list starts with a single fresh Tick.
        """
        ...
    def set_tick_params(self, which: str = ..., reset: bool = ..., **kwargs) -> None:
        """
        Set appearance parameters for ticks, ticklabels, and gridlines.

        For documentation of keyword arguments, see
        :meth:`Axes.tick_params`.
        """
        ...
    def set_clip_path(
        self, clippath: Patch, transform: Transform | None = ...
    ) -> None: ...
    def get_view_interval(self) -> tuple:
        """Return the ``(min, max)`` view limits of this axis."""
        ...
    def set_view_interval(self, vmin, vmax, ignore: bool = ...):
        """
        Set the axis view limits.  This method is for internal use; Matplotlib
        users should typically use e.g. `~.Axes.set_xlim` or `~.Axes.set_ylim`.

        If *ignore* is False (the default), this method will never reduce the
        preexisting view limits, only expand them if *vmin* or *vmax* are not
        within them.  Moreover, the order of *vmin* and *vmax* does not matter;
        the orientation of the axis will not change.

        If *ignore* is True, the view limits will be set exactly to ``(vmin,
        vmax)`` in that order.
        """
        ...
    def get_data_interval(self) -> tuple:
        """Return the ``(min, max)`` data limits of this axis."""
        ...
    def set_data_interval(self, vmin, vmax, ignore: bool = ...):
        """
        Set the axis data limits.  This method is for internal use.

        If *ignore* is False (the default), this method will never reduce the
        preexisting data limits, only expand them if *vmin* or *vmax* are not
        within them.  Moreover, the order of *vmin* and *vmax* does not matter;
        the orientation of the axis will not change.

        If *ignore* is True, the data limits will be set exactly to ``(vmin,
        vmax)`` in that order.
        """
        ...
    def get_inverted(self) -> bool:
        """
        Return whether this Axis is oriented in the "inverse" direction.

        The "normal" direction is increasing to the right for the x-axis and to
        the top for the y-axis; the "inverse" direction is increasing to the
        left for the x-axis and to the bottom for the y-axis.
        """
        ...
    def set_inverted(self, inverted: bool) -> None:
        """
        Set whether this Axis is oriented in the "inverse" direction.

        The "normal" direction is increasing to the right for the x-axis and to
        the top for the y-axis; the "inverse" direction is increasing to the
        left for the x-axis and to the bottom for the y-axis.
        """
        ...
    def set_default_intervals(self):
        """
        Set the default limits for the axis data and view interval if they
        have not been not mutated yet.
        """
        ...
    def get_ticklabel_extents(self, renderer: RendererBase):
        """Get the extents of the tick labels on either side of the axes."""
        ...
    def get_tightbbox(self, renderer: MixedModeRenderer = ..., *, for_layout_only=...):
        """
        Return a bounding box that encloses the axis. It only accounts
        tick labels, axis label, and offsetText.

        If *for_layout_only* is True, then the width of the label (if this
        is an x-axis) or the height of the label (if this is a y-axis) is
        collapsed to near zero.  This allows tight/constrained_layout to ignore
        too-long labels when doing their layout.
        """
        ...
    def get_tick_padding(self): ...
    @allow_rasterization
    def draw(self, renderer, *args, **kwargs): ...
    def get_gridlines(self) -> list[Line2D]:
        r"""Return this Axis' grid lines as a list of `.Line2D`\s."""
        ...
    def get_label(self) -> Text:
        """Return the axis label as a Text instance."""
        ...
    def get_offset_text(self) -> Text:
        """Return the axis offsetText as a Text instance."""
        ...
    def get_pickradius(self):
        """Return the depth of the axis used by the picker."""
        ...
    def get_majorticklabels(self) -> list[Text]:
        """Return this Axis' major tick labels, as a list of `~.text.Text`."""
        ...
    def get_minorticklabels(self) -> list[Text]:
        """Return this Axis' minor tick labels, as a list of `~.text.Text`."""
        ...
    def get_ticklabels(
        self, minor: bool = ..., which: None | Literal["minor", "major", "both"] = ...
    ) -> list[Text]:
        """
        Get this Axis' tick labels.

        Parameters
        ----------
        minor : bool
           Whether to return the minor or the major ticklabels.

        which : None, ('minor', 'major', 'both')
           Overrides *minor*.

           Selects which ticklabels to return

        Returns
        -------
        list of `~Text`
        """
        ...
    def get_majorticklines(self) -> list[Line2D]:
        r"""Return this Axis' major tick lines as a list of `.Line2D`\s."""
        ...
    def get_minorticklines(self) -> list[Line2D]:
        r"""Return this Axis' minor tick lines as a list of `.Line2D`\s."""
        ...
    def get_ticklines(self, minor=...) -> list[Line2D]:
        r"""Return this Axis' tick lines as a list of `.Line2D`\s."""
        ...
    def get_majorticklocs(self) -> list:
        """Return this Axis' major tick locations in data coordinates."""
        ...
    def get_minorticklocs(self) -> list:
        """Return this Axis' minor tick locations in data coordinates."""
        ...
    def get_ticklocs(self, *, minor=...) -> list:
        """Return this Axis' tick locations in data coordinates."""
        ...
    def get_ticks_direction(self, minor: bool = False) -> np.ndarray:
        """
        Get the tick directions as a numpy array

        Parameters
        ----------
        minor : bool, default: False
            True to return the minor tick directions,
            False to return the major tick directions.

        Returns
        -------
        numpy array of tick directions
        """
        ...
    def get_label_text(self) -> str:
        """Get the text of the label."""
        ...
    def get_major_locator(self) -> Locator:
        """Get the locator of the major ticker."""
        ...
    def get_minor_locator(
        self,
    ) -> Locator:
        """Get the locator of the minor ticker."""
        ...
    def get_major_formatter(
        self,
    ) -> Formatter:
        """Get the formatter of the major ticker."""
        ...
    def get_minor_formatter(self) -> Formatter:
        """Get the formatter of the minor ticker."""
        ...
    def get_major_ticks(self, numticks: None | int = ...) -> list[XTick | YTick]:
        r"""Return the list of major `.Tick`\s."""
        ...
    def get_minor_ticks(self, numticks: None | int = ...) -> list[XTick | YTick]:
        r"""Return the list of minor `.Tick`\s."""
        ...
    def grid(self, visible: bool | None = ..., which: str = ..., **kwargs) -> None:
        """
        Configure the grid lines.

        Parameters
        ----------
        visible : bool or None
            Whether to show the grid lines.  If any *kwargs* are supplied, it
            is assumed you want the grid on and *visible* will be set to True.

            If *visible* is *None* and there are no *kwargs*, this toggles the
            visibility of the lines.

        which : {'major', 'minor', 'both'}
            The grid lines to apply the changes on.

        **kwargs : `.Line2D` properties
            Define the line properties of the grid, e.g.::

                grid(color='r', linestyle='-', linewidth=2)
        """
        ...
    def update_units(self, data: Any) -> bool:
        """
        Introspect *data* for units converter and update the
        axis.converter instance if necessary. Return *True*
        if *data* is registered for unit conversion.
        """
        ...
    def have_units(self) -> bool: ...
    def convert_units(self, x): ...
    def set_units(self, u: None | timezone | float | BasicUnit) -> None:
        """
        Set the units for axis.

        Parameters
        ----------
        u : units tag

        Notes
        -----
        The units of any shared axis will also be updated.
        """
        ...
    def get_units(self) -> None | timezone | float | BasicUnit:
        """Return the units for axis."""
        ...
    def set_label_text(self, label: str, fontdict: dict = ..., **kwargs):
        """
        Set the text value of the axis label.

        Parameters
        ----------
        label : str
            Text string.
        fontdict : dict
            Text properties.
        **kwargs
            Merged into fontdict.
        """
        ...
    def set_major_formatter(self, formatter: Formatter | str | Callable) -> None:
        """
        Set the formatter of the major ticker.

        In addition to a `~Formatter` instance,
        this also accepts a ``str`` or function.

        For a ``str`` a `~matplotlib.ticker.StrMethodFormatter` is used.
        The field used for the value must be labeled ``'x'`` and the field used
        for the position must be labeled ``'pos'``.
        See the  `~matplotlib.ticker.StrMethodFormatter` documentation for
        more information.

        For a function, a `~matplotlib.ticker.FuncFormatter` is used.
        The function must take two inputs (a tick value ``x`` and a
        position ``pos``), and return a string containing the corresponding
        tick label.
        See the  `~matplotlib.ticker.FuncFormatter` documentation for
        more information.

        Parameters
        ----------
        formatter : `~Formatter`, ``str``, or function
        """
        ...
    def set_minor_formatter(self, formatter: Formatter | str | Callable) -> None:
        """
        Set the formatter of the minor ticker.

        In addition to a `~Formatter` instance,
        this also accepts a ``str`` or function.
        See `.Axis.set_major_formatter` for more information.

        Parameters
        ----------
        formatter : `~Formatter`, ``str``, or function
        """
        ...
    def set_major_locator(self, locator: Locator) -> None:
        """
        Set the locator of the major ticker.

        Parameters
        ----------
        locator : `~Locator`
        """
        ...
    def set_minor_locator(self, locator: Locator) -> None:
        """
        Set the locator of the minor ticker.

        Parameters
        ----------
        locator : `~Locator`
        """
        ...
    def set_pickradius(self, pickradius: float):
        """
        Set the depth of the axis used by the picker.

        Parameters
        ----------
        pickradius :  float
        """
        ...
    def set_ticklabels(
        self, ticklabels: list[str | Text], *, minor: bool = ..., **kwargs
    ) -> list[Text]:
        r"""
        Set the text values of the tick labels.

        .. admonition:: Discouraged

            The use of this method is discouraged, because of the dependency
            on tick positions. In most cases, you'll want to use
            ``set_[x/y]ticks(positions, labels)`` instead.

            If you are using this method, you should always fix the tick
            positions before, e.g. by using `.Axis.set_ticks` or by explicitly
            setting a `~.ticker.FixedLocator`. Otherwise, ticks are free to
            move and the labels may end up in unexpected positions.

        Parameters
        ----------
        ticklabels : sequence of str or of `.Text`\s
            Texts for labeling each tick location in the sequence set by
            `.Axis.set_ticks`; the number of labels must match the number of
            locations.
        minor : bool
            If True, set minor ticks instead of major ticks.
        **kwargs
            Text properties.

        Returns
        -------
        list of `.Text`\s
            For each tick, includes ``tick.label1`` if it is visible, then
            ``tick.label2`` if it is visible, in that order.
        """
        ...
    def set_ticks(
        self,
        ticks: list[float],
        labels: None | list[str] = ...,
        *,
        minor: bool = ...,
        **kwargs
    ) -> list[XTick | YTick]:
        """
        Set this Axis' tick locations and optionally labels.

        If necessary, the view limits of the Axis are expanded so that all
        given ticks are visible.

        Parameters
        ----------
        ticks : list of floats
            List of tick locations.  The axis `.Locator` is replaced by a
            `~.ticker.FixedLocator`.

            Some tick formatters will not label arbitrary tick positions;
            e.g. log formatters only label decade ticks by default. In
            such a case you can set a formatter explicitly on the axis
            using `.Axis.set_major_formatter` or provide formatted
            *labels* yourself.
        labels : list of str, optional
            List of tick labels. If not set, the labels are generated with
            the axis tick `.Formatter`.
        minor : bool, default: False
            If ``False``, set the major ticks; if ``True``, the minor ticks.
        **kwargs
            `.Text` properties for the labels. These take effect only if you
            pass *labels*. In other cases, please use `~.Axes.tick_params`.

        Notes
        -----
        The mandatory expansion of the view limits is an intentional design
        choice to prevent the surprise of a non-visible tick. If you need
        other limits, you should set the limits explicitly after setting the
        ticks.
        """
        ...
    def axis_date(self, tz: str | datetime.tzinfo = ...):
        """
        Set up axis ticks and labels to treat data along this Axis as dates.

        Parameters
        ----------
        tz : str or `datetime.tzinfo`, default: :rc:`timezone`
            The timezone used to create date labels.
        """
        ...
    def get_tick_space(self) -> int:
        """Return the estimated number of ticks that can fit on the axis."""
        ...
    def get_label_position(self) -> str:
        """
        Return the label position (top or bottom)
        """
        ...
    def set_label_position(self, position: Literal["top", "bottom"]):
        """
        Set the label position (top or bottom)

        Parameters
        ----------
        position : {'top', 'bottom'}
        """
        ...
    def get_minpos(self): ...

class XAxis(Axis):

    axis_name = ...
    _tick_class = XTick
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent) -> bool:
        """Test whether the mouse event occurred in the x axis."""
        ...
    def set_label_position(self, position: Literal["top", "bottom"]) -> None:
        """
        Set the label position (top or bottom)

        Parameters
        ----------
        position : {'top', 'bottom'}
        """
        ...
    def get_text_heights(self, renderer) -> tuple[float, float]:
        """
        Return how much space should be reserved for text above and below the
        Axes, as a pair of floats.
        """
        ...
    def set_ticks_position(
        self, position: Literal["top", "bottom", "both", "default", "none"]
    ) -> None:
        """
        Set the ticks position.

        Parameters
        ----------
        position : {'top', 'bottom', 'both', 'default', 'none'}
            'both' sets the ticks to appear on both positions, but does not
            change the tick labels.  'default' resets the tick positions to
            the default: ticks on both positions, labels at bottom.  'none'
            can be used if you don't want any ticks. 'none' and 'both'
            affect only the ticks, not the labels.
        """
        ...
    def tick_top(self) -> None:
        """
        Move ticks and ticklabels (if present) to the top of the Axes.
        """
        ...
    def tick_bottom(self) -> None:
        """
        Move ticks and ticklabels (if present) to the bottom of the Axes.
        """
        ...
    def get_ticks_position(self) -> str:
        """
        Return the ticks position ("top", "bottom", "default", or "unknown").
        """
        ...
    def get_minpos(self): ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self) -> int: ...

class YAxis(Axis):

    axis_name = ...
    _tick_class = YTick
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def set_label_position(self, position: Literal["left", "right"]) -> None:
        """
        Set the label position (left or right)

        Parameters
        ----------
        position : {'left', 'right'}
        """
        ...
    def set_offset_position(self, position: Literal["left", "right"]) -> None:
        """
        Parameters
        ----------
        position : {'left', 'right'}
        """
        ...
    def get_text_widths(self, renderer): ...
    def set_ticks_position(
        self, position: Literal["left", "right", "both", "default", "none"]
    ) -> None:
        """
        Set the ticks position.

        Parameters
        ----------
        position : {'left', 'right', 'both', 'default', 'none'}
            'both' sets the ticks to appear on both positions, but does not
            change the tick labels.  'default' resets the tick positions to
            the default: ticks on both positions, labels at left.  'none'
            can be used if you don't want any ticks. 'none' and 'both'
            affect only the ticks, not the labels.
        """
        ...
    def tick_right(self) -> None:
        """
        Move ticks and ticklabels (if present) to the right of the Axes.
        """
        ...
    def tick_left(self) -> None:
        """
        Move ticks and ticklabels (if present) to the left of the Axes.
        """
        ...
    def get_ticks_position(self) -> str:
        """
        Return the ticks position ("left", "right", "default", or "unknown").
        """
        ...
    def get_minpos(self): ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self) -> int: ...
