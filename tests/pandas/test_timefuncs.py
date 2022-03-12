# flake8: noqa: F841

import pandas as pd
import datetime as dt

from pandas.testing import assert_series_equal

from . import check_series_result


def test_types_init() -> None:
    ts: pd.Timestamp = pd.Timestamp("2021-03-01T12")
    ts1: pd.Timestamp = pd.Timestamp(dt.date(2021, 3, 15))
    ts2: pd.Timestamp = pd.Timestamp(dt.datetime(2021, 3, 10, 12))
    ts3: pd.Timestamp = pd.Timestamp(pd.Timestamp("2021-03-01T12"))
    ts4: pd.Timestamp = pd.Timestamp(1515590000.1, unit="s")
    ts5: pd.Timestamp = pd.Timestamp(1515590000.1, unit="s", tz="US/Pacific")
    ts6: pd.Timestamp = pd.Timestamp(1515590000100000000)  # plain integer (nanosecond)
    ts7: pd.Timestamp = pd.Timestamp(2021, 3, 10, 12)
    ts8: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12)
    ts9: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12, tz="US/Pacific")


def test_types_arithmetic() -> None:
    ts: pd.Timestamp = pd.to_datetime("2021-03-01")
    ts2: pd.Timestamp = pd.to_datetime("2021-01-01")
    delta: pd.Timedelta = pd.to_timedelta("1 day")

    tsr: pd.Timedelta = ts - ts2
    tsr2: pd.Timestamp = ts + delta
    tsr3: pd.Timestamp = ts - delta
    tsr4: pd.Timedelta = ts - dt.datetime(2021, 1, 3)


def test_types_comparison() -> None:
    ts: pd.Timestamp = pd.to_datetime("2021-03-01")
    ts2: pd.Timestamp = pd.to_datetime("2021-01-01")

    tsr: bool = ts < ts2
    tsr2: bool = ts > ts2


def test_types_pydatetime() -> None:
    ts: pd.Timestamp = pd.Timestamp("2021-03-01T12")

    datet: dt.datetime = ts.to_pydatetime()
    datet2: dt.datetime = ts.to_pydatetime(False)
    datet3: dt.datetime = ts.to_pydatetime(warn=True)


def test_to_timedelta() -> None:
    td: pd.Timedelta = pd.to_timedelta(3, "days")
    tds: pd.Series = pd.to_timedelta([2, 3], "minutes")


def test_timedelta_arithmetic() -> None:
    td1: pd.Timedelta = pd.to_timedelta(3, "days")
    td2: pd.Timedelta = pd.to_timedelta(4, "hours")
    td3: pd.Timedelta = td1 + td2
    td4: pd.Timedelta = td1 - td2
    td5: pd.Timedelta = td1 * 4.3
    td6: pd.Timedelta = td3 / 10.2


def test_timedelta_series_arithmetic() -> None:
    tds1: pd.Series = pd.to_timedelta([2, 3], "minutes")
    td1: pd.Timedelta = pd.Timedelta("2 days")
    r1: pd.Series = tds1 + td1
    r2: pd.Series = tds1 - td1
    r3: pd.Series = tds1 * 4.3
    r4: pd.Series = tds1 / 10.2


def test_timestamp_timedelta_series_arithmetic() -> None:
    tscheck = pd.Series([pd.Timestamp("2022-03-05"), pd.Timestamp("2022-03-06")])
    ts1 = pd.to_datetime(pd.Series(["2022-03-05", "2022-03-06"]))
    check_series_result(ts1, tscheck.dtype)
    assert_series_equal(tscheck, ts1)
    ts2 = pd.to_datetime(pd.Series(["2022-03-08", "2022-03-10"]))
    td1 = pd.to_timedelta([2, 3], "seconds")
    r1 = ts1 - ts2
    check_series_result(r1, td1.dtype)
    r2 = r1 / td1
    check_series_result(r2, float)
    r3 = r1 - td1
    check_series_result(r3, td1.dtype)
    r4 = pd.Timedelta(5, "days") / r1
    check_series_result(r4, float)
    sb = pd.Series([1, 2]) == pd.Series([1, 3])
    check_series_result(sb, bool)
    r5 = sb * r1
    check_series_result(r5, r1.dtype)
