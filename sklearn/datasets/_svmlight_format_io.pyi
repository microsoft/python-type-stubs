from typing import IO, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Mathieu Blondel <mathieu@mblondel.org>
#          Lars Buitinck
#          Olivier Grisel <olivier.grisel@ensta.org>
# License: BSD 3 clause

from contextlib import closing
import io
import os.path
from _typing import FileLike
from numpy.typing import DTypeLike

import numpy as np
import scipy.sparse as sp

from .. import __version__

from ..utils import check_array, IS_PYPY

def load_svmlight_file(
    f: str | IO | int,
    *,
    n_features: int | None = None,
    dtype: DTypeLike = ...,
    multilabel: bool = False,
    zero_based: bool | Literal["auto"] = "auto",
    query_id: bool = False,
    offset: int = 0,
    length: int = ...,
): ...
def _gen_open(f): ...
def _open_and_load(f, dtype, multilabel, zero_based, query_id, offset=0, length=-1): ...
def load_svmlight_files(
    files: ArrayLike | IO | int,
    *,
    n_features: int | None = None,
    dtype: DTypeLike = ...,
    multilabel: bool = False,
    zero_based: bool | Literal["auto"] = "auto",
    query_id: bool = False,
    offset: int = 0,
    length: int = ...,
): ...
def _dump_svmlight(X, y, f, multilabel, one_based, comment, query_id): ...
def dump_svmlight_file(
    X: NDArray | ArrayLike,
    y: ArrayLike,
    f: str | FileLike,
    *,
    zero_based: bool = True,
    comment: str | None = None,
    query_id: ArrayLike | None = None,
    multilabel: bool = False,
): ...
