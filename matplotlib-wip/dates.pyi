import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from dateutil import rrule
from matplotlib._typing import *
from matplotlib.ticker import Locator
from matplotlib.ticker import Formatter
from matplotlib.units import AxisInfo
from matplotlib.axis import Axis

"""
This type stub file was generated by pyright.
"""

from . import _api, ticker, units

"""
This type stub file was generated by pyright.
"""

UTC: datetime.timezone = ...
EPOCH_OFFSET: float = ...
JULIAN_OFFSET: float = ...
MICROSECONDLY: int = ...
HOURS_PER_DAY: int = ...
MIN_PER_HOUR: int = ...
SEC_PER_MIN: int = ...
MONTHS_PER_YEAR: int = ...
DAYS_PER_WEEK: int = ...
DAYS_PER_MONTH: int = ...
DAYS_PER_YEAR: int = ...
MINUTES_PER_DAY: int = ...
SEC_PER_HOUR: int = ...
SEC_PER_DAY: int = ...
SEC_PER_WEEK: int = ...
MUSECONDS_PER_DAY: int = ...
MO: rrule.weekday = ...
TU: rrule.weekday = ...
WE: rrule.weekday = ...
TH: rrule.weekday = ...
FR: rrule.weekday = ...
SA: rrule.weekday = ...
SU: rrule.weekday = ...
WEEKDAYS: tuple[rrule.weekday] = ...
YEARLY: int = ...
MONTHLY: int = ...
WEEKLY: int = ...
DAILY: int = ...
HOURLY: int = ...
MINUTELY: int = ...
SECONDLY: int = ...

def set_epoch(epoch: str):
    """
    Set the epoch (origin for dates) for datetime calculations.

    The default epoch is :rc:`dates.epoch` (by default 1970-01-01T00:00).

    If microsecond accuracy is desired, the date being plotted needs to be
    within approximately 70 years of the epoch. Matplotlib internally
    represents dates as days since the epoch, so floating point dynamic
    range needs to be within a factor of 2^52.

    `~.dates.set_epoch` must be called before any dates are converted
    (i.e. near the import section) or a RuntimeError will be raised.

    See also :doc:`/gallery/ticks/date_precision_and_epochs`.

    Parameters
    ----------
    epoch : str
        valid UTC date parsable by `numpy.datetime64` (do not include
        timezone).

    """
    ...

def get_epoch() -> str:
    """
    Get the epoch used by `.dates`.

    Returns
    -------
    epoch : str
        String for the epoch (parsable by `numpy.datetime64`).
    """
    ...

def datestr2num(d: str, default: datetime.datetime = ...):
    """
    Convert a date string to a datenum using `dateutil.parser.parse`.

    Parameters
    ----------
    d : str or sequence of str
        The dates to convert.

    default : datetime.datetime, optional
        The default date to use when fields are missing in *d*.
    """
    ...

def date2num(d: datetime.datetime | np.datetime64) -> float:
    """
    Convert datetime objects to Matplotlib dates.

    Parameters
    ----------
    d : `datetime.datetime` or `numpy.datetime64` or sequences of these

    Returns
    -------
    float or sequence of floats
        Number of days since the epoch.  See `.get_epoch` for the
        epoch, which can be changed by :rc:`date.epoch` or `.set_epoch`.  If
        the epoch is "1970-01-01T00:00:00" (default) then noon Jan 1 1970
        ("1970-01-01T12:00:00") returns 0.5.

    Notes
    -----
    The Gregorian calendar is assumed; this is not universal practice.
    For details see the module docstring.
    """
    ...

def julian2num(j: float) -> float:
    """
    Convert a Julian date (or sequence) to a Matplotlib date (or sequence).

    Parameters
    ----------
    j : float or sequence of floats
        Julian dates (days relative to 4713 BC Jan 1, 12:00:00 Julian
        calendar or 4714 BC Nov 24, 12:00:00, proleptic Gregorian calendar).

    Returns
    -------
    float or sequence of floats
        Matplotlib dates (days relative to `.get_epoch`).
    """
    ...

