from typing import IO, Literal
from .._typing import Int, ArrayLike, MatrixLike
from contextlib import closing as closing
from numpy import dtype, ndarray
from ..utils import check_array as check_array, IS_PYPY as IS_PYPY
from os import PathLike
from scipy.sparse import spmatrix
import io
import os.path

import numpy as np
import scipy.sparse as sp


def load_svmlight_file(
    f: IO | PathLike | int | str,
    *,
    n_features: None | Int = None,
    dtype: dtype = ...,
    multilabel: bool = False,
    zero_based: bool | Literal["auto", "auto"] = "auto",
    query_id: bool = False,
    offset: Int = 0,
    length: Int = ...,
) -> tuple[spmatrix, ndarray, ndarray]:
    ...


def load_svmlight_files(
    files: IO | int | PathLike | ArrayLike,
    *,
    n_features: None | Int = None,
    dtype: dtype = ...,
    multilabel: bool = False,
    zero_based: bool | Literal["auto", "auto"] = "auto",
    query_id: bool = False,
    offset: Int = 0,
    length: Int = ...,
) -> list[ndarray]:
    ...


def dump_svmlight_file(
    X: MatrixLike | ArrayLike,
    y: MatrixLike,
    f: IO | str,
    *,
    zero_based: bool = True,
    comment: str | None = None,
    query_id: None | ArrayLike = None,
    multilabel: bool = False,
):
    ...
