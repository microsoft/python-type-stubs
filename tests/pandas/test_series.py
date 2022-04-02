# flake8: noqa: F841

import tempfile
from pathlib import Path
from typing import List, Union, TYPE_CHECKING

from pandas._typing import Scalar
from pandas.api.extensions import ExtensionArray

import pandas as pd
import numpy as np

from pandas.core.window import ExponentialMovingWindow
from . import check_dataframe_result, check_series_result

import pytest


def test_types_init() -> None:
    pd.Series(1)
    pd.Series((1, 2, 3))
    pd.Series(np.array([1, 2, 3]))
    pd.Series(data=[1, 2, 3, 4], name="series")
    pd.Series(data=[1, 2, 3, 4], dtype=np.int8)
    pd.Series(data={"row1": [1, 2], "row2": [3, 4]})
    pd.Series(data=[1, 2, 3, 4], index=[4, 3, 2, 1], copy=True)


def test_types_any() -> None:
    res1: bool = pd.Series([False, False]).any()
    res2: bool = pd.Series([False, False]).any(bool_only=False)
    res3: bool = pd.Series([np.nan]).any(skipna=False)


def test_types_all() -> None:
    res1: bool = pd.Series([False, False]).all()
    res2: bool = pd.Series([False, False]).all(bool_only=False)
    res3: bool = pd.Series([np.nan]).all(skipna=False)


def test_types_csv() -> None:
    s = pd.Series(data=[1, 2, 3])
    csv_df: str = s.to_csv()

    with tempfile.NamedTemporaryFile(delete=False) as file:
        s.to_csv(file.name)
        file.close()
        s2: pd.DataFrame = pd.read_csv(file.name)

    with tempfile.NamedTemporaryFile(delete=False) as file:
        s.to_csv(Path(file.name))
        file.close()
        s3: pd.DataFrame = pd.read_csv(Path(file.name))

    # This keyword was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    with tempfile.NamedTemporaryFile(delete=False) as file:
        s.to_csv(file.name, errors="replace")
        file.close()
        s4: pd.DataFrame = pd.read_csv(file.name)


def test_types_copy() -> None:
    s = pd.Series(data=[1, 2, 3, 4])
    s2: pd.Series = s.copy()


def test_types_select() -> None:
    s = pd.Series(data={"row1": 1, "row2": 2})
    s[0]
    s[1:]


def test_types_iloc_iat() -> None:
    s = pd.Series(data={"row1": 1, "row2": 2})
    s2 = pd.Series(data=[1, 2])
    s.loc["row1"]
    s.iat[0]
    s2.loc[0]
    s2.iat[0]


def test_types_loc_at() -> None:
    s = pd.Series(data={"row1": 1, "row2": 2})
    s2 = pd.Series(data=[1, 2])
    s.loc["row1"]
    s.at["row1"]
    s2.loc[1]
    s2.at[1]


def test_multiindex_loc() -> None:
    s = pd.Series([1, 2, 3, 4], index=pd.MultiIndex.from_product([[1, 2], ["a", "b"]]))
    check_series_result(s.loc[1, :])
    check_series_result(s.loc[pd.Index([1]), :])


def test_types_boolean_indexing() -> None:
    s = pd.Series([0, 1, 2])
    s[s > 1]
    s[s]


def test_types_df_to_df_comparison() -> None:
    s = pd.Series(data={"col1": [1, 2]})
    s2 = pd.Series(data={"col1": [3, 2]})
    res_gt: pd.Series = s > s2
    res_ge: pd.Series = s >= s2
    res_lt: pd.Series = s < s2
    res_le: pd.Series = s <= s2
    res_e: pd.Series = s == s2


def test_types_head_tail() -> None:
    s = pd.Series([0, 1, 2])
    s.head(1)
    s.tail(1)


def test_types_sample() -> None:
    s = pd.Series([0, 1, 2])
    s.sample(frac=0.5)
    s.sample(n=1)


def test_types_nlargest_nsmallest() -> None:
    s = pd.Series([0, 1, 2])
    s.nlargest(1)
    s.nlargest(1, "first")
    s.nsmallest(1, "last")
    s.nsmallest(1, "all")


