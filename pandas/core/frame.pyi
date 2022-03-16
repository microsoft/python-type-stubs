from __future__ import annotations
import datetime
import numpy as np
import sys

from pandas.core.indexing import _iLocIndexer, _LocIndexer
from matplotlib.axes import Axes as PlotAxes
from pandas._typing import Axes as Axes, Axis as Axis, FilePathOrBuffer as FilePathOrBuffer, Level as Level, Renamer as Renamer
from pandas._typing import num, SeriesAxisType, AxisType, Dtype, DtypeNp, Label, StrLike, Scalar, IndexType, MaskType, S1
from pandas._typing import ArrayLike as ArrayLike, np_ndarray_str, Timestamp as Timestamp, Timedelta as Timedelta
from pandas.core.arraylike import OpsMixin
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy
from pandas.core.groupby.grouper import Grouper
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex
from pandas.core.resample import Resampler
from pandas.core.window.rolling import Rolling, Window
from pandas.core.series import Series as Series
from pandas.io.formats import console as console, format as fmt
from pandas.io.formats.style import Styler as Styler
from typing import (
    Any,
    Callable,
    Dict,
    Hashable,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
    overload,
    Pattern,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

import numpy as _np
import datetime as _dt

_str = str
_bool = bool

class _iLocIndexerFrame(_iLocIndexer):
    @overload
    def __getitem__(self, idx: Tuple[int, int]) -> Scalar: ...
    @overload
    def __getitem__(self, idx: int) -> Series[S1]: ...
    @overload
    def __getitem__(self, idx: Tuple[Union[IndexType, MaskType], int]) -> Series[S1]: ...
    @overload
    def __getitem__(self, idx: Tuple[int, Union[IndexType, MaskType]]) -> Series[S1]: ...
    @overload
    def __getitem__(self, idx: Union[int, Tuple[Union[IndexType, MaskType], Union[IndexType, MaskType, int]]]) -> DataFrame: ...
    def __setitem__(
        self,
        idx: Union[
            int,
            IndexType,
            Tuple[int, int],
            Tuple[IndexType, int],
            Tuple[IndexType, IndexType],
            Tuple[int, IndexType],
        ],
        value: Union[float, Series[S1], DataFrame],
    ) -> None: ...

class _LocIndexerFrame(_LocIndexer):
    @overload
    def __getitem__(
        self,
        idx: Union[
            Union[IndexType, MaskType],
            List[StrLike],
            Tuple[
                Union[IndexType, MaskType, slice, List[StrLike], Tuple[Union[str, int, slice], ...]],
                Union[List[StrLike], slice, Series[bool], Callable],
            ],
        ],
    ) -> DataFrame: ...
    @overload
    def __getitem__(
        self,
        idx: Tuple[Union[StrLike, Tuple[StrLike, ...]], StrLike],
    ) -> Scalar: ...
    @overload
    def __getitem__(
        self,
        idx: Union[int, StrLike],
    ) -> Series[S1]: ...
    @overload
    def __getitem__(
        self,
        idx: Tuple[int, Union[slice, StrLike]],
    ) -> Series[S1]: ...
    @overload
    def __getitem__(
        self,
        idx: Tuple[Union[IndexType, MaskType], StrLike],
    ) -> Series[S1]: ...
    @overload
    def __getitem__(
        self,
        idx: Tuple[Tuple[Union[StrLike, slice], ...], StrLike],
    ) -> Series[S1]: ...
    @overload
    def __getitem__(self, idx: Index) -> DataFrame: ...
    def __setitem__(
        self,
        idx: Union[
            MaskType,
            StrLike,
            Tuple[Union[MaskType, Index, Sequence[Scalar], Scalar, slice], ...],
        ],
        value: Union[S1, ArrayLike, Series[S1], DataFrame],
    ) -> None: ...

class DataFrame(NDFrame, OpsMixin):
    _ListLike = Union[
        np.ndarray,
        List[Dtype],
        Dict[_str, _np.ndarray],
        Sequence,
        Index,
        Series[S1],
    ]
    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[Dtype, Any]]] = ...,
        index: Optional[Union[Index, _ListLike]] = ...,
        columns: Optional[_ListLike] = ...,
        dtype=...,
        copy: _bool = ...,
    ) -> None: ...
    @property
    def axes(self) -> List[Index]: ...
    @property
    def shape(self) -> Tuple[int, int]: ...
    @property
    def style(self) -> Styler: ...
    def items(self) -> Iterable[Tuple[Optional[Hashable], Series[S1]]]:
        """
Iterate over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with
the column name and the content as a Series.

Yields
------
label : object
    The column names for the DataFrame being iterated over.
content : Series
    The column entries belonging to each label, as a Series.

See Also
--------
DataFrame.iterrows : Iterate over DataFrame rows as
    (index, Series) pairs.
DataFrame.itertuples : Iterate over DataFrame rows as namedtuples
    of the values.

Examples
--------
>>> df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                   'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'])
>>> df
        species   population
panda   bear      1864
polar   bear      22000
koala   marsupial 80000
>>> for label, content in df.items():
...     print(f'label: {label}')
...     print(f'content: {content}', sep='\n')
...
label: species
content:
panda         bear
polar         bear
koala    marsupial
Name: species, dtype: object
label: population
content:
panda     1864
polar    22000
koala    80000
Name: population, dtype: int64
        """
        pass
    def iteritems(self) -> Iterable[Tuple[Label, Series[S1]]]:
        """
Iterate over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with
the column name and the content as a Series.

Yields
------
label : object
    The column names for the DataFrame being iterated over.
content : Series
    The column entries belonging to each label, as a Series.

See Also
--------
DataFrame.iterrows : Iterate over DataFrame rows as
    (index, Series) pairs.
DataFrame.itertuples : Iterate over DataFrame rows as namedtuples
    of the values.

Examples
--------
>>> df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                   'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'])
>>> df
        species   population
panda   bear      1864
polar   bear      22000
koala   marsupial 80000
>>> for label, content in df.items():
...     print(f'label: {label}')
...     print(f'content: {content}', sep='\n')
...
label: species
content:
panda         bear
polar         bear
koala    marsupial
Name: species, dtype: object
label: population
content:
panda     1864
polar    22000
koala    80000
Name: population, dtype: int64
        """
        pass
    def iterrows(self) -> Iterable[Tuple[Label, Series[S1]]]: ...
    def itertuples(self, index: _bool = ..., name: Optional[str] = ...): ...
    def __len__(self) -> int: ...
    @overload
    def dot(self, other: Union[DataFrame, ArrayLike]) -> DataFrame: ...
    @overload
    def dot(self, other: Series[S1]) -> Series[S1]: ...
    def __matmul__(self, other): ...
    def __rmatmul__(self, other): ...
    @classmethod
    def from_dict(cls, data, orient=..., dtype=..., columns=...) -> DataFrame: ...
    def to_numpy(
        self, dtype: Optional[Union[Type[DtypeNp], Dtype]] = ..., copy: _bool = ..., na_value: Optional[Any] = ...
    ) -> _np.ndarray: ...
    @overload
    def to_dict(self) -> Dict[_str, Any]: ...
    @overload
    def to_dict(
        self,
        orient: Literal["records"] = ...,
        into: Hashable = ...,
    ) -> List[Dict[_str, Any]]: ...
    @overload
    def to_dict(
        self,
        orient: Union[_str, Literal["dict", "list", "series", "split", "index"]] = ...,
        into: Hashable = ...,
    ) -> Dict[_str, Any]: ...
    def to_gbq(
        self,
        destination_table,
        project_id=...,
        chunksize=...,
        reauth=...,
        if_exists=...,
        auth_local_webserver=...,
        table_schema=...,
        location=...,
        progress_bar=...,
        credentials=...,
    ) -> None: ...
    @classmethod
    def from_records(cls, data, index=..., exclude=..., columns=..., coerce_float=..., nrows=...) -> DataFrame: ...
    def to_records(
        self,
        index: _bool = ...,
        columnDTypes: Optional[Union[_str, Dict]] = ...,
        indexDTypes: Optional[Union[_str, Dict]] = ...,
    ) -> np.recarray: ...
    def to_stata(
        self,
        path: FilePathOrBuffer,
        convert_dates: Optional[Dict] = ...,
        write_index: _bool = ...,
        byteorder: Optional[Union[_str, Literal["<", ">", "little", "big"]]] = ...,
        time_stamp=...,
        data_label: Optional[_str] = ...,
        variable_labels: Optional[Dict] = ...,
        version: int = ...,
        convert_strl: Optional[List[_str]] = ...,
    ) -> None: ...
    def to_feather(self, path: FilePathOrBuffer, **kwargs) -> None: ...
    @overload
    def to_markdown(self, buf: Optional[FilePathOrBuffer], mode: Optional[_str] = ..., **kwargs) -> None:
        """
Print DataFrame in Markdown-friendly format.

.. versionadded:: 1.0.0

Parameters
----------
buf : str, Path or StringIO-like, optional, default None
    Buffer to write to. If None, the output is returned as a string.
mode : str, optional
    Mode in which file is opened, "wt" by default.
index : bool, optional, default True
    Add index (row) labels.

    .. versionadded:: 1.1.0
storage_options : dict, optional
    Extra options that make sense for a particular storage connection, e.g.
    host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
    are forwarded to ``urllib`` as header options. For other URLs (e.g.
    starting with "s3://", and "gcs://") the key-value pairs are forwarded to
    ``fsspec``. Please see ``fsspec`` and ``urllib`` for more details.

    .. versionadded:: 1.2.0

**kwargs
    These parameters will be passed to `tabulate                 <https://pypi.org/project/tabulate>`_.

Returns
-------
str
    DataFrame in Markdown-friendly format.

Notes
-----
Requires the `tabulate <https://pypi.org/project/tabulate>`_ package.

Examples
        --------
        >>> df = pd.DataFrame(
        ...     data={"animal_1": ["elk", "pig"], "animal_2": ["dog", "quetzal"]}
        ... )
        >>> print(df.to_markdown())
        |    | animal_1   | animal_2   |
        |---:|:-----------|:-----------|
        |  0 | elk        | dog        |
        |  1 | pig        | quetzal    |

        Output markdown with a tabulate option.

        >>> print(df.to_markdown(tablefmt="grid"))
        +----+------------+------------+
        |    | animal_1   | animal_2   |
        +====+============+============+
        |  0 | elk        | dog        |
        +----+------------+------------+
        |  1 | pig        | quetzal    |
        +----+------------+------------+
        """
        pass
    @overload
    def to_markdown(self, mode: Optional[_str] = ..., **kwargs) -> _str: ...
    @overload
    def to_parquet(
        self,
        path: Optional[FilePathOrBuffer],
        engine: Union[_str, Literal["auto", "pyarrow", "fastparquet"]] = ...,
        compression: Union[_str, Literal["snappy", "gzip", "brotli"]] = ...,
        index: Optional[_bool] = ...,
        partition_cols: Optional[List] = ...,
        **kwargs,
    ) -> None: ...
    @overload
    def to_parquet(
        self,
        path: Optional[FilePathOrBuffer] = ...,
        engine: Union[_str, Literal["auto", "pyarrow", "fastparquet"]] = ...,
        compression: Union[_str, Literal["snappy", "gzip", "brotli"]] = ...,
        index: Optional[_bool] = ...,
        partition_cols: Optional[List] = ...,
        **kwargs,
    ) -> bytes: ...
    @overload
    def to_html(
        self,
        buf: Optional[FilePathOrBuffer],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[int, List[int], Dict[Union[_str, int], int]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_html(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[int, List[int], Dict[Union[_str, int], int]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    def info(self, verbose=..., buf=..., max_cols=..., memory_usage=..., null_counts=...) -> None: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> Series[S1]: ...
    def transpose(self, *args, copy: _bool = ...) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _str) -> Series: ...
    @overload
    def __getitem__(self, rows: slice) -> DataFrame: ...
    @overload
    def __getitem__(
        self,
        idx: Union[
            S1,
            Tuple,
            Series[_bool],
            DataFrame,
            List[_str],
            Index[_str],
            np_ndarray_str,
            Sequence[Tuple[Scalar, ...]],
        ],
    ) -> DataFrame: ...
    def __setitem__(self, key, value): ...
    @overload
    def query(self, expr: _str, *, inplace: Literal[True], **kwargs) -> None: ...
    @overload
    def query(self, expr: _str, *, inplace: Literal[False], **kwargs) -> DataFrame: ...
    @overload
    def query(self, expr: _str, inplace: _bool = ..., **kwargs) -> DataFrame: ...
    def eval(self, expr: _str, inplace: _bool = ..., **kwargs): ...
    def select_dtypes(
        self,
        include: Optional[Union[_str, List[_str]]] = ...,
        exclude: Optional[Union[_str, List[_str]]] = ...,
    ) -> DataFrame: ...
    def insert(
        self,
        loc: int,
        column,
        value: Union[int, _ListLike],
        allow_duplicates: _bool = ...,
    ) -> None: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def lookup(self, row_labels: Sequence, col_labels: Sequence) -> np.ndarray: ...
    def align(
        self,
        other: Union[DataFrame, Series[S1]],
        join: Union[_str, Literal["inner", "outer", "left", "right"]] = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        fill_value=...,
        method: Optional[Union[_str, Literal["backfill", "bfill", "pad", "ffill"]]] = ...,
        limit: Optional[int] = ...,
        fill_axis: AxisType = ...,
        broadcast_axis: Optional[AxisType] = ...,
    ) -> DataFrame:
        """
Align two objects on their axes with the specified join method.

Join method is specified for each axis Index.

Parameters
----------
other : DataFrame or Series
join : {'outer', 'inner', 'left', 'right'}, default 'outer'
axis : allowed axis of the other object, default None
    Align on index (0), columns (1), or both (None).
level : int or level name, default None
    Broadcast across a level, matching Index values on the
    passed MultiIndex level.
copy : bool, default True
    Always returns new objects. If copy=False and no reindexing is
    required then original objects are returned.
fill_value : scalar, default np.NaN
    Value to use for missing values. Defaults to NaN, but can be any
    "compatible" value.
method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
    Method to use for filling holes in reindexed Series:

    - pad / ffill: propagate last valid observation forward to next valid.
    - backfill / bfill: use NEXT valid observation to fill gap.

limit : int, default None
    If method is specified, this is the maximum number of consecutive
    NaN values to forward/backward fill. In other words, if there is
    a gap with more than this number of consecutive NaNs, it will only
    be partially filled. If method is not specified, this is the
    maximum number of entries along the entire axis where NaNs will be
    filled. Must be greater than 0 if not None.
fill_axis : {0 or 'index', 1 or 'columns'}, default 0
    Filling axis, method and limit.
broadcast_axis : {0 or 'index', 1 or 'columns'}, default None
    Broadcast values along this axis, if aligning two objects of
    different dimensions.

Returns
-------
(left, right) : (DataFrame, type of other)
    Aligned objects.

Examples
--------
>>> df = pd.DataFrame(
...     [[1, 2, 3, 4], [6, 7, 8, 9]], columns=["D", "B", "E", "A"], index=[1, 2]
... )
>>> other = pd.DataFrame(
...     [[10, 20, 30, 40], [60, 70, 80, 90], [600, 700, 800, 900]],
...     columns=["A", "B", "C", "D"],
...     index=[2, 3, 4],
... )
>>> df
   D  B  E  A
1  1  2  3  4
2  6  7  8  9
>>> other
    A    B    C    D
2   10   20   30   40
3   60   70   80   90
4  600  700  800  900

Align on columns:

>>> left, right = df.align(other, join="outer", axis=1)
>>> left
   A  B   C  D  E
1  4  2 NaN  1  3
2  9  7 NaN  6  8
>>> right
    A    B    C    D   E
2   10   20   30   40 NaN
3   60   70   80   90 NaN
4  600  700  800  900 NaN

We can also align on the index:

>>> left, right = df.align(other, join="outer", axis=0)
>>> left
    D    B    E    A
1  1.0  2.0  3.0  4.0
2  6.0  7.0  8.0  9.0
3  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN
>>> right
    A      B      C      D
1    NaN    NaN    NaN    NaN
2   10.0   20.0   30.0   40.0
3   60.0   70.0   80.0   90.0
4  600.0  700.0  800.0  900.0

Finally, the default `axis=None` will align on both index and columns:

>>> left, right = df.align(other, join="outer", axis=None)
>>> left
     A    B   C    D    E
1  4.0  2.0 NaN  1.0  3.0
2  9.0  7.0 NaN  6.0  8.0
3  NaN  NaN NaN  NaN  NaN
4  NaN  NaN NaN  NaN  NaN
>>> right
       A      B      C      D   E
1    NaN    NaN    NaN    NaN NaN
2   10.0   20.0   30.0   40.0 NaN
3   60.0   70.0   80.0   90.0 NaN
4  600.0  700.0  800.0  900.0 NaN
        """
        pass
    def reindex(**kwargs) -> DataFrame:
        """
Conform Series/DataFrame to new index with optional filling logic.

Places NA/NaN in locations having no value in the previous index. A new object
is produced unless the new index is equivalent to the current one and
``copy=False``.

Parameters
----------

keywords for axes : array-like, optional
    New labels / index to conform to, should be specified using
    keywords. Preferably an Index object to avoid duplicating data.

method : {None, 'backfill'/'bfill', 'pad'/'ffill', 'nearest'}
    Method to use for filling holes in reindexed DataFrame.
    Please note: this is only applicable to DataFrames/Series with a
    monotonically increasing/decreasing index.

    * None (default): don't fill gaps
    * pad / ffill: Propagate last valid observation forward to next
      valid.
    * backfill / bfill: Use next valid observation to fill gap.
    * nearest: Use nearest valid observations to fill gap.

copy : bool, default True
    Return a new object, even if the passed indexes are the same.
level : int or name
    Broadcast across a level, matching Index values on the
    passed MultiIndex level.
fill_value : scalar, default np.NaN
    Value to use for missing values. Defaults to NaN, but can be any
    "compatible" value.
limit : int, default None
    Maximum number of consecutive elements to forward or backward fill.
tolerance : optional
    Maximum distance between original and new labels for inexact
    matches. The values of the index at the matching locations most
    satisfy the equation ``abs(index[indexer] - target) <= tolerance``.

    Tolerance may be a scalar value, which applies the same tolerance
    to all values, or list-like, which applies variable tolerance per
    element. List-like includes list, tuple, array, Series, and must be
    the same size as the index and its dtype must exactly match the
    index's type.

Returns
-------
Series/DataFrame with changed index.

See Also
--------
DataFrame.set_index : Set row labels.
DataFrame.reset_index : Remove row labels or move them to new columns.
DataFrame.reindex_like : Change to same indices as other DataFrame.

Examples
--------
``DataFrame.reindex`` supports two calling conventions

* ``(index=index_labels, columns=column_labels, ...)``
* ``(labels, axis={'index', 'columns'}, ...)``

We *highly* recommend using keyword arguments to clarify your
intent.

Create a dataframe with some fictional data.

>>> index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
>>> df = pd.DataFrame({'http_status': [200, 200, 404, 404, 301],
...                   'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
...                   index=index)
>>> df
           http_status  response_time
Firefox            200           0.04
Chrome             200           0.02
Safari             404           0.07
IE10               404           0.08
Konqueror          301           1.00

Create a new index and reindex the dataframe. By default
values in the new index that do not have corresponding
records in the dataframe are assigned ``NaN``.

>>> new_index = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10',
...              'Chrome']
>>> df.reindex(new_index)
               http_status  response_time
Safari               404.0           0.07
Iceweasel              NaN            NaN
Comodo Dragon          NaN            NaN
IE10                 404.0           0.08
Chrome               200.0           0.02

We can fill in the missing values by passing a value to
the keyword ``fill_value``. Because the index is not monotonically
increasing or decreasing, we cannot use arguments to the keyword
``method`` to fill the ``NaN`` values.

>>> df.reindex(new_index, fill_value=0)
               http_status  response_time
Safari                 404           0.07
Iceweasel                0           0.00
Comodo Dragon            0           0.00
IE10                   404           0.08
Chrome                 200           0.02

>>> df.reindex(new_index, fill_value='missing')
              http_status response_time
Safari                404          0.07
Iceweasel         missing       missing
Comodo Dragon     missing       missing
IE10                  404          0.08
Chrome                200          0.02

We can also reindex the columns.

>>> df.reindex(columns=['http_status', 'user_agent'])
           http_status  user_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

Or we can use "axis-style" keyword arguments

>>> df.reindex(['http_status', 'user_agent'], axis="columns")
           http_status  user_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

To further illustrate the filling functionality in
``reindex``, we will create a dataframe with a
monotonically increasing index (for example, a sequence
of dates).

>>> date_index = pd.date_range('1/1/2010', periods=6, freq='D')
>>> df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
...                    index=date_index)
>>> df2
            prices
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0

Suppose we decide to expand the dataframe to cover a wider
date range.

>>> date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
>>> df2.reindex(date_index2)
            prices
2009-12-29     NaN
2009-12-30     NaN
2009-12-31     NaN
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

The index entries that did not have a value in the original data frame
(for example, '2009-12-29') are by default filled with ``NaN``.
If desired, we can fill in the missing values using one of several
options.

For example, to back-propagate the last valid value to fill the ``NaN``
values, pass ``bfill`` as an argument to the ``method`` keyword.

>>> df2.reindex(date_index2, method='bfill')
            prices
2009-12-29   100.0
2009-12-30   100.0
2009-12-31   100.0
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

Please note that the ``NaN`` value present in the original dataframe
(at index value 2010-01-03) will not be filled by any of the
value propagation schemes. This is because filling while reindexing
does not look at dataframe values, but only compares the original and
desired indexes. If you do want to fill in the ``NaN`` values present
in the original dataframe, use the ``fillna()`` method.

See the :ref:`user guide <basics.reindexing>` for more.
        """
        pass
    @overload
    def drop(
        self,
        labels: Optional[Union[Dtype, List, Set]] = ...,
        axis: AxisType = ...,
        index: Optional[Union[Dtype, List[_str], List[int], Index, Set]] = ...,
        columns: Optional[Union[Dtype, List, Index, Set]] = ...,
        level: Optional[Level] = ...,
        *,
        inplace: Literal[True],
        errors: Union[_str, Literal["ignore", "raise"]] = ...,
    ) -> None: ...
    @overload
    def drop(
        self,
        labels: Optional[Union[Dtype, List, Set]] = ...,
        axis: AxisType = ...,
        index: Optional[Union[Dtype, List[_str], List[int], Index, Set]] = ...,
        columns: Optional[Union[Dtype, List, Index, Set]] = ...,
        level: Optional[Level] = ...,
        *,
        inplace: Literal[False],
        errors: Union[_str, Literal["ignore", "raise"]] = ...,
    ) -> DataFrame: ...
    @overload
    def drop(
        self,
        labels: Optional[Union[Dtype, List, Set]] = ...,
        axis: AxisType = ...,
        index: Optional[Union[Dtype, List[_str], List[int], Index, Set]] = ...,
        columns: Optional[Union[Dtype, List, Index, Set]] = ...,
        level: Optional[Level] = ...,
        inplace: Optional[_bool] = ...,
        errors: Union[_str, Literal["ignore", "raise"]] = ...,
    ) -> DataFrame: ...
    @overload
    def rename(
        self,
        mapper: Optional[Renamer],
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[Level] = ...,
        errors: Union[_str, Literal["ignore", "raise"]] = ...,
    ) -> DataFrame: ...
    @overload
    def rename(
        self,
        index: Optional[Union[Dict[Union[_str, int], _str], Callable]] = ...,
        columns: Optional[Renamer] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[Level] = ...,
        errors: Union[_str, Literal["ignore", "raise"]] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True],
    ) -> None:
        """
Fill NA/NaN values using the specified method.

Parameters
----------
value : scalar, dict, Series, or DataFrame
    Value to use to fill holes (e.g. 0), alternately a
    dict/Series/DataFrame of values specifying which value to use for
    each index (for a Series) or column (for a DataFrame).  Values not
    in the dict/Series/DataFrame will not be filled. This value cannot
    be a list.
method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
    Method to use for filling holes in reindexed Series
    pad / ffill: propagate last valid observation forward to next valid
    backfill / bfill: use next valid observation to fill gap.
axis : {0 or 'index', 1 or 'columns'}
    Axis along which to fill missing values.
inplace : bool, default False
    If True, fill in-place. Note: this will modify any
    other views on this object (e.g., a no-copy slice for a column in a
    DataFrame).
limit : int, default None
    If method is specified, this is the maximum number of consecutive
    NaN values to forward/backward fill. In other words, if there is
    a gap with more than this number of consecutive NaNs, it will only
    be partially filled. If method is not specified, this is the
    maximum number of entries along the entire axis where NaNs will be
    filled. Must be greater than 0 if not None.
downcast : dict, default is None
    A dict of item->dtype of what to downcast if possible,
    or the string 'infer' which will try to downcast to an appropriate
    equal type (e.g. float64 to int64 if possible).

Returns
-------
DataFrame or None
    Object with missing values filled or None if ``inplace=True``.

See Also
--------
interpolate : Fill NaN values using interpolation.
reindex : Conform object to new index.
asfreq : Convert TimeSeries to specified frequency.

Examples
--------
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
...                    [3, 4, np.nan, 1],
...                    [np.nan, np.nan, np.nan, np.nan],
...                    [np.nan, 3, np.nan, 4]],
...                   columns=list("ABCD"))
>>> df
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  NaN  NaN NaN  NaN
3  NaN  3.0 NaN  4.0

Replace all NaN elements with 0s.

>>> df.fillna(0)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  0.0
3  0.0  3.0  0.0  4.0

We can also propagate non-null values forward or backward.

>>> df.fillna(method="ffill")
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  3.0  4.0 NaN  1.0
3  3.0  3.0 NaN  4.0

Replace all NaN elements in column 'A', 'B', 'C', and 'D', with 0, 1,
2, and 3 respectively.

>>> values = {"A": 0, "B": 1, "C": 2, "D": 3}
>>> df.fillna(value=values)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  2.0  1.0
2  0.0  1.0  2.0  3.0
3  0.0  3.0  2.0  4.0

Only replace the first NaN element.

>>> df.fillna(value=values, limit=1)
     A    B    C    D
0  0.0  2.0  2.0  0.0
1  3.0  4.0  NaN  1.0
2  NaN  1.0  NaN  3.0
3  NaN  3.0  NaN  4.0

When filling using a DataFrame, replacement happens along
the same column names and same indices

>>> df2 = pd.DataFrame(np.zeros((4, 4)), columns=list("ABCE"))
>>> df.fillna(df2)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  NaN
3  0.0  3.0  0.0  4.0

Note that column D is not affected since it is not present in df2.
        """
        pass
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[False] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        method: Optional[Union[_str, Literal["backfill", "bfill", "ffill", "pad"]]] = ...,
        axis: Optional[AxisType] = ...,
        *,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> Union[None, DataFrame]: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        method: Optional[Union[_str, Literal["backfill", "bfill", "ffill", "pad"]]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[_bool] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> Union[None, DataFrame]: ...
    @overload
    def replace(
        self,
        to_replace=...,
        value: Optional[Union[Scalar, Sequence, Mapping, Pattern]] = ...,
        limit: Optional[int] = ...,
        regex=...,
        method: Optional[_str] = ...,
        *,
        inplace: Literal[True],
    ) -> None:
        """
Replace values given in `to_replace` with `value`.

Values of the DataFrame are replaced with other values dynamically.

This differs from updating with ``.loc`` or ``.iloc``, which require
you to specify a location to update with some value.

Parameters
----------
to_replace : str, regex, list, dict, Series, int, float, or None
    How to find the values that will be replaced.

    * numeric, str or regex:

        - numeric: numeric values equal to `to_replace` will be
          replaced with `value`
        - str: string exactly matching `to_replace` will be replaced
          with `value`
        - regex: regexs matching `to_replace` will be replaced with
          `value`

    * list of str, regex, or numeric:

        - First, if `to_replace` and `value` are both lists, they
          **must** be the same length.
        - Second, if ``regex=True`` then all of the strings in **both**
          lists will be interpreted as regexs otherwise they will match
          directly. This doesn't matter much for `value` since there
          are only a few possible substitution regexes you can use.
        - str, regex and numeric rules apply as above.

    * dict:

        - Dicts can be used to specify different replacement values
          for different existing values. For example,
          ``{'a': 'b', 'y': 'z'}`` replaces the value 'a' with 'b' and
          'y' with 'z'. To use a dict in this way the `value`
          parameter should be `None`.
        - For a DataFrame a dict can specify that different values
          should be replaced in different columns. For example,
          ``{'a': 1, 'b': 'z'}`` looks for the value 1 in column 'a'
          and the value 'z' in column 'b' and replaces these values
          with whatever is specified in `value`. The `value` parameter
          should not be ``None`` in this case. You can treat this as a
          special case of passing two lists except that you are
          specifying the column to search in.
        - For a DataFrame nested dictionaries, e.g.,
          ``{'a': {'b': np.nan}}``, are read as follows: look in column
          'a' for the value 'b' and replace it with NaN. The `value`
          parameter should be ``None`` to use a nested dict in this
          way. You can nest regular expressions as well. Note that
          column names (the top-level dictionary keys in a nested
          dictionary) **cannot** be regular expressions.

    * None:

        - This means that the `regex` argument must be a string,
          compiled regular expression, or list, dict, ndarray or
          Series of such elements. If `value` is also ``None`` then
          this **must** be a nested dictionary or Series.

    See the examples section for examples of each of these.
value : scalar, dict, list, str, regex, default None
    Value to replace any values matching `to_replace` with.
    For a DataFrame a dict of values can be used to specify which
    value to use for each column (columns not in the dict will not be
    filled). Regular expressions, strings and lists or dicts of such
    objects are also allowed.

inplace : bool, default False
    If True, performs operation inplace and returns None.
limit : int, default None
    Maximum size gap to forward or backward fill.
regex : bool or same types as `to_replace`, default False
    Whether to interpret `to_replace` and/or `value` as regular
    expressions. If this is ``True`` then `to_replace` *must* be a
    string. Alternatively, this could be a regular expression or a
    list, dict, or array of regular expressions in which case
    `to_replace` must be ``None``.
method : {'pad', 'ffill', 'bfill', `None`}
    The method to use when for replacement, when `to_replace` is a
    scalar, list or tuple and `value` is ``None``.

    .. versionchanged:: 0.23.0
        Added to DataFrame.

Returns
-------
DataFrame
    Object after replacement.

Raises
------
AssertionError
    * If `regex` is not a ``bool`` and `to_replace` is not
      ``None``.

TypeError
    * If `to_replace` is not a scalar, array-like, ``dict``, or ``None``
    * If `to_replace` is a ``dict`` and `value` is not a ``list``,
      ``dict``, ``ndarray``, or ``Series``
    * If `to_replace` is ``None`` and `regex` is not compilable
      into a regular expression or is a list, dict, ndarray, or
      Series.
    * When replacing multiple ``bool`` or ``datetime64`` objects and
      the arguments to `to_replace` does not match the type of the
      value being replaced

ValueError
    * If a ``list`` or an ``ndarray`` is passed to `to_replace` and
      `value` but they are not the same length.

See Also
--------
DataFrame.fillna : Fill NA values.
DataFrame.where : Replace values based on boolean condition.
Series.str.replace : Simple string replacement.

Notes
-----
* Regex substitution is performed under the hood with ``re.sub``. The
  rules for substitution for ``re.sub`` are the same.
* Regular expressions will only substitute on strings, meaning you
  cannot provide, for example, a regular expression matching floating
  point numbers and expect the columns in your frame that have a
  numeric dtype to be matched. However, if those floating point
  numbers *are* strings, then you can do this.
* This method has *a lot* of options. You are encouraged to experiment
  and play with this method to gain intuition about how it works.
* When dict is used as the `to_replace` value, it is like
  key(s) in the dict are the to_replace part and
  value(s) in the dict are the value parameter.

Examples
--------

**Scalar `to_replace` and `value`**

>>> s = pd.Series([1, 2, 3, 4, 5])
>>> s.replace(1, 5)
0    5
1    2
2    3
3    4
4    5
dtype: int64

>>> df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
...                    'B': [5, 6, 7, 8, 9],
...                    'C': ['a', 'b', 'c', 'd', 'e']})
>>> df.replace(0, 5)
    A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e

**List-like `to_replace`**

>>> df.replace([0, 1, 2, 3], 4)
    A  B  C
0  4  5  a
1  4  6  b
2  4  7  c
3  4  8  d
4  4  9  e

>>> df.replace([0, 1, 2, 3], [4, 3, 2, 1])
    A  B  C
0  4  5  a
1  3  6  b
2  2  7  c
3  1  8  d
4  4  9  e

>>> s.replace([1, 2], method='bfill')
0    3
1    3
2    3
3    4
4    5
dtype: int64

**dict-like `to_replace`**

>>> df.replace({0: 10, 1: 100})
        A  B  C
0   10  5  a
1  100  6  b
2    2  7  c
3    3  8  d
4    4  9  e

>>> df.replace({'A': 0, 'B': 5}, 100)
        A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
4    4    9  e

>>> df.replace({'A': {0: 100, 4: 400}})
        A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e

**Regular expression `to_replace`**

>>> df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
...                    'B': ['abc', 'bar', 'xyz']})
>>> df.replace(to_replace=r'^ba.$', value='new', regex=True)
        A    B
0   new  abc
1   foo  new
2  bait  xyz

>>> df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)
        A    B
0   new  abc
1   foo  bar
2  bait  xyz

>>> df.replace(regex=r'^ba.$', value='new')
        A    B
0   new  abc
1   foo  new
2  bait  xyz

>>> df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})
        A    B
0   new  abc
1   xyz  new
2  bait  xyz

>>> df.replace(regex=[r'^ba.$', 'foo'], value='new')
        A    B
0   new  abc
1   new  new
2  bait  xyz

Compare the behavior of ``s.replace({'a': None})`` and
``s.replace('a', None)`` to understand the peculiarities
of the `to_replace` parameter:

>>> s = pd.Series([10, 'a', 'a', 'b', 'a'])

When one uses a dict as the `to_replace` value, it is like the
value(s) in the dict are equal to the `value` parameter.
``s.replace({'a': None})`` is equivalent to
``s.replace(to_replace={'a': None}, value=None, method=None)``:

>>> s.replace({'a': None})
0      10
1    None
2    None
3       b
4    None
dtype: object

When ``value`` is not explicitly passed and `to_replace` is a scalar, list
or tuple, `replace` uses the method parameter (default 'pad') to do the
replacement. So this is why the 'a' values are being replaced by 10
in rows 1 and 2 and 'b' in row 4 in this case.

>>> s.replace('a')
0    10
1    10
2    10
3     b
4     b
dtype: object

On the other hand, if ``None`` is explicitly passed for ``value``, it will
be respected:

>>> s.replace('a', None)
0      10
1    None
2    None
3       b
4    None
dtype: object

    .. versionchanged:: 1.4.0
        Previously the explicit ``None`` was silently ignored.
        """
        pass
    @overload
    def replace(
        self,
        to_replace=...,
        value: Optional[Union[Scalar, Sequence, Mapping, Pattern]] = ...,
        limit: Optional[int] = ...,
        regex=...,
        method: Optional[_str] = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def replace(
        self,
        to_replace=...,
        value: Optional[Union[Scalar, Sequence, Mapping, Pattern]] = ...,
        *,
        limit: Optional[int] = ...,
        regex=...,
        method: Optional[_str] = ...,
    ) -> DataFrame: ...
    @overload
    def replace(
        self,
        to_replace=...,
        value: Optional[Union[Scalar, Sequence, Mapping, Pattern]] = ...,
        inplace: Optional[_bool] = ...,
        limit: Optional[int] = ...,
        regex=...,
        method: Optional[_str] = ...,
    ) -> Union[None, DataFrame]: ...
    def shift(
        self,
        periods: int = ...,
        freq=...,
        axis: AxisType = ...,
        fill_value: Optional[Hashable] = ...,
    ) -> DataFrame:
        """
Shift index by desired number of periods with an optional time `freq`.

When `freq` is not passed, shift the index without realigning the data.
If `freq` is passed (in this case, the index must be date or datetime,
or it will raise a `NotImplementedError`), the index will be
increased using the periods and the `freq`. `freq` can be inferred
when specified as "infer" as long as either freq or inferred_freq
attribute is set in the index.

Parameters
----------
periods : int
    Number of periods to shift. Can be positive or negative.
freq : DateOffset, tseries.offsets, timedelta, or str, optional
    Offset to use from the tseries module or time rule (e.g. 'EOM').
    If `freq` is specified then the index values are shifted but the
    data is not realigned. That is, use `freq` if you would like to
    extend the index when shifting and preserve the original data.
    If `freq` is specified as "infer" then it will be inferred from
    the freq or inferred_freq attributes of the index. If neither of
    those attributes exist, a ValueError is thrown.
axis : {0 or 'index', 1 or 'columns', None}, default None
    Shift direction.
fill_value : object, optional
    The scalar value to use for newly introduced missing values.
    the default depends on the dtype of `self`.
    For numeric data, ``np.nan`` is used.
    For datetime, timedelta, or period data, etc. :attr:`NaT` is used.
    For extension dtypes, ``self.dtype.na_value`` is used.

    .. versionchanged:: 1.1.0

Returns
-------
DataFrame
    Copy of input object, shifted.

See Also
--------
Index.shift : Shift values of Index.
DatetimeIndex.shift : Shift values of DatetimeIndex.
PeriodIndex.shift : Shift values of PeriodIndex.
tshift : Shift the time index, using the index's frequency if
    available.

Examples
--------
>>> df = pd.DataFrame({"Col1": [10, 20, 15, 30, 45],
...                    "Col2": [13, 23, 18, 33, 48],
...                    "Col3": [17, 27, 22, 37, 52]},
...                   index=pd.date_range("2020-01-01", "2020-01-05"))
>>> df
            Col1  Col2  Col3
2020-01-01    10    13    17
2020-01-02    20    23    27
2020-01-03    15    18    22
2020-01-04    30    33    37
2020-01-05    45    48    52

>>> df.shift(periods=3)
            Col1  Col2  Col3
2020-01-01   NaN   NaN   NaN
2020-01-02   NaN   NaN   NaN
2020-01-03   NaN   NaN   NaN
2020-01-04  10.0  13.0  17.0
2020-01-05  20.0  23.0  27.0

>>> df.shift(periods=1, axis="columns")
            Col1  Col2  Col3
2020-01-01   NaN    10    13
2020-01-02   NaN    20    23
2020-01-03   NaN    15    18
2020-01-04   NaN    30    33
2020-01-05   NaN    45    48

>>> df.shift(periods=3, fill_value=0)
            Col1  Col2  Col3
2020-01-01     0     0     0
2020-01-02     0     0     0
2020-01-03     0     0     0
2020-01-04    10    13    17
2020-01-05    20    23    27

>>> df.shift(periods=3, freq="D")
            Col1  Col2  Col3
2020-01-04    10    13    17
2020-01-05    20    23    27
2020-01-06    15    18    22
2020-01-07    30    33    37
2020-01-08    45    48    52

>>> df.shift(periods=3, freq="infer")
            Col1  Col2  Col3
2020-01-04    10    13    17
2020-01-05    20    23    27
2020-01-06    15    18    22
2020-01-07    30    33    37
2020-01-08    45    48    52
        """
        pass
    @overload
    def set_index(
        self,
        keys: Union[Label, Sequence],
        drop: _bool = ...,
        append: _bool = ...,
        verify_integrity: _bool = ...,
        *,
        inplace: Literal[True],
    ) -> None: ...
    @overload
    def set_index(
        self,
        keys: Union[Label, Sequence],
        drop: _bool = ...,
        append: _bool = ...,
        verify_integrity: _bool = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def set_index(
        self,
        keys: Union[Label, Sequence],
        drop: _bool = ...,
        append: _bool = ...,
        *,
        verify_integrity: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def set_index(
        self,
        keys: Union[Label, Sequence],
        drop: _bool = ...,
        append: _bool = ...,
        inplace: Optional[_bool] = ...,
        verify_integrity: _bool = ...,
    ) -> Union[None, DataFrame]: ...
    @overload
    def reset_index(
        self,
        level: Union[Level, Sequence[Level]] = ...,
        drop: _bool = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
        *,
        inplace: Literal[True],
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: Union[Level, Sequence[Level]] = ...,
        drop: _bool = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def reset_index(
        self,
        level: Union[Level, Sequence[Level]] = ...,
        drop: _bool = ...,
        *,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
    ) -> DataFrame: ...
    @overload
    def reset_index(
        self,
        level: Union[Level, Sequence[Level]] = ...,
        drop: _bool = ...,
        inplace: Optional[_bool] = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
    ) -> Union[None, DataFrame]: ...
    def isna(self) -> DataFrame:
        """
Detect missing values.

Return a boolean same-sized object indicating if the values are NA.
NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
values.
Everything else gets mapped to False values. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is an NA value.

See Also
--------
DataFrame.isnull : Alias of isna.
DataFrame.notna : Boolean inverse of isna.
DataFrame.dropna : Omit axes labels with missing values.
isna : Top-level isna.

Examples
--------
Show which entries in a DataFrame are NA.

>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
...                    born=[pd.NaT, pd.Timestamp('1939-05-27'),
...                          pd.Timestamp('1940-04-25')],
...                    name=['Alfred', 'Batman', ''],
...                    toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.isna()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

Show which entries in a Series are NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.isna()
0    False
1    False
2     True
dtype: bool
        """
        pass
    def isnull(self) -> DataFrame:
        """
DataFrame.isnull is an alias for DataFrame.isna.

Detect missing values.

Return a boolean same-sized object indicating if the values are NA.
NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
values.
Everything else gets mapped to False values. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is an NA value.

See Also
--------
DataFrame.isnull : Alias of isna.
DataFrame.notna : Boolean inverse of isna.
DataFrame.dropna : Omit axes labels with missing values.
isna : Top-level isna.

Examples
--------
Show which entries in a DataFrame are NA.

>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
...                    born=[pd.NaT, pd.Timestamp('1939-05-27'),
...                          pd.Timestamp('1940-04-25')],
...                    name=['Alfred', 'Batman', ''],
...                    toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.isna()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

Show which entries in a Series are NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.isna()
0    False
1    False
2     True
dtype: bool
        """
        pass
    def notna(self) -> DataFrame:
        """
Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA.
Non-missing values get mapped to True. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).
NA values, such as None or :attr:`numpy.NaN`, get mapped to False
values.

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.notnull : Alias of notna.
DataFrame.isna : Boolean inverse of notna.
DataFrame.dropna : Omit axes labels with missing values.
notna : Top-level notna.

Examples
--------
Show which entries in a DataFrame are not NA.

>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
...                    born=[pd.NaT, pd.Timestamp('1939-05-27'),
...                          pd.Timestamp('1940-04-25')],
...                    name=['Alfred', 'Batman', ''],
...                    toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.notna()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

Show which entries in a Series are not NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.notna()
0     True
1     True
2    False
dtype: bool
        """
        pass
    def notnull(self) -> DataFrame:
        """
DataFrame.notnull is an alias for DataFrame.notna.

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA.
Non-missing values get mapped to True. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).
NA values, such as None or :attr:`numpy.NaN`, get mapped to False
values.

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.notnull : Alias of notna.
DataFrame.isna : Boolean inverse of notna.
DataFrame.dropna : Omit axes labels with missing values.
notna : Top-level notna.

Examples
--------
Show which entries in a DataFrame are not NA.

>>> df = pd.DataFrame(dict(age=[5, 6, np.NaN],
...                    born=[pd.NaT, pd.Timestamp('1939-05-27'),
...                          pd.Timestamp('1940-04-25')],
...                    name=['Alfred', 'Batman', ''],
...                    toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.notna()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

Show which entries in a Series are not NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.notna()
0     True
1     True
2    False
dtype: bool
        """
        pass
    @overload
    def dropna(
        self,
        axis: AxisType = ...,
        how: Union[_str, Literal["any", "all"]] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        *,
        inplace: Literal[True],
    ) -> None: ...
    @overload
    def dropna(
        self,
        axis: AxisType = ...,
        how: Union[_str, Literal["any", "all"]] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def dropna(
        self,
        axis: AxisType = ...,
        how: Union[_str, Literal["any", "all"]] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
    ) -> DataFrame: ...
    @overload
    def dropna(
        self,
        axis: AxisType = ...,
        how: Union[_str, Literal["any", "all"]] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        inplace: Optional[_bool] = ...,
    ) -> Union[None, DataFrame]: ...
    def drop_duplicates(
        self,
        subset=...,
        keep: Union[_str, Literal["first", "last"], _bool] = ...,
        inplace: _bool = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def duplicated(
        self,
        subset: Optional[Union[Hashable, Sequence[Hashable]]] = ...,
        keep: Union[_str, Literal["first", "last"], _bool] = ...,
    ) -> Series[S1]: ...
    @overload
    def sort_values(
        self,
        by: Union[_str, Sequence[_str]],
        axis: AxisType = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True],
        key: Optional[Callable] = ...,
    ) -> None:
        """
Sort by the values along either axis.

Parameters
----------
        by : str or list of str
            Name or list of names to sort by.

            - if `axis` is 0 or `'index'` then `by` may contain index
              levels and/or column labels.
            - if `axis` is 1 or `'columns'` then `by` may contain column
              levels and/or index labels.
axis : {0 or 'index', 1 or 'columns'}, default 0
     Axis to be sorted.
ascending : bool or list of bool, default True
     Sort ascending vs. descending. Specify list for multiple sort
     orders.  If this is a list of bools, must match the length of
     the by.
inplace : bool, default False
     If True, perform operation in-place.
kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'
     Choice of sorting algorithm. See also :func:`numpy.sort` for more
     information. `mergesort` and `stable` are the only stable algorithms. For
     DataFrames, this option is only applied when sorting on a single
     column or label.
na_position : {'first', 'last'}, default 'last'
     Puts NaNs at the beginning if `first`; `last` puts NaNs at the
     end.
ignore_index : bool, default False
     If True, the resulting axis will be labeled 0, 1, …, n - 1.

     .. versionadded:: 1.0.0

key : callable, optional
    Apply the key function to the values
    before sorting. This is similar to the `key` argument in the
    builtin :meth:`sorted` function, with the notable difference that
    this `key` function should be *vectorized*. It should expect a
    ``Series`` and return a Series with the same shape as the input.
    It will be applied to each column in `by` independently.

    .. versionadded:: 1.1.0

Returns
-------
DataFrame or None
    DataFrame with sorted values or None if ``inplace=True``.

See Also
--------
DataFrame.sort_index : Sort a DataFrame by the index.
Series.sort_values : Similar method for a Series.

Examples
--------
>>> df = pd.DataFrame({
...     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2': [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
...     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
... })
>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

Sort by col1

>>> df.sort_values(by=['col1'])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

Sort by multiple columns

>>> df.sort_values(by=['col1', 'col2'])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

Sort Descending

>>> df.sort_values(by='col1', ascending=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D

Putting NAs first

>>> df.sort_values(by='col1', ascending=False, na_position='first')
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B

Sorting with a key function

>>> df.sort_values(by='col4', key=lambda col: col.str.lower())
   col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

Natural sort with the key argument,
using the `natsort <https://github.com/SethMMorton/natsort>` package.

>>> df = pd.DataFrame({
...    "time": ['0hr', '128hr', '72hr', '48hr', '96hr'],
...    "value": [10, 20, 30, 40, 50]
... })
>>> df
    time  value
0    0hr     10
1  128hr     20
2   72hr     30
3   48hr     40
4   96hr     50
>>> from natsort import index_natsorted
>>> df.sort_values(
...    by="time",
...    key=lambda x: np.argsort(index_natsorted(df["time"]))
... )
    time  value
0    0hr     10
3   48hr     40
2   72hr     30
4   96hr     50
1  128hr     20
        """
        pass
    @overload
    def sort_values(
        self,
        by: Union[_str, Sequence[_str]],
        axis: AxisType = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[False],
        key: Optional[Callable] = ...,
    ) -> DataFrame: ...
    @overload
    def sort_values(
        self,
        by: Union[_str, Sequence[_str]],
        axis: AxisType = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        *,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        ignore_index: _bool = ...,
        key: Optional[Callable] = ...,
    ) -> DataFrame: ...
    @overload
    def sort_values(
        self,
        by: Union[_str, Sequence[_str]],
        axis: AxisType = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        inplace: Optional[_bool] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        ignore_index: _bool = ...,
        key: Optional[Callable] = ...,
    ) -> Union[None, DataFrame]: ...
    @overload
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True],
        key: Optional[Callable] = ...,
    ) -> None:
        """
Sort object by labels (along an axis).

Returns a new DataFrame sorted by label if `inplace` argument is
``False``, otherwise updates the original DataFrame and returns None.

Parameters
----------
axis : {0 or 'index', 1 or 'columns'}, default 0
    The axis along which to sort.  The value 0 identifies the rows,
    and 1 identifies the columns.
level : int or level name or list of ints or list of level names
    If not None, sort on values in specified index level(s).
ascending : bool or list-like of bools, default True
    Sort ascending vs. descending. When the index is a MultiIndex the
    sort direction can be controlled for each level individually.
inplace : bool, default False
    If True, perform operation in-place.
kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'
    Choice of sorting algorithm. See also :func:`numpy.sort` for more
    information. `mergesort` and `stable` are the only stable algorithms. For
    DataFrames, this option is only applied when sorting on a single
    column or label.
na_position : {'first', 'last'}, default 'last'
    Puts NaNs at the beginning if `first`; `last` puts NaNs at the end.
    Not implemented for MultiIndex.
sort_remaining : bool, default True
    If True and sorting by level and index is multilevel, sort by other
    levels too (in order) after sorting by specified level.
ignore_index : bool, default False
    If True, the resulting axis will be labeled 0, 1, …, n - 1.

    .. versionadded:: 1.0.0

key : callable, optional
    If not None, apply the key function to the index values
    before sorting. This is similar to the `key` argument in the
    builtin :meth:`sorted` function, with the notable difference that
    this `key` function should be *vectorized*. It should expect an
    ``Index`` and return an ``Index`` of the same shape. For MultiIndex
    inputs, the key is applied *per level*.

    .. versionadded:: 1.1.0

Returns
-------
DataFrame or None
    The original DataFrame sorted by the labels or None if ``inplace=True``.

See Also
--------
Series.sort_index : Sort Series by the index.
DataFrame.sort_values : Sort DataFrame by the value.
Series.sort_values : Sort Series by the value.

Examples
--------
>>> df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150],
...                   columns=['A'])
>>> df.sort_index()
     A
1    4
29   2
100  1
150  5
234  3

By default, it sorts in ascending order, to sort in descending order,
use ``ascending=False``

>>> df.sort_index(ascending=False)
     A
234  3
150  5
100  1
29   2
1    4

A key function can be specified which is applied to the index before
sorting. For a ``MultiIndex`` this is applied to each level separately.

>>> df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])
>>> df.sort_index(key=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4
        """
        pass
    @overload
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Union[Level, List[int], List[_str]]] = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[False],
        key: Optional[Callable] = ...,
    ) -> DataFrame: ...
    @overload
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Union[Level, List[int], List[_str]]] = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        *,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        key: Optional[Callable] = ...,
    ) -> DataFrame: ...
    @overload
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Union[Level, List[int], List[_str]]] = ...,
        ascending: Union[_bool, Sequence[_bool]] = ...,
        inplace: Optional[_bool] = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        key: Optional[Callable] = ...,
    ) -> Union[None, DataFrame]: ...
    def value_counts(
        self,
        subset: Optional[Sequence[Hashable]] = ...,
        normalize: _bool = ...,
        sort: _bool = ...,
        ascending: _bool = ...,
        dropna: _bool = ...,
    ) -> Series[int]: ...
    def nlargest(
        self,
        n: int,
        columns: Union[_str, List[_str]],
        keep: Union[_str, Literal["first", "last", "all"]] = ...,
    ) -> DataFrame: ...
    def nsmallest(
        self,
        n: int,
        columns: Union[_str, List[_str]],
        keep: Union[_str, Literal["first", "last", "all"]] = ...,
    ) -> DataFrame: ...
    def swaplevel(self, i: Level = ..., j: Level = ..., axis: AxisType = ...) -> DataFrame: ...
    def reorder_levels(self, order: List, axis: AxisType = ...) -> DataFrame: ...
    def compare(
        self,
        other: DataFrame,
        align_axis: Axis = ...,
        keep_shape: bool = ...,
        keep_equal: bool = ...,
    ) -> DataFrame: ...
    def combine(
        self,
        other: DataFrame,
        func: Callable,
        fill_value=...,
        overwrite: _bool = ...,
    ) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(
        self,
        other: Union[DataFrame, Series[S1]],
        join: _str = ...,
        overwrite: _bool = ...,
        filter_func: Optional[Callable] = ...,
        errors: Union[_str, Literal["raise", "ignore"]] = ...,
    ) -> None: ...
    def groupby(
        self,
        by: Optional[Union[List[_str], _str]] = ...,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
        dropna: _bool = ...,
    ) -> DataFrameGroupBy:
        """
Group DataFrame using a mapper or by a Series of columns.

A groupby operation involves some combination of splitting the
object, applying a function, and combining the results. This can be
used to group large amounts of data and compute operations on these
groups.

Parameters
----------
by : mapping, function, label, or list of labels
    Used to determine the groups for the groupby.
    If ``by`` is a function, it's called on each value of the object's
    index. If a dict or Series is passed, the Series or dict VALUES
    will be used to determine the groups (the Series' values are first
    aligned; see ``.align()`` method). If a list or ndarray of length
    equal to the selected axis is passed (see the `groupby user guide
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups>`_),
    the values are used as-is to determine the groups. A label or list
    of labels may be passed to group by the columns in ``self``.
    Notice that a tuple is interpreted as a (single) key.
axis : {0 or 'index', 1 or 'columns'}, default 0
    Split along rows (0) or columns (1).
level : int, level name, or sequence of such, default None
    If the axis is a MultiIndex (hierarchical), group by a particular
    level or levels.
as_index : bool, default True
    For aggregated output, return object with group labels as the
    index. Only relevant for DataFrame input. as_index=False is
    effectively "SQL-style" grouped output.
sort : bool, default True
    Sort group keys. Get better performance by turning this off.
    Note this does not influence the order of observations within each
    group. Groupby preserves the order of rows within each group.
group_keys : bool, default True
    When calling apply, add group keys to index to identify pieces.
squeeze : bool, default False
    Reduce the dimensionality of the return type if possible,
    otherwise return a consistent type.

    .. deprecated:: 1.1.0

observed : bool, default False
    This only applies if any of the groupers are Categoricals.
    If True: only show observed values for categorical groupers.
    If False: show all values for categorical groupers.
dropna : bool, default True
    If True, and if group keys contain NA values, NA values together
    with row/column will be dropped.
    If False, NA values will also be treated as the key in groups.

    .. versionadded:: 1.1.0

Returns
-------
DataFrameGroupBy
    Returns a groupby object that contains information about the groups.

See Also
--------
resample : Convenience method for frequency conversion and resampling
    of time series.

Notes
-----
See the `user guide
<https://pandas.pydata.org/pandas-docs/stable/groupby.html>`__ for more
detailed usage and examples, including splitting an object into groups,
iterating through groups, selecting a group, aggregation, and more.

Examples
--------
>>> df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
...                               'Parrot', 'Parrot'],
...                    'Max Speed': [380., 370., 24., 26.]})
>>> df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0
>>> df.groupby(['Animal']).mean()
        Max Speed
Animal
Falcon      375.0
Parrot       25.0

**Hierarchical Indexes**

We can groupby different levels of a hierarchical index
using the `level` parameter:

>>> arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
...           ['Captive', 'Wild', 'Captive', 'Wild']]
>>> index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
>>> df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},
...                   index=index)
>>> df
                Max Speed
Animal Type
Falcon Captive      390.0
       Wild         350.0
Parrot Captive       30.0
       Wild          20.0
>>> df.groupby(level=0).mean()
        Max Speed
Animal
Falcon      370.0
Parrot       25.0
>>> df.groupby(level="Type").mean()
         Max Speed
Type
Captive      210.0
Wild         185.0

We can also choose to include NA in group keys or not by setting
`dropna` parameter, the default setting is `True`.

>>> l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
>>> df = pd.DataFrame(l, columns=["a", "b", "c"])

>>> df.groupby(by=["b"]).sum()
    a   c
b
1.0 2   3
2.0 2   5

>>> df.groupby(by=["b"], dropna=False).sum()
    a   c
b
1.0 2   3
2.0 2   5
NaN 1   4

>>> l = [["a", 12, 12], [None, 12.3, 33.], ["b", 12.3, 123], ["a", 1, 1]]
>>> df = pd.DataFrame(l, columns=["a", "b", "c"])

>>> df.groupby(by="a").sum()
    b     c
a
a   13.0   13.0
b   12.3  123.0

>>> df.groupby(by="a", dropna=False).sum()
    b     c
a
a   13.0   13.0
b   12.3  123.0
NaN 12.3   33.0
        """
        pass
    def pivot(
        self,
        index=...,
        columns=...,
        values=...,
    ) -> DataFrame:
        """
Return reshaped DataFrame organized by given index / column values.

Reshape data (produce a "pivot" table) based on column values. Uses
unique values from specified `index` / `columns` to form axes of the
resulting DataFrame. This function does not support data
aggregation, multiple values will result in a MultiIndex in the
columns. See the :ref:`User Guide <reshaping>` for more on reshaping.

Parameters
----------
index : str or object or a list of str, optional
    Column to use to make new frame's index. If None, uses
    existing index.

    .. versionchanged:: 1.1.0
       Also accept list of index names.

columns : str or object or a list of str
    Column to use to make new frame's columns.

    .. versionchanged:: 1.1.0
       Also accept list of columns names.

values : str, object or a list of the previous, optional
    Column(s) to use for populating new frame's values. If not
    specified, all remaining columns will be used and the result will
    have hierarchically indexed columns.

Returns
-------
DataFrame
    Returns reshaped DataFrame.

Raises
------
ValueError:
    When there are any `index`, `columns` combinations with multiple
    values. `DataFrame.pivot_table` when you need to aggregate.

See Also
--------
DataFrame.pivot_table : Generalization of pivot that can handle
    duplicate values for one index/column pair.
DataFrame.unstack : Pivot based on the index values instead of a
    column.
wide_to_long : Wide panel to long format. Less flexible but more
    user-friendly than melt.

Notes
-----
For finer-tuned control, see hierarchical indexing documentation along
with the related stack/unstack methods.

Reference :ref:`the user guide <reshaping.pivot>` for more examples.

Examples
--------
>>> df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
...                            'two'],
...                    'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
...                    'baz': [1, 2, 3, 4, 5, 6],
...                    'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
>>> df
    foo   bar  baz  zoo
0   one   A    1    x
1   one   B    2    y
2   one   C    3    z
3   two   A    4    q
4   two   B    5    w
5   two   C    6    t

>>> df.pivot(index='foo', columns='bar', values='baz')
bar  A   B   C
foo
one  1   2   3
two  4   5   6

>>> df.pivot(index='foo', columns='bar')['baz']
bar  A   B   C
foo
one  1   2   3
two  4   5   6

>>> df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
      baz       zoo
bar   A  B  C   A  B  C
foo
one   1  2  3   x  y  z
two   4  5  6   q  w  t

You could also assign a list of column names or a list of index names.

>>> df = pd.DataFrame({
...        "lev1": [1, 1, 1, 2, 2, 2],
...        "lev2": [1, 1, 2, 1, 1, 2],
...        "lev3": [1, 2, 1, 2, 1, 2],
...        "lev4": [1, 2, 3, 4, 5, 6],
...        "values": [0, 1, 2, 3, 4, 5]})
>>> df
    lev1 lev2 lev3 lev4 values
0   1    1    1    1    0
1   1    1    2    2    1
2   1    2    1    3    2
3   2    1    2    4    3
4   2    1    1    5    4
5   2    2    2    6    5

>>> df.pivot(index="lev1", columns=["lev2", "lev3"],values="values")
lev2    1         2
lev3    1    2    1    2
lev1
1     0.0  1.0  2.0  NaN
2     4.0  3.0  NaN  5.0

>>> df.pivot(index=["lev1", "lev2"], columns=["lev3"],values="values")
      lev3    1    2
lev1  lev2
   1     1  0.0  1.0
         2  2.0  NaN
   2     1  4.0  3.0
         2  NaN  5.0

A ValueError is raised if there are any duplicates.

>>> df = pd.DataFrame({"foo": ['one', 'one', 'two', 'two'],
...                    "bar": ['A', 'A', 'B', 'C'],
...                    "baz": [1, 2, 3, 4]})
>>> df
   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4

Notice that the first two rows are the same for our `index`
and `columns` arguments.

>>> df.pivot(index='foo', columns='bar', values='baz')
Traceback (most recent call last):
   ...
ValueError: Index contains duplicate entries, cannot reshape
        """
        pass
    def pivot_table(
        self,
        values: Optional[_str] = ...,
        index: Optional[Union[_str, Grouper, Sequence]] = ...,
        columns: Optional[Union[_str, Grouper, Sequence]] = ...,
        aggfunc=...,
        fill_value: Optional[Scalar] = ...,
        margins: _bool = ...,
        dropna: _bool = ...,
        margins_name: _str = ...,
        observed: _bool = ...,
    ) -> DataFrame: ...
    def stack(self, level: Level = ..., dropna: _bool = ...) -> Union[DataFrame, Series[S1]]: ...
    def explode(self, column: Union[_str, Tuple], ignore_index: _bool = ...) -> DataFrame: ...
    def unstack(
        self,
        level: Level = ...,
        fill_value: Optional[Union[int, _str, Dict]] = ...,
    ) -> Union[DataFrame, Series[S1]]: ...
    def melt(
        self,
        id_vars: Optional[Union[Tuple, Sequence, np.ndarray]] = ...,
        value_vars: Optional[Union[Tuple, Sequence, np.ndarray]] = ...,
        var_name: Optional[Scalar] = ...,
        value_name: Scalar = ...,
        col_level: Optional[Union[int, _str]] = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...
    @overload
    def agg(self, func: Union[Callable, _str], axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    @overload
    def agg(self, func: Union[List[Callable], Dict[_str, Callable]] = ..., axis: AxisType = ..., **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, func: Union[Callable, _str], axis: AxisType = ..., **kwargs) -> Series[S1]: ...
    @overload
    def aggregate(self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ..., **kwargs) -> DataFrame: ...
    def transform(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ..., *args, **kwargs
    ) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series[S1]: ...
    @overload
    def apply(
        self, f: Callable, axis: AxisType = ..., raw: _bool = ..., result_type: Optional[_str] = ..., args=..., **kwargs
    ) -> DataFrame: ...
    def applymap(self, func: Callable, na_action: Optional[Literal["ignore"]] = None, **kwargs) -> DataFrame: ...
    def append(
        self,
        other: Union[DataFrame, Series[S1], Dict[Any, Any], List[Dtype]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def join(
        self,
        other: Union[DataFrame, Series[S1], List[DataFrame]],
        on: Optional[Union[_str, List[_str]]] = ...,
        how: Union[_str, Literal["left", "right", "outer", "inner"]] = ...,
        lsuffix: _str = ...,
        rsuffix: _str = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def merge(
        self,
        right: Union[DataFrame, Series[S1]],
        how: Union[_str, Literal["left", "right", "inner", "outer"]] = ...,
        on: Optional[Union[Level, List[Level]]] = ...,
        left_on: Optional[Union[Level, List[Level]]] = ...,
        right_on: Optional[Union[Level, List[Level]]] = ...,
        left_index: _bool = ...,
        right_index: _bool = ...,
        sort: _bool = ...,
        suffixes: Tuple[Optional[_str], Optional[_str]] = ...,
        copy: _bool = ...,
        indicator: Union[_bool, _str] = ...,
        validate: Optional[_str] = ...,
    ) -> DataFrame: ...
    def round(self, decimals: Union[int, Dict, Series[S1]] = ..., *args, **kwargs) -> DataFrame: ...
    def corr(
        self,
        method: Union[_str, Literal["pearson", "kendall", "spearman"]] = ...,
        min_periods: int = ...,
    ) -> DataFrame: ...
    def cov(self, min_periods: Optional[int] = ..., ddof: int = 1) -> DataFrame: ...
    def corrwith(
        self,
        other: Union[DataFrame, Series[S1]],
        axis: Optional[AxisType] = ...,
        drop: _bool = ...,
        method: Union[_str, Literal["pearson", "kendall", "spearman"]] = ...,
    ) -> Series[S1]: ...
    @overload
    def count(self, axis: AxisType = ..., numeric_only: _bool = ..., *, level: Level) -> DataFrame: ...
    @overload
    def count(self, axis: AxisType = ..., level: None = ..., numeric_only: _bool = ...) -> Series[S1]: ...
    def nunique(self, axis: AxisType = ..., dropna=True) -> Series[S1]: ...
    def idxmax(self, axis: AxisType = ..., skipna: _bool = ...) -> Series[S1]: ...
    def idxmin(self, axis: AxisType = ..., skipna: _bool = ...) -> Series[S1]: ...
    @overload
    def mode(
        self, axis: AxisType = ..., skipna: _bool = ..., numeric_only: _bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    @overload
    def mode(
        self, axis: AxisType = ..., skipna: _bool = ..., level: None = ..., numeric_only: _bool = ..., **kwargs
    ) -> Series[S1]: ...
    @overload
    def quantile(
        self,
        q: float = ...,
        axis: AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Union[_str, Literal["linear", "lower", "higher", "midpoint", "nearest"]] = ...,
    ) -> Series[S1]: ...
    @overload
    def quantile(
        self,
        q: List = ...,
        axis: AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Union[_str, Literal["linear", "lower", "higher", "midpoint", "nearest"]] = ...,
    ) -> DataFrame: ...
    def to_timestamp(
        self,
        freq=...,
        how: Union[_str, Literal["start", "end", "s", "e"]] = ...,
        axis: AxisType = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def to_period(self, freq: Optional[_str] = ..., axis: AxisType = ..., copy: _bool = ...) -> DataFrame: ...
    def isin(self, values: Union[Iterable, Series[S1], DataFrame, Dict]) -> DataFrame: ...
    def plot(self, *args, **kwargs) -> PlotAxes: ...
    def hist(
        self,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[PlotAxes] = ...,
        sharex: _bool = ...,
        sharey: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        bins: Union[int, List] = ...,
        backend: Optional[_str] = ...,
        **kwargs,
    ): ...
    def boxplot(
        self,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        ax: Optional[PlotAxes] = ...,
        fontsize: Optional[Union[float, _str]] = ...,
        rot: int = ...,
        grid: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        return_type: Optional[Union[_str, Literal["axes", "dict", "both"]]] = ...,
        backend: Optional[_str] = ...,
        **kwargs,
    ): ...
    sparse = ...

    # The rest of these are remnants from the
    # stubs shipped at preview. They may belong in
    # base classes, or stubgen just failed to generate
    # these.

    Name: _str
    #
    # dunder methods
    def __delitem__(self, key: _str) -> None: ...
    def __exp__(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: AxisType = ...,
        level: Level = ...,
        fill_value: Union[None, float] = ...,
    ) -> DataFrame: ...
    def __iter__(self) -> Iterator: ...
    # properties
    @property
    def at(self): ...  # Not sure what to do with this yet; look at source
    @property
    def bool(self) -> _bool: ...
    @property
    def columns(self) -> Index[_str]: ...
    @columns.setter  # setter needs to be right next to getter; otherwise mypy complains
    def columns(self, cols: Union[List[_str], Index[_str]]) -> None: ...  # type:ignore
    @property
    def dtypes(self) -> Series[S1]: ...
    @property
    def empty(self) -> _bool: ...
    @property
    def iat(self): ...  # Not sure what to do with this yet; look at source
    @property
    def iloc(self) -> _iLocIndexerFrame: ...
    @property
    def index(self) -> Index: ...
    @index.setter
    def index(self, idx: Index) -> None: ...
    @property
    def loc(self) -> _LocIndexerFrame: ...
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def values(self) -> _np.ndarray: ...
    # methods
    def abs(self) -> DataFrame: ...
    def add(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def add_prefix(self, prefix: _str) -> DataFrame: ...
    def add_suffix(self, suffix: _str) -> DataFrame: ...
    @overload
    def all(
        self, axis: AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[S1]: ...
    @overload
    def all(
        self, axis: AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    @overload
    def any(
        self, axis: AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[S1]: ...
    @overload
    def any(self, axis: AxisType = ..., bool_only: _bool = ..., skipna: _bool = ..., *, level: Level, **kwargs) -> DataFrame: ...
    def asof(self, where, subset: Optional[Union[_str, List[_str]]] = ...) -> DataFrame: ...
    def asfreq(
        self,
        freq,
        method: Optional[Union[_str, Literal["backfill", "bfill", "pad", "ffill"]]] = ...,
        how: Optional[Union[_str, Literal["start", "end"]]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[Scalar] = ...,
    ) -> DataFrame: ...
    def astype(
        self,
        dtype: Union[_str, Dtype, Dict[_str, Union[_str, Dtype]]],
        copy: _bool = ...,
        errors: _str = ...,
    ) -> DataFrame: ...
    def at_time(
        self,
        time: Union[_str, datetime.time],
        asof: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    def between_time(
        self,
        start_time: Union[_str, datetime.time],
        end_time: Union[_str, datetime.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True],
    ) -> None: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[_bool] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> Union[None, DataFrame]: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[AxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs,
    ) -> DataFrame: ...
    def convert_dtypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert__boolean: _bool = ...,
    ) -> DataFrame: ...
    def copy(self, deep: _bool = ...) -> DataFrame: ...
    def cummax(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cummin(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumprod(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumsum(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[_str, Literal["all"], List[Dtype]]] = ...,
        exclude: Optional[List[Dtype]] = ...,
        datetime_is_numeric: Optional[_bool] = ...,
    ) -> DataFrame: ...
    def div(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def divide(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def droplevel(self, level: Union[Level, List[Level]] = ..., axis: AxisType = ...) -> DataFrame: ...
    def eq(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def equals(self, other: Union[Series[S1], DataFrame]) -> _bool: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: AxisType = ...,
    ) -> DataFrame: ...
    def exp(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: AxisType = ...): ...  # for now
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True],
    ) -> None: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[False],
    ) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series[S1], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[_bool] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> Union[None, DataFrame]: ...
    def filter(
        self,
        items: Optional[List] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    def first(self, offset) -> DataFrame: ...
    def first_valid_index(self) -> Scalar: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # def from_dict
    # def from_records
    def fulldiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ge(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    # def get
    def gt(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def infer_objects(self) -> DataFrame: ...
    # def info
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        limit_direction: Union[_str, Literal["forward", "backward", "both"]] = ...,
        limit_area: Union[_str, Optional[Literal["inside", "outside"]]] = ...,
        downcast: Optional[Union[_str, Literal["infer"]]] = ...,
        *,
        inplace: Literal[True],
        **kwargs,
    ) -> None: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        limit_direction: Union[_str, Literal["forward", "backward", "both"]] = ...,
        limit_area: Union[_str, Optional[Literal["inside", "outside"]]] = ...,
        downcast: Optional[Union[_str, Literal["infer"]]] = ...,
        *,
        inplace: Literal[False],
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        limit_direction: Union[_str, Literal["forward", "backward", "both"]] = ...,
        limit_area: Union[_str, Optional[Literal["inside", "outside"]]] = ...,
        downcast: Optional[Union[_str, Literal["infer"]]] = ...,
    ) -> DataFrame: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: AxisType = ...,
        limit: Optional[int] = ...,
        inplace: Optional[_bool] = ...,
        limit_direction: Union[_str, Literal["forward", "backward", "both"]] = ...,
        limit_area: Optional[Union[_str, Literal["inside", "outside"]]] = ...,
        downcast: Optional[Union[_str, Literal["infer"]]] = ...,
        **kwargs,
    ) -> DataFrame: ...
    def keys(self) -> Index: ...
    @overload
    def kurt(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def kurt(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    def last(self, offset) -> DataFrame: ...
    def last_valid_index(self) -> Scalar: ...
    def le(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def lt(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    @overload
    def mad(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
    ) -> Series[S1]: ...
    @overload
    def mad(self, axis: Optional[AxisType] = ..., skipna: Optional[_bool] = ..., *, level: Level, **kwargs) -> DataFrame: ...
    def mask(
        self,
        cond: Union[Series[S1], DataFrame, _np.ndarray],
        other=...,
        inplace: _bool = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series: ...
    @overload
    def mean(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def mean(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    @overload
    def median(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def median(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    @overload
    def min(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def min(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series: ...
    def mod(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def mul(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def multiply(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ne(self, other, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def pct_change(
        self, periods: int = ..., fill_method: _str = ..., limit: Optional[int] = ..., freq=..., **kwargs
    ) -> DataFrame: ...
    def pipe(self, func: Callable, *args, **kwargs): ...
    def pop(self, item: _str) -> Series[S1]: ...
    def pow(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs,
    ) -> Series[S1]: ...
    def product(
        self,
        axis: Optional[AxisType] = ...,
        skipna: _bool = ...,
        level: Optional[Level] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs,
    ) -> DataFrame: ...
    def radd(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rank(
        self,
        axis: AxisType = ...,
        method: Union[_str, Literal["average", "min", "max", "first", "dense"]] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Union[_str, Literal["keep", "top", "bottom"]] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> DataFrame: ...
    def rdiv(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def reindex_like(
        self,
        other: DataFrame,
        method: Optional[Union[_str, Literal["backfill", "bfill", "pad", "ffill", "nearest"]]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance=...,
    ) -> DataFrame: ...
    @overload
    def rename_axis(self, mapper=..., *, inplace: Literal[True], axis: Optional[AxisType] = ..., copy: _bool = ...) -> None: ...
    @overload
    def rename_axis(
        self, mapper=..., *, inplace: Literal[False] = ..., axis: Optional[AxisType] = ..., copy: _bool = ...
    ) -> DataFrame: ...
    @overload
    def rename_axis(
        self,
        *,
        inplace: Literal[True],
        index: Optional[Union[_str, Sequence[_str], Dict[Union[_str, int], _str], Callable]] = ...,
        columns: Optional[Union[_str, Sequence[_str], Dict[Union[_str, int], _str], Callable]] = ...,
        copy: _bool = ...,
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        *,
        inplace: Literal[False] = ...,
        index: Optional[Union[_str, Sequence[_str], Dict[Union[_str, int], _str], Callable]] = ...,
        columns: Optional[Union[_str, Sequence[_str], Dict[Union[_str, int], _str], Callable]] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def resample(
        self,
        rule,
        axis: AxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Union[_str, Literal["start", "end", "s", "e"]] = ...,
        kind: Union[_str, Optional[Literal["timestamp", "period"]]] = ...,
        loffset=...,
        base: int = ...,
        on: Optional[_str] = ...,
        level: Optional[Level] = ...,
        origin: Union[Timestamp, Literal["epoch", "start", "start_day", "end", "end_day"]] = ...,
        offset: Optional[Union[Timedelta, _str]] = None,
    ) -> Resampler: ...
    def rfloordiv(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[Union[float, None]] = ...,
    ) -> DataFrame: ...
    def rmod(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rmul(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def rolling(
        self,
        window,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        *,
        win_type: _str,
        on: Optional[_str] = ...,
        axis: SeriesAxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Window: ...
    @overload
    def rolling(
        self,
        window,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        *,
        on: Optional[_str] = ...,
        axis: SeriesAxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Rolling: ...
    def rpow(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rsub(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rtruediv(
        self,
        other,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # sample is missing a weights arg
    @overload
    def sample(
        self,
        frac: Optional[float],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def sample(
        self,
        n: Optional[int],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    @overload
    def set_axis(self, labels: List, inplace: Literal[True], axis: AxisType = ...) -> None: ...
    @overload
    def set_axis(self, labels: List, inplace: Literal[False], axis: AxisType = ...) -> DataFrame: ...
    @overload
    def set_axis(self, labels: List, *, axis: AxisType = ...) -> DataFrame: ...
    @overload
    def set_axis(
        self,
        labels: List,
        axis: AxisType = ...,
        inplace: Optional[_bool] = ...,
    ) -> Union[None, DataFrame]: ...
    @overload
    def skew(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    def slice_shift(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...
    def squeeze(self, axis: Optional[AxisType] = ...): ...
    @overload
    def std(
        self, axis: AxisType = ..., skipna: _bool = ..., ddof: int = ..., numeric_only: _bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    @overload
    def std(
        self, axis: AxisType = ..., skipna: _bool = ..., level: None = ..., ddof: int = ..., numeric_only: _bool = ..., **kwargs
    ) -> Series[S1]: ...
    def sub(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def subtract(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs,
    ) -> Series[S1]: ...
    def swapaxes(self, axis1: AxisType, axis2: AxisType, copy: _bool = ...) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: List, axis: AxisType = ..., is_copy: Optional[_bool] = ..., **kwargs) -> DataFrame: ...
    def tshift(self, periods: int = ..., freq=..., axis: AxisType = ...) -> DataFrame: ...
    def to_clipboard(self, excel: _bool = ..., sep: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[FilePathOrBuffer],
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
        errors: _str = ...,
        storage_options: Optional[Dict[_str, Any]] = ...,
    ) -> None: ...
    @overload
    def to_csv(
        self,
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
        errors: _str = ...,
        storage_options: Optional[Dict[_str, Any]] = ...,
    ) -> _str: ...
    def to_excel(
        self,
        excel_writer,
        sheet_name: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Union[_str, Sequence[_str]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[_str] = ...,
        merge_cells: _bool = ...,
        encoding: Optional[_str] = ...,
        inf_rep: _str = ...,
        verbose: _bool = ...,
        freeze_panes: Optional[Tuple[int, int]] = ...,
    ) -> None: ...
    def to_hdf(
        self,
        path_or_buf: FilePathOrBuffer,
        key: _str,
        mode: _str = ...,
        complevel: Optional[int] = ...,
        complib: Optional[_str] = ...,
        append: _bool = ...,
        format: Optional[_str] = ...,
        index: _bool = ...,
        min_itemsize: Optional[Union[int, Dict[_str, int]]] = ...,
        nan_rep=...,
        dropna: Optional[_bool] = ...,
        data_columns: Optional[List[_str]] = ...,
        errors: _str = ...,
        encoding: _str = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        path_or_buf: Optional[FilePathOrBuffer],
        orient: Optional[Union[_str, Literal["split", "records", "index", "columns", "values", "table"]]] = ...,
        date_format: Optional[Union[_str, Literal["epoch", "iso"]]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Union[_str, Literal["s", "ms", "us", "ns"]] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Union[_str, Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        orient: Optional[Union[_str, Literal["split", "records", "index", "columns", "values", "table"]]] = ...,
        date_format: Optional[Union[_str, Literal["epoch", "iso"]]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Union[_str, Literal["s", "ms", "us", "ns"]] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Union[_str, Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> _str: ...
    @overload
    def to_latex(
        self,
        buf: Optional[FilePathOrBuffer],
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[Union[_str, Tuple[_str, _str]]] = ...,
        label: Optional[_str] = ...,
        position: Optional[str] = ...,
    ) -> None: ...
    @overload
    def to_latex(
        self,
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[Union[_str, Tuple[_str, _str]]] = ...,
        label: Optional[_str] = ...,
        position: Optional[str] = ...,
    ) -> _str: ...
    def to_pickle(
        self,
        path: _str,
        compression: Union[_str, Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
        protocol: int = ...,
    ) -> None: ...
    def to_sql(
        self,
        name: _str,
        con,
        schema: Optional[_str] = ...,
        if_exists: _str = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        chunksize: Optional[int] = ...,
        dtype: Optional[Union[Dict, Scalar]] = ...,
        method: Optional[Union[_str, Callable]] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        buf: Optional[FilePathOrBuffer],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[int, List[int], Dict[Union[_str, int], int]]] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[int, List[int], Dict[Union[_str, int], int]]] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters=...,
        float_format=...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    def to_xarray(self): ...
    def truediv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def truncate(
        self,
        before: Optional[Union[datetime.date, _str, int]] = ...,
        after: Optional[Union[datetime.date, _str, int]] = ...,
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    # def tshift
    def tz_convert(
        self,
        tz,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def tz_localize(
        self,
        tz,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        ambiguous=...,
        nonexistent: _str = ...,
    ) -> DataFrame: ...
    def unique(self) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs,
    ) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs,
    ) -> Series[S1]: ...
    def where(
        self,
        cond: Union[Series[S1], DataFrame, _np.ndarray],
        other=...,
        inplace: _bool = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    def xs(
        self,
        key: Union[_str, Tuple[_str]],
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        drop_level: _bool = ...,
    ) -> DataFrame: ...
