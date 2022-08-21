from typing import Iterable, Sequence
from ._typing import *
from .ticker import Formatter, Locator
from .axis import Axis
from datetime import date

class ConversionError(TypeError): ...

class AxisInfo:
    """
    Information to support default axis labeling, tick labeling, and limits.

    An instance of this class must be returned by
    `ConversionInterface.axisinfo`.
    """

    def __init__(
        self,
        majloc: Locator = ...,
        minloc: Locator = ...,
        majfmt: Formatter = ...,
        minfmt: Formatter = ...,
        label: str | None = ...,
        default_limits: Sequence[date] = ...,
    ) -> None:
        """
        Parameters
        ----------
        majloc, minloc : Locator, optional
            Tick locators for the major and minor ticks.
        majfmt, minfmt : Formatter, optional
            Tick formatters for the major and minor ticks.
        label : str, optional
            The default axis label.
        default_limits : optional
            The default min and max limits of the axis if no data has
            been plotted.

        Notes
        -----
        If any of the above are ``None``, the axis will simply use the
        default value.
        """
        ...

class ConversionInterface:
    """
    The minimal interface for a converter to take custom data types (or
    sequences) and convert them to values Matplotlib can use.
    """

    @staticmethod
    def axisinfo(unit, axis: Axis) -> AxisInfo:
        """Return an `.AxisInfo` for the axis with the specified units."""
        ...
    @staticmethod
    def default_units(x, axis: Axis):
        """Return the default unit for *x* or ``None`` for the given axis."""
        ...
    @staticmethod
    def convert(obj, unit, axis: Axis):
        """
        Convert *obj* using *unit* for the specified *axis*.

        If *obj* is a sequence, return the converted sequence.  The output must
        be a sequence of scalars that can be used by the numpy array layer.
        """
        ...
    @staticmethod
    def is_numlike(x: str) -> bool:
        """
        The Matplotlib datalim, autoscaling, locators etc work with scalars
        which are the units converted to floats given the current unit.  The
        converter may be passed these floats, or arrays of them, even when
        units are set.
        """
        ...

class DecimalConverter(ConversionInterface):
    """Converter for decimal.Decimal data to float."""

    @staticmethod
    def convert(value: Decimal | Iterable, unit, axis: Axis):
        """
        Convert Decimals to floats.

        The *unit* and *axis* arguments are not used.

        Parameters
        ----------
        value : decimal.Decimal or iterable
            Decimal or list of Decimal need to be converted
        """
        ...

class Registry(dict):
    """Register types with conversion interface."""

    def get_converter(self, x) -> ConversionInterface | None:
        """Get the converter interface instance for *x*, or None."""
        ...

registry: dict = ...
