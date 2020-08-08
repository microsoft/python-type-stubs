class GroupBy:
    def all(self, skipna: bool=...) -> bool:
        """Return True if all values in the group are truthful, else False.

Parameters
----------
skipna : bool, default True
    Flag to ignore nan values during truth testing.

Returns
-------
bool

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def any(self, skipna: bool=...) -> bool:
        """Return True if any value in the group is truthful, else False.

Parameters
----------
skipna : bool, default True
    Flag to ignore nan values during truth testing.

Returns
-------
bool

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def bfill(self, limit: Optional[int] = ...) -> FrameOrSeries:
        """Backward fill the values.

Parameters
----------
limit : int, optional
    Limit of how many values to fill.

Returns
-------
Series or DataFrame
    Object with missing values filled.

See Also
--------
Series.backfill
DataFrame.backfill
Series.fillna
DataFrame.fillna
"""
        pass
    def count(self) -> FrameOrSeries:
        """Compute count of group, excluding missing values.

Returns
-------
Series or DataFrame
    Count of values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def cumcount(self, ascending: bool = ...) -> Series:
        """Number each item in each group from 0 to the length of that group - 1.

Essentially this is equivalent to

>>> self.apply(lambda x: pd.Series(np.arange(len(x)), x.index))

Parameters
----------
ascending : bool, default True
    If False, number in reverse, from length of group - 1 to 0.

Returns
-------
Series
    Sequence number of each element within each group.

See Also
--------
.ngroup : Number the groups themselves.

Examples
--------

>>> df = pd.DataFrame([['a'], ['a'], ['a'], ['b'], ['b'], ['a']],
...                   columns=['A'])
>>> df
    A
0  a
1  a
2  a
3  b
4  b
5  a
>>> df.groupby('A').cumcount()
0    0
1    1
2    2
3    0
4    1
5    3
dtype: int64
>>> df.groupby('A').cumcount(ascending=False)
0    3
1    2
2    1
3    1
4    0
5    0
dtype: int64
"""
        pass
    def cummax(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries:
        """Cumulative max for each group.