def num2julian(n: float) -> float:
    """
    Convert a Matplotlib date (or sequence) to a Julian date (or sequence).

    Parameters
    ----------
    n : float or sequence of floats
        Matplotlib dates (days relative to `.get_epoch`).

    Returns
    -------
    float or sequence of floats
        Julian dates (days relative to 4713 BC Jan 1, 12:00:00).
    """
    ...

def num2date(x: float, tz: str | datetime.tzinfo = ...) -> datetime.datetime:
    """
    Convert Matplotlib dates to `~datetime.datetime` objects.

    Parameters
    ----------
    x : float or sequence of floats
        Number of days (fraction part represents hours, minutes, seconds)
        since the epoch.  See `.get_epoch` for the
        epoch, which can be changed by :rc:`date.epoch` or `.set_epoch`.
    tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
        Timezone of *x*. If a string, *tz* is passed to `dateutil.tz`.

    Returns
    -------
    `~datetime.datetime` or sequence of `~datetime.datetime`
        Dates are returned in timezone *tz*.

        If *x* is a sequence, a sequence of `~datetime.datetime` objects will
        be returned.

    Notes
    -----
    The addition of one here is a historical artifact. Also, note that the
    Gregorian calendar is assumed; this is not universal practice.
    For details, see the module docstring.
    """
    ...

def num2timedelta(x) -> tuple[datetime.timedelta, list[datetime.timedelta]]:
    """
    Convert number of days to a `~datetime.timedelta` object.

    If *x* is a sequence, a sequence of `~datetime.timedelta` objects will
    be returned.

    Parameters
    ----------
    x : float, sequence of floats
        Number of days. The fraction part represents hours, minutes, seconds.

    Returns
    -------
    `datetime.timedelta` or list[`datetime.timedelta`]
    """
    ...

def drange(
    dstart: datetime.datetime | datetime.date,
    dend: datetime.datetime | datetime.date,
    delta: datetime.timedelta,
) -> np.ndarray:
    """
    Return a sequence of equally spaced Matplotlib dates.

    The dates start at *dstart* and reach up to, but not including *dend*.
    They are spaced by *delta*.

    Parameters
    ----------
    dstart, dend : `~datetime.datetime`
        The date limits.
    delta : `datetime.timedelta`
        Spacing of the dates.

    Returns
    -------
    `numpy.array`
        A list floats representing Matplotlib dates.

    """
    ...

class DateFormatter(ticker.Formatter):
    """
    Format a tick (in days since the epoch) with a
    `~datetime.datetime.strftime` format string.
    """

    def __init__(
        self, fmt: str, tz: str | datetime.tzinfo = ..., *, usetex: bool = ...
    ) -> None:
        """
        Parameters
        ----------
        fmt : str
            `~datetime.datetime.strftime` format string
        tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
            Ticks timezone.
        usetex : bool, default: :rc:`text.usetex`
            To enable/disable the use of TeX's math mode for rendering the
            results of the formatter.
        """
        ...
    def __call__(self, x, pos=...): ...
    def set_tzinfo(self, tz): ...

