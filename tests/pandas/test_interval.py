# flake8: noqa: F841
from typing import TYPE_CHECKING
import pandas as pd

if not TYPE_CHECKING:

    def reveal_type(arg, **kwargs):
        pass


def test_interval_init() -> None:
    i1: pd.Interval = pd.Interval(1, 2, closed="both")
    i2: pd.Interval = pd.Interval(1, right=2, closed="right")
    i3: pd.Interval = pd.Interval(left=1, right=2, closed="left")


def test_interval_arithmetic() -> None:
    i1: pd.Interval = pd.Interval(1, 2, closed="both")
    i2: pd.Interval = pd.Interval(1, right=2, closed="right")

    i3: pd.Interval = i1 + 1
    i4: pd.Interval = i1 - 1
    i5: pd.Interval = i1 * 2
    i6: pd.Interval = i1 / 2
    i7: pd.Interval = i1 // 2


def test_max_intervals() -> None:
    i1 = pd.Interval(pd.Timestamp("2000-01-01"), pd.Timestamp("2000-01-02"), closed="both")
    i2 = pd.Interval(pd.Timestamp("2000-01-01T12:00:00"), pd.Timestamp("2000-01-02"), closed="both")
    print(max(i1.left, i2.left))


def test_interval_length() -> None:
    i1 = pd.Interval(pd.Timestamp("2000-01-01"), pd.Timestamp("2000-01-03"), closed="both")
    reveal_type(i1.length, expected_string="Timedelta")
    reveal_type(i1.left, expected_string="Timestamp")
    reveal_type(i1.right, expected_string="Timestamp")
    reveal_type(i1.mid, expected_string="Timestamp")
    i1.length.total_seconds()
    pd.Timestamp("2001-01-02") in i1
    i1 + pd.Timedelta(seconds=20)

    reveal_type(i1 + pd.Timedelta(seconds=20), expected_string="Interval[Timestamp]")
    if TYPE_CHECKING:
        20 in i1  # type: ignore
        i1 + pd.Timestamp("2000-03-03")  # type: ignore
        i1 * 3  # type: ignore
        i1 * pd.Timedelta(seconds=20)  # type: ignore

    i2 = pd.Interval(10, 20)
    reveal_type(i2.length, expected_type=int)
    reveal_type(i2.left, expected_type=int)
    reveal_type(i2.right, expected_type=int)
    reveal_type(i2.mid, expected_type=float)

    15 in i2
    reveal_type(i2 + 3, expected_string="Interval[int]")
    reveal_type(i2 + 3.2, expected_string="Interval[float]")
    reveal_type(i2 * 4, expected_string="Interval[int]")
    reveal_type(i2 * 4.2, expected_string="Interval[float]")

    if TYPE_CHECKING:
        pd.Timestamp("2001-01-02") in i2  # type: ignore
        i2 + pd.Timedelta(seconds=20)  # type: ignore
    reveal_type(pd.Timestamp("2001-02-02"))

    i3 = pd.Interval(13.2, 19.5)
    reveal_type(i3.length, expected_type=float)
    reveal_type(i3.left, expected_type=float)
    reveal_type(i3.right, expected_type=float)
    reveal_type(i3.mid, expected_type=float)

    15.4 in i3
    reveal_type(i3 + 3, expected_string="Interval[float]")
    reveal_type(i3 * 3, expected_string="Interval[float]")
    if TYPE_CHECKING:
        pd.Timestamp("2001-01-02") in i3  # type: ignore
        i3 + pd.Timedelta(seconds=20)  # type: ignore
