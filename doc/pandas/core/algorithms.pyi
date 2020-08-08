def factorize(
    values: Any, sort: bool = ..., na_sentinel: int = ..., size_hint: Union[int, None] = None,
) -> Tuple[_np.ndarray, Union[_np.ndarray, Index]]:
    """Encode the object as an enumerated type or categorical variable.

This method is useful for obtaining a numeric representation of an
array when all that matters is identifying distinct values. `factorize`
is available as both a top-level function :func:`pandas.factorize`,
and as a method :meth:`Series.factorize` and :meth:`Index.factorize`.

Parameters
----------
values : sequence
    A 1-D sequence. Sequences that aren't pandas objects are
    coerced to ndarrays before factorization.
sort : bool, default False
    Sort `uniques` and shuffle `codes` to maintain the
    relationship.

na_sentinel : int, default -1
    Value to mark "not found".
size_hint : int, optional
    Hint to the hashtable sizer.

Returns
-------
codes : ndarray
    An integer ndarray that's an indexer into `uniques`.
    ``uniques.take(codes)`` will have the same values as `values`.
uniques : ndarray, Index, or Categorical
    The unique valid values. When `values` is Categorical, `uniques`
    is a Categorical. When `values` is some other pandas object, an
    `Index` is returned. Otherwise, a 1-D ndarray is returned.

    .. note ::

       Even if there's a missing value in `values`, `uniques` will
       *not* contain an entry for it.

See Also
--------
cut : Discretize continuous-valued array.
unique : Find the unique value in an array.

Examples
--------
These examples all show factorize as a top-level method like
``pd.factorize(values)``. The results are identical for methods like
:meth:`Series.factorize`.

>>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'])
>>> codes
array([0, 0, 1, 2, 0])
>>> uniques
array(['b', 'a', 'c'], dtype=object)

With ``sort=True``, the `uniques` will be sorted, and `codes` will be
shuffled so that the relationship is the maintained.

>>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'], sort=True)
>>> codes
array([1, 1, 0, 2, 1])
>>> uniques
array(['a', 'b', 'c'], dtype=object)

Missing values are indicated in `codes` with `na_sentinel`
(``-1`` by default). Note that missing values are never
included in `uniques`.

>>> codes, uniques = pd.factorize(['b', None, 'a', 'c', 'b'])
>>> codes
array([ 0, -1,  1,  2,  0])
>>> uniques
array(['b', 'a', 'c'], dtype=object)

Thus far, we've only factorized lists (which are internally coerced to
NumPy arrays). When factorizing pandas objects, the type of `uniques`
will differ. For Categoricals, a `Categorical` is returned.

>>> cat = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
>>> codes, uniques = pd.factorize(cat)
>>> codes
array([0, 0, 1])
>>> uniques
[a, c]
Categories (3, object): [a, b, c]

Notice that ``'b'`` is in ``uniques.categories``, despite not being
present in ``cat.values``.

For all other pandas objects, an Index of the appropriate type is
returned.

>>> cat = pd.Series(['a', 'a', 'c'])
>>> codes, uniques = pd.factorize(cat)
>>> codes
array([0, 0, 1])
>>> uniques
Index(['a', 'c'], dtype='object')
"""
    pass