class ConciseDateFormatter(ticker.Formatter):
    """
    A `.Formatter` which attempts to figure out the best format to use for the
    date, and to make it as compact as possible, but still be complete. This is
    most useful when used with the `AutoDateLocator`::

    >>> locator = AutoDateLocator()
    >>> formatter = ConciseDateFormatter(locator)

    Parameters
    ----------
    locator : `.ticker.Locator`
        Locator that this axis is using.

    tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
        Passed to `.dates.num2date`.

    formats : list of 6 strings, optional
        Format strings for 6 levels of tick labelling: mostly years,
        months, days, hours, minutes, and seconds.  Strings use
        the same format codes as `~datetime.datetime.strftime`.  Default is
        ``['%Y', '%b', '%d', '%H:%M', '%H:%M', '%S.%f']``

    zero_formats : list of 6 strings, optional
        Format strings for tick labels that are "zeros" for a given tick
        level.  For instance, if most ticks are months, ticks around 1 Jan 2005
        will be labeled "Dec", "2005", "Feb".  The default is
        ``['', '%Y', '%b', '%b-%d', '%H:%M', '%H:%M']``

    offset_formats : list of 6 strings, optional
        Format strings for the 6 levels that is applied to the "offset"
        string found on the right side of an x-axis, or top of a y-axis.
        Combined with the tick labels this should completely specify the
        date.  The default is::

            ['', '%Y', '%Y-%b', '%Y-%b-%d', '%Y-%b-%d', '%Y-%b-%d %H:%M']

    show_offset : bool, default: True
        Whether to show the offset or not.

    usetex : bool, default: :rc:`text.usetex`
        To enable/disable the use of TeX's math mode for rendering the results
        of the formatter.

    Examples
    --------
    See :doc:`/gallery/ticks/date_concise_formatter`

    .. plot::

        import datetime
        import matplotlib.dates as mdates

        base = datetime.datetime(2005, 2, 1)
        dates = np.array([base + datetime.timedelta(hours=(2 * i))
                          for i in range(732)])
        N = len(dates)
        np.random.seed(19680801)
        y = np.cumsum(np.random.randn(N))

        fig, ax = plt.subplots(constrained_layout=True)
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)

        ax.plot(dates, y)
        ax.set_title('Concise Date Formatter')

    """

    formats: list[str] = ...
    offset_formats: list[str] = ...
    zero_formats: list[str] = ...

    def __init__(
        self,
        locator: ticker.Locator,
        tz: str | datetime.tzinfo = ...,
        formats: list[str] = ...,
        offset_formats: list[str] = ...,
        zero_formats: list[str] = ...,
        show_offset: bool = ...,
        *,
        usetex: bool = ...
    ) -> None:
        """
        Autoformat the date labels.  The default format is used to form an
        initial string, and then redundant elements are removed.
        """
        ...
    def __call__(self, x, pos=...): ...
    def format_ticks(self, values): ...
    def get_offset(self): ...
    def format_data_short(self, value): ...

class AutoDateFormatter(ticker.Formatter):
    """
    A `.Formatter` which attempts to figure out the best format to use.  This
    is most useful when used with the `AutoDateLocator`.

    `.AutoDateFormatter` has a ``.scale`` dictionary that maps tick scales (the
    interval in days between one major tick) to format strings; this dictionary
    defaults to ::

        self.scaled = {
            DAYS_PER_YEAR: rcParams['date.autoformat.year'],
            DAYS_PER_MONTH: rcParams['date.autoformat.month'],
            1: rcParams['date.autoformat.day'],
            1 / HOURS_PER_DAY: rcParams['date.autoformat.hour'],
            1 / MINUTES_PER_DAY: rcParams['date.autoformat.minute'],
            1 / SEC_PER_DAY: rcParams['date.autoformat.second'],
            1 / MUSECONDS_PER_DAY: rcParams['date.autoformat.microsecond'],
        }

    The formatter uses the format string corresponding to the lowest key in
    the dictionary that is greater or equal to the current scale.  Dictionary
    entries can be customized::

        locator = AutoDateLocator()
        formatter = AutoDateFormatter(locator)
        formatter.scaled[1/(24*60)] = '%M:%S' # only show min and sec

    Custom callables can also be used instead of format strings.  The following
    example shows how to use a custom format function to strip trailing zeros
    from decimal seconds and adds the date to the first ticklabel::

        def my_format_function(x, pos=None):
            x = matplotlib.dates.num2date(x)
            if pos == 0:
                fmt = '%D %H:%M:%S.%f'
            else:
                fmt = '%H:%M:%S.%f'
            label = x.strftime(fmt)
            label = label.rstrip("0")
            label = label.rstrip(".")
            return label

        formatter.scaled[1/(24*60)] = my_format_function
    """

    def __init__(self, locator, tz=..., defaultfmt=..., *, usetex=...) -> None:
        """
        Autoformat the date labels.

        Parameters
        ----------
        locator : `.ticker.Locator`
            Locator that this axis is using.

        tz : str or `~datetime.tzinfo`, optional
            Passed to `.dates.num2date`.

        defaultfmt : str
            The default format to use if none of the values in ``self.scaled``
            are greater than the unit returned by ``locator._get_unit()``.

        usetex : bool, default: :rc:`text.usetex`
            To enable/disable the use of TeX's math mode for rendering the
            results of the formatter. If any entries in ``self.scaled`` are set
            as functions, then it is up to the customized function to enable or
            disable TeX's math mode itself.
        """
        ...
    def __call__(self, x, pos=...): ...