def test_types_filter() -> None:
    s = pd.Series(data=[1, 2, 3, 4], index=["cow", "coal", "coalesce", ""])
    s.filter(items=["cow"])
    s.filter(regex="co.*")
    s.filter(like="al")


def test_types_setting() -> None:
    s = pd.Series([0, 1, 2])
    s[3] = 4
    s[s == 1] = 5
    s[:] = 3


def test_types_drop() -> None:
    s = pd.Series([0, 1, 2])
    res: pd.Series = s.drop(0)
    res2: pd.Series = s.drop([0, 1])
    res3: pd.Series = s.drop(0, axis=0)
    res4: None = s.drop([0, 1], inplace=True, errors="raise")
    res5: None = s.drop([0, 1], inplace=True, errors="ignore")


def test_types_drop_multilevel() -> None:
    index = pd.MultiIndex(
        levels=[["top", "bottom"], ["first", "second", "third"]], codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]]
    )
    s = pd.Series(data=[1, 2, 3, 4, 5, 6], index=index)
    res: pd.Series = s.drop(labels="first", level=1)


def test_types_dropna() -> None:
    s = pd.Series([1, np.nan, np.nan])
    res: pd.Series = s.dropna()
    res2: None = s.dropna(axis=0, inplace=True)


def test_types_fillna() -> None:
    s = pd.Series([1, np.nan, np.nan, 3])
    res: pd.Series = s.fillna(0)
    res2: pd.Series = s.fillna(0, axis="index")
    res3: pd.Series = s.fillna(method="backfill", axis=0)
    res4: None = s.fillna(method="bfill", inplace=True)
    res5: pd.Series = s.fillna(method="pad")
    res6: pd.Series = s.fillna(method="ffill", limit=1)


def test_types_sort_index() -> None:
    s = pd.Series([1, 2, 3], index=[2, 3, 1])
    res: pd.Series = s.sort_index()
    res2: None = s.sort_index(ascending=False, inplace=True)
    res3: pd.Series = s.sort_index(kind="mergesort")


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_sort_index_with_key() -> None:
    s = pd.Series([1, 2, 3], index=["a", "B", "c"])
    res: pd.Series = s.sort_index(key=lambda k: k.str.lower())


def test_types_sort_values() -> None:
    s = pd.Series([4, 2, 1, 3])
    res: pd.Series = s.sort_values(0)
    res2: pd.Series = s.sort_values(ascending=False)
    res3: None = s.sort_values(inplace=True, kind="quicksort")
    res4: pd.Series = s.sort_values(na_position="last")
    res5: pd.Series = s.sort_values(ignore_index=True)


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_sort_values_with_key() -> None:
    s = pd.Series([1, 2, 3], index=[2, 3, 1])
    res: pd.Series = s.sort_values(key=lambda k: -k)


def test_types_shift() -> None:
    s = pd.Series([1, 2, 3])
    s.shift()
    s.shift(axis=0, periods=1)
    s.shift(-1, fill_value=0)


def test_types_rank() -> None:
    s = pd.Series([1, 1, 2, 5, 6, np.nan, "milion"])
    s.rank()
    s.rank(axis=0, na_option="bottom")
    s.rank(method="min", pct=True)
    s.rank(method="dense", ascending=True)
    s.rank(method="first", numeric_only=True)


def test_types_mean() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    f1: float = s.mean()
    s1: pd.Series = s.mean(axis=0, level=0)
    f2: float = s.mean(skipna=False)
    f3: float = s.mean(numeric_only=False)


def test_types_median() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    f1: float = s.median()
    s1: pd.Series = s.median(axis=0, level=0)
    f2: float = s.median(skipna=False)
    f3: float = s.median(numeric_only=False)


def test_types_sum() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.sum()
    s.sum(axis=0, level=0)
    s.sum(skipna=False)
    s.sum(numeric_only=False)
    s.sum(min_count=4)


def test_types_cumsum() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.cumsum()
    s.cumsum(axis=0)
    s.cumsum(skipna=False)


def test_types_min() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.min()
    s.min(axis=0)
    s.min(level=0)
    s.min(skipna=False)


