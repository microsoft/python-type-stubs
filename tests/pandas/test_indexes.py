import pandas as pd

from typing import TYPE_CHECKING

if not TYPE_CHECKING:

    def reveal_type(*args, **kwargs):
        pass


def test_index_unique():

    df = pd.DataFrame({"x": [1, 2, 3, 4]}, index=pd.Index([1, 2, 3, 2]))
    ind = df.index
    i2 = ind.unique()
    reveal_type(i2, expected_text="Index[Unknown]")
