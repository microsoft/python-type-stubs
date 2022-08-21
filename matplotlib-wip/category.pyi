import numpy as np
from typing import Any, Iterable
from .units import AxisInfo
from .axis import Axis

from . import ticker, units

class StrCategoryConverter(units.ConversionInterface):
    @staticmethod
    def convert(
        value: str | Iterable, unit: UnitData, axis: Axis
    ) -> float | np.ndarray:
        """
        Convert strings in *value* to floats using mapping information stored
        in the *unit* object.

        Parameters
        ----------
        value : str or iterable
            Value or list of values to be converted.
        unit : `.UnitData`
            An object mapping strings to integers.
        axis : `~Axis`
            The axis on which the converted value is plotted.

            .. note:: *axis* is unused.

        Returns
        -------
        float or np.ndarray[float]
        """
        ...
    @staticmethod
    def axisinfo(unit: UnitData, axis: Axis) -> AxisInfo:
        """
        Set the default axis ticks and labels.

        Parameters
        ----------
        unit : `.UnitData`
            object string unit information for value
        axis : `~Axis`
            axis for which information is being set

            .. note:: *axis* is not used

        Returns
        -------
        `~AxisInfo`
            Information to support default tick labeling

        """
        ...
    @staticmethod
    def default_units(data: str, axis: Axis) -> UnitData:
        """
        Set and update the `~Axis` units.

        Parameters
        ----------
        data : str or iterable of str
        axis : `~Axis`
            axis on which the data is plotted

        Returns
        -------
        `.UnitData`
            object storing string to integer mapping
        """
        ...

class StrCategoryLocator(ticker.Locator):
    """Tick at every integer mapping of the string data."""

    def __init__(self, units_mapping: dict[str, int]) -> None:
        """
        Parameters
        ----------
        units_mapping : dict
            Mapping of category names (str) to indices (int).
        """
        ...
    def __call__(self): ...
    def tick_values(self, vmin, vmax): ...

class StrCategoryFormatter(ticker.Formatter):
    """String representation of the data at every tick."""

    def __init__(self, units_mapping: dict[str, int]) -> None:
        """
        Parameters
        ----------
        units_mapping : dict
            Mapping of category names (str) to indices (int).
        """
        ...
    def __call__(self, x, pos=...): ...
    def format_ticks(self, values): ...

class UnitData:
    def __init__(self, data=...) -> None:
        """
        Create mapping between unique categorical values and integer ids.

        Parameters
        ----------
        data : iterable
            sequence of string values
        """
        ...
    def update(self, data: bytes):
        """
        Map new values to integer identifiers.

        Parameters
        ----------
        data : iterable of str or bytes

        Raises
        ------
        TypeError
            If elements in *data* are neither str nor bytes.
        """
        ...