def test_types_max() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.max()
    s.max(axis=0)
    s.max(level=0)
    s.max(skipna=False)


def test_types_quantile() -> None:
    s = pd.Series([1, 2, 3, 10])
    s.quantile([0.25, 0.5])
    s.quantile(0.75)
    s.quantile()
    s.quantile(interpolation="nearest")


def test_types_clip() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.clip(lower=0, upper=5)
    s.clip(lower=0, upper=5, inplace=True)


def test_types_abs() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.abs()


def test_types_var() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.var()
    s.var(axis=0, ddof=1)
    s.var(skipna=True, numeric_only=False)


def test_types_std() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.std()
    s.std(axis=0, ddof=1)
    s.std(skipna=True, numeric_only=False)


def test_types_idxmin() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.idxmin()
    s.idxmin(axis=0)


def test_types_idxmax() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.idxmax()
    s.idxmax(axis=0)


def test_types_value_counts() -> None:
    s = pd.Series([1, 2])
    s.value_counts()


def test_types_unique() -> None:
    s = pd.Series([-10, 2, 2, 3, 10, 10])
    s.unique()


def test_types_apply() -> None:
    s = pd.Series([-10, 2, 2, 3, 10, 10])
    s.apply(lambda x: x ** 2)
    s.apply(np.exp)
    s.apply(str)


def test_types_element_wise_arithmetic() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    res_add1: pd.Series = s + s2
    res_add2: pd.Series = s.add(s2, fill_value=0)

    res_sub: pd.Series = s - s2
    res_sub2: pd.Series = s.sub(s2, fill_value=0)

    res_mul: pd.Series = s * s2
    res_mul2: pd.Series = s.mul(s2, fill_value=0)

    res_div: pd.Series = s / s2
    res_div2: pd.Series = s.div(s2, fill_value=0)

    res_floordiv: pd.Series = s // s2
    res_floordiv2: pd.Series = s.floordiv(s2, fill_value=0)

    res_mod: pd.Series = s % s2
    res_mod2: pd.Series = s.mod(s2, fill_value=0)

    res_pow: pd.Series = s ** abs(s2)
    res_pow2: pd.Series = s.pow(abs(s2), fill_value=0)


def test_types_scalar_arithmetic() -> None:
    s = pd.Series([0, 1, -10])

    res_add1: pd.Series = s + 1
    res_add2: pd.Series = s.add(1, fill_value=0)

    res_sub: pd.Series = s - 1
    res_sub2: pd.Series = s.sub(1, fill_value=0)

    res_mul: pd.Series = s * 2
    res_mul2: pd.Series = s.mul(2, fill_value=0)

    res_div: pd.Series = s / 2
    res_div2: pd.Series = s.div(2, fill_value=0)

    res_floordiv: pd.Series = s // 2
    res_floordiv2: pd.Series = s.floordiv(2, fill_value=0)

    res_mod: pd.Series = s % 2
    res_mod2: pd.Series = s.mod(2, fill_value=0)

    res_pow: pd.Series = s ** 2
    res_pow1: pd.Series = s ** 0
    res_pow2: pd.Series = s ** 0.213
    res_pow3: pd.Series = s.pow(0.5)


def test_types_groupby() -> None:
    s = pd.Series([4, 2, 1, 8], index=["a", "b", "a", "b"])
    s.groupby(["a", "b", "a", "b"])
    s.groupby(level=0)
    s.groupby(s > 2)


# This added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_group_by_with_dropna_keyword() -> None:
    s = pd.Series([1, 2, 3, 3], index=["col1", "col2", "col3", np.nan])
    s.groupby(level=0, dropna=True).sum()
    s.groupby(level=0, dropna=False).sum()
    s.groupby(level=0).sum()


def test_types_plot() -> None:
    pytest.skip()
    s = pd.Series([0, 1, 1, 0, -10])
    s.plot.hist()


def test_types_window() -> None:
    s = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s.expanding()
    s.expanding(axis=0, center=True)

    s.rolling(2)
    s.rolling(2, axis=0, center=True)


