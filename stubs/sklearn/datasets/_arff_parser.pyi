import itertools
import re
from collections import OrderedDict as OrderedDict
from collections.abc import Generator as Generator
from gzip import GzipFile
from typing import Any, Literal, Sequence

import numpy as np
import scipy as sp
from numpy import ndarray
from pandas import DataFrame, Series
from scipy.sparse import spmatrix

from ..externals._arff import ArffSparseDataType as ArffSparseDataType
from ..utils import check_pandas_support as check_pandas_support, get_chunk_n_rows as get_chunk_n_rows

def load_arff_from_gzip_file(
    gzip_file: GzipFile,
    parser: Literal["pandas", "liac-arff"],
    output_type: Literal["numpy", "sparse", "pandas"],
    openml_columns_info: dict,
    feature_names_to_select: list[str] | Sequence[str],
    target_names_to_select: Sequence[str] | list[Any | str],
    shape: None | tuple[int, int] = None,
) -> tuple[
    DataFrame | ndarray | spmatrix,
    DataFrame | ndarray | Series,
    DataFrame | None,
    list[str] | None,
]: ...