class rrulewrapper:
    """
    A simple wrapper around a `dateutil.rrule` allowing flexible
    date tick specifications.
    """

    def __init__(self, freq, tzinfo=..., **kwargs) -> None:
        """
        Parameters
        ----------
        freq : {YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY}
            Tick frequency. These constants are defined in `dateutil.rrule`,
            but they are accessible from `matplotlib.dates` as well.
        tzinfo : `datetime.tzinfo`, optional
            Time zone information. The default is None.
        **kwargs
            Additional keyword arguments are passed to the `dateutil.rrule`.
        """
        ...
    def set(self, **kwargs):
        """Set parameters for an existing wrapper."""
        ...
    def __getattr__(self, name): ...
    def __setstate__(self, state): ...

class DateLocator(ticker.Locator):
    """
    Determines the tick locations when plotting dates.

    This class is subclassed by other Locators and
    is not meant to be used on its own.
    """

    hms0d = ...
    def __init__(self, tz=...) -> None:
        """
        Parameters
        ----------
        tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
        """
        ...
    def set_tzinfo(self, tz):
        """
        Set timezone info. str or `~datetime.tzinfo`.
        """
        ...
    def datalim_to_dt(self):
        """Convert axis data interval to datetime objects."""
        ...
    def viewlim_to_dt(self):
        """Convert the view interval to datetime objects."""
        ...
    def nonsingular(self, vmin, vmax):
        """
        Given the proposed upper and lower extent, adjust the range
        if it is too close to being singular (i.e. a range of ~0).
        """
        ...

class RRuleLocator(DateLocator):
    def __init__(self, o, tz=...) -> None: ...
    def __call__(self): ...
    def tick_values(self, vmin, vmax): ...
    @staticmethod
    def get_unit_generic(freq): ...

class AutoDateLocator(DateLocator):
    """
    On autoscale, this class picks the best `DateLocator` to set the view
    limits and the tick locations.

    Attributes
    ----------
    intervald : dict

        Mapping of tick frequencies to multiples allowed for that ticking.
        The default is ::

            self.intervald = {
                YEARLY  : [1, 2, 4, 5, 10, 20, 40, 50, 100, 200, 400, 500,
                           1000, 2000, 4000, 5000, 10000],
                MONTHLY : [1, 2, 3, 4, 6],
                DAILY   : [1, 2, 3, 7, 14, 21],
                HOURLY  : [1, 2, 3, 4, 6, 12],
                MINUTELY: [1, 5, 10, 15, 30],
                SECONDLY: [1, 5, 10, 15, 30],
                MICROSECONDLY: [1, 2, 5, 10, 20, 50, 100, 200, 500,
                                1000, 2000, 5000, 10000, 20000, 50000,
                                100000, 200000, 500000, 1000000],
            }

        where the keys are defined in `dateutil.rrule`.

        The interval is used to specify multiples that are appropriate for
        the frequency of ticking. For instance, every 7 days is sensible
        for daily ticks, but for minutes/seconds, 15 or 30 make sense.

        When customizing, you should only modify the values for the existing
        keys. You should not add or delete entries.

        Example for forcing ticks every 3 hours::

            locator = AutoDateLocator()
            locator.intervald[HOURLY] = [3]  # only show every 3 hours
    """

    def __init__(
        self, tz=..., minticks=..., maxticks=..., interval_multiples=...
    ) -> None:
        """
        Parameters
        ----------
        tz : str or `~datetime.tzinfo`, default: :rc:`timezone`
            Ticks timezone.
        minticks : int
            The minimum number of ticks desired; controls whether ticks occur
            yearly, monthly, etc.
        maxticks : int
            The maximum number of ticks desired; controls the interval between
            ticks (ticking every other, every 3, etc.).  For fine-grained
            control, this can be a dictionary mapping individual rrule
            frequency constants (YEARLY, MONTHLY, etc.) to their own maximum
            number of ticks.  This can be used to keep the number of ticks
            appropriate to the format chosen in `AutoDateFormatter`. Any
            frequency not specified in this dictionary is given a default
            value.
        interval_multiples : bool, default: True
            Whether ticks should be chosen to be multiple of the interval,
            locking them to 'nicer' locations.  For example, this will force
            the ticks to be at hours 0, 6, 12, 18 when hourly ticking is done
            at 6 hour intervals.
        """
        ...
    def __call__(self): ...
    def tick_values(self, vmin, vmax): ...
    def nonsingular(self, vmin, vmax): ...
    def get_locator(self, dmin, dmax):
        """Pick the best locator based on a distance."""
        ...