def test_types_cov() -> None:
    s1 = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s2 = pd.Series([0, 2, 12, -4, 7, 9, 2])
    s1.cov(s2)
    s1.cov(s2, min_periods=1)
    # ddof param was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    s1.cov(s2, ddof=2)


def test_update() -> None:
    s1 = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s1.update(pd.Series([0, 2, 12]))
    # Series.update() accepting objects that can be coerced to a Series was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    s1.update([1, 2, -4, 3])
    s1.update([1, "b", "c", "d"])
    s1.update({1: 9, 3: 4})


def test_to_markdown() -> None:
    pytest.importorskip("tabulate")
    s = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s.to_markdown()
    s.to_markdown(buf=None, mode="wt")
    # index param was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    s.to_markdown(index=False)


# compare() method added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_compare() -> None:
    s1 = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s2 = pd.Series([0, 2, 12, -4, 7, 9, 2])
    s1.compare(s2)
    s2.compare(s1, align_axis="columns", keep_shape=True, keep_equal=True)


def test_types_agg() -> None:
    s = pd.Series([1, 2, 3], index=["col1", "col2", "col3"])
    s.agg("min")
    s.agg(x=max, y="min", z=np.mean)
    s.agg("mean", axis=0)


def test_types_describe() -> None:
    s = pd.Series([1, 2, 3, np.datetime64("2000-01-01")])
    s.describe()
    s.describe(percentiles=[0.5], include="all")
    s.describe(exclude=np.number)
    # datetime_is_numeric param added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    s.describe(datetime_is_numeric=True)


def test_types_resample() -> None:
    s = pd.Series(range(9), index=pd.date_range("1/1/2000", periods=9, freq="T"))
    s.resample("3T").sum()
    # origin and offset params added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    s.resample("20min", origin="epoch", offset=pd.Timedelta(value=2, unit="minutes"))


# set_flags() method added in 1.2.0 https://pandas.pydata.org/docs/whatsnew/v1.2.0.html
def test_types_set_flags() -> None:
    pd.Series([1, 2], index=["a", "b"]).set_flags(allows_duplicate_labels=False)
    pd.Series([3, 4], index=["a", "a"]).set_flags(allows_duplicate_labels=True)
    pd.Series([5, 2], index=["a", "a"])


def test_types_getitem() -> None:
    s = pd.Series({"key": [0, 1, 2, 3]})
    key: List[int] = s["key"]
    s2 = pd.Series([0, 1, 2, 3])
    value: int = s2[0]
    s3: pd.Series = s[:2]


def test_types_eq() -> None:
    s1 = pd.Series([1, 2, 3])
    res1: pd.Series = s1 == 1
    s2 = pd.Series([1, 2, 4])
    res2: pd.Series = s1 == s2


def test_types_rename_axis() -> None:
    s: pd.Series = pd.Series([1, 2, 3]).rename_axis("A")


def test_types_values() -> None:
    n1: Union[np.ndarray, ExtensionArray] = pd.Series([1, 2, 3]).values
    n2: Union[np.ndarray, ExtensionArray] = pd.Series(list("aabc")).values
    n3: Union[np.ndarray, ExtensionArray] = pd.Series(list("aabc")).astype("category").values
    n4: Union[np.ndarray, ExtensionArray] = pd.Series(pd.date_range("20130101", periods=3, tz="US/Eastern")).values


def test_types_rename() -> None:
    # Scalar
    s1 = pd.Series([1, 2, 3]).rename("A")
    check_series_result(s1)
    # Hashable Sequence
    s2 = pd.Series([1, 2, 3]).rename(("A", "B"))
    check_series_result(s2)

    # Optional
    s3 = pd.Series([1, 2, 3]).rename(None)
    check_series_result(s3)

    # Functions
    def add1(x: int) -> int:
        return x + 1

    s4 = pd.Series([1, 2, 3]).rename(add1)
    check_series_result(s4)

    # Dictionary
    s5 = pd.Series([1, 2, 3]).rename({1: 10})
    check_series_result(s5)
    # inplace
    s6: None = pd.Series([1, 2, 3]).rename("A", inplace=True)

    if TYPE_CHECKING:
        s7 = pd.Series([1, 2, 3]).rename({1: [3, 4, 5]})  # type: ignore[dict-item]


