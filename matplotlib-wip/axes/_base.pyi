from matplotlib.axis import XAxis, YAxis
from matplotlib.image import AxesImage
from matplotlib.legend import Legend
from matplotlib.table import Table
import numpy as np
from typing import Any, Callable, Collection, Literal, Sequence, overload
from matplotlib._typing import *
from matplotlib.transforms import Bbox, BboxBase, Transform
from matplotlib.backend_bases import RendererBase
from matplotlib.patches import Patch
from matplotlib.backend_bases import MouseButton, MouseEvent
from matplotlib.container import Container
from matplotlib.lines import Line2D
from matplotlib.figure import Figure
from matplotlib.scale import ScaleBase
from matplotlib.artist import Artist, allow_rasterization
from ._axes import Axes

class _axis_method_wrapper:
    def __init__(self, attr_name, method_name, *, doc_sub=...) -> None: ...
    def __set_name__(self, owner, name): ...

class _AxesBase(Artist):
    name = ...

    def __str__(self) -> str: ...
    def __init__(
        self,
        fig: Figure,
        rect: Sequence[float],
        *,
        facecolor=...,
        frameon: bool = True,
        sharex: Axes = ...,
        sharey: Axes = ...,
        label=...,
        xscale=...,
        yscale=...,
        box_aspect: float = ...,
        **kwargs
    ) -> None: ...
    def __getstate__(self): ...
    def __setstate__(self, state): ...
    def __repr__(self): ...
    def get_window_extent(self, renderer=..., *args, **kwargs) -> Sequence[float]: ...
    def set_figure(self, fig: Figure): ...
    @property
    def viewLim(self): ...
    def get_xaxis_transform(self, which=...) -> Transform: ...
    def get_xaxis_text1_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_xaxis_text2_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_yaxis_transform(self, which=...) -> Transform: ...
    def get_yaxis_text1_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_yaxis_text2_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_position(self, original: bool = ...) -> Bbox: ...
    def set_position(
        self,
        pos: Sequence[float] | Bbox,
        which: Literal["both", "active", "original"] = ...,
    ) -> None: ...
    def reset_position(self) -> None: ...
    def set_axes_locator(
        self, locator: Callable[[Axes, RendererBase], Bbox]
    ) -> None: ...
    def get_axes_locator(self):
        """
        Return the axes_locator.
        """
        ...
    def sharex(self, other: Axes) -> None: ...
    def sharey(self, other: Axes) -> None: ...
    def clear(self) -> None: ...
    @property
    def artists(self): ...
    @property
    def collections(self): ...
    @property
    def images(self): ...
    @property
    def lines(self): ...
    @property
    def patches(self): ...
    @property
    def tables(self): ...
    @property
    def texts(self): ...
    def cla(self) -> None:
        """Clear the Axes."""
        ...
    def get_facecolor(self) -> Color:
        """Get the facecolor of the Axes."""
        ...
    def set_facecolor(self, color: Color): ...
    def set_prop_cycle(self, *args, **kwargs):
        """
        Set the property cycle of the Axes.

        The property cycle controls the style properties such as color,
        marker and linestyle of future plot commands. The style properties
        of data already added to the Axes are not modified.

        Call signatures::

          set_prop_cycle(cycler)
          set_prop_cycle(label=values[, label2=values2[, ...]])
          set_prop_cycle(label, values)

        Form 1 sets given `~cycler.Cycler` object.

        Form 2 creates a `~cycler.Cycler` which cycles over one or more
        properties simultaneously and set it as the property cycle of the
        Axes. If multiple properties are given, their value lists must have
        the same length. This is just a shortcut for explicitly creating a
        cycler and passing it to the function, i.e. it's short for
        ``set_prop_cycle(cycler(label=values label2=values2, ...))``.

        Form 3 creates a `~cycler.Cycler` for a single property and set it
        as the property cycle of the Axes. This form exists for compatibility
        with the original `cycler.cycler` interface. Its use is discouraged
        in favor of the kwarg form, i.e. ``set_prop_cycle(label=values)``.

        Parameters
        ----------
        cycler : Cycler
            Set the given Cycler. *None* resets to the cycle defined by the
            current style.

        label : str
            The property key. Must be a valid `.Artist` property.
            For example, 'color' or 'linestyle'. Aliases are allowed,
            such as 'c' for 'color' and 'lw' for 'linewidth'.

        values : iterable
            Finite-length iterable of the property values. These values
            are validated and will raise a ValueError if invalid.

        See Also
        --------
        matplotlib.rcsetup.cycler
            Convenience function for creating validated cyclers for properties.
        cycler.cycler
            The original function for creating unvalidated cyclers.

        Examples
        --------
        Setting the property cycle for a single property:

        >>> ax.set_prop_cycle(color=['red', 'green', 'blue'])

        Setting the property cycle for simultaneously cycling over multiple
        properties (e.g. red circle, green plus, blue cross):

        >>> ax.set_prop_cycle(color=['red', 'green', 'blue'],
        ...                   marker=['o', '+', 'x'])

        """
        ...
    def get_aspect(self) -> Literal["auto"] | float: ...
    def set_aspect(
        self,
        aspect: Literal["auto", "equal"] | float,
        adjustable: None | Literal["box", "datalim"] = ...,
        anchor: None | str | Sequence[float] = ...,
        share: bool = False,
    ): ...
    def get_adjustable(self) -> str: ...
    def set_adjustable(
        self, adjustable: Literal["box", "datalim"], share: bool = False
    ): ...
    def get_box_aspect(self) -> float | None: ...
    def set_box_aspect(self, aspect: float | None = ...) -> None: ...
    def get_anchor(self) -> str: ...
    def set_anchor(
        self,
        anchor: Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        share: bool = False,
    ): ...
    def get_data_ratio(self): ...
    def apply_aspect(self, position=...): ...
    def axis(self, *args, emit: bool = ..., **kwargs):
        """
        Convenience method to get or set some axis properties.

        Call signatures::

          xmin, xmax, ymin, ymax = axis()
          xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
          xmin, xmax, ymin, ymax = axis(option)
          xmin, xmax, ymin, ymax = axis(**kwargs)

        Parameters
        ----------
        xmin, xmax, ymin, ymax : float, optional
            The axis limits to be set.  This can also be achieved using ::

                ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

        option : bool or str
            If a bool, turns axis lines and labels on or off. If a string,
            possible values are:

            ======== ==========================================================
            Value    Description
            ======== ==========================================================
            'on'     Turn on axis lines and labels. Same as ``True``.
            'off'    Turn off axis lines and labels. Same as ``False``.
            'equal'  Set equal scaling (i.e., make circles circular) by
                     changing axis limits. This is the same as
                     ``ax.set_aspect('equal', adjustable='datalim')``.
                     Explicit data limits may not be respected in this case.
            'scaled' Set equal scaling (i.e., make circles circular) by
                     changing dimensions of the plot box. This is the same as
                     ``ax.set_aspect('equal', adjustable='box', anchor='C')``.
                     Additionally, further autoscaling will be disabled.
            'tight'  Set limits just large enough to show all data, then
                     disable further autoscaling.
            'auto'   Automatic scaling (fill plot box with data).
            'image'  'scaled' with axis limits equal to data limits.
            'square' Square plot; similar to 'scaled', but initially forcing
                     ``xmax-xmin == ymax-ymin``.
            ======== ==========================================================

        emit : bool, default: True
            Whether observers are notified of the axis limit change.
            This option is passed on to `~.Axes.set_xlim` and
            `~.Axes.set_ylim`.

        Returns
        -------
        xmin, xmax, ymin, ymax : float
            The axis limits.

        See Also
        --------
        Axes.set_xlim
        Axes.set_ylim
        """
        ...
    def get_legend(self) -> Legend | None:
        """Return the `.Legend` instance, or None if no legend is defined."""
        ...
    def get_images(self) -> list[AxesImage]: ...
    def get_lines(self) -> list[Line2D]: ...
    def get_xaxis(self) -> XAxis: ...
    def get_yaxis(self) -> YAxis: ...
    get_xgridlines = ...
    get_xticklines = ...
    get_ygridlines = ...
    get_yticklines = ...
    def has_data(self) -> bool: ...
    def add_artist(self, a: Artist) -> Artist: ...
    def add_child_axes(self, ax: _AxesBase) -> Axes: ...
    def add_collection(self, collection: Collection, autolim=...) -> Collection: ...
    def add_image(self, image: AxesImage) -> AxesImage: ...
    def add_line(self, line: Line2D) -> Line2D: ...
    def add_patch(self, p: Patch) -> Patch: ...
    def add_table(self, tab: Table) -> Table: ...
    def add_container(self, container: Container) -> Container: ...
    def relim(self, visible_only: bool = ...): ...
    def update_datalim(self, xys, updatex: bool = ..., updatey: bool = ...): ...
    def in_axes(self, mouseevent) -> bool: ...
    get_autoscalex_on = ...
    get_autoscaley_on = ...
    set_autoscalex_on = ...
    set_autoscaley_on = ...
    def get_autoscale_on(self) -> bool: ...
    def set_autoscale_on(self, b: bool): ...
    @property
    def use_sticky_edges(self) -> bool: ...
    @use_sticky_edges.setter
    def use_sticky_edges(self, b): ...
    def set_xmargin(self, m: float): ...
    def set_ymargin(self, m: float): ...
    def margins(
        self, *margins, x: float = ..., y: float = ..., tight: bool | None = True
    ) -> tuple[float, float]: ...
    def set_rasterization_zorder(self, z: float | None) -> None: ...
    def get_rasterization_zorder(self) -> float: ...
    def autoscale(
        self,
        enable: bool | None = ...,
        axis: Literal["both", "x", "y"] = ...,
        tight: bool | None = ...,
    ) -> None: ...
    def autoscale_view(
        self, tight: bool | None = ..., scalex: bool = True, scaley: bool = True
    ) -> None: ...
    @allow_rasterization
    def draw(self, renderer): ...
    def draw_artist(self, a: Artist) -> None: ...
    def redraw_in_frame(self) -> None: ...
    def get_renderer_cache(self): ...
    def get_frame_on(self) -> bool: ...
    def set_frame_on(self, b: bool) -> None: ...
    def get_axisbelow(self) -> tuple[bool, Literal["line"]]: ...
    def set_axisbelow(self, b: bool | Literal["line"]) -> None: ...
    def grid(
        self,
        visible: bool | None = ...,
        which: Literal["major", "minor", "both"] = ...,
        axis: Literal["both", "x", "y"] = ...,
        **kwargs
    ) -> None: ...
    def ticklabel_format(
        self,
        *,
        axis: Literal["x", "y", "both"] = ...,
        style: Literal["sci", "scientific", "plain"] = ...,
        scilimits=...,
        useOffset: bool | float = ...,
        useLocale: bool = ...,
        useMathText: bool = ...
    ): ...
    def locator_params(
        self, axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
    ) -> None: ...
    def tick_params(self, axis: Literal["x", "y", "both"] = ..., **kwargs) -> None: ...
    def set_axis_off(self) -> None: ...
    def set_axis_on(self) -> None: ...
    def get_xlabel(self) -> str: ...
    def set_xlabel(
        self,
        xlabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["left", "center", "right"] = ...,
        **kwargs
    ): ...
    def invert_xaxis(self) -> None: ...
    xaxis_inverted = ...
    def get_xbound(self) -> tuple[float, float]: ...
    def set_xbound(
        self, lower: float | None = ..., upper: float | None = ...
    ) -> None: ...
    def get_xlim(self) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: tuple[float | np.datetime64, float | np.datetime64],
        *,
        emit: bool = ...,
        auto: bool | None = ...,
        xmin: float = ...,
        xmax: float = ...
    ) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: float | np.datetime64 = ...,
        right: float | np.datetime64 = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        xmin: float = ...,
        xmax: float = ...
    ) -> tuple[float, float]: ...
    def get_xscale(self) -> str: ...
    def set_xscale(
        self, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    ): ...
    get_xticks = ...
    set_xticks = ...
    get_xmajorticklabels = ...
    get_xminorticklabels = ...
    get_xticklabels = ...
    set_xticklabels = ...
    def get_ylabel(self) -> str: ...
    def set_ylabel(
        self,
        ylabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["bottom", "center", "top"] = ...,
        **kwargs
    ) -> None: ...
    def invert_yaxis(self) -> None: ...
    yaxis_inverted = ...
    def get_ybound(self) -> tuple[float, float]: ...
    def set_ybound(
        self, lower: float | None = ..., upper: float | None = ...
    ) -> None: ...
    def get_ylim(self) -> tuple[float, float]: ...
    def set_ylim(
        self,
        bottom: float = ...,
        top: float = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        ymin: float = ...,
        ymax: float = ...
    ): ...
    get_yscale = ...
    def set_yscale(
        self, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    ) -> None: ...
    get_yticks = ...
    set_yticks = ...
    get_ymajorticklabels = ...
    get_yminorticklabels = ...
    get_yticklabels = ...
    set_yticklabels = ...
    xaxis_date = ...
    yaxis_date = ...
    def format_xdata(self, x) -> str: ...
    def format_ydata(self, y) -> str: ...
    def format_coord(self, x, y) -> str: ...
    def minorticks_on(self) -> None: ...
    def minorticks_off(self) -> None: ...
    def can_zoom(self) -> bool: ...
    def can_pan(self) -> bool: ...
    def get_navigate(self) -> bool: ...
    def set_navigate(self, b: bool) -> None: ...
    def get_navigate_mode(self) -> str | None: ...
    def set_navigate_mode(self, b: str | None) -> None: ...
    def start_pan(self, x: float, y: float, button: MouseButton) -> None: ...
    def end_pan(self) -> None: ...
    def drag_pan(
        self, button: MouseButton, key: str | None, x: float, y: float
    ) -> None: ...
    def get_children(self): ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def contains_point(self, point) -> bool: ...
    def get_default_bbox_extra_artists(self) -> list[Artist]: ...
    def get_tightbbox(
        self,
        renderer: RendererBase = ...,
        call_axes_locator: bool = ...,
        bbox_extra_artists: list | None = ...,
        *,
        for_layout_only=...
    ) -> BboxBase: ...
    def twinx(self) -> Axes: ...
    def twiny(self) -> Axes: ...
    def get_shared_x_axes(self):
        """Return an immutable view on the shared x-axes Grouper."""
        ...
    def get_shared_y_axes(self):
        """Return an immutable view on the shared y-axes Grouper."""
        ...
