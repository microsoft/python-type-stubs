import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.transforms import Transform
from matplotlib.text import Text
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import Locator
from matplotlib.lines import Line2D
from matplotlib.ticker import Formatter
from matplotlib.transforms import Bbox
from matplotlib.axis import Axis
from matplotlib.axes import Axes
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Affine2D

"""
This type stub file was generated by pyright.
"""

import matplotlib.axis as maxis
import matplotlib.ticker as mticker
import matplotlib.transforms as mtransforms
from matplotlib import _api
from matplotlib.axes import Axes

"""
This type stub file was generated by pyright.
"""

class PolarTransform(Transform):
    """
    The base polar transform.  This handles projection *theta* and
    *r* into Cartesian coordinate space *x* and *y*, but does not
    perform the ultimate affine transformation into the correct
    position.
    """

    input_dims = ...
    def __init__(self, axis=..., use_rmin=..., _apply_theta_transforms=...) -> None: ...
    def transform_non_affine(self, tr) -> list: ...
    def transform_path_non_affine(self, path): ...
    def inverted(self): ...

class PolarAffine(Affine2DBase):
    """
    The affine part of the polar projection.  Scales the output so
    that maximum radius rests on the edge of the axes circle.
    """

    def __init__(self, scale_transform, limits) -> None:
        """
        *limits* is the view limit of the data.  The only part of
        its bounds that is used is the y limits (for the radius limits).
        The theta range is handled by the non-affine transform.
        """
        ...
    def get_matrix(self): ...

class InvertedPolarTransform(Transform):
    """
    The inverse of the polar transform, mapping Cartesian
    coordinate space *x* and *y* back to *theta* and *r*.
    """

    input_dims = ...
    def __init__(self, axis=..., use_rmin=..., _apply_theta_transforms=...) -> None: ...
    def transform_non_affine(self, xy) -> list: ...
    def inverted(self): ...

class ThetaFormatter(mticker.Formatter):
    """
    Used to format the *theta* tick labels.  Converts the native
    unit of radians into degrees and adds a degree symbol.
    """

    def __call__(self, x, pos=...): ...

class _AxisWrapper:
    def __init__(self, axis) -> None: ...
    def get_view_interval(self): ...
    def set_view_interval(self, vmin, vmax): ...
    def get_minpos(self): ...
    def get_data_interval(self): ...
    def set_data_interval(self, vmin, vmax): ...
    def get_tick_space(self): ...

class ThetaLocator(mticker.Locator):
    """
    Used to locate theta ticks.

    This will work the same as the base locator except in the case that the
    view spans the entire circle. In such cases, the previously used default
    locations of every 45 degrees are returned.
    """

    def __init__(self, base) -> None: ...
    def set_axis(self, axis): ...
    def __call__(self): ...
    def refresh(self): ...
    def view_limits(self, vmin, vmax): ...

class ThetaTick(maxis.XTick):
    """
    A theta-axis tick.

    This subclass of `.XTick` provides angular ticks with some small
    modification to their re-positioning such that ticks are rotated based on
    tick location. This results in ticks that are correctly perpendicular to
    the arc spine.

    When 'auto' rotation is enabled, labels are also rotated to be parallel to
    the spine. The label padding is also applied here since it's not possible
    to use a generic axes transform to produce tick-specific padding.
    """

    def __init__(self, axes, *args, **kwargs) -> None: ...
    def update_position(self, loc): ...

class ThetaAxis(maxis.XAxis):
    """
    A theta Axis.

    This overrides certain properties of an `.XAxis` to provide special-casing
    for an angular axis.
    """

    axis_name = ...
    _tick_class = ThetaTick
    def clear(self): ...

class RadialLocator(mticker.Locator):
    """
    Used to locate radius ticks.

    Ensures that all ticks are strictly positive.  For all other tasks, it
    delegates to the base `.Locator` (which may be different depending on the
    scale of the *r*-axis).
    """

    def __init__(self, base, axes=...) -> None: ...
    def set_axis(self, axis): ...
    def __call__(self): ...
    def nonsingular(self, vmin, vmax): ...
    def view_limits(self, vmin, vmax): ...