Returns
-------
Series or DataFrame

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def cummin(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries:
        """Cumulative min for each group.

Returns
-------
Series or DataFrame

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def cumprod(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries:
        """Cumulative product for each group.

Returns
-------
Series or DataFrame

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def cumsum(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries:
        """Cumulative sum for each group.

Returns
-------
Series or DataFrame

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def describe(self, **kwargs) -> FrameOrSeries:
        """Generate descriptive statistics.

Descriptive statistics include those that summarize the central
tendency, dispersion and shape of a
dataset's distribution, excluding ``NaN`` values.

Analyzes both numeric and object series, as well
as ``DataFrame`` column sets of mixed data types. The output
will vary depending on what is provided. Refer to the notes
below for more detail.

Parameters
----------
percentiles : list-like of numbers, optional
    The percentiles to include in the output. All should
    fall between 0 and 1. The default is
    ``[.25, .5, .75]``, which returns the 25th, 50th, and
    75th percentiles.
include : 'all', list-like of dtypes or None (default), optional
    A white list of data types to include in the result. Ignored
    for ``Series``. Here are the options:

    - 'all' : All columns of the input will be included in the output.
    - A list-like of dtypes : Limits the results to the
      provided data types.
      To limit the result to numeric types submit
      ``numpy.number``. To limit it instead to object columns submit
      the ``numpy.object`` data type. Strings
      can also be used in the style of
      ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
      select pandas categorical columns, use ``'category'``
    - None (default) : The result will include all numeric columns.
exclude : list-like of dtypes or None (default), optional,
    A black list of data types to omit from the result. Ignored
    for ``Series``. Here are the options:

    - A list-like of dtypes : Excludes the provided data types
      from the result. To exclude numeric types submit
      ``numpy.number``. To exclude object columns submit the data
      type ``numpy.object``. Strings can also be used in the style of
      ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
      exclude pandas categorical columns, use ``'category'``
    - None (default) : The result will exclude nothing.

Returns
-------
Series or DataFrame
    Summary statistics of the Series or Dataframe provided.

See Also
--------
DataFrame.count: Count number of non-NA/null observations.
DataFrame.max: Maximum of the values in the object.
DataFrame.min: Minimum of the values in the object.
DataFrame.mean: Mean of the values.
DataFrame.std: Standard deviation of the observations.
DataFrame.select_dtypes: Subset of a DataFrame including/excluding
    columns based on their dtype.

Notes
-----
For numeric data, the result's index will include ``count``,
``mean``, ``std``, ``min``, ``max`` as well as lower, ``50`` and
upper percentiles. By default the lower percentile is ``25`` and the
upper percentile is ``75``. The ``50`` percentile is the
same as the median.

For object data (e.g. strings or timestamps), the result's index
will include ``count``, ``unique``, ``top``, and ``freq``. The ``top``
is the most common value. The ``freq`` is the most common value's
frequency. Timestamps also include the ``first`` and ``last`` items.

If multiple object values have the highest count, then the
``count`` and ``top`` results will be arbitrarily chosen from
among those with the highest count.

For mixed data types provided via a ``DataFrame``, the default is to
return only an analysis of numeric columns. If the dataframe consists
only of object and categorical data without any numeric columns, the
default is to return an analysis of both the object and categorical
columns. If ``include='all'`` is provided as an option, the result
will include a union of attributes of each type.

The `include` and `exclude` parameters can be used to limit
which columns in a ``DataFrame`` are analyzed for the output.
The parameters are ignored when analyzing a ``Series``.

Examples
--------
Describing a numeric ``Series``.

>>> s = pd.Series([1, 2, 3])
>>> s.describe()
count    3.0
mean     2.0
std      1.0
min      1.0
25%      1.5
50%      2.0
75%      2.5
max      3.0
dtype: float64

Describing a categorical ``Series``.

>>> s = pd.Series(['a', 'a', 'b', 'c'])
>>> s.describe()
count     4
unique    3
top       a
freq      2
dtype: object

Describing a timestamp ``Series``.

>>> s = pd.Series([
...   np.datetime64("2000-01-01"),
...   np.datetime64("2010-01-01"),
...   np.datetime64("2010-01-01")
... ])
>>> s.describe()
count                       3
unique                      2
top       2010-01-01 00:00:00
freq                        2
first     2000-01-01 00:00:00
last      2010-01-01 00:00:00
dtype: object

Describing a ``DataFrame``. By default only numeric fields
are returned.

>>> df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
...                    'numeric': [1, 2, 3],
...                    'object': ['a', 'b', 'c']
...                   })
>>> df.describe()
       numeric
count      3.0
mean       2.0
std        1.0
min        1.0
25%        1.5
50%        2.0
75%        2.5
max        3.0

Describing all columns of a ``DataFrame`` regardless of data type.

>>> df.describe(include='all')
        categorical  numeric object
count            3      3.0      3
unique           3      NaN      3
top              f      NaN      c
freq             1      NaN      1
mean           NaN      2.0    NaN
std            NaN      1.0    NaN
min            NaN      1.0    NaN
25%            NaN      1.5    NaN
50%            NaN      2.0    NaN
75%            NaN      2.5    NaN
max            NaN      3.0    NaN

Describing a column from a ``DataFrame`` by accessing it as
an attribute.

>>> df.numeric.describe()
count    3.0
mean     2.0
std      1.0
min      1.0
25%      1.5
50%      2.0
75%      2.5
max      3.0
Name: numeric, dtype: float64

Including only numeric columns in a ``DataFrame`` description.

>>> df.describe(include=[np.number])
       numeric
count      3.0
mean       2.0
std        1.0
min        1.0
25%        1.5
50%        2.0
75%        2.5
max        3.0

Including only string columns in a ``DataFrame`` description.

>>> df.describe(include=[np.object])
       object
count       3
unique      3
top         c
freq        1

Including only categorical columns from a ``DataFrame`` description.

>>> df.describe(include=['category'])
       categorical
count            3
unique           3
top              f
freq             1

Excluding numeric columns from a ``DataFrame`` description.