class YearLocator(RRuleLocator):
    """
    Make ticks on a given day of each year that is a multiple of base.

    Examples::

      # Tick every year on Jan 1st
      locator = YearLocator()

      # Tick every 5 years on July 4th
      locator = YearLocator(5, month=7, day=4)
    """

    def __init__(self, base=..., month=..., day=..., tz=...) -> None:
        """
        Mark years that are multiple of base on a given month and day
        (default jan 1).
        """
        ...

class MonthLocator(RRuleLocator):
    """
    Make ticks on occurrences of each month, e.g., 1, 3, 12.
    """

    def __init__(self, bymonth=..., bymonthday=..., interval=..., tz=...) -> None:
        """
        Mark every month in *bymonth*; *bymonth* can be an int or
        sequence.  Default is ``range(1, 13)``, i.e. every month.

        *interval* is the interval between each iteration.  For
        example, if ``interval=2``, mark every second occurrence.
        """
        ...

class WeekdayLocator(RRuleLocator):
    """
    Make ticks on occurrences of each weekday.
    """

    def __init__(self, byweekday=..., interval=..., tz=...) -> None:
        """
        Mark every weekday in *byweekday*; *byweekday* can be a number or
        sequence.

        Elements of *byweekday* must be one of MO, TU, WE, TH, FR, SA,
        SU, the constants from :mod:`dateutil.rrule`, which have been
        imported into the :mod:`matplotlib.dates` namespace.

        *interval* specifies the number of weeks to skip.  For example,
        ``interval=2`` plots every second week.
        """
        ...

class DayLocator(RRuleLocator):
    """
    Make ticks on occurrences of each day of the month.  For example,
    1, 15, 30.
    """

    def __init__(self, bymonthday=..., interval=..., tz=...) -> None:
        """
        Mark every day in *bymonthday*; *bymonthday* can be an int or sequence.

        Default is to tick every day of the month: ``bymonthday=range(1, 32)``.
        """
        ...

class HourLocator(RRuleLocator):
    """
    Make ticks on occurrences of each hour.
    """

    def __init__(self, byhour=..., interval=..., tz=...) -> None:
        """
        Mark every hour in *byhour*; *byhour* can be an int or sequence.
        Default is to tick every hour: ``byhour=range(24)``

        *interval* is the interval between each iteration.  For
        example, if ``interval=2``, mark every second occurrence.
        """
        ...

class MinuteLocator(RRuleLocator):
    """
    Make ticks on occurrences of each minute.
    """

    def __init__(self, byminute=..., interval=..., tz=...) -> None:
        """
        Mark every minute in *byminute*; *byminute* can be an int or
        sequence.  Default is to tick every minute: ``byminute=range(60)``

        *interval* is the interval between each iteration.  For
        example, if ``interval=2``, mark every second occurrence.
        """
        ...

class SecondLocator(RRuleLocator):
    """
    Make ticks on occurrences of each second.
    """

    def __init__(self, bysecond=..., interval=..., tz=...) -> None:
        """
        Mark every second in *bysecond*; *bysecond* can be an int or
        sequence.  Default is to tick every second: ``bysecond = range(60)``

        *interval* is the interval between each iteration.  For
        example, if ``interval=2``, mark every second occurrence.

        """
        ...