def test_types_ne() -> None:
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([1, 2, 4])
    s3: pd.Series = s1 != s2


def test_types_bfill() -> None:
    s1 = pd.Series([1, 2, 3])
    s2: pd.Series = s1.bfill(inplace=False)
    s3: None = s1.bfill(inplace=True)


def test_types_ewm() -> None:
    s1 = pd.Series([1, 2, 3])
    w1: ExponentialMovingWindow = s1.ewm(com=0.3, min_periods=0, adjust=False, ignore_na=True, axis=0)
    w2: ExponentialMovingWindow = s1.ewm(alpha=0.4)
    w3: ExponentialMovingWindow = s1.ewm(span=1.6)
    w4: ExponentialMovingWindow = s1.ewm(halflife=0.7)


def test_types_ffill() -> None:
    s1 = pd.Series([1, 2, 3])
    s2: pd.Series = s1.ffill(inplace=False)
    s3: None = s1.ffill(inplace=True)


def test_types_as_type() -> None:
    s1 = pd.Series([1, 2, 8, 9])
    s2: pd.Series = s1.astype("int32")


def test_types_dot() -> None:
    s1 = pd.Series([0, 1, 2, 3])
    s2 = pd.Series([-1, 2, -3, 4])
    df1 = pd.DataFrame([[0, 1], [-2, 3], [4, -5], [6, 7]])
    n1 = np.array([[0, 1], [1, 2], [-1, -1], [2, 0]])
    sc1: Scalar = s1.dot(s2)
    sc2: Scalar = s1 @ s2
    s3: pd.Series = s1.dot(df1)
    s4: pd.Series = s1 @ df1
    n2: np.ndarray = s1.dot(n1)
    n3: np.ndarray = s1 @ n1


def test_series_loc_setitem() -> None:
    s = pd.Series([1, 2, 3, 4, 5])
    v = s.loc[[0, 2, 4]].values
    s.loc[[0, 2, 4]] = v


def test_series_min_max_sub_axis() -> None:
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [5, 4, 3, 2, 1]})
    s1 = df.min(axis=1)
    s2 = df.max(axis=1)
    s3 = s2 - s1


def test_series_index_isin() -> None:
    s = pd.Series([1, 2, 3, 4, 5], index=[1, 2, 2, 3, 3])
    t1 = s.loc[s.index.isin([1, 3])]
    t2 = s.loc[~s.index.isin([1, 3])]
    t3 = s[s.index.isin([1, 3])]
    t4 = s[~s.index.isin([1, 3])]
    check_series_result(t1)
    check_series_result(t2)
    check_series_result(t3)
    check_series_result(t4)


def test_series_invert() -> None:
    s1 = pd.Series([True, False, True])
    s2 = ~s1
    check_series_result(s2, bool)
    s3 = pd.Series([1, 2, 3])
    check_series_result(s3[s2])
    check_series_result(s3.loc[s2])


def test_series_multiindex_getitem() -> None:
    s = pd.Series([1, 2, 3, 4], index=pd.MultiIndex.from_product([["a", "b"], ["x", "y"]]))
    s1: pd.Series = s["a", :]


def test_series_mul() -> None:
    s = pd.Series([1, 2, 3])
    sm = s * 4
    check_series_result(sm)
    ss = s - 4
    check_series_result(ss)
    sm2 = s * s
    check_series_result(sm2)
    sp = s + 4
    check_series_result(sp)


def test_reset_index() -> None:
    s = pd.Series([1, 2, 3, 4], index=pd.MultiIndex.from_product([["a", "b"], ["c", "d"]], names=["ab", "cd"]))
    r1 = s.reset_index()
    check_dataframe_result(r1)
    r2 = s.reset_index(["ab"])
    check_dataframe_result(r2)
    r3 = s.reset_index("ab")
    check_dataframe_result(r3)
    r4 = s.reset_index(drop=True)
    check_series_result(r4)
    r5 = s.reset_index(["ab"], drop=True)
    check_series_result(r5)
    
def test_series_add_str() -> None:
    s = pd.Series(["abc", "def"])
    check_series_result(s + "x")
    check_series_result("x" + s)
    