>>> df.describe(exclude=[np.number])
       categorical object
count            3      3
unique           3      3
top              f      c
freq             1      1

Excluding object columns from a ``DataFrame`` description.

>>> df.describe(exclude=[np.object])
       categorical  numeric
count            3      3.0
unique           3      NaN
top              f      NaN
freq             1      NaN
mean           NaN      2.0
std            NaN      1.0
min            NaN      1.0
25%            NaN      1.5
50%            NaN      2.0
75%            NaN      2.5
max            NaN      3.0
"""
        pass
    def head(self, n: int = ...) -> FrameOrSeries:
        """Return first n rows of each group.

Similar to ``.apply(lambda x: x.head(n))``, but it returns a subset of rows
from the original DataFrame with original index and order preserved
(``as_index`` flag is ignored).

Does not work for negative values of `n`.

Returns
-------
Series or DataFrame
        
See Also
--------
Series.groupby
DataFrame.groupby

Examples
--------

>>> df = pd.DataFrame([[1, 2], [1, 4], [5, 6]],
...                   columns=['A', 'B'])
>>> df.groupby('A').head(1)
    A  B
0  1  2
2  5  6
>>> df.groupby('A').head(-1)
Empty DataFrame
Columns: [A, B]
Index: []
"""
        pass
    def mean(self, **kwargs) -> FrameOrSeries:
        """Compute mean of groups, excluding missing values.

Returns
-------
pandas.Series or pandas.DataFrame
        
See Also
--------
Series.groupby
DataFrame.groupby

Examples
--------
>>> df = pd.DataFrame({'A': [1, 1, 2, 1, 2],
...                    'B': [np.nan, 2, 3, 4, 5],
...                    'C': [1, 2, 1, 1, 2]}, columns=['A', 'B', 'C'])

Groupby one column and return the mean of the remaining columns in
each group.

>>> df.groupby('A').mean()
        B         C
A
1  3.0  1.333333
2  4.0  1.500000

Groupby two columns and return the mean of the remaining column.

>>> df.groupby(['A', 'B']).mean()
        C
A B
1 2.0  2
    4.0  1
2 3.0  1
    5.0  2

Groupby one column and return the mean of only particular column in
the group.

>>> df.groupby('A')['B'].mean()
A
1    3.0
2    4.0
Name: B, dtype: float64
"""
        pass
    def median(self, **kwargs) -> FrameOrSeries:
        """Compute median of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex

Returns
-------
Series or DataFrame
    Median of values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def min(self, **kwargs) -> FrameOrSeries:
        """Number each group from 0 to the number of groups - 1.

This is the enumerative complement of cumcount.  Note that the
numbers given to the groups match the order in which the groups
would be seen when iterating over the groupby object, not the
order they are first observed.

Parameters
----------
ascending : bool, default True
    If False, number in reverse, from number of group - 1 to 0.

Returns
-------
Series
    Unique numbers for each group.

See Also
--------
.cumcount : Number the rows in each group.

Examples
--------

>>> df = pd.DataFrame({"A": list("aaabba")})
>>> df
    A
0  a
1  a
2  a
3  b
4  b
5  a
>>> df.groupby('A').ngroup()
0    0
1    0
2    0
3    1
4    1
5    0
dtype: int64
>>> df.groupby('A').ngroup(ascending=False)
0    1
1    1
2    1
3    0
4    0
5    1
dtype: int64
>>> df.groupby(["A", [1,1,2,3,2,1]]).ngroup()
0    0
1    0
2    1
3    3
4    2
5    0
dtype: int64
"""
        pass
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> FrameOrSeries:
        """Take the nth row from each group if n is an int, or a subset of rows
if n is a list of ints.

If dropna, will take the nth non-null row, dropna is either
'all' or 'any'; this is equivalent to calling dropna(how=dropna)
before the groupby.

Parameters
----------
n : int or list of ints
    A single nth value for the row or a list of nth values.
dropna : None or str, optional
    Apply the specified dropna operation before counting which row is
    the nth row. Needs to be None, 'any' or 'all'.

Returns
-------
Series or DataFrame
    N-th value within each group.
        
See Also
--------
Series.groupby
DataFrame.groupby

Examples
--------

>>> df = pd.DataFrame({'A': [1, 1, 2, 1, 2],
...                    'B': [np.nan, 2, 3, 4, 5]}, columns=['A', 'B'])
>>> g = df.groupby('A')
>>> g.nth(0)
        B
A
1  NaN
2  3.0
>>> g.nth(1)
        B
A
1  2.0
2  5.0
>>> g.nth(-1)
        B
A
1  4.0
2  5.0
>>> g.nth([0, 1])
        B
A
1  NaN
1  2.0
2  3.0
2  5.0

Specifying `dropna` allows count ignoring ``NaN``

>>> g.nth(0, dropna='any')
        B
A
1  2.0
2  3.0

NaNs denote group exhausted when using dropna

>>> g.nth(3, dropna='any')
    B
A
1 NaN
2 NaN

Specifying `as_index=False` in `groupby` keeps the original index.

>>> df.groupby('A', as_index=False).nth(1)
    A    B
1  1  2.0
4  2  5.0
"""
        pass
    def ohlc(self) -> DataFrame:
        """Compute sum of values, excluding missing values.

For multiple groupings, the result index will be a MultiIndex

Returns
-------
DataFrame
    Open, high, low and close values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit = ..., freq = ..., axis: AxisType = ...,
    ) -> FrameOrSeries:
        """Calculate pct_change of each value to previous entry in group.

