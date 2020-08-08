def read_stata(
    path: FilePathOrBuffer,
    convert_dates: bool = ...,
    convert_categoricals: bool = ...,
    index_col: Optional[str] = ...,
    convert_missing: bool = ...,
    preserve_dtypes: bool = ...,
    columns: Optional[Sequence[str]] = ...,
    order_categoricals: bool = ...,
    chunksize: Optional[int] = ...,
    iterator: bool = ...,
) -> DataFrame: 
    """Read Stata file into DataFrame.

Parameters
----------
filepath_or_buffer : str, path object or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid
    URL schemes include http, ftp, s3, and file. For file URLs, a host is
    expected. A local file could be: ``file://localhost/path/to/table.dta``.

    If you want to pass in a path object, pandas accepts any ``os.PathLike``.

    By file-like object, we refer to objects with a ``read()`` method,
    such as a file handler (e.g. via builtin ``open`` function)
    or ``StringIO``.
convert_dates : bool, default True
    Convert date variables to DataFrame time values.
convert_categoricals : bool, default True
    Read value labels and convert columns to Categorical/Factor variables.
index_col : str, optional
    Column to set as index.
convert_missing : bool, default False
    Flag indicating whether to convert missing values to their Stata
    representations.  If False, missing values are replaced with nan.
    If True, columns containing missing values are returned with
    object data types and missing values are represented by
    StataMissingValue objects.
preserve_dtypes : bool, default True
    Preserve Stata datatypes. If False, numeric data are upcast to pandas
    default types for foreign data (float64 or int64).
columns : list or None
    Columns to retain.  Columns will be returned in the given order.  None
    returns all columns.
order_categoricals : bool, default True
    Flag indicating whether converted categorical data are ordered.
chunksize : int, default None
    Return StataReader object for iterations, returns chunks with
    given number of lines.
iterator : bool, default False
    Return StataReader object.

Returns
-------
DataFrame or StataReader

See Also
--------
io.stata.StataReader : Low-level reader for Stata data files.
DataFrame.to_stata: Export Stata data files.

Examples
--------
Read a Stata dta file:

>>> df = pd.read_stata('filename.dta')

Read a Stata dta file in 10,000 line chunks:

>>> itr = pd.read_stata('filename.dta', chunksize=10000)
>>> for chunk in itr:
...     do_something(chunk)
"""
    pass
