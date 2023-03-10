from typing import Any, Literal, Sequence
from collections.abc import Generator as Generator
from collections import OrderedDict as OrderedDict
from ..externals._arff import ArffSparseDataType as ArffSparseDataType
from ..utils import (
    check_pandas_support as check_pandas_support,
    get_chunk_n_rows as get_chunk_n_rows,
)
from numpy import ndarray
from gzip import GzipFile
from scipy.sparse import spmatrix
import itertools
import re

import numpy as np
import pandas as pd
import scipy as sp


def load_arff_from_gzip_file(
    gzip_file: GzipFile,
    parser: Literal["pandas", "liac-arff"],
    output_type: Literal["numpy", "sparse", "pandas"],
    openml_columns_info: dict,
    feature_names_to_select: Sequence[str] | list[str],
    target_names_to_select: Sequence[str] | list[Any | str],
    shape: tuple[int, int] | None = None,
) -> tuple[
    pd.DataFrame | ndarray | spmatrix,
    pd.DataFrame | ndarray | pd.Series, 
    pd.DataFrame | None,
    list[str] | None,
]:
    ...