Returns
-------
Series or DataFrame
    Percentage changes within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def rank(
        self, method: str = ..., ascending: bool = ..., na_option: str = ..., pct: bool = ..., axis: int = ...,
    ) -> DataFrame:
        """Provide the rank of values within each group.

Parameters
----------
method : {'average', 'min', 'max', 'first', 'dense'}, default 'average'
    * average: average rank of group.
    * min: lowest rank in group.
    * max: highest rank in group.
    * first: ranks assigned in order they appear in the array.
    * dense: like 'min', but rank always increases by 1 between groups.
ascending : bool, default True
    False for ranks by high (1) to low (N).
na_option : {'keep', 'top', 'bottom'}, default 'keep'
    * keep: leave NA values where they are.
    * top: smallest rank if ascending.
    * bottom: smallest rank if descending.
pct : bool, default False
    Compute percentage rank of data within each group.
axis : int, default 0
    The axis of the object over which to compute the rank.

Returns
-------
DataFrame with ranking of values within each group

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def sem(self, ddof: int = ...) -> FrameOrSeries:
        """Compute standard error of the mean of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex.

Parameters
----------
ddof : int, default 1
    Degrees of freedom.

Returns
-------
Series or DataFrame
    Standard error of the mean of values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def size(self) -> Series:
        """Compute group sizes.

Returns
-------
Series
    Number of rows in each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def std(self, ddof: int = ...) -> FrameOrSeries:
        """Compute standard deviation of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex.

Parameters
----------
ddof : int, default 1
    Degrees of freedom.

Returns
-------
Series or DataFrame
    Standard deviation of values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass
    def tail(self, n: int = ...) -> FrameOrSeries:
        """Return last n rows of each group.

Similar to ``.apply(lambda x: x.tail(n))``, but it returns a subset of rows
from the original DataFrame with original index and order preserved
(``as_index`` flag is ignored).

Does not work for negative values of `n`.

Returns
-------
Series or DataFrame
        
See Also
--------
Series.groupby
DataFrame.groupby

Examples
--------

>>> df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]],
...                   columns=['A', 'B'])
>>> df.groupby('A').tail(1)
    A  B
1  a  2
3  b  2
>>> df.groupby('A').tail(-1)
Empty DataFrame
Columns: [A, B]
Index: []
"""
        pass
    def var(self, ddof: int = ...) -> FrameOrSeries:
        """Compute variance of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex.

Parameters
----------
ddof : int, default 1
    Degrees of freedom.

Returns
-------
Series or DataFrame
    Variance of values within each group.

See Also
--------
Series.groupby
DataFrame.groupby
"""
        pass