class MicrosecondLocator(DateLocator):
    """
    Make ticks on regular intervals of one or more microsecond(s).

    .. note::

        By default, Matplotlib uses a floating point representation of time in
        days since the epoch, so plotting data with
        microsecond time resolution does not work well for
        dates that are far (about 70 years) from the epoch (check with
        `~.dates.get_epoch`).

        If you want sub-microsecond resolution time plots, it is strongly
        recommended to use floating point seconds, not datetime-like
        time representation.

        If you really must use datetime.datetime() or similar and still
        need microsecond precision, change the time origin via
        `.dates.set_epoch` to something closer to the dates being plotted.
        See :doc:`/gallery/ticks/date_precision_and_epochs`.

    """

    def __init__(self, interval=..., tz=...) -> None:
        """
        *interval* is the interval between each iteration.  For
        example, if ``interval=2``, mark every second microsecond.

        """
        ...
    def set_axis(self, axis): ...
    def set_view_interval(self, vmin, vmax): ...
    def set_data_interval(self, vmin, vmax): ...
    def __call__(self): ...
    def tick_values(self, vmin, vmax): ...

def epoch2num(e: list[float]) -> np.ndarray:
    """
    Convert UNIX time to days since Matplotlib epoch.

    Parameters
    ----------
    e : list of floats
        Time in seconds since 1970-01-01.

    Returns
    -------
    `numpy.array`
        Time in days since Matplotlib epoch (see `~.dates.get_epoch()`).
    """
    ...

def num2epoch(d: list[float]) -> np.ndarray:
    """
    Convert days since Matplotlib epoch to UNIX time.

    Parameters
    ----------
    d : list of floats
        Time in days since Matplotlib epoch (see `~.dates.get_epoch()`).

    Returns
    -------
    `numpy.array`
        Time in seconds since 1970-01-01.
    """
    ...

def date_ticker_factory(span, tz=..., numticks=...):
    """
    Create a date locator with *numticks* (approx) and a date formatter
    for *span* in days.  Return value is (locator, formatter).
    """
    ...

class DateConverter(units.ConversionInterface):
    """
    Converter for `datetime.date` and `datetime.datetime` data, or for
    date/time data represented as it would be converted by `date2num`.

    The 'unit' tag for such data is None or a tzinfo instance.
    """

    def __init__(self, *, interval_multiples=...) -> None: ...
    def axisinfo(self, unit, axis):
        """
        Return the `~AxisInfo` for *unit*.

        *unit* is a tzinfo instance or None.
        The *axis* argument is required but not used.
        """
        ...
    @staticmethod
    def convert(value, unit, axis):
        """
        If *value* is not already a number or sequence of numbers, convert it
        with `date2num`.

        The *unit* and *axis* arguments are not used.
        """
        ...
    @staticmethod
    def default_units(x, axis):
        """
        Return the tzinfo instance of *x* or of its first element, or None
        """
        ...

class ConciseDateConverter(DateConverter):
    def __init__(
        self,
        formats=...,
        zero_formats=...,
        offset_formats=...,
        show_offset=...,
        *,
        interval_multiples=...
    ) -> None: ...
    def axisinfo(self, unit, axis): ...

class _SwitchableDateConverter:
    """
    Helper converter-like object that generates and dispatches to
    temporary ConciseDateConverter or DateConverter instances based on
    :rc:`date.converter` and :rc:`date.interval_multiples`.
    """

    def axisinfo(self, *args, **kwargs): ...
    def default_units(self, *args, **kwargs): ...
    def convert(self, *args, **kwargs): ...

__all__ = (
    "datestr2num",
    "date2num",
    "num2date",
    "num2timedelta",
    "drange",
    "epoch2num",
    "num2epoch",
    "set_epoch",
    "get_epoch",
    "DateFormatter",
    "ConciseDateFormatter",
    "AutoDateFormatter",
    "DateLocator",
    "RRuleLocator",
    "AutoDateLocator",
    "YearLocator",
    "MonthLocator",
    "WeekdayLocator",
    "DayLocator",
    "HourLocator",
    "MinuteLocator",
    "SecondLocator",
    "MicrosecondLocator",
    "rrule",
    "MO",
    "TU",
    "WE",
    "TH",
    "FR",
    "SA",
    "SU",
    "YEARLY",
    "MONTHLY",
    "WEEKLY",
    "DAILY",
    "HOURLY",
    "MINUTELY",
    "SECONDLY",
    "MICROSECONDLY",
    "relativedelta",
    "DateConverter",
    "ConciseDateConverter",
    "rrulewrapper",
)
