from typing import IO, Literal
from contextlib import closing as closing
from numpy import dtype, ndarray
from scipy.sparse import spmatrix
from .._typing import PathLike, Int, ArrayLike, MatrixLike
from ..utils import check_array as check_array, IS_PYPY as IS_PYPY
import io
import os.path

import numpy as np
import scipy.sparse as sp


def load_svmlight_file(
    f: PathLike | str | IO | int,
    *,
    n_features: None | Int = None,
    dtype: dtype = ...,
    multilabel: bool = False,
    zero_based: Literal["auto", "auto"] | bool = "auto",
    query_id: bool = False,
    offset: Int = 0,
    length: Int = ...,
) -> tuple[spmatrix, ndarray, ndarray]:
    ...


def load_svmlight_files(
    files: PathLike | ArrayLike | IO | int,
    *,
    n_features: None | Int = None,
    dtype: dtype = ...,
    multilabel: bool = False,
    zero_based: Literal["auto", "auto"] | bool = "auto",
    query_id: bool = False,
    offset: Int = 0,
    length: Int = ...,
) -> list[ndarray]:
    ...


def dump_svmlight_file(
    X: MatrixLike | ArrayLike,
    y: MatrixLike,
    f: str | IO,
    *,
    zero_based: bool = True,
    comment: None | str = None,
    query_id: None | ArrayLike = None,
    multilabel: bool = False,
):
    ...
