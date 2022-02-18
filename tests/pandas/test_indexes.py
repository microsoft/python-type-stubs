import pandas as pd


from typing import TYPE_CHECKING, Any

if not TYPE_CHECKING:

    def reveal_type(*args, **kwargs):
        pass


if TYPE_CHECKING:
    from pandas._typing import np_ndarray_bool
else:
    np_ndarray_bool = Any


def test_index_unique():

    df = pd.DataFrame({"x": [1, 2, 3, 4]}, index=pd.Index([1, 2, 3, 2]))
    ind = df.index
    i2 = ind.unique()
    reveal_type(i2, expected_text="Index[Unknown]")


def test_index_isin():
    ind = pd.Index([1, 2, 3, 4, 5])
    isin = ind.isin([2, 4])
    reveal_type(isin, expected_type=np_ndarray_bool)


def test_index_astype():
    indi = pd.Index([1, 2, 3])
    inds = pd.Index(["a", "b", "c"])
    indc = indi.astype(inds.dtype)