class _ThetaShift(mtransforms.ScaledTranslation):
    """
    Apply a padding shift based on axes theta limits.

    This is used to create padding for radial ticks.

    Parameters
    ----------
    axes : `~Axes`
        The owning axes; used to determine limits.
    pad : float
        The padding to apply, in points.
    mode : {'min', 'max', 'rlabel'}
        Whether to shift away from the start (``'min'``) or the end (``'max'``)
        of the axes, or using the rlabel position (``'rlabel'``).
    """

    def __init__(
        self, axes: Axes, pad: float, mode: Literal["min", "max", "rlabel"]
    ) -> None: ...
    def get_matrix(self): ...

class RadialTick(maxis.YTick):
    """
    A radial-axis tick.

    This subclass of `.YTick` provides radial ticks with some small
    modification to their re-positioning such that ticks are rotated based on
    axes limits.  This results in ticks that are correctly perpendicular to
    the spine. Labels are also rotated to be perpendicular to the spine, when
    'auto' rotation is enabled.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc): ...

class RadialAxis(maxis.YAxis):
    """
    A radial Axis.

    This overrides certain properties of a `.YAxis` to provide special-casing
    for a radial axis.
    """

    axis_name = ...
    _tick_class = RadialTick
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self): ...

class _WedgeBbox(Bbox):
    """
    Transform (theta, r) wedge Bbox into axes bounding box.

    Parameters
    ----------
    center : (float, float)
        Center of the wedge
    viewLim : `~Bbox`
        Bbox determining the boundaries of the wedge
    originLim : `~Bbox`
        Bbox determining the origin for the wedge, if different from *viewLim*
    """

    def __init__(
        self, center: tuple[float, float], viewLim: Bbox, originLim: Bbox, **kwargs
    ) -> None: ...
    def get_points(self): ...

class PolarAxes(Axes):
    """
    A polar graph projection, where the input dimensions are *theta*, *r*.

    Theta starts pointing east and goes anti-clockwise.
    """

    name = ...
    def __init__(
        self,
        *args,
        theta_offset=...,
        theta_direction=...,
        rlabel_position=...,
        **kwargs
    ) -> None: ...
    def clear(self): ...
    def get_xaxis_transform(self, which=...): ...
    def get_xaxis_text1_transform(self, pad): ...
    def get_xaxis_text2_transform(self, pad): ...
    def get_yaxis_transform(self, which=...): ...
    def get_yaxis_text1_transform(self, pad): ...
    def get_yaxis_text2_transform(self, pad): ...
    def draw(self, renderer): ...
    def set_thetamax(self, thetamax):
        """Set the maximum theta limit in degrees."""
        ...
    def get_thetamax(self):
        """Return the maximum theta limit in degrees."""
        ...
    def set_thetamin(self, thetamin):
        """Set the minimum theta limit in degrees."""
        ...
    def get_thetamin(self):
        """Get the minimum theta limit in degrees."""
        ...
    def set_thetalim(self, *args, **kwargs):
        r"""
        Set the minimum and maximum theta values.

        Can take the following signatures:

        - ``set_thetalim(minval, maxval)``: Set the limits in radians.
        - ``set_thetalim(thetamin=minval, thetamax=maxval)``: Set the limits
          in degrees.

        where minval and maxval are the minimum and maximum limits. Values are
        wrapped in to the range :math:`[0, 2\pi]` (in radians), so for example
        it is possible to do ``set_thetalim(-np.pi / 2, np.pi / 2)`` to have
        an axis symmetric around 0. A ValueError is raised if the absolute
        angle difference is larger than a full circle.
        """
        ...
    def set_theta_offset(self, offset):
        """
        Set the offset for the location of 0 in radians.
        """
        ...
    def get_theta_offset(self):
        """
        Get the offset for the location of 0 in radians.
        """
        ...
    def set_theta_zero_location(self, loc: str, offset: float = ...):
        """
        Set the location of theta's zero.

        This simply calls `set_theta_offset` with the correct value in radians.

        Parameters
        ----------
        loc : str
            May be one of "N", "NW", "W", "SW", "S", "SE", "E", or "NE".
        offset : float, default: 0
            An offset in degrees to apply from the specified *loc*. **Note:**
            this offset is *always* applied counter-clockwise regardless of
            the direction setting.
        """
        ...
    def set_theta_direction(self, direction):
        """
        Set the direction in which theta increases.

        clockwise, -1:
           Theta increases in the clockwise direction

        counterclockwise, anticlockwise, 1:
           Theta increases in the counterclockwise direction
        """
        ...
    def get_theta_direction(self):
        """
        Get the direction in which theta increases.

        -1:
           Theta increases in the clockwise direction

        1:
           Theta increases in the counterclockwise direction
        """
        ...
    def set_rmax(self, rmax: float):
        """
        Set the outer radial limit.

        Parameters
        ----------
        rmax : float
        """
        ...
    def get_rmax(self) -> float:
        """
        Returns
        -------
        float
            Outer radial limit.
        """
        ...
    def set_rmin(self, rmin: float):
        """
        Set the inner radial limit.

        Parameters
        ----------
        rmin : float
        """
        ...
    def get_rmin(self) -> float:
        """
        Returns
        -------
        float
            The inner radial limit.
        """
        ...
    def set_rorigin(self, rorigin: float):
        """
        Update the radial origin.

        Parameters
        ----------
        rorigin : float
        """
        ...
    def get_rorigin(self) -> float:
        """
        Returns
        -------
        float
        """
        ...
    def get_rsign(self): ...
    def set_rlim(self, bottom=..., top=..., emit=..., auto=..., **kwargs):
        """
        Set the radial axis view limits.

        This function behaves like `.Axes.set_ylim`, but additionally supports
        *rmin* and *rmax* as aliases for *bottom* and *top*.

        See Also
        --------
        .Axes.set_ylim
        """
        ...
    def get_rlabel_position(self) -> float:
        """
        Returns
        -------
        float
            The theta position of the radius labels in degrees.
        """
        ...
    def set_rlabel_position(self, value: float):
        """
        Update the theta position of the radius labels.

        Parameters
        ----------
        value : number
            The angular position of the radius labels in degrees.
        """
        ...
    def set_yscale(self, *args, **kwargs): ...
    def set_rscale(self, *args, **kwargs): ...
    def set_rticks(self, *args, **kwargs): ...
    def set_thetagrids(
        self, angles, labels: None = ..., fmt: str | None = ..., **kwargs
    ):
        """
        Set the theta gridlines in a polar plot.

        Parameters
        ----------
        angles : tuple with floats, degrees
            The angles of the theta gridlines.

        labels : tuple with strings or None
            The labels to use at each theta gridline. The
            `.projections.polar.ThetaFormatter` will be used if None.

        fmt : str or None
            Format string used in `matplotlib.ticker.FormatStrFormatter`.
            For example '%f'. Note that the angle that is used is in
            radians.

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
        .PolarAxes.set_rgrids
        .Axis.get_gridlines
        .Axis.get_ticklabels
        """
        ...
    def set_rgrids(
        self,
        radii,
        labels: None = ...,
        angle: float = ...,
        fmt: str | None = ...,
        **kwargs
    ):
        """
        Set the radial gridlines on a polar plot.

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
        .PolarAxes.set_thetagrids
        .Axis.get_gridlines
        .Axis.get_ticklabels
        """
        ...
    def format_coord(self, theta, r): ...
    def get_data_ratio(self):
        """
        Return the aspect ratio of the data itself.  For a polar plot,
        this should always be 1.0
        """
        ...
    def can_zoom(self):
        """
        Return whether this axes supports the zoom box button functionality.

        Polar axes do not support zoom boxes.
        """
        ...
    def can_pan(self):
        """
        Return whether this axes supports the pan/zoom button functionality.

        For polar axes, this is slightly misleading. Both panning and
        zooming are performed by the same button. Panning is performed
        in azimuth while zooming is done along the radial.
        """
        ...
    def start_pan(self, x: float, y: float, button: MouseButton): ...
    def end_pan(self): ...
    def drag_pan(self, button: MouseButton, key: str | None, x: float, y: float): ...
